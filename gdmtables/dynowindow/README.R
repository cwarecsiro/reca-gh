# install

library(devtools)
install_github('cwarecsiro/reca-gh/gdmtables/pyper.git')

url = 'git+https://github.com/cwarecsiro/reca-gh/gdmtables/geonpy.git'

# windows
Sys.which('python')
grep('python', Sys.getenv())

py_exe = 'C:\\Users\\war42q\\AppData\\Local\\Continuum\\Anaconda3\\python.exe'

usr_py = sprintf('%s pip install --user %s', py_exe, url)
sys_py = sprintf('%s pip install %s', py_exe, url)

shell('setx PATH "C:\\Users\\war42q\\AppData\\Local\\Continuum\\Anaconda3\\python.exe"')
