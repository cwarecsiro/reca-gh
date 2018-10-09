Project methods
===============

Developing and describing climatology’s of extremes from daily climate data
---------------------------------------------------------------------------

Here we describe an approach to summarise long-term daily climate data to capture both average trends and extremes for a specified period. Climatology’s are traditionally described either by mean conditions for each month of the year over a number of years (e.g. total rainfall in July 1970-1980), and their extremes by annual anomalies (e.g. time series of hottest day for each year). These approaches follow a common approach, working from daily data and then summarising along two dimensions of time, within and between years, and in the case of mean values for a period, are identical. However, when extremes, such as maximum and minimum are considered, there is a divergence of information content.
Two main types of climate data are recorded, those that accumulate (such as precipitation and evaporation: e.g. 20mm + 23mm= 43mm over two days) and those that don’t, such as temperature (20°C & 23°C != 43°C over two days). The former are often accumulated over a period (e.g. Total Monthly or Annual Precipitation), whereas the latter are usually averaged (e.g. Mean Monthly or Annual Temperature). However, it is equally valid to summarise accumulating data as a mean daily value. This has three advantages: 1. the two data types are presented in a compatible form, 2. There is no need to consider the variable number of days in a month once the statistics have been calculated (consider total precipitation for Jan, 31 days and Feb, 28/29 days), 3. Mean for period, maximum daily and minimum daily measures are directly comparable.

**Step 1: Summary of daily data into monthly data**
A first step in all cases is to calculate monthly statistics for all months in a period (e.g., 1981-1991). Four statistics are calculated; mean of daily data (MEAN), maximum of daily data (MAX), minimum of daily data (MIN) and range (RNG), as MAX-MIN, taking differing month lengths into account. These are all in units with a daily time stamp: evaporation per day (md-1), mean daily temperature (°C).

.. image:: ./images/fig1.png	
  :width: 400
  :align: center
Figure 1: Calculating monthly statistics.

The resultant data comprise four matrices (month by year) of monthly statistics. Each of these can be summarised in two ways:

**Method 1: “Climatology”**
This is the approach applied as standard for calculating average long term monthly statistics. For each of the matrices, statistics are first calculated for all years in the period for each month. Then the 12 monthly statistics are summarised to generate a statistic for the whole matrix.

.. image:: ./images/fig2.png	
  :width: 800
  :align: center

**Method 2: “Weather”**
Alernatively, annual summary statistics can be calculated first. This is the approach employed to examine inter-annual variation and anomalies. For each of the matrices, statistics (daily mean, minimum or maximum) are first calculated for all months in the period for year. Then the annual statistics are summarised to generate a statistic for the whole matrix.

.. image:: ./images/fig3.png	
  :width: 800
  :align: center

These two approaches will generate the same results for the mean calculation, but will present different summaries for the other variables. Consider an input matrix of the maximum (MAX) precipitation for all months calculated from daily data. If we then calculate the maximum (MAX) using the two methods, we will measure different things. Using method 1, we first calculate the maximum (MAX) of this matrix for each month, i.e. the highest recorded precipitation in each of the 12 months for each year. This could then be averaged (MEAN) within each of the months across all years, and then also (MEAN) across all the monthly averages, to obtain the annual mean of the maximum monthly precipitations for the period. Using method 2, we first calculate the maximum (MAX) for each year, i.e. the highest precipitation in each year. This could then be averaged (MEAN) across all years to obtain the mean of the annual maximum precipitations for the period. The second approach will average the wettest days in all years (a descriptor of the wettest part of the year), whereas the first approach will average the wettest days of each month, providing a description of the whole year.

Kristen: If the annual mean is the goal, do they both end up the same?  

Kristen: Could you present as equations also?   

Kristen: H0: Applied across different merological variables (precipitation, maximum and minimum temperatures), approach 1 retains more of the inherent seasonal relationships among variables, and is more likely to have a stronger correlation with ecological responses. 


