"""
windows
=======

Module to help calculate the climate window stats for a given 2d time series

The main function will be passed a 2D array where the columns denote months, and rows different coordinates.
This will then need to be summarised into a 1D array. Pass in the same args as denote the variable naming schema to 
determine methods applied. Or can this be determined by passing in a variable code? For example, is TX always MAX_CMEAN_MAX?
Probably. And the first max is irrelevant anyway as it's already calculated. The only fiddly bit it working out how to 
chop the time series up. Go with back-calculating 12 months from the month in question, and then for the years specified in the
window arg. Can revise later.

"""

import sys, os, re, numpy as np
import pandas as pd
from itertools import groupby
import operator, json
import pandas as pd
import feather

STATS = {'TX': 'max', 'TN': 'min', 'PT': 'mean'}

def parse_stat(stat):
    return(getattr(np, stat))

def calc_climatology_window(arr, stat):
    
    cuts = arr.shape[1] / 12
    cuts = np.arange(0, arr.shape[1], 12).tolist()
    yearly = np.dstack([arr[:, i:i + 12] for i in cuts])
    yearly_mean = np.mean(yearly, axis = 1)
    stat = parse_stat(stat)
    yearly_stat = stat(yearly_mean, axis = 1)
    
    # anything else?
    
    return(yearly_stat)
