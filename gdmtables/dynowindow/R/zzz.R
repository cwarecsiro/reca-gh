.onLoad = function(libname, pkgname){
  
  this_env = unname(Sys.info()['sysname'])
  
  if(this_env == 'Windows'){
    
    pth = unname(Sys.which('python'))
    if (pth == ''){
      pth = NULL
    }
    
    conda = 'C:\\Users\\war42q\\AppData\\Local\\Continuum\\Anaconda3\\python.exe'
    if(file.exists(conda)){
      pth = c(pth, conda)
    }
    
    sys_conda = 'C:\\ProgramData\\Anaconda3\\python.exe'
    if(file.exists(sys_conda)){
      pth = c(pth, sys_conda)
    }
    
    if(is.null(pth)){
      warning(sprintf('%s %s', 
                      'Cannot locate a version of python.', 
                      'A variable exe needs to be available pointing to a python .exe'))
    } else {
      
      # probably should choose among these sensible (by date?) Choose opt 1 for now.
      exe <<- pth[1]
      
    }
    
  } else {
    
    # assume linux - this good enough?
    # Should test this? 
    # vers = system(python -c 'import sys; print sys.version_info', intern = TRUE)
    
    exe <<- 'python3'
    
  }

}