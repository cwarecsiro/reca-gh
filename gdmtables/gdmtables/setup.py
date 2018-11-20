from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension("gdmtables", ["/OSM/CBR/LW_BACKCAST/work/code/reca-gh/gdmtables/gdmtables/sample_sitepairs.pyx"],
             include_dirs=[numpy.get_include()],
             #extra_compile_args=['-qopenmp'],
             #extra_link_args=['-qopenmp']),   
             )]
    #Extension(
    #    "manhatten",
    #    ["/home/war42q/SGAT/manhatten.pyx"],
    #    include_dirs=[numpy.get_include()],
    #    extra_compile_args=['-qopenmp'],
    #    extra_link_args=['-qopenmp'],
    #)
    


setup(
    name='gdmtables',
    ext_modules=cythonize(ext_modules),
)