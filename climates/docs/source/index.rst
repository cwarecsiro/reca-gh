.. climates documentation master file, created by
   sphinx-quickstart on Mon Sep  3 11:55:16 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Climates documentation
======================
``climates`` is a package for climate related processing. 
Includes routines for calculating climate indicies only at present.  
  
Requires
--------  
maclab package to be installed  

Quickstart
----------

Install:: 

	pip --user git+ etc  


Example::
	
	$module load python/3.6.1
	$calc -f filelist.txt -i TXx -d tifs -v
	

Package contents
----------------
.. toctree::
   :maxdepth: 3
   
   manual
   climate_indicies


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
