install
=======

install R pkg
-------------

::
  >>> library(devtools)
  >>> install_github('cwarecsiro/reca-gh/gdmtables/pyper.git')


install py pkg
--------------

::
  >>> url = 'git+https://github.com/cwarecsiro/reca-gh/gdmtables/geonpy.git'

Ways to find a python exe on windows ::
  >>> Sys.which('python')
  >>> grep('python', Sys.getenv())

Anaconda might be installed here: ::
  >>> usr = unname(Sys.info()['user'])
  >>> py_exe = sprintf('C:\\User\\%s\\AppData\\Local\\Continuum\\Anaconda3\\python.exe',
                 usr)

Else... ::
  >>> py_exe = 'python'
  >>> py_exe = 'python3'


Format call for local install: ::
  >>> pip = sprintf('%s pip install --user %s', py_exe, url)

Or admin access install: ::
  >>> pip = sprintf('%s pip install %s', py_exe, url)

Install pkg: ::
  >>> stdout = system(pip, intern = TRUE)

For ease, optionally set python PATH variable: ::
  >>> shell('setx PATH "C:\\Users\\war42q\\AppData\\Local\\Continuum\\Anaconda3\\python.exe"')
