#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a climatology of climate indicies
"""
import sys, os, re, numpy as np
sys.path.append('/home/war42q/')
from maclab.maclab import spatial as sp
from maclab.maclab import utils as ut
from maclab.maclab import slurm as sl
import pandas as pd
from itertools import groupby
import rasterio
from affine import Affine
from rasterio.crs import CRS
import operator, json
from . import core
import argparse

def config(args):
    """Configure parsed arguments.
    
    Parameters
    ----------
    args: argparse args
    
    Returns
    -------
	four items for input to routines
        list of src nc files
        list of indicies to calculate
        destination dir to write to
        keyword arguments
    """
    # txt file listing nc files
    files = vars(args)['file_list']
    with open(files) as f:
        src = f.readlines()
    f.close()
    src = [x.strip() for x in src] 

    # indicie(s) as list
    indicies = vars(args)['indicie']
    
    # dst dir
    dst = vars(args)['dst']
    if os.path.exists(dst) is not True:
        os.mkdir(dst)

    # check for additional args
    kwargs = vars(args)['args_dict']
    
    return(src, indicies, dst, kwargs)

def valid_indicies(indicies):
    """Check whether indicies are valid.
    
    Parameters
    ----------
    indicies: list of strings
    strings to relate to one of the available options
    """
    # indicies available in calc_indicies 
    indicie_opts = ["TXx", "TNx", "TXn", "TNn", "FD", "R1", "Rx1day"]

    for i in indicies:
        if i not in indicie_opts:
            print('{0} is not a valid indicie. ' + \
                  'Provided indicie must match one of {1}'.\
                  format(i, indicie_opts))
            sys.exit()
			
def gen_meta(src):
    """Generate meta template."""
    meta = sp.Raster(src[0]).meta
    meta['count'] = 1
    meta['dtype'] = 'float32'
    meta['driver'] = 'GTiff'
    meta['nodata'] = -9999

    rm_keys = ['blockxsize', 'blockysize', 'tiled']
    for k in rm_keys:
        if k in meta:
            del meta[k]
    return(meta)

def parse_stat(indicie):
    """Parse matched numpy function."""
    if indicie in ['TXx', 'TNx', 'Rx1day', 'FD', 'R1']:
        return(getattr(np, 'max'))
    if indicie in ['TNn', 'TXn']:
        return(getattr(np, 'min'))

def calc(args):
    """Main function to calculate climatologies of indicies.
    
    Parameters
    ----------
    args: arparse list of args
    
    Returns
    -------
    GTiff files written to dst arg
    """
    src, indicies, dst, kwargs = config(args)
    valid_indicies(indicies)
    if args.verbose:
        print('Reading in {0} files'.format(len(src)))
    meta = gen_meta(src)
    nodata = meta['nodata']
        
    if kwargs is None and args.verbose:
       print('no additional args supplied')
    
    for i in indicies:
        # get matched function
        parse_func = getattr(core, i)
		
        # dir for monthly grids if required
        if args.write_months:
            month_dst = '{0}/monthly_{1}'.format(dst, i)
            if os.path.exists is not True:
                os.mkdir(month_dst)
        
        # run
        monthly_outputs = []
        for f in src:
            if kwargs:
                output_f = parse_func(filepath = f, **kwargs)
            else:
                output_f = parse_func(filepath = f)
            if args.write_months:
                f_dst = '{0}/{1}_{2}.tif'.format(month_dst, i, f[:-3])
                with rasterio.open(f_dst, 'w', **meta) as output:
                    output.write(output_f.astype('float32'), 1)
            monthly_outputs.append(output_f)
        
        # generate climatologies
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', \
                 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        by_months = dict.fromkeys(months)
        # cut outputs by months, assuming 12 months are given for each year
        if len(monthly_outputs)%12 != 0:
            print('number of files supplied is not divisible into years: \n' + \
                  'cannot calculate climatology')
            sys.exit()
        cuts = [np.arange(i, len(monthly_outputs), 12) for i in range(12)]
        for m in range(12):
            by_months[months[m]] = np.dstack([monthly_outputs[j] for j in cuts[m]])
        # calc monthly means across years
        yearly = np.dstack([np.mean(by_months[m], axis = 2) for m in months])
        stat = parse_stat(i)
        output_i = stat(yearly, axis = 2)
        
        # write
        if args.filename:
            this_dst = '{0}/{1}_{2}.tif'.format(dst, i, args.filename)
        else:
            this_dst = '{0}/{1}.tif'.format(dst, i)
        with rasterio.open(this_dst, 'w', **meta) as output:
            output.write(output_i.astype('float32'), 1)
        if args.verbose:
            print('indicie {0} written to {1}'.format(i, this_dst))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Derive climatologies of climate indices',
                                    add_help=True,
                                    epilog="Note: indicies available are: \n" + \
                                    "TXx TNx TXn TNn FD R1 Rx1day")
    parser.add_argument('-f','--file-list', \
                        help='path to txt file with list of nc files. <Required> Set flag',\
                        required=True)
    parser.add_argument('-i','--indicie', nargs='+', \
                        help='list of indicies to calculate. To view, call ' +\
                        '$calc_indicies.py --options'
                        '<Required> Set flag', \
                        required=True)
    parser.add_argument('-a', '--args-dict', \
                        help='additional args to supply to any indicie functions called. ' + \
                        'These need to be passed as a dictionary. ' +
                        '<Optional> Set flag', type=json.loads)
    parser.add_argument('-k', '--cel2kel', \
                        help='Convert input array from celsius to kelvin. ' + \
                        '<Optional> Set flag', action="store_true")
    parser.add_argument('-d','--dst', \
                        help='destination directory to write to.' + \
                        'Will be created if it does not exist <Required> Set flag',\
                        required=True)
    parser.add_argument('-fn', '--filename', \
                        help='String to add to add to the filename. By default, the filename ' + \
                        'is given as <indicie>.tif. <Optional> Set flag')
    parser.add_argument("-w", "--write-months", action="store_true",
                        help='write monthly indicies to files. ' + \
					    'By default, the files will use --file-list basenames as filenames and ' + \
					    '--dst/monthly_<indicie> as the destination directory.')
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="print messages to console")

    args = parser.parse_args()
    calc(args)