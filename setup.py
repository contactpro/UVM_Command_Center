# -*- coding: utf-8 -*-
# A setup.py script to create an executable of a Python Contact Manager Tkinter App.
# contact_management_python.py is the Contact Management Tkinter application source code.
# This also demonstrates the method for creating a Windows executable that
# does not have an associated console. This setup.py script is also used
# to create the MSI install file.
#
# This setup.py script is typically run with the following commands:
#
# COMMAND to BUILD and create the EXECUTABLE:   python setup.py build
#
# COMMAND to DISTRIBUTE and create the MSI INSTALLER:   python setup.py bdist_msi
#
# PLEASE FOLLOW THESE DIRECTIONS ......
#
# STEP #1:    python setup.py build 
# 
# Run the build process by running this setup.py script with
# the command: 'python setup.py build'
#
# COMMAND OPTIONS: http://cx-freeze.readthedocs.io/en/latest/script.html 
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application.
#
# STEP #2:
#
# Check the \build directory to verify a successful BUILD was executed
# by looking for the contact_management_python.exe that was created
# in \build\exe.win-amd64-3.6 directory.
#
# *** Be sure to copy the _methods.py file to the proper directory
# as noted at the end of this comments section.
#
# Then, Verify the application runs by typing contact_management_python.exe
# or by double clicking "contact_management_python.exe". 
#
# STEP #3:
#
# Resolve any BUILD errors that may appear
# as a POP-UP BOX by googling the solution, typically on stackoverflow. 
#
# Once the contact_management_python.exe runs successfully (with no error box popup),
# then the setup.py script has generated a CLEAN BUILD or a GOOD BUILD,
# by creating the "contact_management_python" executable, which you verified
# by observing that the application runs as expected. 
#
# STEP #4:    python setup.py bdist_msi 
# 
# Next, Generate the MSI Installer script to enable you to install and distribute
# your executable by running the this same setup.py script with
# the command "python setup.py bdist_msi" which will create
# a directory called /dist where you will see the MSI installer
# script called "CM-14.2-amd64.msi"
#
# COMMAND OPTIONS: http://cx-freeze.readthedocs.io/en/latest/distutils.html 
#
# Note that the MSI Installer executable that installs this contact management
# application is named CM-14.2-amd64.msi and is located in the /dist folder
# below where you just ran the setup.py script.
#
# STEP #5:
#
# Copy the MSI installer, CM-14.2-amd64.msi, to a new Folder named something like
# C:/...... /CM_MSI_INSTALLER_VERSION_14.2/ and then double click on the CM-14.2-amd64.msi
# installer to verify the install script presents a pop-up window asking you
# which directory you want to install the application in.
#
# Click NEXT to install the application and then click FINISH.
#
# STEP #6:
#
# Once the Installer is finished, locate the EXECUTABLE called "contact_management_python.exe"
# and right click on the EXECUATBLE "contact_management_python.exe" and select PIN-TO-START-MENU.
# Then go to your WINDOWS 10 Start Menu and Click on the contact_management Icon to run
# the Contact Management Application.
#
# STEP #7:
#
# Verify that the "contact_management_python" application runs by creating
# a new CONTACT LIST and adding some data and SAVING the data and then VIEW the DATA
# using all the buttons and functionality in the Contact Management Application.
#
######################################################################################
#
# We need this:
#
# build_exe_options = {
# "include_msvcr": True  
# }
#
######################################################################################
#
#  NOTE: The actual paths below have changed and are now simply examples ....
#        Actual Paths (below) of Python36/Lib ....
#        and PYTHON_3_FREEZE/work_fourteen/build/exe.win-amd64-3.6/lib/numpy/core ....
#        need to be updated (!!!) 
#
######################################################################################
#
# Adding to numpy includes in main py file and setup, and also ....
#
# Need to COPY this file:  (Forward / may be required in script)
# 
# c:/Users/chipcoder4972/AppData/Local/Programs/Python/Python36/Lib/site-packages/numpy/core/_methods.py
#
# to this path after BUILD:
#
# c:/Users/chipcoder4972/Desktop/Documents/PYTHON_3_CODE/PYTHON_3_FREEZE/work_fourteen/build/exe.win-amd64-3.6/lib/numpy/core/_methods.py
#
################ Same _methods.py file just with forward or backward file path ##############
#
# Need to COPY this file:  
# 
# c:\Users\chipcoder4972\AppData\Local\Programs\Python\Python36\Lib\site-packages\numpy\core\_methods.py
#
# to this path after BUILD:
#
# c:\Users\chipcoder4972\Desktop\Documents\PYTHON_3_CODE\PYTHON_3_FREEZE\work_fourteen\build\exe.win-amd64-3.6\lib\numpy\core\_methods.py
#
#############################################################################################
#
# I solve it by
# find "_methods" in site-packages/numpy/core/ and copy it to build/exe.win-amd64-3.6/numpy/core/,
# build and run and it works.
#
# Maybe we can eventually script the above copy with: 
#
# os.path.join(PYTHON_INSTALL_DIR, 'Lib', 'site-packages', 'numpy', 'core', '_methods.py')],
# 
######################################################################################


from __future__ import print_function
import httplib2
import pprint
import os
import subprocess
import glob
import socket
import urllib.parse
import urllib.request
import inspect
import webbrowser
import shutil
# from PIL import ImageTk, Image
from PIL import Image
from PIL import ImageTk
from shutil import copyfile
import platform
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email.utils import make_msgid
from email.utils import formatdate
import csv
import sys
import traceback
import threading
import time
import datetime
import random
import configparser
import xlsxwriter
import numpy
import pandas as pd

import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from tkinter.messagebox import *

from configparser import ConfigParser

from openpyxl import workbook

# integration of gmail send scope oauth2 json

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes

from apiclient import errors

#try:
#    import argparse 
#    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
#except ImportError:
#    flags = None

from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('contact_management_python.py', base=base)
]

print("\n" + "..... BUILD and DIST Executable = contact_management_python.py")
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
print("\n" + "..... PYTHON_INSTALL_DIR = " + str(PYTHON_INSTALL_DIR) )
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
print("\n" + "..... TCL_LIBRARY = " + str(os.environ['TCL_LIBRARY']) )
print("\n" + "..... TK_LIBRARY = " + str(os.environ['TK_LIBRARY']) )
print("\n")

build_exe_options = {'build_exe': {
    'include_files':[os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), \
                     os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')],
    'include_msvcr': True
    }}

setup(name='CM',
      version='14.2',
      description='cx_Freeze Tkinter script for contact_management_python.py - version 14.2 - 64Bit',
      options = build_exe_options,
      executables=executables
      )


