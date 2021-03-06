__author__ = 'Patrick Emami'

from setuptools import setup, find_packages

VERSION = '1.0.2'
DESCRIPTION = 'A Python Framework for implementing Discrete and Continuous POMDPs'

setup(name='POMDPy',
      version=VERSION,
      description=DESCRIPTION,
      author='Patrick Emami',
      author_email='pemami@ufl.edu',
      url='http://pemami4911.github.io/POMDPy/',
      packages=find_packages(),
      package_data={
          'pomdpy': ['config/*.json', 'config/*.txt']
          },
      license='MIT',
      install_requires='numpy'
      )
