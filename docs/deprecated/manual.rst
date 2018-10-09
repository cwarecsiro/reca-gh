``climate_indicies`` use
========================

Calculating climate indicies 
----------------------------
basic use goes something like this from within python:: 

	>>> from climates.climate_indicies import core 
	>>> TXx = core.TXx(monthly_tmin)

where monthly_tmin.nc might be loaded using the following:: 

	>>> from maclab.maclab import spatial as sp 
	>>> monthly_tmin_dataset = sp.Raster(monthly_tmin.nc) 
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