#' @title Obs-pair climate window builder thing 
#' 
#' @description Generate climate window summary variables for obs-pair input
#' 
#' @param pairs str(filepath) or data.frame like object. Obs pair table with year and month cols (x1, y1, year1, mon1, x2, y2 etc).
#' @param variables vector of variable names. Variable names must be file names without an extension.
#' @param mstat str, statistic to summarize monthly variables to a notional year.
#' @param cstat str, statistic to summarize yearly variables over window period.
#' @param window int, length of climate window in years.
#' @return data.frame
#' 
#'@importFrom feather write_feather read_feather
#'@export
gen_windows = function(pairs, variables, mstat, cstat, window, 
                       pairs_dst = NULL, npy_src = NULL){
  
  if(!exists('exe')){
    stop(sprintf('%s %s', 
                 'Cannot locate a version of python.', 
                 'A variable exe needs to be available pointing to a python .exe'))
  }
  
  type_pairs = class(pairs)
  if(type_pairs != 'character'){
  
    # data.frame like
  
    if(!is.null(pairs_dst)){
      path_dst = tempfile(fileext = '.feather')
    }  
    
    write_feather(pairs_dst, pairs)
    
  } else {
    
    pairs_dst = pairs
  }
    
  pyfile = paste(.libPaths(), 'dynowindow/exec/pyper.py', sep = '/')
  
  call = sprintf('%s %s -f %s -s %s -m %s -e %s -w %s -src %s', 
                 exe, pyfile, pairs_dst, mstat, cstat, variables, window)
  
  if(!is.null(npy_src)){
    call = sprintf('%s -src %s', call, npy_src)
  }
  
  # pass to python
  output_fp = system(call, intern = TRUE)
  
  # ...?
  output = tryCatch({
    read_feather(output_fp)
  }, error = function(e){e}
  )
  
  if(!length(grep('data.frame', class(output)))){
    stop(sprintf('Could not read %s', output_fp))
  
  } else {
    
    return(as.data.frame(output))
  }
  
}

# exe = 'C:\\Users\\war42q\\AppData\\Local\\Continuum\\Anaconda3\\python.exe'
# src = '//lw-osm-02-cdc/OSM_CBR_LW_BACKCAST_work/code/reca-gh/gdmtables/gdmtables/pyper.py'
# f = '//lw-osm-02-cdc/OSM_CBR_LW_BACKCAST_work/DEV/war42q/junk/testxy.feather'
# s = 'mean'
# m = 'mean'
# e = 'ND_test'
# src_g = '//lw-osm-02-cdc/OSM_CBR_LW_BACKCAST_work/DEV/war42q/junk'
# 
# call = sprintf('%s %s -f %s -s %s -m %s -e %s -w %s -src %s',
#                exe,
#                src, f, s, m, e, 15, src_g)
# 
# system(call, intern = TRUE)
# file.exists('C:\\Users\\war42q\\AppData\\Local\\Temp\\tmp05aifbn8.feather')
