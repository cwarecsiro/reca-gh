Climate indicies overview
=========================

Introduction
------------
Routines to calculate modified versions of seven of the standard climate indicies are available.  

See here for a description: https://icdc.cen.uni-hamburg.de/1/daten/climate-indices.html

And here for some more detail: https://icdc.cen.uni-hamburg.de/1/daten/climate-indices.html

Climate indicies description
----------------------------
The main routine in climate_indicies will calculate the monthly climatology of indicies over a period of years, and summarize this first by avergeing over months, and then by finding the chosen summary statistic over the 12 averaged months.  
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
			