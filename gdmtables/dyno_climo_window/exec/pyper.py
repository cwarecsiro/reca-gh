"""
pyper
=====

Conduit between R and python to create temporal obs-pair tables.

Must: 
- accept a list of variable names that match existing geonpy files.
"""
import feather
import subprocess
import argparse
import sys
import os
import re
import tempfile
import numpy as np
#import geonpy
import sys, os
sys.path.append('//lw-osm-02-cdc/OSM_CBR_LW_BACKCAST_work/code/reca-gh/gdmtables/dyno_climo_window/exec')
import testmod

ROOT = '/OSM/CBR/LW_BACKCAST/work/DEV/geonpy'

def write_feather(arr, dst, variables):
    df = pd.DataFrame(arr)
    varnames = [os.path.basename(i) for i in variables]
    varnames = [i.split('.')[0] for i in varnames]
    varnames = ['{}_1'.format(i) for i in varnames]
    varnames = ['x_1', 'y_1', 'x_2', 'y_2'] + varnames + varnames
    df.columns = varnames
    feather.write_dataframe(df, dst)

    
def read_feather(src):
    """Read feather site-pair file
    
    Parameters
    ----------
    src: str, filepath, required
        File must be feather format, and have four cols (x1, y1, x2, y2)
            
    Returns
    -------
    Numpy array
    """
    df = feather.read_dataframe(src)
    #df.columns = ['x1', 'y1', 'x2', 'y2']
    return(np.array(df))


def config(args):
    """Config optparse args. """
    # -f
    pairs = read_feather(vars(args)['filepath'])
    
    # -src
    src = vars(args)['variable_source']
    if not src:
        src = ROOT
    
    # -e 
    var = vars(args)['variable_list']
    variables = ['{}/{}.npy'.format(src, i) for i in var]
    check = [os.path.exists(i) for i in variables]
    if not all(check):
        err = [variables[i] for i in range(len(variables)) if not check[i]] 
        raise(FileNotFoundError('Could not find {}'.format(err)))
    
    # -s
    stat = vars(args)['clim_stat']
    cstat = getattr(np, stat)
    
    # -m
    stat = vars(args)['month_stat']
    mstat = getattr(np, stat)
    
    # -w 
    window = vars(args)['window']
    
    # -d
    d = tempfile.NamedTemporaryFile(suffix='.feather').name   
    
    return(pairs, variables, mstat, cstat, d)
    
    
def main(args):
    """Main function. """
    pairs, variables, mstat, cstat, window, d = config(args)
    
    # output container...
    output = np.zeros((pairs.shape[0], len(variables))).astype('float32')
    
    # sites
    s1_sites = pairs[:, 0:2]
    s2_sites = pairs[:, 4:6]
    sites = [s1_sites, s2_sites]
    
    # indexes
    t1 = pairs[:, 2:4]
    t2 = pairs[:, 6:8]
    s1_slices = gen_multi_index_slice(t1, window)
    s2_slices = gen_multi_index_slice(t2, window)
    slices = [s1_slices, s2_slices]
    
    # loop over sites and variables
    for s in range(2):
        
        v_idx = 0
        for v in variables:
        
            var_v = Geonpy(v)
            pairs[:, v_idx] = var_v.read_points(sites[i], dim_idx = slices[i])  
            del var_v
            
            v_idx += 1
        
    output = np.hstack([pairs, output])
    write_feather(output, d, variables)
    
    # print(main) on run
    return(d)

def main_test(args):
    #pairs, variables, mstat, cstat, d = config(args)
    testmod.foo()
    return
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Coordinates from R to python - variablefy - pass back to R',
                                    add_help=True,
                                    epilog="Note: variables available are: \n" + \
                                    "TX TN FD R1 etc")
    parser.add_argument('-f','--filepath', \
                        help='path to feather file containing obs/site-pair coordinates. ' + 
                        'Must include columns of dates (year and month) for each coordinate. ' + 
                        'E.g. x1, y1, year1, month1, x2, y2 etc... <Required> Set flag', required=True)
    parser.add_argument('-e','--variable-list', nargs='+', \
                        help='variables to extract. Names need to match file names in src(without ext). ' + 
                        '<Required> Set flag', required=True)
    parser.add_argument('-s', '--clim-stat', \
                        help='stat to apply over the climatology. ' + \
                        'Needs to be something numpy recognizes. Note that for range this should be ptp.' +
                        '<Required> Set flag', required=True)
    parser.add_argument('-m', '--month-stat', \
                        help='stat to apply over months. ' + \
                        'Needs to be something numpy recognizes. Note that for range this should be ptp.' +
                        '<Required> Set flag', required=True)
    parser.add_argument('-w', '--window', \
                        help='window length in years. ' + \
                        '<Required> Set flag', required=True)
    parser.add_argument('-d','--dst', \
                        help='destination directory to write to.' + \
                        'Will use temp if it does not exist. <Optional> set flag',\
                        required=False)
    parser.add_argument('-src', '--variable-source', \
                        help='Path to geonpy files. Default option is given. ' + \
                        'Which is... <Optional> Set flag')
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="print messages to console")

    args = parser.parse_args()
    print(main_test(args))
    