"""Create test nc file set"""

import xarray, numpy as np
template = np.zeros((2,2))
daily = [template + i for i in range(1, 366)]
months = np.cumsum(np.array([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
monthly = [daily[months[i]:months[i+1]] for i in range(12)]
yearly_1 = [xarray.DataArray(np.dstack(m)) for m in monthly]
yearly_2 = [y + 1 for y in yearly_1]

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
names_1 = ['{0}/{1}_2017.nc'.format(test_dir, m) for m in months]
names_2 = ['{0}/{1}_2018.nc'.format(test_dir, m) for m in months]
for i in range(12):
    A = np.rollaxis(np.array(yearly_1[i]), 2)
    N = xarray.Dataset(
        data_vars={'climate':    (('day', 'x', 'y'), A)},
        coords={'x': [120, 130],
                'y': [-30, -40],
                'day': np.arange(1, A.shape[0] + 1, 1).tolist()})
    N.to_netcdf(names_1[i], 'w')
for i in range(12):
    A = np.rollaxis(np.array(yearly_2[i]), 2)
    N = xarray.Dataset(
        data_vars={'climate':    (('day', 'x', 'y'), A)},
        coords={'x': [120, 130],
                'y': [-30, -40],
                'day': np.arange(1, A.shape[0] + 1, 1).tolist()})
    N.to_netcdf(names_2[i], 'w')
    
files = names_1 + names_2
with open('/OSM/CBR/LW_BACKCAST/work/code/reca/climate_indicies/tests/filelist.txt', 'w') as f:
    for l in files:
        f.write(l + '\n')
    f.close()