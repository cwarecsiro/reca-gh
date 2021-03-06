% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/dynowindow.R
\name{gen_windows}
\alias{gen_windows}
\title{Obs-pair climate window builder thing}
\usage{
gen_windows(pairs, variables, mstat, cstat, window, pairs_dst = NULL,
  npy_src = NULL)
}
\arguments{
\item{pairs}{str(filepath) or data.frame like object. Obs pair table with year and month cols (x1, y1, year1, mon1, x2, y2 etc).}

\item{variables}{vector of variable names. Variable names must be file names without an extension.}

\item{mstat}{str, statistic to summarize monthly variables to a notional year.}

\item{cstat}{str, statistic to summarize yearly variables over window period.}

\item{window}{int, length of climate window in years.}
}
\value{
data.frame
}
\description{
Generate climate window summary variables for obs-pair input
}
