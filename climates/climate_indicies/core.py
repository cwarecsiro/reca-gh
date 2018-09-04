# -*- coding: utf-8 -*-
"""
Routines to calculate a select number of climate indicies

Indicies:
	- TXx: monthly maximum value of daily maximim temperature
	- TXn: monthly minimum value of daily maximim temperature	
	- TNx: monthly maximum value of daily minimum temperature
	- TNn: monthly minimum value of daily minimum temperature
	- R1: monthly proportion of days with rain
	- Rx1day: monthly maximum of daily precipitation
	- FD: monthly proportion of days with frost
	
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
import operator, json

def consecutive_days(arr, threshold = 1.0, logical_operation = '<'):
    """
	Calculate n consecutive days an operation is met for a threshold.
    
    Parameters
    ----------
    arr: ndarry
        time needs to be the first dim
    threshold: float, int
        number which to apply operation to
    logical_operation: str
        operator which can be understood by operator mappings.
        Supported are <, <=, >, >=, and ==
    
    Returns
    -------
    2D array 
    """
    mappings = {'<': operator.lt, '<=': operator.le,
                '==': operator.eq, '>': operator.gt,
                '>=': operator.ge} 
    rows, cols = arr.shape[1], arr.shape[2]
    n_elements = rows * cols
    n_days = arr.shape[0]
    arr = mappings[logical_operation](arr, threshold).astype(int)
    arr = arr.reshape(n_days, n_elements).T
    counter = []
    for line in arr:
        if 1 in line:
            counter.append(max(sum(1 for _ in g) for k, g in groupby(line) if k == 1))
        else:
            counter.append(0)
    output_2d = np.array(counter).reshape(rows, cols)
    return(output_2d)

def TXx(filepath):
    """Monthly maximum value of daily maximim temperature."""
    month = sp.Raster(filepath)
    meta = month.meta
    nodata = meta['nodata']
    data = month.read().array.astype('float32') # n days ndarray
    data = np.ma.array(data, mask = (data == nodata))
    return(np.max(data, axis = 2))
	
def TXn(filepath):
    """Monthly mimimum value of daily maximim temperature."""
    month = sp.Raster(filepath)
    meta = month.meta
    nodata = meta['nodata']
    data = month.read().array.astype('float32') # n days ndarray
    data = np.ma.array(data, mask = (data == nodata))
    return(np.min(data, axis = 2))
	
def TNx(filepath):
    """Monthly maximum value of daily minimum temperature."""
    month = sp.Raster(filepath)
    meta = month.meta
    nodata = meta['nodata']
    data = month.read().array.astype('float32') # n days ndarray
    data = np.ma.array(data, mask = (data == nodata))
    return(np.max(data, axis = 2))
	
def TNn(filepath):
    """Monthly minimum value of daily minimum temperature."""
    month = sp.Raster(filepath)
    meta = month.meta
    nodata = meta['nodata']
    data = month.read().array.astype('float32') # n days ndarray
    data = np.ma.array(data, mask = (data == nodata))
    return(np.min(data, axis = 2))
	
def Rx1day(filepath):
    """Monthly maximum 1-day precipitation."""
    month = sp.Raster(filepath)
    meta = month.meta
    nodata = meta['nodata']
    data = month.read().array.astype('float32') # n days ndarray
    data = np.ma.array(data, mask = (data == nodata))
    return(np.max(data, axis = 2))

def FD(filepath):
    """Monthly proportion of frost days."""
    month = sp.Raster(filepath)
    meta = month.meta
    nodata = meta['nodata']
    data = month.read().array.astype('float32') # n days ndarray
    data = np.ma.array(data, mask = (data == nodata))
    frost = data < 0
    return(np.sum(frost, axis = 2) / data.shape[2])
	
def R1(filepath, threshold = 1):
    """Monthly proportion of rain days."""
    month = sp.Raster(filepath)
    meta = month.meta
    nodata = meta['nodata']
    data = month.read().array.astype('float32') # n days ndarray
    data = np.ma.array(data, mask = (data == nodata))
    rain = data > threshold
    return(np.sum(rain, axis = 2) / data.shape[2])

def cel2kel(arr):
    """Convert masked array in Celsius to Kelvin."""
    arr+=273.15
    return(arr)
    