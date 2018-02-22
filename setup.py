'''
Created on 25 Jan 2018

@author: HP
'''

from setuptools import setup

setup(name = "system info",
      version = "0.1",
      description = "Basic info for Software Engineering",
      url = " ",
      author = "Amy McCormack",
      author_email = "amy.mccormack@ucdconnect.ie",
      license = "GPL3",
      packages = ['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
        }
      )
