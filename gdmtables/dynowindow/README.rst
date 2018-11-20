Install
=======

**install R pkg**

  >>> library(devtools)
  >>> install_github('cwarecsiro/reca-gh/gdmtables/pyper.git')


**install py pkg**

  >>> url = 'git+https://github.com/cwarecsiro/reca-gh/gdmtables/geonpy.git'
  >>> pip = sprintf('python pip install --user %s', url)
  >>> stdout = system(pip, intern = TRUE)
Remove ``--user`` flag to install system wide  

Ways to find a python exe on windows
  >>> Sys.which('python')
  >>> grep('python', Sys.getenv())

Anaconda installation might be here:
  >>> usr = unname(Sys.info()['user'])
  >>> py_exe = sprintf('C:\\User\\%s\\AppData\\Local\\Continuum\\Anaconda3\\python.exe',
                 usr)

For future ease, optionally set python PATH variable: ::
  >>> shell('setx PATH "C:\\Users\\war42q\\AppData\\Local\\Continuum\\Anaconda3\\python.exe"')
