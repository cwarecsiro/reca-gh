User Manual
===========

Introduction
------------

This package will (hopefully) collect different climate related
processing routines.

Presently, it only houses those to derive a few climate indicies with.

Climate indicies description
----------------------------
Routines to calculate modified versions of seven of the standard climate indicies are available.  

The main routine will calculate the monthly climatology of indicies over a period of years, and summarize this first by avergeing over months, and then by finding the chosen summary statistic over the 12 averaged months.  
For example, given a 30 year window between 1946-1975, the calculation for TXx goes as follows:

1. calculate monthly maximum of daily maximum temperature
2. calculate the mean monthly maximum for each month between 1946-1975
3. for each cell, find the maximum value.  

:TXx:
	The maximum of the average monthly extreme maximum temperatures. 
	
	Where :math:`TXx` is the maximum of average monthly maximum daily maximum temperatures, calculated for month :math:`k`, and year :math:`j`, in :math:`N` years.   
		.. math::
			TXx = max(\frac{\sum_{n=1}^{j}max(tmax\_daily_{kj})}{N})
		
:TXn:
	The minimum of the average monthly extreme maximum temperatures.  
	
	Where :math:`TXn` is the minimum of average monthly maximum daily maximum temperatures, calculated for month :math:`k`, and year :math:`j`, in :math:`N` years.   
		.. math::
			TXn = min(\frac{\sum_{n=1}^{j}max(tmax\_daily_{kj})}{N})

:TNx:
	The maximum of the average monthly extreme minimum temperatures.  
	
	Where :math:`TNx` is the maximum of average monthly minimum daily minimum temperatures, calculated for month :math:`k`, and year :math:`j`, in :math:`N` years.   
		.. math::
			TNx = max(\frac{\sum_{n=1}^{j}min(tmin\_daily_{kj})}{N})
		
:TNn:
	The minimum of the average monthly extreme minimum temperatures.  
	
	Where :math:`TNn` is the minimum of average monthly minimum daily minimum temperatures, calculated for month :math:`k`, and year :math:`j`, in :math:`N` years.   
		.. math::
			TNn = min(\frac{\sum_{n=1}^{j}min(tmin\_daily_{kj})}{N})
			
:R1:
	The maximum of the average monthly count of days when precipitation > 1mm.
	
	Where :math:`R1` is the maximum of the average monthly count of days where precipitation > 1mm for for :math:`d` days in month :math:`k`, and year :math:`j`, in :math:`N` years. 
		.. math::
			R1 = max(\frac{\sum_{n=1}^{j}(\sum_{n=1}^{d}(ppt\_daily_{dkj}))}{N})
			
:Rx1day:
	The maximum of the average monthly extreme precipitation.
	
	Where :math:`Rx1day` is the maximum of the average monthly maximum daily precipitation, calculated for month :math:`k`, and year :math:`j`, in :math:`N` years. 
		.. math::
			Rx1day = max(\frac{\sum_{n=1}^{j}max(ppt\_daily_{kj})}{N})

:FD:
	The maximum of the average monthly count of days when temperatures were < 0°C.
	
	Where :math:`FD` is the maximum of the average monthly count of days where daily minimum temperatures were < 0°C for :math:`d` days in month :math:`k`, and year :math:`j`, in :math:`N` years.
		.. math::
			FD = max(\frac{\sum_{n=1}^{j}(\sum_{n=1}^{d}(tmin\_daily_{dkj}))}{N})
			
Calculating climate indicies 
----------------------------
basic use goes something like this from within python:: 

	>>> from climates.climate_indicies import core 
	>>> TXx = core.TXx(monthly_tmin)

where monthly_tmin.nc might be loaded using the following:: 

	>>> from maclab.maclab import spatial as sp 
	>>> monthly_tmin_dataset = sp.Raster(monthly\_tmin.nc) 
	>>> monthly_tmin = monthly_tmin_dataset.read().array  
	

Command line interface
----------------------
climate_indicies is primarily set up as a command line tool, figuring
it might be useful for others, and only to run as jobs submitted to a cluster.

It can be used as follows (to get help)

.. code-block:: console

    $ calc --help
	usage: calc.py [-h] -f FILE_LIST -i INDICIE [INDICIE ...] [-a ARGS_DICT] [-k]
				-d DST [-fn FILENAME] [-w] [-v]

	Derive climatologies of climate indices

	optional arguments:
	-h, --help            show this help message and exit
	-f FILE_LIST, --file-list FILE_LIST
							path to txt file with list of nc files. <Required> Set
							flag
	-i INDICIE [INDICIE ...], --indicie INDICIE [INDICIE ...]
							list of indicies to calculate. To view, call
							$calc_indicies.py --options<Required> Set flag
	-a ARGS_DICT, --args-dict ARGS_DICT
							additional args to supply to any indicie functions
							called. These need to be passed as a dictionary.
							<Optional> Set flag
	-k, --cel2kel         Convert input array from celsius to kelvin. <Optional>
							Set flag
	-d DST, --dst DST     destination directory to write to.Will be created if
							it does not exist <Required> Set flag
	-fn FILENAME, --filename FILENAME
							String to add to add to the filename. By default, the
							filename is given as <indicie>.tif. <Optional> Set
							flag
	-w, --write-months    write monthly indicies to files. By default, the files
							will use --file-list basenames as filenames and
							--dst/monthly_<indicie> as the destination directory.
	-v, --verbose         print messages to console
	
	Note: indicies available are: TXx TNx TXn TNn FD R1 Rx1day

and to caclualte TXx, for example

.. code-block:: console

    $ calc -f filelist.txt -i TXx -d tifs -v