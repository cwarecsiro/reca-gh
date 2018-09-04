from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='climates',
      version='0.0.1',
      description='Climate processing tools',
      url='http://github.com/cwarecsiro/climates',
      author='Chris Ware',
      author_email='chris.ware@csiro.au',
      license='NA',
      packages=['climate_indicies'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'calc = climate_indicies.calc.__main__:main'
        ]
    },
)