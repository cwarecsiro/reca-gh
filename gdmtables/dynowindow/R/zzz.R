.onLoad = function(libname, pkgname){
  
  this_env = unname(Sys.info()['sysname'])
  
  if(this_env == 'windows'){
    
    pth = unname(Sys.which('python'))
    if (pth == ''){
      pth = NULL
    }
    
    conda = 'C:\\Users\\war42q\\AppData\\Local\\Continuum\\Anaconda3\\python.exe'
    if(file.exists(conda)){
      pth = c(pth, conda)
    }
    
    if(is.null(pth)){
      warning(sprintf('%s %s', 
                      'Cannot locate a version of python.', 
                      'A variable exe needs to be available pointing to a python .exe'))
    } else {
      
      exe <<- pth[1]
      
    }
    
  } else {
    
    # assume linux - this good enough?
    
    exe <<- 'python3'
    
  }

}