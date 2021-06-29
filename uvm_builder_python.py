######################################################################
#
# Author: Michael Hughes
#
# Program: uvm_builder_python.py 
#  
# Version: Demo 
#   
# Date:  
#
# Description: UVM Testbench Builder
#
# Language: Python 3.6.2
#
######################################################################
#
#      In main():
#
#      root = tk.Tk()
#      cm_app = App(root)
#
#      In App(root) are the Toplevels:
#
# ..root = tk.Tk() = .
# .... each object = .!app
# .... each_object = .!toplevel.!excel_import_export
# .... each_object = .!toplevel2.!app_status_panel
# .... each_object = .!toplevel3.!cm_app_doc_media
# .... each_object = .!toplevel4.!user_gui_config_class
# .... each_object = .!toplevel5.!user_gui_config_class
# .... each_object = .!toplevel6.!user_gui_config_class
# .... each_object = .!toplevel7.!list_builder
# .... each_object = .!toplevel8.!view_contact_list
# .... each_object = .!toplevel9.!new_contact_list
# .... each_object = .!toplevel10.!select_contact_list
# .... each_object = .!toplevel11.!system_admin_info
# .... each_object = .!toplevel12.!email_gmail_class
# .... each_object = .!toplevel13.!config_setting_class
#
######################################################################
#
# get ip address ... similar to windows command line: ipconfig
# 
# import socket
# 
# socket.gethostname()
# 
# socket.gethostbyname(socket.getfqdn())
# 
# https://www.youtube.com/watch?v=h-drFf4oU24
#
#####################################################################
#
#  VERSION 14.1 CHANGE:  home_dir = userprofile_global # os.path.expanduser('~')
# 
######################################################################

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

##############################################################################
#  
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
#
SCOPES = "https://mail.google.com"
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
selected_email_address_LIST_GLOBAL = []
DEST_or_CC_email_address_FLAG_GLOBAL = ""
email_list_from_listbox_ready_global = False
hostname_via_socket = "HOSTNAME_VIA_SOCKET_NOT_SET"
ipv4_address_global  = "IPv4_Address_NOT_SET"
contact_lists_dict_count = "Count_Not_Set"
contact_lists_csv_count = "Count_Not_Set"
gmail_oauth2_json_file_test_global = None
gmail_oauth2_status_global = None
gmail_oauth2_exceptions_status_global = None
gmail_oauth2_SPECIFIC_EXCEPTION_global = "Specific_OAUTH2_Exception"
gmail_smtp_allow_less_secure_apps_global = None
gmail_smtp_status_global = None
gmail_smtp_exceptions_status_global = None
gmail_smtp_SPECIFIC_EXCEPTION_global = "Specific_SMTP_Exception"
gmail_logged_in_global = None
cm_dict_file_startup_test_global = None
cm_csv_file_startup_test_global = None
cm_notes_file_startup_test_global = None
insert_first_contact_global = False
gmail_mode_global = "gmail_mode_global NOT SET"
fullpath_gmail_oauth2_credentials_global = "PATH NOT SET for client_secret.json"
fullpath_exception_logfile_global = "EXCEPTION LOGFILE PATH NOT SET"
credential_home_dir_global = "PATH NOT SET for credential_home_dir_global"
credential_appdata_dir_global = "PATH NOT SET for credential_appdata_dir_global"
credential_home_path_global = "PATH NOT SET for credential_home_path_global"
credential_appdata_path_global = "PATH NOT SET for credential_appdata_path_global"
client_secret_path_global = "PATH NOT SET for client_secret_path_global"
client_secret_dir_global = "PATH NOT SET for client_secret_dir_global"
valid_client_secret_key_format_global = False
mode_select_global = "MODE Not Set"
mode_select_build_list_global = "BUILD LIST MODE Not Set"
request_mainscreen_config_update_global = False
textbox_edit_mode_select_global = "TEXTBOX EDIT MODE NOT SET"
listbox_color_value_global = "dark slate gray"  # "COLOR CONFIGURATION LISTBOX INITIALIZATION"
listbox_color_moment_global = "dark slate gray" # "LISTBOX COLOR MOMENT INITIALIZATION"
selected_dictionary_loaded_global = {}
selected_dictionary_record_index_global = 1
selected_dictionary_record_index_focus_global = 1
kick_thread_to_update_main_entry_widgets = False
kick_thread_to_update_email_contact_entry_widgets = False
num_of_dictionary_data_records_global = 0
username_global = "USERNAME Path Not Set"
userprofile_global = "USERPROFILE_GLOBAL_NOT_SET"
appdata_path_global = "APPDATA Path Not Set"
cm_appdatafiles_path_global = "CM_APPDATAFILES Path Not Set"
fullpath_app_config_ini_global = "APPDATA_CONFIG_INI Path Not Set"
fullpath_med_config_ini_global = "MEDICAL_RECORD_INI Path Not Set"
mainscreen_bg_color_val_global = "ivory4"
viewscreen_bg_color_val_global = "ivory4"
selectlist_bg_color_val_global = "ivory4"
newlist_bg_color_val_global = "ivory4"
usermanual_bg_color_val_global = "ivory4"
config_bg_color_val_global = "ivory4"
mainscreen_fg_color_val_global = "ivory4"
viewscreen_fg_color_val_global = "ivory4"
selectlist_fg_color_val_global = "ivory4"
newlist_fg_color_val_global = "ivory4"
usermanual_fg_color_val_global = "ivory4"
config_fg_color_val_global = "ivory4"
app_config_ini_val_global = "app_config.ini"
app_config_request_global = False
fullpath_fn_cm_listbox_file_global = "FULLPATH_FN_CM_LISTBOX_FILE Not Set"
fullpath_fn_dict_filename_global = "FULLPATH_FN_DICT_FILENAME Not Set"
fullpath_cnotes_dict_file_global = "FULLPATH_CNOTES_DICT_FILE Not Set"
fullpath_fn_cm_sw_app_logfile_global = "FULLPATH_FN_CM_SW_APP_LOGFILE Not Set"
import_excel_csv_userprofile_global = "IMPORT EXCEL CSV USERPROFILE DIR Not Set"
import_excel_csv_cm_appdata_global = "IMPORT EXCEL CSV APPDATA DIR Not Set"
export_csv_excel_userprofile_global = "EXPORT CSV TO EXCEL USERPROFILE DIR Not Set"
export_csv_excel_cm_appdata_global = "EXPORT CSV TO EXCEL APPDATA DIR Not Set"
export_to_excel_listbox_select_fn_global = "EXPORT CSV TO EXCEL LISTBOX FILE Not Set"
new_excel_file_created_global = "NEW EXCEL FILE CREATED GLOBAL Not Set"
user_gui_title_value_global = "USER GUI DATA Not Set"
user_gui_title_bg_color_value_global = "USER GUI DATA Not Set"
user_gui_title_fg_color_value_global = "USER GUI DATA Not Set"
user_gui_bg_color_value_global = "USER GUI DATA Not Set"
user_gui_fg_color_value_global = "USER GUI DATA Not Set"
user_gui_label_bg_color_value_global = "USER GUI DATA Not Set"
user_gui_label_fg_color_value_global = "USER GUI DATA Not Set"
user_gui_entry_bg_color_value_global = "USER GUI DATA Not Set"
user_gui_entry_fg_color_value_global = "USER GUI DATA Not Set"
user_gui_text_bg_color_value_global = "USER GUI DATA Not Set"
user_gui_text_fg_color_value_global = "USER GUI DATA Not Set"
USER_GUI_Config_Class_inst_LIST = []
fullpath_med_config_ini_global = "NOT YET SET - fullpath_med_config_ini_global"
group1_frame1_user_label = "Set by app_config.ini"
group1_frame1_status_text = "Set by app_config.ini"
group1_frame1_user_button = "Set by app_config.ini"
group1_frame2_user_label = "Set by app_config.ini"
group1_frame2_status_text = "Set by app_config.ini"
group1_frame2_user_button = "Set by app_config.ini"
group1_frame3_user_label = "Set by app_config.ini"
group1_frame3_status_text = "Set by app_config.ini"
group1_frame3_user_button = "Set by app_config.ini"
group1_frame4_user_label = "Set by app_config.ini"
group1_frame4_status_text = "Set by app_config.ini"
group1_frame4_user_button = "Set by app_config.ini"
group1_frame5_user_label = "Set by app_config.ini"
group1_frame5_status_text = "Set by app_config.ini"
group1_frame5_user_button = "Set by app_config.ini"
group1_frame6_user_label = "Set by app_config.ini"
group1_frame6_status_text = "Set by app_config.ini"
group1_frame6_user_button = "Set by app_config.ini"
group1_frame7_user_label = "Set by app_config.ini"
group1_frame7_status_text = "Set by app_config.ini"
group1_frame7_user_button = "Set by app_config.ini"
group1_frame8_user_label = "Set by app_config.ini"
group1_frame8_status_text = "Set by app_config.ini"
group1_frame8_user_button = "Set by app_config.ini"
group1_frame9_user_label = "Set by app_config.ini"
group1_frame9_status_text = "Set by app_config.ini"
group1_frame9_user_button = "Set by app_config.ini"
group1_frame10_user_label = "Set by app_config.ini"
group1_frame10_status_text = "Set by app_config.ini"
group1_frame10_user_button = "Set by app_config.ini"
group1_frame11_user_label = "Set by app_config.ini"
group1_frame11_status_text = "Set by app_config.ini"
group1_frame11_user_button = "Set by app_config.ini"
group1_frame12_user_label = "Set by app_config.ini"
group1_frame12_status_text = "Set by app_config.ini"
group1_frame12_user_button = "Set by app_config.ini"
group2_frame1_user_label = "Set by app_config.ini"
group2_frame1_status_text = "Set by app_config.ini"
group2_frame1_user_button = "Set by app_config.ini"
group2_frame2_user_label = "Set by app_config.ini"
group2_frame2_status_text = "Set by app_config.ini"
group2_frame2_user_button = "Set by app_config.ini"
group2_frame3_user_label = "Set by app_config.ini"
group2_frame3_status_text = "Set by app_config.ini"
group2_frame3_user_button = "Set by app_config.ini"
group2_frame4_user_label = "Set by app_config.ini"
group2_frame4_status_text = "Set by app_config.ini"
group2_frame4_user_button = "Set by app_config.ini"
group2_frame5_user_label = "Set by app_config.ini"
group2_frame5_status_text = "Set by app_config.ini"
group2_frame5_user_button = "Set by app_config.ini"
group2_frame6_user_label = "Set by app_config.ini"
group2_frame6_status_text = "Set by app_config.ini"
group2_frame6_user_button = "Set by app_config.ini"
group2_frame7_user_label = "Set by app_config.ini"
group2_frame7_status_text = "Set by app_config.ini"
group2_frame7_user_button = "Set by app_config.ini"
group2_frame8_user_label = "Set by app_config.ini"
group2_frame8_status_text = "Set by app_config.ini"
group2_frame8_user_button = "Set by app_config.ini"
group2_frame9_user_label = "Set by app_config.ini"
group2_frame9_status_text = "Set by app_config.ini"
group2_frame9_user_button = "Set by app_config.ini"
group2_frame10_user_label = "Set by app_config.ini"
group2_frame10_status_text = "Set by app_config.ini"
group2_frame10_user_button = "Set by app_config.ini"
group2_frame11_user_label = "Set by app_config.ini"
group2_frame11_status_text = "Set by app_config.ini"
group2_frame11_user_button = "Set by app_config.ini"
group2_frame12_user_label = "Set by app_config.ini"
group2_frame12_status_text = "Set by app_config.ini"
group2_frame12_user_button = "Set by app_config.ini"
group3_frame1_user_label = "Set by app_config.ini"
group3_frame1_status_text = "Set by app_config.ini"
group3_frame1_user_button = "Set by app_config.ini"
group3_frame2_user_label = "Set by app_config.ini"
group3_frame2_status_text = "Set by app_config.ini"
group3_frame2_user_button = "Set by app_config.ini"
group3_frame3_user_label = "Set by app_config.ini"
group3_frame3_status_text = "Set by app_config.ini"
group3_frame3_user_button = "Set by app_config.ini"
group3_frame4_user_label = "Set by app_config.ini"
group3_frame4_status_text = "Set by app_config.ini"
group3_frame4_user_button = "Set by app_config.ini"
group3_frame5_user_label = "Set by app_config.ini"
group3_frame5_status_text = "Set by app_config.ini"
group3_frame5_user_button = "Set by app_config.ini"
group3_frame6_user_label = "Set by app_config.ini"
group3_frame6_status_text = "Set by app_config.ini"
group3_frame6_user_button = "Set by app_config.ini"
group3_frame7_user_label = "Set by app_config.ini"
group3_frame7_status_text = "Set by app_config.ini"
group3_frame7_user_button = "Set by app_config.ini"
group3_frame8_user_label = "Set by app_config.ini"
group3_frame8_status_text = "Set by app_config.ini"
group3_frame8_user_button = "Set by app_config.ini"
group3_frame9_user_label = "Set by app_config.ini"
group3_frame9_status_text = "Set by app_config.ini"
group3_frame9_user_button = "Set by app_config.ini"
group3_frame10_user_label = "Set by app_config.ini"
group3_frame10_status_text = "Set by app_config.ini"
group3_frame10_user_button = "Set by app_config.ini"
group3_frame11_user_label = "Set by app_config.ini"
group3_frame11_status_text = "Set by app_config.ini"
group3_frame11_user_button = "Set by app_config.ini"
group3_frame12_user_label = "Set by app_config.ini"
group3_frame12_status_text = "Set by app_config.ini"
group3_frame12_user_button = "Set by app_config.ini"
group4_frame1_user_label = "Set by app_config.ini"
group4_frame1_status_text = "Set by app_config.ini"
group4_frame1_user_button = "Set by app_config.ini"
group4_frame2_user_label = "Set by app_config.ini"
group4_frame2_status_text = "Set by app_config.ini"
group4_frame2_user_button = "Set by app_config.ini"
group4_frame3_user_label = "Set by app_config.ini"
group4_frame3_status_text = "Set by app_config.ini"
group4_frame3_user_button = "Set by app_config.ini"
group4_frame4_user_label = "Set by app_config.ini"
group4_frame4_status_text = "Set by app_config.ini"
group4_frame4_user_button = "Set by app_config.ini"
group4_frame5_user_label = "Set by app_config.ini"
group4_frame5_status_text = "Set by app_config.ini"
group4_frame5_user_button = "Set by app_config.ini"
group4_frame6_user_label = "Set by app_config.ini"
group4_frame6_status_text = "Set by app_config.ini"
group4_frame6_user_button = "Set by app_config.ini"
group4_frame7_user_label = "Set by app_config.ini"
group4_frame7_status_text = "Set by app_config.ini"
group4_frame7_user_button = "Set by app_config.ini"
group4_frame8_user_label = "Set by app_config.ini"
group4_frame8_status_text = "Set by app_config.ini"
group4_frame8_user_button = "Set by app_config.ini"
group4_frame9_user_label = "Set by app_config.ini"
group4_frame9_status_text = "Set by app_config.ini"
group4_frame9_user_button = "Set by app_config.ini"
group4_frame10_user_label = "Set by app_config.ini"
group4_frame10_status_text = "Set by app_config.ini"
group4_frame10_user_button = "Set by app_config.ini"
group4_frame11_user_label = "Set by app_config.ini"
group4_frame11_status_text = "Set by app_config.ini"
group4_frame11_user_button = "Set by app_config.ini"
group4_frame12_user_label = "Set by app_config.ini"
group4_frame12_status_text = "Set by app_config.ini"
group4_frame12_user_button = "Set by app_config.ini"
group5_frame1_user_label = "Set by app_config.ini"
group5_frame1_status_text = "Set by app_config.ini"
group5_frame1_user_button = "Set by app_config.ini"
group5_frame2_user_label = "Set by app_config.ini"
group5_frame2_status_text = "Set by app_config.ini"
group5_frame2_user_button = "Set by app_config.ini"
group5_frame3_user_label = "Set by app_config.ini"
group5_frame3_status_text = "Set by app_config.ini"
group5_frame3_user_button = "Set by app_config.ini"
group5_frame4_user_label = "Set by app_config.ini"
group5_frame4_status_text = "Set by app_config.ini"
group5_frame4_user_button = "Set by app_config.ini"
group5_frame5_user_label = "Set by app_config.ini"
group5_frame5_status_text = "Set by app_config.ini"
group5_frame5_user_button = "Set by app_config.ini"
group5_frame6_user_label = "Set by app_config.ini"
group5_frame6_status_text = "Set by app_config.ini"
group5_frame6_user_button = "Set by app_config.ini"
group5_frame7_user_label = "Set by app_config.ini"
group5_frame7_status_text = "Set by app_config.ini"
group5_frame7_user_button = "Set by app_config.ini"
group5_frame8_user_label = "Set by app_config.ini"
group5_frame8_status_text = "Set by app_config.ini"
group5_frame8_user_button = "Set by app_config.ini"
group5_frame9_user_label = "Set by app_config.ini"
group5_frame9_status_text = "Set by app_config.ini"
group5_frame9_user_button = "Set by app_config.ini"
group5_frame10_user_label = "Set by app_config.ini"
group5_frame10_status_text = "Set by app_config.ini"
group5_frame10_user_button = "Set by app_config.ini"
group5_frame11_user_label = "Set by app_config.ini"
group5_frame11_status_text = "Set by app_config.ini"
group5_frame11_user_button = "Set by app_config.ini"
group5_frame12_user_label = "Set by app_config.ini"
group5_frame12_status_text = "Set by app_config.ini"
group5_frame12_user_button = "Set by app_config.ini"
group6_frame1_user_label = "Set by app_config.ini"
group6_frame1_status_text = "Set by app_config.ini"
group6_frame1_user_button = "Set by app_config.ini"
group6_frame2_user_label = "Set by app_config.ini"
group6_frame2_status_text = "Set by app_config.ini"
group6_frame2_user_button = "Set by app_config.ini"
group6_frame3_user_label = "Set by app_config.ini"
group6_frame3_status_text = "Set by app_config.ini"
group6_frame3_user_button = "Set by app_config.ini"
group6_frame4_user_label = "Set by app_config.ini"
group6_frame4_status_text = "Set by app_config.ini"
group6_frame4_user_button = "Set by app_config.ini"
group6_frame5_user_label = "Set by app_config.ini"
group6_frame5_status_text = "Set by app_config.ini"
group6_frame5_user_button = "Set by app_config.ini"
group6_frame6_user_label = "Set by app_config.ini"
group6_frame6_status_text = "Set by app_config.ini"
group6_frame6_user_button = "Set by app_config.ini"
group6_frame7_user_label = "Set by app_config.ini"
group6_frame7_status_text = "Set by app_config.ini"
group6_frame7_user_button = "Set by app_config.ini"
group6_frame8_user_label = "Set by app_config.ini"
group6_frame8_status_text = "Set by app_config.ini"
group6_frame8_user_button = "Set by app_config.ini"
group6_frame9_user_label = "Set by app_config.ini"
group6_frame9_status_text = "Set by app_config.ini"
group6_frame9_user_button = "Set by app_config.ini"
group6_frame10_user_label = "Set by app_config.ini"
group6_frame10_status_text = "Set by app_config.ini"
group6_frame10_user_button = "Set by app_config.ini"
group6_frame11_user_label = "Set by app_config.ini"
group6_frame11_status_text = "Set by app_config.ini"
group6_frame11_user_button = "Set by app_config.ini"
group6_frame12_user_label = "Set by app_config.ini"
group6_frame12_status_text = "Set by app_config.ini"
group6_frame12_user_button = "Set by app_config.ini"
group7_frame1_user_label = "Set by app_config.ini"
group7_frame1_status_text = "Set by app_config.ini"
group7_frame1_user_button = "Set by app_config.ini"
group7_frame2_user_label = "Set by app_config.ini"
group7_frame2_status_text = "Set by app_config.ini"
group7_frame2_user_button = "Set by app_config.ini"
group7_frame3_user_label = "Set by app_config.ini"
group7_frame3_status_text = "Set by app_config.ini"
group7_frame3_user_button = "Set by app_config.ini"
group7_frame4_user_label = "Set by app_config.ini"
group7_frame4_status_text = "Set by app_config.ini"
group7_frame4_user_button = "Set by app_config.ini"
group7_frame5_user_label = "Set by app_config.ini"
group7_frame5_status_text = "Set by app_config.ini"
group7_frame5_user_button = "Set by app_config.ini"
group7_frame6_user_label = "Set by app_config.ini"
group7_frame6_status_text = "Set by app_config.ini"
group7_frame6_user_button = "Set by app_config.ini"
group7_frame7_user_label = "Set by app_config.ini"
group7_frame7_status_text = "Set by app_config.ini"
group7_frame7_user_button = "Set by app_config.ini"
group7_frame8_user_label = "Set by app_config.ini"
group7_frame8_status_text = "Set by app_config.ini"
group7_frame8_user_button = "Set by app_config.ini"
group7_frame9_user_label = "Set by app_config.ini"
group7_frame9_status_text = "Set by app_config.ini"
group7_frame9_user_button = "Set by app_config.ini"
group7_frame10_user_label = "Set by app_config.ini"
group7_frame10_status_text = "Set by app_config.ini"
group7_frame10_user_button = "Set by app_config.ini"
group7_frame11_user_label = "Set by app_config.ini"
group7_frame11_status_text = "Set by app_config.ini"
group7_frame11_user_button = "Set by app_config.ini"
group7_frame12_user_label = "Set by app_config.ini"
group7_frame12_status_text = "Set by app_config.ini"
group7_frame12_user_button = "Set by app_config.ini"
group8_frame1_user_label = "Set by app_config.ini"
group8_frame1_status_text = "Set by app_config.ini"
group8_frame1_user_button = "Set by app_config.ini"
group8_frame2_user_label = "Set by app_config.ini"
group8_frame2_status_text = "Set by app_config.ini"
group8_frame2_user_button = "Set by app_config.ini"
group8_frame3_user_label = "Set by app_config.ini"
group8_frame3_status_text = "Set by app_config.ini"
group8_frame3_user_button = "Set by app_config.ini"
group8_frame4_user_label = "Set by app_config.ini"
group8_frame4_status_text = "Set by app_config.ini"
group8_frame4_user_button = "Set by app_config.ini"
group8_frame5_user_label = "Set by app_config.ini"
group8_frame5_status_text = "Set by app_config.ini"
group8_frame5_user_button = "Set by app_config.ini"
group8_frame6_user_label = "Set by app_config.ini"
group8_frame6_status_text = "Set by app_config.ini"
group8_frame6_user_button = "Set by app_config.ini"
group8_frame7_user_label = "Set by app_config.ini"
group8_frame7_status_text = "Set by app_config.ini"
group8_frame7_user_button = "Set by app_config.ini"
group8_frame8_user_label = "Set by app_config.ini"
group8_frame8_status_text = "Set by app_config.ini"
group8_frame8_user_button = "Set by app_config.ini"
group8_frame9_user_label = "Set by app_config.ini"
group8_frame9_status_text = "Set by app_config.ini"
group8_frame9_user_button = "Set by app_config.ini"
group8_frame10_user_label = "Set by app_config.ini"
group8_frame10_status_text = "Set by app_config.ini"
group8_frame10_user_button = "Set by app_config.ini"
group8_frame11_user_label = "Set by app_config.ini"
group8_frame11_status_text = "Set by app_config.ini"
group8_frame11_user_button = "Set by app_config.ini"
group8_frame12_user_label = "Set by app_config.ini"
group8_frame12_status_text = "Set by app_config.ini"
group8_frame12_user_button = "Set by app_config.ini"
group9_frame1_user_label = "Set by app_config.ini"
group9_frame1_status_text = "Set by app_config.ini"
group9_frame1_user_button = "Set by app_config.ini"
group9_frame2_user_label = "Set by app_config.ini"
group9_frame2_status_text = "Set by app_config.ini"
group9_frame2_user_button = "Set by app_config.ini"
group9_frame3_user_label = "Set by app_config.ini"
group9_frame3_status_text = "Set by app_config.ini"
group9_frame3_user_button = "Set by app_config.ini"
group9_frame4_user_label = "Set by app_config.ini"
group9_frame4_status_text = "Set by app_config.ini"
group9_frame4_user_button = "Set by app_config.ini"
group9_frame5_user_label = "Set by app_config.ini"
group9_frame5_status_text = "Set by app_config.ini"
group9_frame5_user_button = "Set by app_config.ini"
group9_frame6_user_label = "Set by app_config.ini"
group9_frame6_status_text = "Set by app_config.ini"
group9_frame6_user_button = "Set by app_config.ini"
group9_frame7_user_label = "Set by app_config.ini"
group9_frame7_status_text = "Set by app_config.ini"
group9_frame7_user_button = "Set by app_config.ini"
group9_frame8_user_label = "Set by app_config.ini"
group9_frame8_status_text = "Set by app_config.ini"
group9_frame8_user_button = "Set by app_config.ini"
group9_frame9_user_label = "Set by app_config.ini"
group9_frame9_status_text = "Set by app_config.ini"
group9_frame9_user_button = "Set by app_config.ini"
group9_frame10_user_label = "Set by app_config.ini"
group9_frame10_status_text = "Set by app_config.ini"
group9_frame10_user_button = "Set by app_config.ini"
group9_frame11_user_label = "Set by app_config.ini"
group9_frame11_status_text = "Set by app_config.ini"
group9_frame11_user_button = "Set by app_config.ini"
group9_frame12_user_label = "Set by app_config.ini"
group9_frame12_status_text = "Set by app_config.ini"
group9_frame12_user_button = "Set by app_config.ini"
group10_frame1_user_label = "Set by app_config.ini"
group10_frame1_status_text = "Set by app_config.ini"
group10_frame1_user_button = "Set by app_config.ini"
group10_frame2_user_label = "Set by app_config.ini"
group10_frame2_status_text = "Set by app_config.ini"
group10_frame2_user_button = "Set by app_config.ini"
group10_frame3_user_label = "Set by app_config.ini"
group10_frame3_status_text = "Set by app_config.ini"
group10_frame3_user_button = "Set by app_config.ini"
group10_frame4_user_label = "Set by app_config.ini"
group10_frame4_status_text = "Set by app_config.ini"
group10_frame4_user_button = "Set by app_config.ini"
group10_frame5_user_label = "Set by app_config.ini"
group10_frame5_status_text = "Set by app_config.ini"
group10_frame5_user_button = "Set by app_config.ini"
group10_frame6_user_label = "Set by app_config.ini"
group10_frame6_status_text = "Set by app_config.ini"
group10_frame6_user_button = "Set by app_config.ini"
group10_frame7_user_label = "Set by app_config.ini"
group10_frame7_status_text = "Set by app_config.ini"
group10_frame7_user_button = "Set by app_config.ini"
group10_frame8_user_label = "Set by app_config.ini"
group10_frame8_status_text = "Set by app_config.ini"
group10_frame8_user_button = "Set by app_config.ini"
group10_frame9_user_label = "Set by app_config.ini"
group10_frame9_status_text = "Set by app_config.ini"
group10_frame9_user_button = "Set by app_config.ini"
group10_frame10_user_label = "Set by app_config.ini"
group10_frame10_status_text = "Set by app_config.ini"
group10_frame10_user_button = "Set by app_config.ini"
group10_frame11_user_label = "Set by app_config.ini"
group10_frame11_status_text = "Set by app_config.ini"
group10_frame11_user_button = "Set by app_config.ini"
group10_frame12_user_label = "Set by app_config.ini"
group10_frame12_status_text = "Set by app_config.ini"
group10_frame12_user_button = "Set by app_config.ini"
OBJECT_toplevel_excel_import_export = object
OBJECT_toplevel_app_status_panel = object
OBJECT_toplevel_cm_app_doc_media = object
OBJECT_toplevel_user_gui_1_config_class = object
OBJECT_toplevel_user_gui_2_config_class = object
OBJECT_toplevel_user_gui_3_config_class = object
OBJECT_toplevel_user_gui_4_config_class = object
OBJECT_toplevel_user_gui_5_config_class = object
OBJECT_toplevel_user_gui_6_config_class = object
OBJECT_toplevel_user_gui_7_config_class = object
OBJECT_toplevel_user_gui_8_config_class = object
OBJECT_toplevel_user_gui_9_config_class = object
OBJECT_toplevel_user_gui_10_config_class = object
gui_group_one_object = object
gui_group_two_object = object
gui_group_three_object = object
gui_group_four_object = object
gui_group_five_object = object
gui_group_six_object = object
gui_group_seven_object = object
gui_group_eight_object = object
gui_group_nine_object = object
gui_group_ten_object = object
user_defined_gui_group_one = object
user_defined_gui_group_two = object
user_defined_gui_group_three = object
user_defined_gui_group_four = object
user_defined_gui_group_five = object
user_defined_gui_group_six = object
user_defined_gui_group_seven = object
user_defined_gui_group_eight = object
user_defined_gui_group_nine = object
user_defined_gui_group_ten = object
OBJECT_IN_APP_user_gui_1_config_class = object
OBJECT_IN_APP_user_gui_2_config_class = object
OBJECT_IN_APP_user_gui_3_config_class = object
OBJECT_IN_APP_user_gui_4_config_class = object
OBJECT_IN_APP_user_gui_5_config_class = object
OBJECT_IN_APP_user_gui_6_config_class = object
OBJECT_IN_APP_user_gui_7_config_class = object
OBJECT_IN_APP_user_gui_8_config_class = object
OBJECT_IN_APP_user_gui_9_config_class = object
OBJECT_IN_APP_user_gui_10_config_class = object
OBJECT_toplevel_list_builder = object
OBJECT_toplevel_view_contact_list = object
OBJECT_toplevel_new_contact_list = object
OBJECT_toplevel_select_contact_list = object
OBJECT_toplevel_system_admin_info = object
OBJECT_toplevel_email_gmail_class = object
OBJECT_toplevel_config_setting_class = object
OBJECT_IN_APP_cm_app_doc_media = object
OBJECT_IN_APP_excel_import_export = object
OBJECT_IN_APP_app_status_panel = object
OBJECT_IN_APP_list_builder = object
OBJECT_IN_APP_view_contact_list = object
OBJECT_IN_APP_new_contact_list = object
OBJECT_IN_APP_select_contact_list = object
OBJECT_IN_APP_system_admin_info = object
OBJECT_IN_APP_email_gmail_class = object
OBJECT_IN_APP_config_setting_class = object
OBJECT_main = object
instance_object_LIST = []
instance_object_winfo_id_LIST = []
instance_object_winfo_parent_LIST = []
user_defined_gui_instance_count_GLOBAL = 0
listbox_file_capture_global = False
cm_listbox_file_global = "No Contact List Selected"
dict_filename_global = "No Contact Dictionary"
cnotes_dict_file_global = "CNOTES_DICT_FILE Not Set"
prepend_cnotes_dict_file_global = "PREPEND_CNOTES_DICT_FILE Not Set"
master_cm_list_name_global = "SELECT or Create NEW Contact List"
textbox_newfile_capture_global = False
cm_textbox_newfile_global = "No New Contact List Created"
first_insert_data_entry = 0
window_select_global = "window_select_global NOT YET SET"
night_mode_selection = 1


####################################################################################
""" Description: Contact Management Software Program. 
    This Contact Management Software Program is implemented
    with very large FONT (Letter Sizes) to improve productivity. """ 
####################################################################################
# .... each_object = .!toplevel.!excel_import_export
# .... each_object = .!toplevel2.!app_status_panel
# .... each_object = .!toplevel3.!cm_app_doc_media
# .... each_object = .!toplevel4.!user_gui_config_class
# .... each_object = .!toplevel5.!user_gui_config_class
# .... each_object = .!toplevel6.!user_gui_config_class
# .... each_object = .!toplevel7.!list_builder
# .... each_object = .!toplevel8.!view_contact_list
# .... each_object = .!toplevel9.!new_contact_list
# .... each_object = .!toplevel10.!select_contact_list
# .... each_object = .!toplevel11.!system_admin_info
# .... each_object = .!toplevel12.!email_gmail_class
# .... each_object = .!toplevel13.!config_setting_class
####################################################################################

class App(Frame):    #( object)
      """
      This is the App Class. 

      The App Class is defined by the statement:  class App(object): 

      The App Class has the following attributes:

      List App Class Attributes here. 

      """       
      def __init__(self, master):
            global selected_email_address_LIST_GLOBAL
            global DEST_or_CC_email_address_FLAG_GLOBAL
            global hostname_via_socket
            global ipv4_address_global
            global gmail_oauth2_json_file_test_global
            global gmail_oauth2_status_global
            global gmail_oauth2_exceptions_status_global
            global gmail_oauth2_SPECIFIC_EXCEPTION_global
            global gmail_smtp_allow_less_secure_apps_global
            global gmail_smtp_status_global
            global gmail_smtp_exceptions_status_global
            global gmail_smtp_SPECIFIC_EXCEPTION_global
            global gmail_logged_in_global
            global cm_dict_file_startup_test_global
            global cm_csv_file_startup_test_global
            global cm_notes_file_startup_test_global
            global insert_first_contact_global
            global userprofile_global
            global fullpath_gmail_oauth2_credentials_global
            global credential_home_dir_global
            global credential_appdata_dir_global
            global credential_home_path_global
            global credential_appdata_path_global
            global client_secret_path_global
            global valid_client_secret_key_format_global
            global gmail_mode_global
            global mode_select_global
            global mode_select_build_list_global
            global request_mainscreen_config_update_global
            global textbox_edit_mode_select_global
            global selected_dictionary_loaded_global
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global kick_thread_to_update_main_entry_widgets
            global kick_thread_to_update_email_contact_entry_widgets
            global num_of_dictionary_data_records_global
            global listbox_file_capture_global
            global cm_listbox_file_global
            global dict_filename_global
            global cnotes_dict_file_global
            global master_cm_list_name_global
            global cm_appdatafiles_path_global
            global listbox_color_value_global
            global listbox_color_moment_global
            global fullpath_app_config_ini_global
            global fullpath_med_config_ini_global
            global mainscreen_bg_color_val_global
            global mainscreen_bg_color_val_global
            global viewscreen_bg_color_val_global
            global selectlist_bg_color_val_global
            global newlist_bg_color_val_global
            global usermanual_bg_color_val_global
            global config_bg_color_val_global
            global mainscreen_fg_color_val_global
            global viewscreen_fg_color_val_global
            global selectlist_fg_color_val_global
            global newlist_fg_color_val_global
            global usermanual_fg_color_val_global
            global config_fg_color_val_global
            global app_config_ini_val_global
            global app_config_request_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global
            global fullpath_cnotes_dict_file_global
            global fullpath_fn_cm_sw_app_logfile_global
            global import_excel_csv_userprofile_global
            global import_excel_csv_cm_appdata_global
            global export_csv_excel_userprofile_global
            global export_csv_excel_cm_appdata_global
            global export_to_excel_listbox_select_fn_global
            global new_excel_file_created_global
            global user_gui_title_value_global
            global user_gui_title_bg_color_value_global
            global user_gui_title_fg_color_value_global
            global user_gui_bg_color_value_global
            global user_gui_fg_color_value_global
            global user_gui_label_bg_color_value_global
            global user_gui_label_fg_color_value_global
            global user_gui_entry_bg_color_value_global
            global user_gui_entry_fg_color_value_global
            global user_gui_text_bg_color_value_global
            global user_gui_text_fg_color_value_global
            global USER_GUI_Config_Class_inst_LIST
            global group1_frame1_user_label
            global group1_frame1_status_text
            global group1_frame1_user_button
            global group1_frame2_user_label
            global group1_frame2_status_text
            global group1_frame2_user_button
            global group1_frame3_user_label
            global group1_frame3_status_text
            global group1_frame3_user_button
            global group1_frame4_user_label
            global group1_frame4_status_text
            global group1_frame4_user_button
            global group1_frame5_user_label
            global group1_frame5_status_text
            global group1_frame5_user_button
            global group1_frame6_user_label
            global group1_frame6_status_text
            global group1_frame6_user_button
            global group1_frame7_user_label
            global group1_frame7_status_text
            global group1_frame7_user_button
            global group1_frame8_user_label
            global group1_frame8_status_text
            global group1_frame8_user_button
            global group1_frame9_user_label
            global group1_frame9_status_text
            global group1_frame9_user_button
            global group1_frame10_user_label
            global group1_frame10_status_text
            global group1_frame10_user_button
            global group1_frame11_user_label
            global group1_frame11_status_text
            global group1_frame11_user_button
            global group1_frame12_user_label
            global group1_frame12_status_text
            global group1_frame12_user_button
            global group2_frame1_user_label
            global group2_frame1_status_text
            global group2_frame1_user_button
            global group2_frame2_user_label
            global group2_frame2_status_text
            global group2_frame2_user_button
            global group2_frame3_user_label
            global group2_frame3_status_text
            global group2_frame3_user_button
            global group2_frame4_user_label
            global group2_frame4_status_text
            global group2_frame4_user_button
            global group2_frame5_user_label
            global group2_frame5_status_text
            global group2_frame5_user_button
            global group2_frame6_user_label
            global group2_frame6_status_text
            global group2_frame6_user_button
            global group2_frame7_user_label
            global group2_frame7_status_text
            global group2_frame7_user_button
            global group2_frame8_user_label
            global group2_frame8_status_text
            global group2_frame8_user_button
            global group2_frame9_user_label
            global group2_frame9_status_text
            global group2_frame9_user_button
            global group2_frame10_user_label
            global group2_frame10_status_text
            global group2_frame10_user_button
            global group2_frame11_user_label
            global group2_frame11_status_text
            global group2_frame11_user_button
            global group2_frame12_user_label
            global group2_frame12_status_text
            global group2_frame12_user_button
            global group3_frame1_user_label
            global group3_frame1_status_text
            global group3_frame1_user_button
            global group3_frame2_user_label
            global group3_frame2_status_text
            global group3_frame2_user_button
            global group3_frame3_user_label
            global group3_frame3_status_text
            global group3_frame3_user_button
            global group3_frame4_user_label
            global group3_frame4_status_text
            global group3_frame4_user_button
            global group3_frame5_user_label
            global group3_frame5_status_text
            global group3_frame5_user_button
            global group3_frame6_user_label
            global group3_frame6_status_text
            global group3_frame6_user_button
            global group3_frame7_user_label
            global group3_frame7_status_text
            global group3_frame7_user_button
            global group3_frame8_user_label
            global group3_frame8_status_text
            global group3_frame8_user_button
            global group3_frame9_user_label
            global group3_frame9_status_text
            global group3_frame9_user_button
            global group3_frame10_user_label
            global group3_frame10_status_text
            global group3_frame10_user_button
            global group3_frame11_user_label
            global group3_frame11_status_text
            global group3_frame11_user_button
            global group3_frame12_user_label
            global group3_frame12_status_text
            global group3_frame12_user_button
            global instance_object_LIST
            global instance_object_winfo_id_LIST
            global instance_object_winfo_parent_LIST
            global user_defined_gui_instance_count_GLOBAL
            global OBJECT_toplevel_cm_app_doc_media
            global OBJECT_toplevel_excel_import_export
            global OBJECT_toplevel_app_status_panel
            global user_defined_gui_group_one
            global user_defined_gui_group_two
            global user_defined_gui_group_three
            global user_defined_gui_group_four
            global user_defined_gui_group_five
            global user_defined_gui_group_six
            global user_defined_gui_group_seven
            global user_defined_gui_group_eight
            global user_defined_gui_group_nine
            global user_defined_gui_group_ten
            global OBJECT_toplevel_user_gui_1_config_class
            global OBJECT_toplevel_user_gui_2_config_class
            global OBJECT_toplevel_user_gui_3_config_class
            global OBJECT_toplevel_user_gui_1_config_class
            global OBJECT_toplevel_user_gui_2_config_class
            global OBJECT_toplevel_user_gui_3_config_class
            global OBJECT_toplevel_user_gui_4_config_class
            global OBJECT_toplevel_user_gui_5_config_class
            global OBJECT_toplevel_user_gui_6_config_class
            global OBJECT_toplevel_user_gui_7_config_class
            global OBJECT_toplevel_user_gui_8_config_class
            global OBJECT_toplevel_user_gui_9_config_class
            global OBJECT_toplevel_user_gui_10_config_class
            global gui_group_one_object
            global gui_group_two_object
            global gui_group_three_object
            global gui_group_four_object
            global gui_group_five_object
            global gui_group_six_object
            global gui_group_seven_object
            global gui_group_eight_object
            global gui_group_nine_object
            global gui_group_ten_object
            global OBJECT_IN_APP_user_gui_1_config_class
            global OBJECT_IN_APP_user_gui_2_config_class
            global OBJECT_IN_APP_user_gui_3_config_class
            global OBJECT_IN_APP_user_gui_4_config_class
            global OBJECT_IN_APP_user_gui_5_config_class
            global OBJECT_IN_APP_user_gui_6_config_class
            global OBJECT_IN_APP_user_gui_7_config_class
            global OBJECT_IN_APP_user_gui_8_config_class
            global OBJECT_IN_APP_user_gui_9_config_class
            global OBJECT_IN_APP_user_gui_10_config_class
            global OBJECT_toplevel_list_builder
            global OBJECT_toplevel_view_contact_list
            global OBJECT_toplevel_new_contact_list
            global OBJECT_toplevel_select_contact_list
            global OBJECT_toplevel_system_admin_info
            global OBJECT_toplevel_email_gmail_class
            global OBJECT_toplevel_config_setting_class
            global OBJECT_IN_APP_cm_app_doc_media
            global OBJECT_IN_APP_excel_import_export
            global OBJECT_IN_APP_app_status_panel
            global OBJECT_IN_APP_list_builder
            global OBJECT_IN_APP_view_contact_list
            global OBJECT_IN_APP_new_contact_list
            global OBJECT_IN_APP_select_contact_list
            global OBJECT_IN_APP_system_admin_info
            global OBJECT_IN_APP_email_gmail_class
            global OBJECT_IN_APP_config_setting_class
            global OBJECT_main
            global window_select_global
            global night_mode_selection
            Frame.__init__(self, master)
            self.grid()

            #self.master = master
            #self.frame = tk.Frame(self.master)
            
            #self.master = master
            #self.frame = tk.Frame(self.master)

            # Set Messagebox Font
            self.master.option_add('*Dialog.msg.font', 'Helvetica 16')

            self.master.configure(background=str(mainscreen_bg_color_val_global) )
            
            self.session_index = 1

            self.session_review_index = 1

            contactList = []

            # self.this_person = []

            gfn = ''
            gln = ''
            gsa = ''
            gct = ''
            gst = ''
            gzc = ''
            gpn = ''
            gem = ''
            gws = ''
 
            count_inserts = 0 

            this_contacts = {}
            
            large_font = ('Verdana',20)
            minilarge_font = ('Verdana',16)
            minilarge_14_font = ('Verdana',14)
            medium_font = ('Verdana',12,'bold')
            small_font = ('Verdana',10)
            menubar_font = ('Helvetica', '12')
            
            self.master.title("UVM Testbench Builder Application Software")

            # Max Screen Size with the Title Bar - BEST Choice 
            self.master.wm_state('zoomed')

            OBJECT_main = self.master

            # print(".... str(OBJECT_main) = " + str(OBJECT_main) )
            # print(".... Just OBJECT_main = ")
            # print(OBJECT_main)

            # Create an OBJECT Variable to control tk WINDOW_INSTANCE.exists() and WINDOW_INSTANCE.lift()
            self.instance_object_focus = self.master

            # Initialize OBJECT Variables to OBJECT TYPE (then try None)  
            # to control tk WINDOW_INSTANCE.exists() and WINDOW_INSTANCE.lift() 
            OBJECT_toplevel_cm_app_doc_media = self.master
            OBJECT_toplevel_excel_import_export = self.master
            OBJECT_toplevel_app_status_panel = self.master
            OBJECT_toplevel_user_gui_1_config_class = self.master
            OBJECT_toplevel_user_gui_2_config_class = self.master
            OBJECT_toplevel_user_gui_3_config_class = self.master
            OBJECT_toplevel_user_gui_4_config_class = self.master
            OBJECT_toplevel_user_gui_5_config_class = self.master
            OBJECT_toplevel_user_gui_6_config_class = self.master
            OBJECT_toplevel_user_gui_7_config_class = self.master
            OBJECT_toplevel_user_gui_8_config_class = self.master
            OBJECT_toplevel_user_gui_9_config_class = self.master
            OBJECT_toplevel_user_gui_10_config_class = self.master
            OBJECT_toplevel_list_builder = self.master
            OBJECT_toplevel_view_contact_list = self.master
            OBJECT_toplevel_new_contact_list = self.master
            OBJECT_toplevel_select_contact_list = self.master
            OBJECT_toplevel_system_admin_info = self.master
            OBJECT_toplevel_email_gmail_class = self.master
            OBJECT_toplevel_config_setting_class = self.master
 
            OBJECT_IN_APP_cm_app_doc_media = self.master
            OBJECT_IN_APP_excel_import_export = self.master
            OBJECT_IN_APP_app_status_panel = self.master
            OBJECT_IN_APP_user_gui_1_config_class = self.master
            OBJECT_IN_APP_user_gui_2_config_class = self.master
            OBJECT_IN_APP_user_gui_3_config_class = self.master
            OBJECT_IN_APP_user_gui_4_config_class = self.master
            OBJECT_IN_APP_user_gui_5_config_class = self.master
            OBJECT_IN_APP_user_gui_6_config_class = self.master
            OBJECT_IN_APP_user_gui_7_config_class = self.master
            OBJECT_IN_APP_user_gui_8_config_class = self.master
            OBJECT_IN_APP_user_gui_9_config_class = self.master
            OBJECT_IN_APP_user_gui_10_config_class = self.master
            OBJECT_IN_APP_list_builder = self.master
            OBJECT_IN_APP_view_contact_list = self.master
            OBJECT_IN_APP_new_contact_list = self.master
            OBJECT_IN_APP_select_contact_list = self.master
            OBJECT_IN_APP_system_admin_info = self.master
            OBJECT_IN_APP_email_gmail_class = self.master
            OBJECT_IN_APP_config_setting_class = self.master
            
            self.excel_import_export_button = Button(self.master, text = "UVM SEQ ITEM", \
                width=15,height=2, background="midnight blue", fg="deep sky blue", command = self.sys_admin_View_UVM_SEQ_ITEM_method)

            self.excel_import_export_button.grid(row=2, column=0, sticky=W)
            self.excel_import_export_button.config(font=('Helvetica', 14 ) )
            self.excel_import_export_button.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

            #############################################################################
            #
            # Implement Options Menu Drop Down to Select Entry Mode or Browse Mode
            #   
            # Use OptionsMenu to set mode_select_global = "Browse Mode" or "Entry Mode"
            #
            #############################################################################
            #
            # OPTION MENU WIDGET for MODE SELECT - selects from OptionMenu and
            # sets MODE SELECT GLOBAL which is utilized to set 
            # MODE SELECT INDICATOR WIDGET value as:
            #
            #    Browse Mode  or  Entry_Mode  or  Edit_Mode
            #
            # Note that default is mode_select_global = "Browse Mode" because
            # if we are switching screens back and forth, we want to maintain
            # workflow speed and the "index_focus_global" dictionary pointer.
            #
            #############################################################################
            #
            List_of_Program_Modes = ["Browse Mode", "Entry Mode", "Edit Mode"]

            mode_select_global = "Browse Mode"


            self.sort_contact_list_button = Button(self.master, text = "UVM SEQUENCE", \
                  width=15,height=2, font=('Helvetica', '14'), background="midnight blue", fg="deep sky blue", \
                  activebackground="cyan", activeforeground="blue2", command = self.sys_admin_View_UVM_SEQUENCE_method)

            self.sort_contact_list_button.grid(row=3, column=0, sticky=W)
            self.sort_contact_list_button.config(borderwidth=5, activebackground="cyan4", activeforeground="cyan")

###########################################################################################
         
            scroll_label = ['','','','','','']

            r = 3
            for c in scroll_label:
                  if r > 3 and r < 11:
                       if r == 4:
                             bindto = "forward_fast"
                             speedbutton_1 = Button(self.master, text = "UVM SEQUENCER", \
                             width=15,height=2, font=('Helvetica', '14'), \
                             background="midnight blue", fg="deep sky blue", command = self.forward_fast)
                             speedbutton_1.grid(row=r,column=0, sticky=W)
                             speedbutton_1.config(borderwidth=5)
                             speedbutton_1.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

                       elif r == 5:
                             bindto = "forward_scroll"
                             speedbutton_2 = Button(self.master, text = "UVM DRIVER", \
                             width=15,height=2, font=('Helvetica', '14'), \
                             background="midnight blue", fg="deep sky blue", command = self.forward_scroll)
                             speedbutton_2.grid(row=r,column=0, sticky=W)
                             speedbutton_2.config(borderwidth=5)
                             speedbutton_2.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")
                             #speedbutton_2.bind("<Enter>", self.forward_scroll)
                             #speedbutton_2.bind("<Leave>", self.forward_scroll)
                       elif r == 6:
                             bindto = "forward_tick"
                             speedbutton_3 = Button(self.master, text = "UVM MONITOR", \
                             width=15,height=2, font=('Helvetica', '14'), \
                             background="midnight blue", fg="deep sky blue", command = self.forward_tick)
                             speedbutton_3.grid(row=r,column=0, sticky=W)
                             speedbutton_3.config(borderwidth=5)
                             speedbutton_3.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")
                             #speedbutton_3.bind("<Enter>", self.forward_tick)
                             #speedbutton_3.bind("<Leave>", self.forward_tick)
                             ###########################################################################
                       elif r == 7:
                             bindto = "backward_tick"
                             speedbutton_4 = Button(self.master, text = "UVM AGENT", \
                             width=15,height=2, font=('Helvetica', '14'), \
                             background="midnight blue", fg="deep sky blue", command = self.backward_tick)
                             speedbutton_4.grid(row=r,column=0, sticky=W)
                             speedbutton_4.config(borderwidth=5)
                             speedbutton_4.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")
                             #speedbutton_4.bind("<Enter>", self.backward_tick)
                             #speedbutton_4.bind("<Leave>", self.backward_tick) 
                             ############################################################################
                       elif r == 8:
                             bindto = "backward_scroll"
                             speedbutton_5 = Button(self.master, text = "UVM ENV", \
                             width=15,height=2, font=('Helvetica', '14'), \
                             background="midnight blue", fg="deep sky blue", command = self.sys_admin_View_UVM_ENV_method)
                             speedbutton_5.grid(row=r,column=0, sticky=W)
                             speedbutton_5.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")
                             #speedbutton_5.bind("<Enter>", self.backward_scroll)
                             #speedbutton_5.bind("<Leave>", self.backward_scroll)
                       elif r == 9:
                             bindto = "backward_fast"
                             speedbutton_6 = Button(self.master, text = "NOT USED", \
                             width=15,height=2, font=('Helvetica', '14'), \
                             background="midnight blue", fg="deep sky blue", command = self.sys_admin_View_UVM_SCBD_method)
                             speedbutton_6.grid(row=2,column=0, sticky=E)
                             speedbutton_6.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")
                             #speedbutton_6.bind("<Enter>", self.backward_fast)
                             #speedbutton_6.bind("<Leave>", self.backward_fast)
                       elif r == 10:
                             bindto = "backward_fast"
                             speedbutton_7 = Button(self.master, text = "NOT USED", \
                             width=15,height=2, font=('Helvetica', '14'), \
                             background="midnight blue", fg="deep sky blue", command = self.sys_admin_View_UVM_TB_PKG_method)
                             speedbutton_7.grid(row=3,column=0, sticky=E)
                             speedbutton_7.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

                  r = r + 1


######################################################################################

            List_of_WINDOWS = ["WINDOW SELECT", "cm_app_doc_media", "excel_import_export", "app_status_panel", \
                               "list_builder", "view_contact_list", "new_contact_list", \
                               "select_contact_list","system_admin_info","email_gmail_class","config_setting_class", \
                               "CRM STARTUP", "MEDICAL RECORD", "COMMAND CENTER", "E X I T"]

            window_select_global = "WINDOW SEL"

            self.window_select_opt_menu_select = StringVar()
            self.window_select_opt_menu_select.set(str(window_select_global) )   # initialize OptionMenu for window Select
            self.window_select_optionsmenu_inst = OptionMenu(self.master, self.window_select_opt_menu_select, \
            *List_of_WINDOWS, command=self.func_set_window_select_global)
            self.window_select_optionsmenu_inst.grid(row=1, column=0) 
            self.window_select_optionsmenu_inst.config(borderwidth=5, background="cyan4", fg="black", font=('Helvetica', 14) )

            menu_window_select = self.window_select_optionsmenu_inst.nametowidget(self.window_select_optionsmenu_inst.menuname) 
            menu_window_select.configure(font=("Helvetica", 14), bg="light sea green") 

###################################################################################### 

            self.sys_admin_view_button = Button(self.master, text = "SYSTEM ADMIN", \
                  width=15,height=1, font=('Helvetica', '14'), \
                  background="black", fg="deep sky blue", command = self.system_administration_View_method)
            
            self.sys_admin_view_button.grid(row=10, column=0, sticky=W)
            self.sys_admin_view_button.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

###################################################################################### 
##
##    Implement BUILD-COMPILE-SIMULATION-ANALYZE using PYTHON and TKINTER GUI
##    to automate UVM Testbench FPGA/ASICSOC Design Verification.
##  
######################################################################################

            self.build_button = Button(self.master, text = "BUILD", \
                  width=15,height=1, font=('Helvetica', '14'), \
                  background="midnight blue", fg="deep sky blue", command = self.system_administration_View_method)
            
            self.build_button.grid(row=1, column=1, sticky=W)
            self.build_button.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

###################################################################################### 

            self.compile_button = Button(self.master, text = "COMPILE", \
                  width=15,height=1, font=('Helvetica', '14'), \
                  background="midnight blue", fg="deep sky blue", command = self.system_administration_View_method)
            
            self.compile_button.grid(row=1, column=2, sticky=W)
            self.compile_button.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

###################################################################################### 

            self.simulation_button = Button(self.master, text = "SIMULATION", \
                  width=15,height=1, font=('Helvetica', '14'), \
                  background="midnight blue", fg="deep sky blue", command = self.system_administration_View_method)
            
            self.simulation_button.grid(row=1, column=3, sticky=W)
            self.simulation_button.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

###################################################################################### 

            self.analysis_button = Button(self.master, text = "ANALYSIS", \
                  width=15,height=1, font=('Helvetica', '14'), \
                  background="midnight blue", fg="deep sky blue", command = self.system_administration_View_method)
            
            self.analysis_button.grid(row=1, column=4, sticky=W)
            self.analysis_button.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

###################################################################################### 

            self.app_status_display_select_button = Button(self.master, \
                text = "STATUS PANEL", width=15, height=1, command = self.select_App_Status_Display_method)
            
            self.app_status_display_select_button.grid(row=9, column=0, sticky=W)
            self.app_status_display_select_button.config(borderwidth=5, \
                  background="midnight blue", fg="deep sky blue", font=('Helvetica', 14 ) )
            self.app_status_display_select_button.config(activebackground="cyan", activeforeground="blue2")

###################################################################################### 

            self.build_dual_list_button2 = Button(self.master, text = "UVM SCBD", \
                width=15, height=2, font=('Helvetica', '14'), \
                background="midnight blue", fg="deep sky blue", command = self.build_list_from_dual_listbox_window_method)
            
            self.build_dual_list_button2.grid(row=2, column=1, sticky=W)
            self.build_dual_list_button2.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

###################################################################################### 

            self.build_dual_list_button = Button(self.master, text = "UVM TB PKG", \
                width=15, height=2, font=('Helvetica', '14'), \
                background="midnight blue", fg="deep sky blue", command = self.build_list_from_dual_listbox_window_method)
            
            self.build_dual_list_button.grid(row=3, column=1, sticky=W)
            self.build_dual_list_button.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

######################################################################################  

            self.build_dual_list3_button = Button(self.master, text = "UVM TB CFG", \
                width=15, height=2, font=('Helvetica', '14'), \
                background="midnight blue", fg="deep sky blue", command = self.build_list_from_dual_listbox_window_method)
            
            self.build_dual_list3_button.grid(row=4, column=1, sticky=W)
            self.build_dual_list3_button.config(borderwidth=5, activebackground="cyan", activeforeground="blue2")

######################################################################################  


            # Initialize Program with the First Contact List
            self.create_first_contact_list_on_startup()

            ###################################################################
            #
            # ENTER FIRST RECORD of Contact Data to Initialize Databases
            # and provide an example for Users. This First Data Record
            # is required so that other Classes and Methods that use the
            # database will avoid the KeyError Exception when encountering
            # an EMPTY Contact List Dictionary. 
            # 
            ###################################################################
            #
            # Load the current DICTIONARY Contact List File - dict_file_cm_listbox_file_global
            # which is stored in APPDATA at fullpath_fn_dict_filename_global

            self.textFile = open(fullpath_fn_dict_filename_global, 'r')

            # This command takes the file object opened with the open() and reads it
            # into a string which we can now use to count the RECORDS in the Dictionary
            # because upon prograam startup we only want ONE INITIAL RECORD to be
            # in the CONTACT-LIST-ONE Contact List.  
            # 
            self.textString = self.textFile.read()

            # Count the DATA RECORDS in the string by counting the
            # number of "DATA_RECORD_DELIMITER:" patterns 
            self.num_data_records = self.textString.count("DATA_RECORD_DELIMITER:")
            #
            # ONLY If the number of DATA RECORDS in CONTACT-LIST-ONE is ZERO (less than 1),
            # do we execute:  self.first_Contact_Data_Entry() 
            #
            if self.num_data_records < 1:
                self.first_Contact_Data_Entry()

            ###########################################################################################
            
            # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
            # WHICH SETS THE selected_dictionary_loaded_global GLOBAL.  

            inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
            loaded_contact_dict_acquired_GLOBAL = inst_loaded_Process_Dict_File.read_target_dict_file()

            # NOTE:
            # selected_dictionary_record_index_global = 1
            # selected_dictionary_record_index_focus_global = 1

            kick_thread_to_update_main_entry_widgets = True
                   

      ######################################################################################
      #
      # Method to Create the First Contact List so the User begins with an initial
      # Contact List and all the associated Database Files. 
      #
      # This method is called at the end of the init of the App Class (above)
      #
      # Method:  create_first_contact_list_on_startup()
      #     
      ######################################################################################

      def create_first_contact_list_on_startup(self):
          global cm_listbox_file_global
          global dict_filename_global
          global cnotes_dict_file_global
          global prepend_cnotes_dict_file_global
          global master_cm_list_name_global
          global listbox_file_capture_global
          global cm_textbox_newfile_global
          global textbox_newfile_capture_global
          global fullpath_fn_cm_listbox_file_global
          global fullpath_fn_dict_filename_global
          global fullpath_cnotes_dict_file_global
          global fullpath_prepend_cnotes_dict_file_global
          global selected_dictionary_record_index_global

          ###########################################################################
          #
          # This method names the FIRST (or initial) contact list name
          # and sets the cm_textbox_newfile_global
          # and cm_textbox_newfile_global used in THREAD to 
          # set the CONTACT LIST ENTRY BOX in the App Class
          # USING THE GLOBAL VARIABLE cm_listbox_file_global. 
          #
          ###########################################################################
          #
          #  textbox_newfile_capture_global = False
          #
          #  will be set to True to trigger update of the Contact List name
          #  in the MAIN SCREEN by the thread in main. 
          #
          #  cm_textbox_newfile_global = "CONTACT-LIST-ONE" 
          #
          ###########################################################################


          cm_textbox_newfile_global = "CONTACT-LIST-ONE"
          master_cm_list_name_global = "CONTACT-LIST-ONE"
          textbox_newfile_capture_global = True

          # Create NEW FILES for the cm_list_CONTACT_LIST_NAME 
          # and dict_file_CONTACT_LIST_NAME and the
          # cnotes_CONTACT_LIST_NAME Globals filenames.
          cm_listbox_file_global = "cm_list_" + str(cm_textbox_newfile_global) + ".txt"
          dict_filename_global = "dict_file_" + str(cm_textbox_newfile_global) + ".txt"
          cnotes_dict_file_global = "cnotes_" + str(cm_textbox_newfile_global) + ".txt"

          # Create APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
          # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
          # which gives us the FULL PATH NAME to our contact_management.py data files. 
       
          fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
       
          fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )

          fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

          fullpath_prepend_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )
        
       
          # Create the new Contact List File and add Titles 
          with open(fullpath_fn_cm_listbox_file_global, 'a') as wf_titles:
                wf_titles.flush()
                wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "," + "\n")


        
          # Create the File for Contact DICTIONARY Filename dict_filename_global
          with open(fullpath_fn_dict_filename_global, 'a') as new_wdictf:
                new_wdictf.flush()
                new_wdictf.write("\n")


          # Create the File for Contact NOTES DICTIONARY Filename cnotes_dict_file_global
          with open(fullpath_cnotes_dict_file_global, 'a') as new_notes_wdictf:
                new_notes_wdictf.flush()
                new_notes_wdictf.write("\n")


          # write a new logfile to update the logfile items each time a new Contact List is Created
          inst_Write_Main_Logfile_first_contact_list = Write_Main_Logfile()
          inst_Write_Main_Logfile_first_contact_list.write_update_logfile()
        
          return
    

      #####################################################################
      #
      #     global OBJECT_toplevel_cm_app_doc_media
      #     global OBJECT_toplevel_excel_import_export
      #     global OBJECT_toplevel_app_status_panel
      #     global OBJECT_toplevel_user_gui_config_class
      #     global OBJECT_toplevel_list_builder
      #     global OBJECT_toplevel_view_contact_list
      #     global OBJECT_toplevel_new_contact_list
      #     global OBJECT_toplevel_select_contact_list
      #     global OBJECT_toplevel_system_admin_info
      #     global OBJECT_toplevel_email_gmail_class
      #     global OBJECT_toplevel_config_setting_class
      #  
      # List_of_WINDOWS = ["WINDOW SELECT", "cm_app_doc_media", "excel_import_export", "app_status_panel", \
      #                    "user_gui_config_class", "list_builder", "view_contact_list", "new_contact_list", \
      #                    "select_contact_list","system_admin_info", "email_gmail_class", "config_setting_class"]
      #
      # window_select_global = "WINDOW SELECT"
      #
      def func_set_window_select_global(self, window_select_opt_menu_select):
             global window_select_global

             # Set the GLOBAL for the newly selected window_select_global 
             window_select_global = str(window_select_opt_menu_select)

             if window_select_global == "WINDOW SELECT":

                 return
             
             elif (window_select_global == "cm_app_doc_media"):

                   # print(".... select window:  cm_app_doc_media ")
                   self.cm_app_doc_media_window_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "excel_import_export"):

                   # print(".... select window:  excel_import_export ")
                   self.export_CSV_for_Excel_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "app_status_panel"):

                   # print(".... select window:  app_status_panel ")
                   self.select_App_Status_Display_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "list_builder"):

                   # print(".... select window:  list_builder ")
                   self.build_list_from_dual_listbox_window_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "view_contact_list"):

                   # print(".... select window:  view_contact_list ")
                   self.view_mode_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "new_contact_list"):

                   # print(".... select window:  new_contact_list ")
                   self.new_list_window_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "select_contact_list"):

                   # print(".... select window:  select_contact_list ")
                   self.new_window_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )
 
             elif (window_select_global == "system_admin_info"): 

                 # print(".... select window:  system_admin_info ")
                 self.system_administration_View_method()
                 window_select_global = "WINDOW SELECT"
                 self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "email_gmail_class"):

                   # print(".... select window:  email_gmail_class ")
                   self.email_Gmail_Feature_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "config_setting_class"):

                   # print(".... select window:  config_setting_class ")
                   self.config_App_Settings_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "CRM STARTUP"):

                   # print(".... select window:   CRM STARTUP")
                   self.crm_startup_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "MEDICAL RECORD"):

                   # print(".... select window:  MEDICAL RECORD ")
                   self.user_defined_gui_window_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "COMMAND CENTER"):

                   # print(".... select window:  COMMAND CENTER STARTUP ")
                   self.COMMAND_CENTER_STARTUP_method()
                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )

             elif (window_select_global == "E X I T"):

                   window_select_global = "WINDOW SELECT"
                   self.window_select_opt_menu_select.set(str(window_select_global) )
                   # print(".... E X I T .... self.exit_Handler")
                   self.exit_Handler()
                   
             else:
                   pass


             
      ######################################################################################
      #    
      # crm_startup_screen_show_method to cycle through a SET OF SCREENS to quickly activate 
      # the Customer Relationship Management (CRM) Screen Views. 
      #        
      ######################################################################################
      #
      def crm_startup_screen_show_method(self):
          global master_cm_list_name_global
          global cm_filename_value
          global cm_listbox_file_global
          global dict_filename_global
          global fullpath_fn_cm_listbox_file_global
          global fullpath_fn_dict_filename_global
          global cnotes_dict_file_global
          global fullpath_cnotes_dict_file_global
          global kick_thread_to_update_main_entry_widgets
          global kick_thread_to_update_email_contact_entry_widgets
          global selected_dictionary_record_index_global
          global selected_dictionary_record_index_focus_global

          # print(".... CRM STARTUP method is active ......")

          # Set All CONTACT LIST GLOBALS to CONTACT-LIST-ONE

          master_cm_list_name_global = "CONTACT-LIST-ONE"
          cm_filename_value = "cm_list_" + str(master_cm_list_name_global) + ".txt"
          cm_listbox_file_global = cm_filename_value
          dict_filename_global = "dict_file_" + str(master_cm_list_name_global) + ".txt"
          fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
          fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )
          cnotes_dict_file_global = "cnotes_" + str(master_cm_list_name_global) + ".txt"
          fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

          # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
          # WHICH UPDATES and SETS THE selected_dictionary_loaded_global GLOBAL.    

          inst_load_and_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
          startup_loaded_contact_dict_acquired = inst_load_and_Process_Dict_File.read_target_dict_file()

          # write a new logfile to update the logfile items each time a new Contact List is Created
          inst_Write_Main_Logfile_start_sequence_contact_list = Write_Main_Logfile()
          inst_Write_Main_Logfile_start_sequence_contact_list.write_update_logfile()

          selected_dictionary_record_index_global = 1
          selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global

          kick_thread_to_update_main_entry_widgets = False
          kick_thread_to_update_email_contact_entry_widgets = False

          time.sleep(.25)

          kick_thread_to_update_main_entry_widgets = True

          self.system_administration_View_method()

          self.after(2000, lambda: self.new_list_window_method() )

          self.after(3000, lambda: self.new_window_method() )

          self.after(4000, lambda: self.view_mode_method() )

          self.after(5000, lambda: self.export_CSV_for_Excel_method() )

          self.after(6000, lambda: self.build_list_from_dual_listbox_window_method() )

          self.after(7000, lambda: self.cm_app_doc_media_window_method() )

          self.after(8000, lambda: self.email_Gmail_Feature_method() )

          self.after(8050, lambda: self.kick_thread_email_entry_widgets() )

          self.after(9000, lambda: self.select_App_Status_Display_method() )

          self.after(10000, lambda: self.config_App_Settings_method() )

          self.after(11000, lambda: OBJECT_main.lift() )

          self.after(11050, lambda: self.kick_thread_main_entry_widgets() )

          self.after(11100, lambda: self.COMMAND_CENTER_STARTUP_method() )



      def FLASH_NIGHT_MODE_SELECT_BUTTON_yellow(self):
          self.night_mode_button.config(background="DarkGoldenrod1", foreground="black")

      def FLASH_NIGHT_MODE_SELECT_BUTTON_pink(self):
          self.night_mode_button.config(background="deep pink", foreground="black")

      def FLASH_NIGHT_MODE_SELECT_BUTTON_blue(self):
          self.night_mode_button.config(background="dodger blue", foreground="black")

      def FLASH_NIGHT_MODE_SELECT_BUTTON_red(self):
          self.night_mode_button.config(background="red", foreground="black")

      def FLASH_NIGHT_MODE_SELECT_BUTTON_cyan(self):
          self.night_mode_button.config(background="cyan", foreground="black")

      def FLASH_NIGHT_MODE_SELECT_BUTTON_green(self):
          self.night_mode_button.config(background="light sea green", foreground="black")

      def FLASH_NIGHT_MODE_SELECT_BUTTON_normal(self):
          self.night_mode_button.config(background="dark slate gray", foreground = "light sea green")


      def kick_thread_email_entry_widgets(self):
          global kick_thread_to_update_email_contact_entry_widgets
          kick_thread_to_update_email_contact_entry_widgets = True


      def kick_thread_main_entry_widgets(self):
          global kick_thread_to_update_main_entry_widgets
          kick_thread_to_update_main_entry_widgets = True
          
          
      ######################################################################################
      #     
      # crm_startup_method to activate a SET OF SCREENS to setup the USER  
      # with Customer Relationship Management (CRM) Screen Views. 
      #       
      ######################################################################################
      #
      def crm_startup_method(self):

          # #  self.display_messagebox_CYCLE_SCREENS()

          self.crm_startup_screen_show_method()


      ######################################################################################
      # 
      # Mode Select Optons Menu StringVar setting ... 
      #  
      # if mode_select_global == "Browse Mode":
      # then insert a check for existance of DICTIONARY FILE here ...... if not then messagebox 
      #  
      # Set Contact Textbox StringVar Values from STORED DICTIONARY FILE 
      #    
      # First disable Contact Textbox Entry and clear Contact Textbox 
      #     
      ######################################################################################
      #
      def func_set_mode_select_global(self, mode_select_opt_menu_select):
             global mode_select_global
             global selected_dictionary_record_index_global
             global selected_dictionary_record_index_focus_global
             global kick_thread_to_update_main_entry_widgets

             # Set the GLOBAL for the newly selected mode_select_global (Entry, Edit, or Browse mode)
             mode_select_global = str(mode_select_opt_menu_select)

             if mode_select_global != "Edit Mode":
             
                 self.entry_first.set(str("") )
                 self.entry_first.set(str("") )
                 self.entry_last.set(str("") )
                 self.entry_streetadd.set(str("") )
                 self.entry_citytown.set(str("") )
                 self.entry_state.set(str("") )
                 self.entry_zipcode.set(str("") )
                 self.entry_phonenum.set(str("") )
                 self.entry_email.set(str("") )
                 self.entry_website.set(str("") )
                 self.contact_dict_count_status.set(str("") )
                 

             # Verify there is a DICTIONARY Selected - adding "Edit Mode"
             if (str(dict_filename_global) == "No Contact Dictionary") and (mode_select_global == "Browse Mode"):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nBrowse Mode requires that you\nfirst SELECT an existing Contact List\nto Browse Contacts\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

             elif (str(dict_filename_global) == "No Contact Dictionary") and (mode_select_global == "Entry Mode"):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nEntry Mode requires that you\nfirst SELECT a Contact List or create a NEW Contact List\nto Enter and Edit Contacts\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

             elif (str(dict_filename_global) == "No Contact Dictionary") and (mode_select_global == "Edit Mode"):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nEdit Mode requires that you\nfirst SELECT a Contact List or create a NEW Contact List\nto Enter and Edit Contacts\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

             elif (mode_select_global == "Browse Mode") and (str(dict_filename_global) != "No Contact Dictionary"):
                   
                   # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
                   # WHICH SETS THE selected_dictionary_loaded_global GLOBAL.  

                   inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
                   loaded_contact_dict_acquired_GLOBAL = inst_loaded_Process_Dict_File.read_target_dict_file()

                   #selected_dictionary_record_index_global = 1
                   #selected_dictionary_record_index_focus_global = 1
                   
                   kick_thread_to_update_main_entry_widgets = True

             elif  (mode_select_global == "Entry Mode") and (str(dict_filename_global) != "No Contact Dictionary"):

                   pass

             elif  (mode_select_global == "Edit Mode") and (str(dict_filename_global) != "No Contact Dictionary"):

                   # Edit_Mode means that the USER is interested in EDITING the current Contact
                   # that is displayed on the Main Screen. Note that when the USER selects Edit_Mode,
                   # we must capture the state of the following pointers:
                   #
                   #  selected_dictionary_record_index_global   AND   selected_dictionary_record_index_focus_global
                   # 
                   # then verify that the Main Screen Entry Widgets are enabled for modification of data,
                   # and then wait for the USER to complete their editing of the Main Screen Entry Widgets 
                   # contact data which will be captured with the SAVE CONTACT ENTRY BUTTON.

                   #  EDIT MODE will be executed in method:  self.edit_mode_contact_update()

                   pass

             else:
                   pass



      #####################################################################################
      #
      #   Method:   decision_SAVE_CONTACT_ENTRY(self)
      # 
      #   DECISION to select METHOD when SAVE_CONTACT_ENTRY Button is pressed.
      #
      #   DECISION will select method executed based on:
      #
      #   mode_select_global == "Entry Mode"   or   "Edit Mode"  or  "Browse Mode"
      #
      #   and based on whether a CONTACT LIST has been selected: 
      #
      #   i.e.  str(dict_filename_global) != "No Contact Dictionary")
      #
      #####################################################################################
      def decision_SAVE_CONTACT_ENTRY(self):
          global mode_select_global
          global dict_filename_global

          # # print(".... IN METHOD decision_SAVE_CONTACT_ENTRY.... mode_select_global = " + str(mode_select_global) )
            
          if ( (mode_select_global == "Entry Mode") and (str(dict_filename_global) != "No Contact Dictionary") ):
              self.finished_Data_Entry()
              
          elif ( (mode_select_global == "Edit Mode") and (str(dict_filename_global) != "No Contact Dictionary") ):
              self.edit_mode_contact_update()
              
          elif ( (mode_select_global == "Browse Mode") and (str(dict_filename_global) != "No Contact Dictionary") ):

              messagebox.showinfo("Contact Manager Guide ...", \
              "ATTENTION: \n\nPlease Select ENTRY MODE or EDIT MODE\nto ENTER or EDIT DATA in a Contact List.\nSee ENTRY MODE\nand EDIT MODE\nand BROWSE MODE\nMenu Widget\nat Top of Screen.")
              return

          elif (str(dict_filename_global) == "No Contact Dictionary"):
              messagebox.showinfo("Contact Manager Guide ...", \
              "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
              return



      #####################################################################################
      #   
      #   "Edit Mode" selection executes this METHOD to capture contact data updates. 
      #
      #####################################################################################
      def edit_mode_contact_update(self):
            global mode_select_global
            global cm_listbox_file_global
            global dict_filename_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global

            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return
  
            elif (str(self.entry_first.get() ) == "" or str(self.entry_last.get() ) == ""):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease .... FIRST and LAST NAME\nare REQUIRED or MANDATORY\nEntries to the Contact List.\nPlease Type in\nFIRST and LAST NAME.")
                  return

            # Scrolling IS INHIBITED DURING EDIT MODE ...
            # Dictionary Counters are Stationary ...
            #  
            # 1. ENTER NEW MODIFIED DATA RECORD to dic file and cm_list file by
            #    using self.finished_Data_Entry() 
            #
            # 2. THEN, GO BACK to each Database File and Delete *** specific number DATA RECORD ***
            # 
            # Execute Data Entry of the NEW Modified Contact Data
            # (with scrolling INHIBITED as a result of being in "Edit Mode".
            self.finished_Data_Entry()

            # Now we can focus on the remaining task of DELETING the OLD DATA RECORD ....
            # Now we can focus on the remaining task of DELETING the OLD DATA RECORD ....
            # Now we can focus on the remaining task of DELETING the OLD DATA RECORD ....
            #
            # Although, for this Version 8.0 BUILD, the issue of leaving the
            # old data record in the database is OK. 




      ######################################################################################
      # 
      #  METHOD TO CLICK OR SCROLL THROUGH CONTACTS USING methods:
      #
      #  forward_click()  and   backward_click()  and  emulate_the_scroll_method()
      # 
      #  which are using:
      #
      #  selected_dictionary_loaded_global
      #  selected_dictionary_record_index_global
      #  selected_dictionary_record_index_focus_global
      #  num_of_dictionary_data_records_global
      #  kick_thread_to_update_main_entry_widgets 
      #  kick_thread_to_update_email_contact_entry_widgets
      #  
      #  Also, if str(dict_filename_global) == "No Contact Dictionary",  
      #  this check for existance of DICTIONARY FILE here would 
      #  generate messagebox if no dictionary (contact list) is selected.
      #  However, Note that the App Class init method creates a default dictionary
      #  contact list called CONTACT-LIST-ONE to assure that there IS
      #  always a CONTACT LIST (and associated dictionary) selected.
      #  
      #  Set Main Screen Contact Textbox StringVar Values from STORED DICTIONARY FILE.
      #     
      ######################################################################################
      #                   
      def emulate_the_scroll_method(self):
          global kick_thread_to_update_main_entry_widgets
          # Verify there is a DICTIONARY Selected
          if str(dict_filename_global) == "No Contact Dictionary":
              messagebox.showinfo("Contact Manager Guide ...", \
              "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
              return

          elif mode_select_global == "Browse Mode":
                
              # Update the Main Screen Widgets with the new dictionary increment
              # or decrememtn pointer index by kicking this Thread in main():
              kick_thread_to_update_main_entry_widgets = True



      #####################################################################################
      # 
      #   Calls - Contact Manager Application Documentation Media Class - CM_App_Doc_Media
      #
      #####################################################################################
      #
      # Method to open new window for Application Documentation Media. 
      # 
      def cm_app_doc_media_window_method(self):
          global OBJECT_IN_APP_cm_app_doc_media

          if ( (OBJECT_toplevel_cm_app_doc_media.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_cm_app_doc_media) ):
              OBJECT_toplevel_cm_app_doc_media.lift()
              # print(".... OBJECT_toplevel_cm_app_doc_media.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_cm_app_doc_media))
          else:
              self.cm_app_doc_media_WINDOW = tk.Toplevel(self.master)
              self.cm_app_doc_media = CM_App_Doc_Media(self.cm_app_doc_media_WINDOW)

              OBJECT_IN_APP_cm_app_doc_media = self.cm_app_doc_media


          
      #####################################################################################
      # 
      #   Calls - User GUI Configuration Class - USER_GUI_Config_Class  
      #
      #####################################################################################
      # 
      # Method to open new windows for User GUI Configuration Class. 
      # 
      def user_defined_gui_window_method(self):
            global USER_GUI_Config_Class_inst_LIST
            global user_defined_gui_group_one
            global user_defined_gui_group_two
            global user_defined_gui_group_three
            global user_defined_gui_group_four
            global user_defined_gui_group_five
            global user_defined_gui_group_six
            global user_defined_gui_group_seven
            global user_defined_gui_group_eight
            global user_defined_gui_group_nine
            global user_defined_gui_group_ten
            global user_defined_gui_instance_count_GLOBAL
            global OBJECT_IN_APP_user_gui_1_config_class
            global OBJECT_IN_APP_user_gui_2_config_class
            global OBJECT_IN_APP_user_gui_3_config_class
            global OBJECT_IN_APP_user_gui_4_config_class
            global OBJECT_IN_APP_user_gui_5_config_class
            global OBJECT_IN_APP_user_gui_6_config_class
            global OBJECT_IN_APP_user_gui_7_config_class
            global OBJECT_IN_APP_user_gui_8_config_class
            global OBJECT_IN_APP_user_gui_9_config_class
            global OBJECT_IN_APP_user_gui_10_config_class

            if ( (OBJECT_toplevel_user_gui_1_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_1_config_class) ):
                OBJECT_toplevel_user_gui_1_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_1_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_1_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 1              
            
                # Instance of USER_GUI_Config_Class - GROUP ONE
                self.user_defined_gui_WINDOW_group_one = tk.Toplevel(self.master)
                user_defined_gui_group_one = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_one)

                OBJECT_IN_APP_user_gui_1_config_class = user_defined_gui_group_one


            if ( (OBJECT_toplevel_user_gui_2_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_2_config_class) ):
                OBJECT_toplevel_user_gui_2_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_2_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_2_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 2
            
                # Instance of USER_GUI_Config_Class - GROUP TWO
                self.user_defined_gui_WINDOW_group_two = tk.Toplevel(self.master)
                user_defined_gui_group_two = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_two)

                OBJECT_IN_APP_user_gui_2_config_class = user_defined_gui_group_two

                
            if ( (OBJECT_toplevel_user_gui_3_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_3_config_class) ):
                OBJECT_toplevel_user_gui_3_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_3_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_3_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 3

                # Instance of USER_GUI_Config_Class - GROUP THREE 
                self.user_defined_gui_WINDOW_group_three = tk.Toplevel(self.master)
                user_defined_gui_group_three = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_three)

                OBJECT_IN_APP_user_gui_3_config_class = user_defined_gui_group_three

               
            if ( (OBJECT_toplevel_user_gui_4_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_4_config_class) ):
                OBJECT_toplevel_user_gui_4_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_4_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_4_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 4

                # Instance of USER_GUI_Config_Class - GROUP FOUR
                self.user_defined_gui_WINDOW_group_four = tk.Toplevel(self.master)
                user_defined_gui_group_four = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_four)

                OBJECT_IN_APP_user_gui_4_config_class = user_defined_gui_group_four

               
            if ( (OBJECT_toplevel_user_gui_5_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_5_config_class) ):
                OBJECT_toplevel_user_gui_5_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_5_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_5_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 5

                # Instance of USER_GUI_Config_Class - GROUP FIVE
                self.user_defined_gui_WINDOW_group_five = tk.Toplevel(self.master)
                user_defined_gui_group_five = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_five)

                OBJECT_IN_APP_user_gui_5_config_class = user_defined_gui_group_five

                
            if ( (OBJECT_toplevel_user_gui_6_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_6_config_class) ):
                OBJECT_toplevel_user_gui_6_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_6_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_6_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 6

                # Instance of USER_GUI_Config_Class - GROUP SIX 
                self.user_defined_gui_WINDOW_group_six = tk.Toplevel(self.master)
                user_defined_gui_group_six = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_six)

                OBJECT_IN_APP_user_gui_6_config_class = user_defined_gui_group_six

               
            if ( (OBJECT_toplevel_user_gui_7_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_7_config_class) ):
                OBJECT_toplevel_user_gui_7_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_7_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_7_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 7

                # Instance of USER_GUI_Config_Class - GROUP SEVEN
                self.user_defined_gui_WINDOW_group_seven = tk.Toplevel(self.master)
                user_defined_gui_group_seven = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_seven)

                OBJECT_IN_APP_user_gui_7_config_class = user_defined_gui_group_seven


            if ( (OBJECT_toplevel_user_gui_8_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_8_config_class) ):
                OBJECT_toplevel_user_gui_8_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_8_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_8_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 8

                # Instance of USER_GUI_Config_Class - GROUP EIGHT  
                self.user_defined_gui_WINDOW_group_eight = tk.Toplevel(self.master)
                user_defined_gui_group_eight = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_eight)

                OBJECT_IN_APP_user_gui_8_config_class = user_defined_gui_group_eight
                

            if ( (OBJECT_toplevel_user_gui_9_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_9_config_class) ):
                OBJECT_toplevel_user_gui_9_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_9_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_9_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 9

                # Instance of USER_GUI_Config_Class - GROUP NINE
                self.user_defined_gui_WINDOW_group_nine = tk.Toplevel(self.master)
                user_defined_gui_group_nine = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_nine)

                OBJECT_IN_APP_user_gui_9_config_class = user_defined_gui_group_nine


            if ( (OBJECT_toplevel_user_gui_10_config_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_user_gui_10_config_class) ):
                OBJECT_toplevel_user_gui_10_config_class.lift()
                # print(".... OBJECT_toplevel_user_gui_10_config_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_user_gui_10_config_class))
            else:
                user_defined_gui_instance_count_GLOBAL = 10

                # Instance of USER_GUI_Config_Class - GROUP TEN
                self.user_defined_gui_WINDOW_group_ten = tk.Toplevel(self.master)
                user_defined_gui_group_ten = USER_GUI_Config_Class(self.user_defined_gui_WINDOW_group_ten)

                OBJECT_IN_APP_user_gui_10_config_class = user_defined_gui_group_ten

                
      ##################################################################################### 
      # 
      #   VIEW System Administration Info Screen - class System_Admin_Info(Frame)   
      #  
      #####################################################################################
      # Method to open new window with TEXTBOX to VIEW System Administration Information.
      def system_administration_View_method(self):
          global fullpath_fn_cm_sw_app_logfile_global
          global OBJECT_IN_APP_system_admin_info

          if ( (OBJECT_toplevel_system_admin_info.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_system_admin_info) ):
              OBJECT_toplevel_system_admin_info.lift()
              # print(".... OBJECT_toplevel_system_admin_info.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_system_admin_info))
          else:
              self.system_administration_View = tk.Toplevel(self.master)
              self.cm_app_sys_admin = System_Admin_Info(self.system_administration_View)

              OBJECT_IN_APP_system_admin_info = self.cm_app_sys_admin

                
      ##################################################################################### 
      # 
      #   UVM SEQ ITEM - TEMPLATE WINDOW
      #  
      #####################################################################################
      # Method to open new window with TEXTBOX to VIEW System Administration Information.
      def sys_admin_View_UVM_SEQ_ITEM_method(self):
          global fullpath_fn_cm_sw_app_logfile_global
          global OBJECT_IN_APP_system_admin_info

          if ( (OBJECT_toplevel_system_admin_info.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_system_admin_info) ):
              OBJECT_toplevel_system_admin_info.lift()
              # print(".... OBJECT_toplevel_system_admin_info.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_system_admin_info))
          else:
              self.system_administration_View = tk.Toplevel(self.master)
              self.cm_app_sys_admin = System_Admin_Info(self.system_administration_View)

              OBJECT_IN_APP_system_admin_info = self.cm_app_sys_admin

                
      ##################################################################################### 
      # 
      #   UVM SEQUENCE - TEMPLATE WINDOW
      #  
      #####################################################################################
      # Method to open new window with TEXTBOX to VIEW System Administration Information.
      def sys_admin_View_UVM_SEQUENCE_method(self):
          global fullpath_fn_cm_sw_app_logfile_global
          global OBJECT_IN_APP_system_admin_info

          if ( (OBJECT_toplevel_system_admin_info.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_system_admin_info) ):
              OBJECT_toplevel_system_admin_info.lift()
              # print(".... OBJECT_toplevel_system_admin_info.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_system_admin_info))
          else:
              self.system_administration_View = tk.Toplevel(self.master)
              self.cm_app_sys_admin = System_Admin_Info(self.system_administration_View)

              OBJECT_IN_APP_system_admin_info = self.cm_app_sys_admin


                
      ##################################################################################### 
      # 
      #   UVM ENV - TEMPLATE WINDOW
      #  
      #####################################################################################
      # Method to open new window with TEXTBOX to VIEW System Administration Information.
      def sys_admin_View_UVM_ENV_method(self):
          global fullpath_fn_cm_sw_app_logfile_global
          global OBJECT_IN_APP_system_admin_info

          if ( (OBJECT_toplevel_system_admin_info.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_system_admin_info) ):
              OBJECT_toplevel_system_admin_info.lift()
              # print(".... OBJECT_toplevel_system_admin_info.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_system_admin_info))
          else:
              self.system_administration_View = tk.Toplevel(self.master)
              self.cm_app_sys_admin = System_Admin_Info(self.system_administration_View)

              OBJECT_IN_APP_system_admin_info = self.cm_app_sys_admin

                
      ##################################################################################### 
      # 
      #   UVM SCBD - TEMPLATE WINDOW
      #  
      #####################################################################################
      # Method to open new window with TEXTBOX to VIEW System Administration Information.
      def sys_admin_View_UVM_SCBD_method(self):
          global fullpath_fn_cm_sw_app_logfile_global
          global OBJECT_IN_APP_system_admin_info

          if ( (OBJECT_toplevel_system_admin_info.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_system_admin_info) ):
              OBJECT_toplevel_system_admin_info.lift()
              # print(".... OBJECT_toplevel_system_admin_info.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_system_admin_info))
          else:
              self.system_administration_View = tk.Toplevel(self.master)
              self.cm_app_sys_admin = System_Admin_Info(self.system_administration_View)

              OBJECT_IN_APP_system_admin_info = self.cm_app_sys_admin

               
      ##################################################################################### 
      # 
      #   UVM TB PKG - TEMPLATE WINDOW
      #  
      #####################################################################################
      # Method to open new window with TEXTBOX to VIEW System Administration Information.
      def sys_admin_View_UVM_TB_PKG_method(self):
          global fullpath_fn_cm_sw_app_logfile_global
          global OBJECT_IN_APP_system_admin_info

          if ( (OBJECT_toplevel_system_admin_info.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_system_admin_info) ):
              OBJECT_toplevel_system_admin_info.lift()
              # print(".... OBJECT_toplevel_system_admin_info.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_system_admin_info))
          else:
              self.system_administration_View = tk.Toplevel(self.master)
              self.cm_app_sys_admin = System_Admin_Info(self.system_administration_View)

              OBJECT_IN_APP_system_admin_info = self.cm_app_sys_admin




      #####################################################################################
      # 
      #   Email Feature Class and Methods:  Instantiaing class Email_Gmail_Class
      #
      #####################################################################################
      #
      # Method execute Email (Gmail) functionality.
      # Open new window and add Email (Gmail) functionality.
      # 
      def email_Gmail_Feature_method(self):
            global OBJECT_IN_APP_email_gmail_class
            #
            # Before we launch a new window, be sure we have a DICTIONARY LOADED.
            #
            # Note that OAUTH2 Credentials will have to be acquired from a Google Console
            # to operate the secure GMAIL API. Here are the Instructions: 
            #
            # https://developers.google.com/gmail/api/quickstart/python
            #
            # https://console.developers.google.com/flows/enableapi?apiid=gmail
            #
            # Verify there is a DICTIONARY Selected.
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen.\n\n..... Press OK to Continue .....\n")
                  
                  return

            if ( (OBJECT_toplevel_email_gmail_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_email_gmail_class) ):
                OBJECT_toplevel_email_gmail_class.lift()
                # print(".... OBJECT_toplevel_email_gmail_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_email_gmail_class))
            else:
                self.email_Gmail_Feature = tk.Toplevel(self.master)
                self.cm_app_email = Email_Gmail_Class(self.email_Gmail_Feature)

                OBJECT_IN_APP_email_gmail_class = self.cm_app_email


      ##################################################################################################
      # 
      #   BUILD a NEW or EXISTING CONTACT LIST from EXISTING CONTACTS LISTS using TWO LISTBOX WIDGETS    
      #
      ##################################################################################################
      # Method to open new window with two LISTBOXES to BUILD a NEW or EXISTING CONTACT LIST
      # from EXISTING CONTACTS LISTS using TWO LISTBOX WIDGETS. 
      def build_list_from_dual_listbox_window_method(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global OBJECT_IN_APP_list_builder

            if ( (OBJECT_toplevel_list_builder.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_list_builder) ):
                OBJECT_toplevel_list_builder.lift()
                # print(".... OBJECT_toplevel_list_builder.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_list_builder))
            else:
                # self.contact_dict_count_status.set(str("") )
                selected_dictionary_record_index_global = 1
                selected_dictionary_record_index_focus_global = 1
             
                # self.build_list_dual_listbox_window = tk.Toplevel(self.master)
                # self.cm_app_dual_listbox = List_Builder(self.build_list_dual_listbox_window)
                # OBJECT_IN_APP_list_builder = self.cm_app_dual_listbox


      #####################################################################################
      # 
      #   SELECT CONTACT LIST from LISTBOX    
      #
      #####################################################################################
      # Method to open new window with LISTBOX of cm_list_ files to select a CONTACT LIST.
      def new_window_method(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global OBJECT_IN_APP_select_contact_list

            if ( (OBJECT_toplevel_select_contact_list.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_select_contact_list) ):
                OBJECT_toplevel_select_contact_list.lift()
                # print(".... OBJECT_toplevel_select_contact_list.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_select_contact_list))
            else:
                self.entry_first.set(str("") )
                self.entry_first.set(str("") )
                self.entry_last.set(str("") )
                self.entry_streetadd.set(str("") )
                self.entry_citytown.set(str("") )
                self.entry_state.set(str("") )
                self.entry_zipcode.set(str("") )
                self.entry_phonenum.set(str("") )
                self.entry_email.set(str("") )
                self.entry_website.set(str("") )
                self.contact_dict_count_status.set(str("") )
                selected_dictionary_record_index_global = 1
                selected_dictionary_record_index_focus_global = 1
             
                self.select_contact_list_Window = tk.Toplevel(self.master)
                self.cm_app_select_contact_list = Select_Contact_List(self.select_contact_list_Window)

                OBJECT_IN_APP_select_contact_list = self.cm_app_select_contact_list



      #####################################################################################
      #
      #   APPLICATION STATUS PANEL DISPLAY
      #
      ##################################################################################### 
      # 
      def select_App_Status_Display_method(self):
            global gmail_oauth2_json_file_test_global
            global gmail_oauth2_status_global
            global gmail_oauth2_exceptions_status_global
            global gmail_oauth2_SPECIFIC_EXCEPTION_global
            global gmail_smtp_allow_less_secure_apps_global
            global gmail_smtp_status_global
            global gmail_smtp_exceptions_status_global
            global gmail_smtp_SPECIFIC_EXCEPTION_global
            global gmail_logged_in_global
            global cm_dict_file_startup_test_global
            global cm_csv_file_startup_test_global
            global cm_notes_file_startup_test_global
            global valid_client_secret_key_format_global
            global OBJECT_IN_APP_app_status_panel

            if ( (OBJECT_toplevel_app_status_panel.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_app_status_panel) ):
                OBJECT_toplevel_app_status_panel.lift()
                # print(".... OBJECT_toplevel_app_status_panel.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_app_status_panel))
            else:
                self.app_status_panel_Window = tk.Toplevel(self.master)
                self.cm_app_status_panel = App_Status_Panel(self.app_status_panel_Window)

                OBJECT_IN_APP_app_status_panel = self.cm_app_status_panel


      #####################################################################################
      #
      #   CONFIGURE APP SETTINGS 
      #
      ##################################################################################### 
      # Method to read app_config.ini file and CONFIGURE APP SETTINGS.
      def config_App_Settings_method(self):
            global fullpath_app_config_ini_global
            global mainscreen_bg_color_val_global
            global viewscreen_bg_color_val_global
            global OBJECT_IN_APP_config_setting_class

            if ( (OBJECT_toplevel_config_setting_class.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_config_setting_class) ):
                OBJECT_toplevel_config_setting_class.lift()
                # print(".... OBJECT_toplevel_config_setting_class.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_config_setting_class))
            else:
                self.config_App_Settings = tk.Toplevel(self.master)
                self.cm_app_config_app_settings = Config_Setting_Class(self.config_App_Settings)
                
                OBJECT_IN_APP_config_setting_class = self.cm_app_config_app_settings


                
      #######################################################################
      #
      #   CREATE NEW CONTACT LIST FILE and new DICTIONARY FILE from TEXTBOX
      #
      #######################################################################
      # Method to open new window with TEXTBOX to ENTER a CONTACT LIST NAME
      # that is then used to update the GLOBALS :
      # cm_textbox_newfile_global,
      # cm_listbox_file_global,
      # dict_filename_global,
      # and then CREATE the FILES for
      # cm_list_  and  dict_file_
      def new_list_window_method(self):
            global selected_dictionary_record_index_global
            global OBJECT_IN_APP_new_contact_list

            if ( (OBJECT_toplevel_new_contact_list.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_new_contact_list) ):
                OBJECT_toplevel_new_contact_list.lift()
                # print(".... OBJECT_toplevel_new_contact_list.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_new_contact_list))
            else:                
                self.entry_first.set(str("") )
                self.entry_first.set(str("") )
                self.entry_last.set(str("") )
                self.entry_streetadd.set(str("") )
                self.entry_citytown.set(str("") )
                self.entry_state.set(str("") )
                self.entry_zipcode.set(str("") )
                self.entry_phonenum.set(str("") )
                self.entry_email.set(str("") )
                self.entry_website.set(str("") )
                self.contact_dict_count_status.set(str("") )
                selected_dictionary_record_index_global = 0
            
                self.new_contact_list_Window = tk.Toplevel(self.master)
                self.cm_app_new_contact_list = New_Contact_List(self.new_contact_list_Window)

                OBJECT_IN_APP_new_contact_list = self.cm_app_new_contact_list



      ######################################################3333#################
      #
      #   VIEW CONTACTS extracted from CONTACT DICTIONARY FILE in LARGE TEXTBOX
      #
      #######################################################3333################
      # Method to open a new window to VIEW CONTACTS by  
      # extracting them with a read() from the dict_file_
      # into a string variable, and then splitting that
      # string variable by searching for DATA_RECORD_DELIMITER 
      # and KEY_SYNC strings to process data and display the
      # data to a LARGE TEXTBOX. 
      def view_mode_method(self):
            global dict_filename_global
            global viewscreen_bg_color_val_global
            global selected_dictionary_record_index_global
            global OBJECT_IN_APP_view_contact_list

            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

            if ( (OBJECT_toplevel_view_contact_list.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_view_contact_list) ):
                OBJECT_toplevel_view_contact_list.lift()
                # print(".... OBJECT_toplevel_view_contact_list.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_view_contact_list))
            else:            
                self.entry_first.set(str("") )
                self.entry_first.set(str("") )
                self.entry_last.set(str("") )
                self.entry_streetadd.set(str("") )
                self.entry_citytown.set(str("") )
                self.entry_state.set(str("") )
                self.entry_zipcode.set(str("") )
                self.entry_phonenum.set(str("") )
                self.entry_email.set(str("") )
                self.entry_website.set(str("") )
                self.contact_dict_count_status.set(str("") )
                selected_dictionary_record_index_global = 0
            
                # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
                # WHICH UPDATES and SETS THE selected_dictionary_loaded_global GLOBAL.   

                inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
                loaded_contact_dict_acquired = inst_loaded_Process_Dict_File.read_target_dict_file()
            
                self.view_contact_list_Window = tk.Toplevel(self.master)
                self.cm_app_view_contact_list = View_Contact_List(self.view_contact_list_Window)

                OBJECT_IN_APP_view_contact_list = self.cm_app_view_contact_list

                

      ##############################################################################
      #
      #   E X P O R T  (Contact List CSV to Excel) 
      #     
      #   EXPORT CSV DATA for EXCEL SPREADHSEET and EXCEL WORKBOOKS.
      #
      #   I M P O R T  (Excel CSV or any CSV to Contact Management Contact List)
      #
      #   IMPORT CSV FROM EXCEL TO CONTACT MANAGEMENT APP CONTACT LIST.
      #
      def export_CSV_for_Excel_method(self):
            global username_global
            global userprofile_global
            global appdata_path_global
            global cm_appdatafiles_path_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global
            global cm_listbox_file_global
            global dict_filename_global
            global master_cm_list_name_global
            global import_excel_csv_userprofile_global
            global import_excel_csv_cm_appdata_global
            global export_csv_excel_userprofile_global
            global export_csv_excel_cm_appdata_global
            global export_to_excel_listbox_select_fn_global
            global new_excel_file_created_global
            global OBJECT_IN_APP_excel_import_export

            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

            if ( (OBJECT_toplevel_excel_import_export.winfo_exists() ) == True) and ("toplevel" in str(OBJECT_toplevel_excel_import_export) ):
                OBJECT_toplevel_excel_import_export.lift()
                # print(".... OBJECT_toplevel_excel_import_export.winfo_exists() ) == True:  lift() " + str(OBJECT_toplevel_excel_import_export))
            else:            
                # Open Window for Export to Excel LISTBOX Selection
                self.excel_import_export_Window = tk.Toplevel(self.master)
                self.cm_app_excel_import_export = Excel_Import_Export(self.excel_import_export_Window)

                OBJECT_IN_APP_excel_import_export = self.cm_app_excel_import_export



      ###################################################
      #
      # SORT AND RE-WRITE DATA FILES 
      #
      ###################################################
      #
      def sort_Contact_List(self):
            global dict_filename_global
            global fullpath_fn_dict_filename_global
            global selected_dictionary_record_index_global
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

            self.entry_first.set(str("") )
            self.entry_first.set(str("") )
            self.entry_last.set(str("") )
            self.entry_streetadd.set(str("") )
            self.entry_citytown.set(str("") )
            self.entry_state.set(str("") )
            self.entry_zipcode.set(str("") )
            self.entry_phonenum.set(str("") )
            self.entry_email.set(str("") )
            self.entry_website.set(str("") )
            self.contact_dict_count_status.set(str("") )
            selected_dictionary_record_index_global = 0
            
            # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES 

            inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
            contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()

            messagebox.showinfo("Contact Manager Guide ...", \
            "ATTENTION: \n\nSTATUS UPDATE:\nYour Contact Data\nhas been SORTED\nby LAST NAME\n..... Press OK to Continue .....")

            return



      def forward_fast(self):
          pass

            
      def forward_scroll(self):
            # (self, event)
            pass
            ## #print("Executing - forward_scroll METHOD")
            #self.report_event(event)

            
      def forward_tick(self):
            # (self, event)
            pass
            ## #print("Executing - forward_tick METHOD")
            #self.report_event(event)  


      #################################################################
      #
      #  Implement Forward Click Button Control
      #  to SCROLL through selected DICTIONARY
      # 
      #################################################################
      #
      def forward_click(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global num_of_dictionary_data_records_global
            global kick_thread_to_update_email_contact_entry_widgets

            # print(".... FORWARD-CLICK .... selected_dictionary_record_index_global = " + str(selected_dictionary_record_index_global) )

            # print(".... FORWARD-CLICK .... selected_dictionary_record_index_focus_global = " + str(selected_dictionary_record_index_focus_global) )
            
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return
            elif mode_select_global == "Browse Mode":
                  test_forward_count = selected_dictionary_record_index_global + 1
                  if test_forward_count <= num_of_dictionary_data_records_global:
                        selected_dictionary_record_index_global +=1
                        selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global
                        self.emulate_the_scroll_method()
                  elif test_forward_count > num_of_dictionary_data_records_global:
                        return
            elif ( (mode_select_global == "Entry Mode") or (mode_select_global == "Edit Mode") ):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease Select BROWSE MODE\nto Scroll the Contact List.\nSee BROWSE MODE\nand ENTRY MODE\nand EDIT MODE\nMenu Widget\nat Top of Screen.")

            # Each time the Main Class Instance Contact Button Increments or Decrements:
            # kick the main() widgets update thread to update email screen widgets
            # that display contact info, specifically:
            # -- Widget that Displays FIRST NAME  LAST NAME
            # -- Widget that Displays DESTINATION EMAIL ADDRESS
            # -- WIDGET that displays CONTACT NUMBER STATUS
            # by setting kick_thread_to_update_email_contact_entry_widgets = True
            kick_thread_to_update_email_contact_entry_widgets = True


            
                  
      #################################################################
      #
      #  Implement Backward Click Button Control
      #  to SCROLL through selected DICTIONARY   
      #
      #################################################################
      #
      def backward_click(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global num_of_dictionary_data_records_global
            global kick_thread_to_update_email_contact_entry_widgets

            # print(".... BACKWARD-CLICK .... selected_dictionary_record_index_global = " + str(selected_dictionary_record_index_global) )

            # print(".... BACKWARD-CLICK .... selected_dictionary_record_index_focus_global = " + str(selected_dictionary_record_index_focus_global) )
            
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return
            elif mode_select_global == "Browse Mode":
                  test_backward_count = selected_dictionary_record_index_global - 1
                  if test_backward_count >= 1:
                        selected_dictionary_record_index_global -=1
                        selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global
                        self.emulate_the_scroll_method()
                  elif test_backward_count < 1:
                        return
            elif ( (mode_select_global == "Entry Mode") or (mode_select_global == "Edit Mode") ):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease Select BROWSE MODE\nto Scroll the Contact List.\nSee BROWSE MODE\nand ENTRY MODE\nand EDIT MODE\nMenu Widget\nat Top of Screen.")
                  
            # Each time the Main Class Instance Contact Button Increments or Decrements:
            # kick the main() widgets update thread to update email screen widgets
            # that display contact info, specifically:
            # -- Widget that Displays FIRST NAME  LAST NAME
            # -- Widget that Displays DESTINATION EMAIL ADDRESS
            # -- WIDGET that displays CONTACT NUMBER STATUS
            # by setting kick_thread_to_update_email_contact_entry_widgets = True
            kick_thread_to_update_email_contact_entry_widgets = True


            
      def backward_tick(self):
            # (self, event)
            pass
            ## #print("Executing - backward_tick METHOD")
            #self.report_event(event)

            
      def backward_scroll(self):
            # (self, event)
            pass
            ## #print("Executing - backward_scroll METHOD")
            #self.report_event(event)

            
      def backward_fast(self):
            # (self, event)
            pass
            ## #print("Executing - backward_fast METHOD")
            #self.report_event(event)

      #
      # KEEP THESE HERE FOR IMPLEMENTING HOVER SCROLL
      #
      #def report_event(self,event):   
      #      # print ("Event Time: " + str(event.time) + "  EventType: " + str(event.type) + \
      #             "  EventWidgetId: " + str(event.widget) + "  EventKeySymbol: " + str(event.keysym) )

                  

      def exit_Handler(self):
            
            if askyesno('Verify', 'Do you really want to EXIT ?'):
                 self.master.destroy()
                 self.master.quit()
                 sys.exit()
            else:
                showinfo('No', 'EXIT Cancelled.')



      def lower_main_WINDOW(self):
          self.master.lower()   # It works - It lowers the window.

                

      #######################################################################
      #   
      #   INSERT CONTACT DATA with INCREMENTING DATA TAGS 
      #   to each of the CONTACT TEXTBOX ENTRY WIDGETS 
      #
      def insert_Data_Entry(self):
            global first_insert_data_entry
            global dict_filename_global
            global master_cm_list_name_global
            global OBJECT_toplevel_cm_app_doc_media
            if mode_select_global == "Browse Mode":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease Select ENTRY MODE\nto Enter Data to Contact List.\nSee ENTRY MODE\nand BROWSE MODE\nMenu Widget\nat Top of Screen.")
                  return
            
            elif str(dict_filename_global) == "No Contact Dictionary":
                   messagebox.showinfo("Contact Manager Guide ...", \
                   "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                   return

            ##############################################################
            #
            #  Temporary Code to see OBJECT LISTS:  
            #
            # print("  ")
            
            # for each_object in instance_object_LIST:
            #       print(".... each_object = " + str(each_object) )
                  
            # print("  ")
            
            # for each_object_winfo_id in instance_object_winfo_id_LIST:
            #       print(".... each_object_winfo_id = " + str(each_object_winfo_id) )
                  
            # print("  ")

            # for each_object_winfo_parent in instance_object_winfo_parent_LIST:
            #       print(".... each_object_winfo_parent = " + str(each_object_winfo_parent) )
                  
            # print("  ")

            # print("OBJECT_toplevel_excel_import_export = " + str(OBJECT_toplevel_excel_import_export) )
            # print("OBJECT_toplevel_app_status_panel = " + str(OBJECT_toplevel_app_status_panel) )
            # print("OBJECT_toplevel_cm_app_doc_media = " + str(OBJECT_toplevel_cm_app_doc_media) )
            # print("OBJECT_toplevel_user_gui_1_config_class = " + str(OBJECT_toplevel_user_gui_1_config_class) )
            # print("OBJECT_toplevel_user_gui_2_config_class = " + str(OBJECT_toplevel_user_gui_2_config_class) )
            # print("OBJECT_toplevel_user_gui_3_config_class = " + str(OBJECT_toplevel_user_gui_3_config_class) )
            # print("OBJECT_toplevel_list_builder = " + str(OBJECT_toplevel_list_builder) )
            # print("OBJECT_toplevel_view_contact_list = " + str(OBJECT_toplevel_view_contact_list) )
            # print("OBJECT_toplevel_new_contact_list = " + str(OBJECT_toplevel_new_contact_list) )
            # print("OBJECT_toplevel_select_contact_list = " + str(OBJECT_toplevel_select_contact_list) )
            # print("OBJECT_toplevel_system_admin_info = " + str(OBJECT_toplevel_system_admin_info) )
            # print("OBJECT_toplevel_email_gmail_class = " + str(OBJECT_toplevel_email_gmail_class) )
            # print("OBJECT_toplevel_config_setting_class = " + str(OBJECT_toplevel_config_setting_class) )

            # print("OBJECT_IN_APP_excel_import_export = " + str(OBJECT_IN_APP_excel_import_export) )
            # print("OBJECT_IN_APP_app_status_panel = " + str(OBJECT_IN_APP_app_status_panel) )
            # print("OBJECT_IN_APP_cm_app_doc_media = " + str(OBJECT_IN_APP_cm_app_doc_media) )
            # print("OBJECT_IN_APP_user_gui_1_config_class = " + str(OBJECT_IN_APP_user_gui_1_config_class) )
            # print("OBJECT_IN_APP_user_gui_2_config_class = " + str(OBJECT_IN_APP_user_gui_2_config_class) )
            # print("OBJECT_IN_APP_user_gui_3_config_class = " + str(OBJECT_IN_APP_user_gui_3_config_class) )
            # print("OBJECT_IN_APP_list_builder = " + str(OBJECT_IN_APP_list_builder) )
            # print("OBJECT_IN_APP_view_contact_list = " + str(OBJECT_IN_APP_view_contact_list) )
            # print("OBJECT_IN_APP_new_contact_list = " + str(OBJECT_IN_APP_new_contact_list) )
            # print("OBJECT_IN_APP_select_contact_list = " + str(OBJECT_IN_APP_select_contact_list) )
            # print("OBJECT_IN_APP_system_admin_info = " + str(OBJECT_IN_APP_system_admin_info) )
            # print("OBJECT_IN_APP_email_gmail_class = " + str(OBJECT_IN_APP_email_gmail_class) )
            # print("OBJECT_IN_APP_config_setting_class = " + str(OBJECT_IN_APP_config_setting_class) )

            #  >>> import Tkinter as tk
            #  >>> root = tk.Tk()
            #  >>> label = tk.Label(root, text="Hello, world")
            #  >>> label.winfo_exists()
            #  1
            #  >>> root.winfo_children()
            #  [<Tkinter.Label instance at 0x0000000002ADC1C8>]
            #  >>> label.destroy()
            #  >>> label.winfo_exists()
            #  0
            #  >>> root.winfo_children()
            #  []

            # NOTE: Use WINDOW_INSTANCE.winfo_exists() to determine which toplevel windows
            # exist, which means they were created and not destroyed.   

            #
            ##############################################################
            #
            # Create Lists to Test Database Random Generator Functions 
            #
            ##############################################################
            #
            fn_list = ["Mike", "Dave", "Elliot", "Bill", "Pete", "Tim", "John", "Karl", "Frank", "Jim", "Adam", "Janet",\
                       "Brad", "Mary", "Sally", "Kim", "Janet", "Christian", "Susan", "Laura", "Tricia", "Kelly"]
            ln_list = ["AAAA", "BBBB", "CCCC", "DDDD", "EEEE", "FFFF", "GGGG", "HHHH", "IIII", "JJJJ", "KKKK", "LLLL",\
                       "MMMM", "NNNN", "OOOO", "PPPP", "QQQQ", "RRRR", "SSSS", "TTTT", "UUUU", "VVVV", "WWWW", "XXXX", "YYYY", "ZZZZ"]
            sa_list = ["24 Driftwood Ave", "85 Elmer Street", "18 Redman Drive", "56 Holmes Road", "32 Wiley Ave", "94 Intrepid Drive"]
            ct_list = ["Someport", "Middlewaretown", "Portsentry", "Newcinna", "OverKinsell", \
                       "Livingnice", "Harvidian", "Boxbathio", "Rochelleview", "Elcina", "Rocklowland"]
            st_list = ["RI", "MA", "CT", "VA", "FL", "NH", "VT", "ME", "NY", "PA", \
                       "SC", "NC", "TN", "CA", "TX", "NM", "CO", "WY", "MI", "IL", "OH"]
            zc_list = ["02840", "04865", "24523", "54978", "03496", "02910", "04655", "42077", "90210", "90588", "72143", "40211"]
            pn_list = ["000-000-0000"]
            em_list = ["thismail@gmail.com", "thatmail@gmail.com", "yourmail@gmail.com", "theirmail@gmail.com", "othermail@gmail.com"]
            ws_list = ["http://www.google.com", "http://www.linkedin.com", "http://www.monster.com", "http://www.indeed.com"]
             
            ran_fn = random.choice(fn_list)
            ran_ln = random.choice(ln_list)
            ran_sa = random.choice(sa_list)
            ran_ct = random.choice(ct_list)
            ran_st = random.choice(st_list)
            ran_zc = random.choice(zc_list)
            ran_pn = random.choice(pn_list)
            ran_em = random.choice(em_list)
            ran_ws = random.choice(ws_list)
             
            first_insert_data_entry += 1
            data_tag = str(first_insert_data_entry)
            self.entry_first.set(str(ran_fn) + str(data_tag) )
            self.entry_last.set(str(ran_ln) + str(data_tag) )
            self.entry_streetadd.set(str(ran_sa) + str(data_tag) )
            self.entry_citytown.set(str(ran_ct) + str(data_tag) )
            self.entry_state.set(str(ran_st) + str(data_tag) )
            self.entry_zipcode.set(str(ran_zc) + str(data_tag) )
            self.entry_phonenum.set(str(ran_pn) + str(data_tag) )
            self.entry_email.set(str(ran_em) + str(data_tag) )
            self.entry_website.set(str(ran_ws) + str(data_tag) )
            return 
            


      ###################################################################
      #
      # ENTER FIRST RECORD of Contact Data to Initialize Databases
      # and provide an example for Users. This First Data Record
      # is required so that other Classes and Methods that use the
      # database will avoid the KeyError Exception when encountering
      # an EMPTY Contact List Dictionary. 
      # 
      ###################################################################
      #
      def first_Contact_Data_Entry(self):
            global cm_listbox_file_global
            global dict_filename_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global

            # write data record to object/class/method 

            # write data records to cm_list_file
            # Note that we use the FULLPATH - fullpath_fn_cm_listbox_file_global

            with open(fullpath_fn_cm_listbox_file_global, 'a') as wf:
                  for x in range(0, 10):
                        if x == 0: wf.flush()
                        #------------------------------------------------------------------------
                        if x == 1: wf.write("First Name" + ",")
                        elif x == 2: wf.write("Last Name" + ",")
                        elif x == 3: wf.write("Street Address" + ",")
                        elif x == 4: wf.write("City or Town" + ",")
                        elif x == 5: wf.write("State" + ",")
                        elif x == 6: wf.write("Zip Code" + ",")
                        elif x == 7: wf.write("Phone Number" + ",")
                        elif x == 8: wf.write("Email Address" + ",")
                        elif x == 9: wf.write("Website" + "\n")
                        else: pass
            
            this_person = Person("First Name", "Last Name", "Street Address", \
                        "City or Town", "State", "Zip Code", "Phone Number", \
                        "Email Address", "Website")

            gfn = this_person.get_Firstname()
            gln = this_person.get_Lastname()
            gsa = this_person.get_Streetadd()
            gct = this_person.get_Citytown()
            gst = this_person.get_State()
            gzc = this_person.get_Zipcode()
            gpn = this_person.get_Phonenum()
            gem = this_person.get_Email()
            gws = this_person.get_Website()

            # Create DICTIONARY to store contact data
            contact_dict = {"First_Name_KEY": str(gfn), "Last_Name_KEY": str(gln), "Street_Address_KEY": str(gsa), \
                            "City_Town_KEY": str(gct), "State_KEY": str(gst), "Zip_Code_KEY": str(gzc), \
                            "Phone_Number_KEY": str(gpn), "EMail_KEY": str(gem), "Website_KEY": str(gws) }

            # Store_Contact_Dict in Store_Contact_Dict Class 
            contact_dict_instance = Store_Contact_Dict(this_contact_dict = contact_dict)
            contact_dict_instance.set_contact_dict(new_this_contact_dict = contact_dict)
            get_contact_dict_call = contact_dict_instance.get_contact_dict()


            # Write contact data dictionary to dict_filename file from class method get_contact_dict_call
            # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
            with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                  for x in range(0, 10):
                        if x == 0:
                              wdictf.flush()
                              wdictf.write("DATA_RECORD_DELIMITER:")
                        elif x == 1: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["First_Name_KEY"] ) )
                        elif x == 2: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Last_Name_KEY"] ) )
                        elif x == 3: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Street_Address_KEY"] ) )
                        elif x == 4: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["City_Town_KEY"] ) )
                        elif x == 5: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["State_KEY"] ) )
                        elif x == 6: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Zip_Code_KEY"] ) )
                        elif x == 7: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Phone_Number_KEY"] ) )
                        elif x == 8: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["EMail_KEY"] ) )
                        elif x == 9: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Website_KEY"] ) )
                        else: pass

            self.session_index += 1

            # Now delete the ENTRY Text Fields to prepare for next ENTRY

            self.entry_first.set('')
            self.entry_last.set('')
            self.entry_streetadd.set('')
            self.entry_citytown.set('') 
            self.entry_state.set('')
            self.entry_zipcode.set('') 
            self.entry_phonenum.set('')
            self.entry_email.set('')
            self.entry_website.set('')

                  
            
      #################################################
      #
      # ENTER Contact Data .....  
      # 
      #################################################
      #
      def finished_Data_Entry(self):
            global cm_listbox_file_global
            global dict_filename_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global

            # print(".... IN METHOD finished_Data_Entry.... mode_select_global = " + str(mode_select_global) )

            # write data record to object/class/method 

            # write data records to cm_list_file
            # Note that we use the FULLPATH - fullpath_fn_cm_listbox_file_global

            with open(fullpath_fn_cm_listbox_file_global, 'a') as wf:
                  for x in range(0, 10):
                        if x == 0: wf.flush()
                        #------------------------------------------------------------------------
                        if x == 1: wf.write(self.entry_first.get() + ",")
                        elif x == 2: wf.write(self.entry_last.get() + ",")
                        elif x == 3: wf.write(self.entry_streetadd.get() + ",")
                        elif x == 4: wf.write(self.entry_citytown.get() + ",")
                        elif x == 5: wf.write(self.entry_state.get() + ",")
                        elif x == 6: wf.write(self.entry_zipcode.get() + ",")
                        elif x == 7: wf.write(self.entry_phonenum.get() + ",")
                        elif x == 8: wf.write(self.entry_email.get() + ",")
                        elif x == 9: wf.write(self.entry_website.get() + "\n")
                        else: pass
            
            
            this_person = Person(self.entry_first.get(), self.entry_last.get(), self.entry_streetadd.get(), \
                        self.entry_citytown.get(), self.entry_state.get(), self.entry_zipcode.get(), self.entry_phonenum.get(), \
                        self.entry_email.get(), self.entry_website.get())

         
            gfn = this_person.get_Firstname()
            gln = this_person.get_Lastname()
            gsa = this_person.get_Streetadd()
            gct = this_person.get_Citytown()
            gst = this_person.get_State()
            gzc = this_person.get_Zipcode()
            gpn = this_person.get_Phonenum()
            gem = this_person.get_Email()
            gws = this_person.get_Website()

            # Create DICTIONARY to store contact data
            contact_dict = {"First_Name_KEY": str(gfn), "Last_Name_KEY": str(gln), "Street_Address_KEY": str(gsa), \
                            "City_Town_KEY": str(gct), "State_KEY": str(gst), "Zip_Code_KEY": str(gzc), \
                            "Phone_Number_KEY": str(gpn), "EMail_KEY": str(gem), "Website_KEY": str(gws) }

            # Store_Contact_Dict in Store_Contact_Dict Class 
            contact_dict_instance = Store_Contact_Dict(this_contact_dict = contact_dict)
            contact_dict_instance.set_contact_dict(new_this_contact_dict = contact_dict)
            get_contact_dict_call = contact_dict_instance.get_contact_dict()     


            # Write contact data dictionary to dict_filename file from class method get_contact_dict_call
            # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
            with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                  for x in range(0, 10):
                        if x == 0:
                              wdictf.flush()
                              wdictf.write("DATA_RECORD_DELIMITER:")
                        elif x == 1: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["First_Name_KEY"] ) )
                        elif x == 2: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Last_Name_KEY"] ) )
                        elif x == 3: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Street_Address_KEY"] ) )
                        elif x == 4: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["City_Town_KEY"] ) )
                        elif x == 5: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["State_KEY"] ) )
                        elif x == 6: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Zip_Code_KEY"] ) )
                        elif x == 7: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Phone_Number_KEY"] ) )
                        elif x == 8: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["EMail_KEY"] ) )
                        elif x == 9: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Website_KEY"] ) )
                        else: pass
                                       

            self.session_index += 1

 
            # Now delete the ENTRY Text Fields to prepare for next ENTRY

            self.entry_first.set('')
            self.entry_last.set('')
            self.entry_streetadd.set('')
            self.entry_citytown.set('') 
            self.entry_state.set('')
            self.entry_zipcode.set('') 
            self.entry_phonenum.set('')
            self.entry_email.set('')
            self.entry_website.set('')





##############################################################################
#
# Get_EMail_List_from_Contact_List_Name
#
# return self.email_LIST_from_contact_list
#
# Usage: email_list = Get_EMail_List_from_Contact_List_Name.get_email_list()
#
##############################################################################
#
class Get_EMail_List_from_Contact_List_Name(object):
    def __init__(self, master):
        self.email_LIST_from_contact_list = []


    def get_email_list(self):
        # Extract the LIST of email addresses from the ACTIVE CONTACT LIST (Global)
        # DICTIONARY Contact List File - dict_file_cm_listbox_file_global
        # which is stored in APPDATA at fullpath_fn_dict_filename_global

        self.textFile = open(fullpath_fn_dict_filename_global, 'r')

        # This takes the file object opened with the open() and turns it into a string which 
        # you can now use textString in a text widget.
        self.textString = self.textFile.read()

        # Close the Dictionary File 
        self.textFile.close()

        # Count the DATA RECORDS in the string by counting the
        # number of "DATA_RECORD_DELIMITER:" patterns 
        self.num_data_records = self.textString.count("DATA_RECORD_DELIMITER:")
        
        self.num_data_records_plus_one = self.num_data_records + 1
        # Operate on the textString to search for DATA_RECORD_DELIMITER: and KEY_SYNC: sub-strings  
        for record_index in range (1, self.num_data_records_plus_one):
             self.data_record_string = self.textString.split("DATA_RECORD_DELIMITER:")[record_index]
             for key_index in range (1, 10):
                   key_indexed_string = self.data_record_string.split("KEY_SYNC:")[key_index]
                   if key_index == 1:  # FIRST NAME
                        pass
                   if key_index == 2:  # LAST NAME
                        pass
                   if key_index == 3:  # STREET ADDRESS
                        pass
                   if key_index == 4:  # CITY / TOWN
                        pass
                   if key_index == 5:  # STATE
                        pass
                   if key_index == 6:  # ZIP CODE
                        pass
                   if key_index == 7:  # PHONE NUMBER
                        pass
                   if key_index == 8:  # EMAIL ADDRESS
                        self.email_LIST_from_contact_list.append(key_indexed_string)
                   if key_index == 9:  # WEBSITE
                        pass

        # return the email_LIST_from_contact_list 
        return self.email_LIST_from_contact_list

  

##############################################################################
#
# class: Select_Email_Address_List
#
# ACQUIRE THE CURRENTLY SELECTED CONTACT LIST (GLOBAL) and then
#
# SELECT EMAIL ADDRESS(ES) FROM A LISTBOX. 
#
# RETURN A LIST OF SELECTED EMAIL ADDRESS(ES). 
#
##############################################################################
#
class Select_Email_Address_List(Frame):  #(object):
    def __init__(self, master):
        global selected_email_address_LIST_GLOBAL
        global DEST_or_CC_email_address_FLAG_GLOBAL
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global fullpath_cnotes_dict_file_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global kick_thread_to_update_main_entry_widgets
        global OBJECT_toplevel_select_contact_list
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        
        # self.master = master
        # self.frame = tk.Frame(self.master)  

        # self.master = master
        # self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")
        
        self.master.configure(background=str(selectlist_bg_color_val_global) )

        self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - Select EMAIL ADDRRESS or ADDRESSES from LISTBOX.")
        
        self.select_file_button = Button(self.master, text = "CLICK HERE after SELECTING \nEmail Address or Multiple Addresses\n(Use CNTL to SELECT Multiple Addresses)", \
            width=35,height=3, font=('Helvetica', '12'), background="light sea green", command = self.get_Listbox_File)
            
        self.select_file_button.grid(row=1, column=0, sticky = W)
        # self.select_file_button.bind("<Button-1>", self.get_Listbox_File) 


        self.tk_lower_status_panel_Button = Button(self.master, text = "MAIN SCREEN", \
        width = 15, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.lower_the_window)
        self.tk_lower_status_panel_Button.grid(row=4, column=0, padx=5, pady=5, sticky = SE)  
        self.tk_lower_status_panel_Button.config(borderwidth=5)


        self.quit_status_panel_Button = Button(self.master, text = "EXIT", \
        width = 7, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.close_windows)
        self.quit_status_panel_Button.grid(row=4, column=0, padx=5, pady=5, sticky = SW)
        self.quit_status_panel_Button.config(borderwidth=5)

        # TEXTBOX to display CONTACT LIST (master_cm_list_name_global) TITLE at top of window   

        self.title_1_text_box = Text(self.master, width=42, height = 1)
        self.title_1_text_box.grid(row=0, column=1, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="light sea green")

        text_1_TITLE = "Contact List: " + str(master_cm_list_name_global) 

        self.title_1_text_box.insert(END, text_1_TITLE)

        self.lbox = Listbox(self.master, width=52, height = 22, selectmode=EXTENDED)
        self.lbox.grid(row=2, column=1, sticky = W)
        self.lbox.config(borderwidth=10, font=('Helvetica', '12'), background="light sea green") 
        self.lbox.bind("<<ListboxSelect>>", self.OnListBoxSelect)

        # create a Scrollbar and associate it with self.lbox 
        self.scrollb = Scrollbar(self.master, command=self.lbox.yview)
        self.scrollb.grid(row=2, column=2, sticky='NSEW')
        self.lbox['yscrollcommand'] = self.scrollb.set

        # Load all email addresses from ACTIVE CONTACT LIST into the LISTBOX.  
        results = []

        # Instantiate Get_EMail_List_from_Contact_List_Name Class
        get_email_list_instance = Get_EMail_List_from_Contact_List_Name(self.master)

        # Create Email List Object
        results = get_email_list_instance.get_email_list()

        # Load LISTBOX with email addresses of Contact List
        for email_address_item in results:
               self.lbox.insert(0, email_address_item)

        # Initialize Class Object for selected_email_address_LIST
        self.selected_email_address_LIST = []
    

    def get_Listbox_File(self):
        global selected_email_address_LIST_GLOBAL
        global DEST_or_CC_email_address_FLAG_GLOBAL
        global email_list_from_listbox_ready_global

        verify_listbox_selection = self.lbox.curselection()

        try:
               test_cm_filename_value = str(self.lbox.get(verify_listbox_selection[0] ) )
        except IndexError as err:
               messagebox.showinfo("Contact Manager Guide ...", \
               "ATTENTION: \n\nPlease SELECT an EMAIL ADDRESS from the LISTBOX ..... \n\n OPERATOR ERROR (Index Error): \n" + str(err) )
               self.master.lift()
               return
         
        selection = self.lbox.curselection()

        #print("  ")
        #print(".... selection = " + str(selection) )
        #print("  ")

        for item in selection:
            self.selected_email_address_LIST.append(str(self.lbox.get(item) ) )

        #########################################################################################
        #
        # SET the GLOBAL:  selected_email_address_LIST_GLOBAL  
        #
        selected_email_address_LIST_GLOBAL = self.selected_email_address_LIST
        #
        # SET a GLOBAL to ALERT the EMAIL_LIST_THREAD in the EMAIL CLASS that the LIST id ready.
        email_list_from_listbox_ready_global = True
        #
        # print(" ")
        # print(".... Setting  selected_email_address_LIST_GLOBAL:  " + str(selected_email_address_LIST_GLOBAL ) )
        # print(" ")
        # print(".... DEST_or_CC_email_address_FLAG_GLOBAL = " + str(DEST_or_CC_email_address_FLAG_GLOBAL) )
        # print(" ")
        # print(".... N O W   S E T   DEST or CC   E N T R Y   W I D G E T   FROM HERE")
        # print(" ")

        #
        #########################################################################################

        # Set listbox_file_capture_global to trigger EMAIL ADDRESS List Entry Textbox Update 
        # as we have completed registering all the Listbox Filename variable settings  
        # We will reset this listbox_file_capture_global back to False after we 
        # update the EMAIL ADDRESS List Entry Textbox with the Listbox Filename selected 
        listbox_file_capture_global = True


        # close listbox frame window after storing selected EMAIL ADDRESS DATA 
        self.master.destroy()
        return 
          


    def OnListBoxSelect(self, event):
        global listbox_file_capture_global
        listbox_file_capture_global = "False"
        widget = event.widget
        selection = widget.curselection()
        email_addr_value = widget.get(selection[0])
        selection_value_tuple = [selection, email_addr_value]
        return email_addr_value



    def lower_the_window(self):
          # These CYCLE Buttons have been changed to 
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()



    def close_windows(self):
        self.master.destroy()


  

######################################################
#
#   The Email_Gmail_Class .....
#
######################################################
class Email_Gmail_Class(Frame):  #(object):
      def __init__(self, master, **kw):
            global DEST_or_CC_email_address_FLAG_GLOBAL
            global selected_email_address_LIST_GLOBAL
            global email_list_from_listbox_ready_global
            global gmail_oauth2_json_file_test_global
            global gmail_oauth2_status_global
            global gmail_oauth2_exceptions_status_global
            global gmail_oauth2_SPECIFIC_EXCEPTION_global
            global gmail_smtp_allow_less_secure_apps_global
            global gmail_smtp_status_global
            global gmail_smtp_exceptions_status_global
            global gmail_smtp_SPECIFIC_EXCEPTION_global
            global gmail_mode_global
            global user_profile_global
            global credential_home_dir_global
            global credential_appdata_dir_global
            global credential_home_path_global
            global credential_appdata_path_global
            global client_secret_path_global
            global textbox_edit_mode_select_global
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global kick_thread_to_update_main_entry_widgets
            global kick_thread_to_update_email_contact_entry_widgets
            global fullpath_prepend_cnotes_dict_file_global
            global prepend_cnotes_dict_file_global
            global fullpath_cnotes_dict_file_global
            global OBJECT_toplevel_email_gmail_class
            global instance_object_LIST
            Frame.__init__(self, master)
            self.grid()
        
            # self.master = master
            # self.frame = tk.Frame(self.master)
            
            # self.master = master
            # self.frame = tk.Frame(self.master)

            self.master.grid_rowconfigure(0, weight=1)
            self.master.grid_columnconfigure(0, weight=1)

            self.email_title = "INITIALIZE EMAIL TITLE"
            self.email_content = "INITIALIZE EMAIL CONTENT"
            self.source_email_address = "INITIALIZE SOURCE EMAIL ADDRESS"
            self.source_email_password = "INITIALIZE SOURCE EMAIL PASSWORD"
            self.destination_1_email_address = "INITIALIZE DESTINATION EMAIL ADDRESS"

            #######################################################################################
            #
            # Create variables associated with the Email Attachment:
            #
            # We will get a LIST of OBJECTS for the Email Attachment from the Dialog Method:
            #
            #      self.dialog_to_get_file_attachment()    which has a 
            #
            # return_object_list = [data, file_full_path]
            #
            # and then we Extract objects from the self.dialog_to_get_file_attachment() method
            #
            # return list as follows: 
            #
            # self.file_email_attachment_FULL_PATH = self.dialog_to_get_file_attachment()
            #
            # and then we can build everythng from the FULL PATH FILENAME as follows:
            #
            # the_file_full_path = self.file_email_attachment_FULL_PATH[self.attachment_file_index]
            #
            # filename = os.path.basename(the_file_full_path)
            #
            # file_type = filename.split(".")[1]
            #
            # content_type, encoding = mimetypes.guess_type(the_file_full_path)
            #
            # if content_type is None or encoding is not None:
            #     content_type = 'application/octet-stream'
            #
            # main_type, sub_type = content_type.split('/', 1)
            # 
            # print(".... the_file_full_path = " + str(the_file_full_path) )
            # print(".... filename = " + str(filename) )
            # print(".... content_type = " + str(content_type) )
            # print(".... main_type = " + str(main_type) )
            # print(".... sub_type = " + str(sub_type) )
            # print(".... file_type = " + str(file_type) )
            # print(".... encoding = " + str(encoding) )
            #
            ########################################################################################
            #
            # Note: This Email Attachment self.dialog_to_get_file_attachment() Method is
            #
            # initiated or triggered by pressing the EMAIL ATTACHMENTS tk Button, which will
            #
            # run the self.dialog_to_get_file_attachment() METHOD and generate the
            #
            # EMAIL ATTACHMENT FILE OBJECT LIST with the help of Dialog Windows user selections.
            #
            # CREATE the OBJECTS for the EMAIL Attachment:

            self.EMAIL_MESSAGE = "EMAIL_MESSAGE_VALUE_NOT_YET_SET"

            self.message_cummulative = "message_cummulative_NOT_YET_SET"

            self.EMAIL_base64_urlsafe_b64encode_message = "EMAIL_base64_urlsafe_b64encode_message_VALUE_NOT_SET"

            self.file_email_attachment_BYTES_TYPE_OBJECT = b"INITIALIZE_THIS_AS_A_BYTES_TYPE_OBJECT"

            self.file_email_attachment_FULL_PATH = []

            self.attachment_file_index = 0
            
            self.file_email_attachment_FILE_NAME = []

            self.file_email_attachment_FILE_TYPE = []

            self.file_email_attachment_CONTENT_TYPE = []           

            self.file_email_attachment_MAIN_TYPE = []

            self.file_email_attachment_SUB_TYPE = []

            self.file_email_attachment_ENCODING = []

            self.EMAIL_ATTACHMENT_OPTION_FLAG = False
            
            #
            # 
            #######################################################################################
            
            huge_font = ('Verdana',32)
            large_font = ('Verdana',20)
            minilarge_font = ('Verdana',16)
            VERANDA_16_font = ('Verdana',16)
            VERANDA_14_font = ('Verdana',14)
            VERANDA_12_font = ('Verdana',12)
            VERANDA_10_font = ('Verdana',10)
            medium_font = ('Verdana',12,'bold')
            small_font = ('Verdana',10)
            menubar_font = ('Helvetica', '12')

            # Max Screen Size with the Title Bar - BEST Choice 
            self.master.wm_state('zoomed')

            # Another way to set screen size (other than BEST Choice above
            # self.master.geometry("900x550")

            OBJECT_toplevel_email_gmail_class = self.master
            instance_object_LIST.append(self.master)

            self.master.configure(background="dark slate gray")

            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - Email and Contact Notes")

            ################################################################################################
            #  
            # Add Drop Down Menu for Textbox Edit Modes (to create framework for Textbox Edit events) 
            #    
            ################################################################################################

            List_of_Textbox_Edit_Modes = ["EDIT MENU", "CUT Selected Text - (CNTL-X)", \
                                          "COPY Selected Text - (CNTL-C)", "PASTE to Cursor - (CNTL-V)", \
                                          "CLEAR Email or NOTES Content", "CLEAR Email STATUS Only", \
                                          "DELETE NOTES for SELECTED CONTACT LIST"]

            textbox_edit_mode_select_global = "EDIT MENU"

            self.tb_mode_select_opt_menu_select = StringVar()
            self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )   # initialize OptionMenu 
            self.tb_mode_select_optionsmenu_inst = OptionMenu(self.master, self.tb_mode_select_opt_menu_select, \
            *List_of_Textbox_Edit_Modes, command=self.func_set_textbox_edit_mode_select_global)
            self.tb_mode_select_optionsmenu_inst.grid(sticky = NW, row=0, column=1)
            self.tb_mode_select_optionsmenu_inst.config(borderwidth=10, \
                  background="light sea green", font=('Helvetica', 14) , height = 2)

            tb_menu_mode_select = self.tb_mode_select_optionsmenu_inst.nametowidget(self.tb_mode_select_optionsmenu_inst.menuname) 
            tb_menu_mode_select.configure(font=("Helvetica", 18), bg="light sea green")

            ################################################################################################ 

            self.select_file_button = Button(self.master, text = "SEND EMAIL", \
                  width=16, height=2, font=('Helvetica', '24'), background="light sea green", borderwidth=10)

            self.select_file_button.grid(row=0, column=0, sticky = NW)
            self.select_file_button.bind("<Button-1>", self.get_decision_Textbox_File)


            ################################################################################################
            #
            # Add tk Button with command for method:  email_attachment_option_method() 
            #
            # to select an Email Attachment.  
            #
            ################################################################################################

            
            ################################################################################################
            #
            # Implement Options Menu Drop Down to Select OAUTH2_Gmail_Mode or SMTP_Gmail_Mode
            #  
            # Use OptionsMenu to set gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode"
            #
            ################################################################################################
            #
            # OPTION MENU WIDGET selects from OptionMenu and
            # sets gmail_mode_global which control email methods:
            # gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode"
            #
            # Note that default is gmail_mode_global = "SMTP_Gmail_Mode" because
            # it is easier for the user at this stage of development.  
            #
            ################################################################################################


            List_of_Email_Modes = ["OAUTH2_Gmail_Mode", "SMTP_Gmail_Mode"]

            gmail_mode_global = "SMTP_Gmail_Mode"

            self.email_mode_select_opt_menu_select = StringVar()
            self.email_mode_select_opt_menu_select.set(str(gmail_mode_global) )   # initialize OptionMenu 
            self.email_mode_select_optionsmenu_inst = OptionMenu(self.master, self.email_mode_select_opt_menu_select, \
                *List_of_Email_Modes, command=self.func_set_email_mode_select_global)
            self.email_mode_select_optionsmenu_inst.grid(row=0, column=1, sticky = NE)
            self.email_mode_select_optionsmenu_inst.config(borderwidth=5, background="light sea green", font=('Helvetica', 14 ), height = 2)

            email_menu_mode_select = self.email_mode_select_optionsmenu_inst.nametowidget(self.email_mode_select_optionsmenu_inst.menuname) 
            email_menu_mode_select.configure(font=("Helvetica", 18), bg="light sea green")

            # Email Attachments Button

            self.select_attachment_button = Button(self.master, text = "ATTACH TO EMAIL", \
                  width=16, height=2, font=('Helvetica', '14'), background="light sea green", borderwidth=10)

            self.select_attachment_button.grid(row=0, column=1, sticky = N)
            self.select_attachment_button.bind("<Button-1>", self.email_attachment_option_method)
            

            self.load_next_contact_Button = Button(self.master, text = "NEXT CONTACT", width = 12, height = 1, \
                  font=('Helvetica', 10, "bold"), background="light sea green", borderwidth=5, command = self.load_next_contact)

            self.load_next_contact_Button.grid(row=3, column=1, sticky = E)

            self.load_previous_contact_Button = Button(self.master, text = "PREV CONTACT", width = 12, height = 1, \
                  font=('Helvetica', 10, "bold"), background="light sea green", borderwidth=5, command = self.load_previous_contact)

            self.load_previous_contact_Button.grid(row=4, column=1, sticky = E)

            ################################################################################### 

            # INSERT LABEL FOR SOURCE EMAIL ADDRESS 
            self.label_source_email_address = "Your Gmail Address:"
            self.mylabel_seadr = Label(self.master, text = self.label_source_email_address, font=minilarge_font)
            self.mylabel_seadr.config(height = 1, width=25, anchor = E)
            self.mylabel_seadr.config(bg='ivory4', fg='gray25')  
            self.mylabel_seadr.grid(row=1, column=0, sticky = NE)

            # INSERT LABEL FOR SOURCE EMAIL PASSWORD 
            self.label_source_email_password = "Your Gmail Password:"
            self.mylabel_sepwd = Label(self.master, text = self.label_source_email_password, font=minilarge_font)
            self.mylabel_sepwd.config(height = 1, width=25, anchor = E)
            self.mylabel_sepwd.config(bg='ivory4', fg='gray25')  
            self.mylabel_sepwd.grid(row=2, column=0, sticky = NW)

            # INSERT LABEL FOR DESTINATION 1 EMAIL ADDRESS  
            self.label_destination_1_email_address = "To:"
            self.mylabel_dest_1_adr = Label(self.master, text = self.label_destination_1_email_address, font=minilarge_font)
            self.mylabel_dest_1_adr.config(height = 1, width=4, anchor = E)
            self.mylabel_dest_1_adr.config(bg='ivory4', fg='gray25')  
            self.mylabel_dest_1_adr.grid(row=3, column=0, sticky = NE)

            # INSERT SELECT DEST BUTTON FOR DESTINATION 1 EMAIL ADDRESS - like email_attachment_option_method 
            self.select_dest_list_Button = Button(self.master, text = "Select To Email Address", width = 20, height = 1, \
                  font=('Helvetica', 12, "bold"), background="cyan4", borderwidth=5, command = self.select_dest_address)
            
            self.select_dest_list_Button.grid(row=3, column=0, sticky = NW)

            # INSERT LABEL FOR DESTINATION CC EMAIL ADDRESS 
            self.label_destination_cc_email_address = "Cc:"
            self.mylabel_dest_cc_adr = Label(self.master, text = self.label_destination_cc_email_address, font=minilarge_font)
            self.mylabel_dest_cc_adr.config(height = 1, width=4, anchor = E)
            self.mylabel_dest_cc_adr.config(bg='ivory4', fg='gray25')  
            self.mylabel_dest_cc_adr.grid(row=4, column=0, sticky = NE)

            # INSERT SELECT CC BUTTON FOR DESTINATION CC EMAIL ADDRESS 
            self.select_cc_list_Button = Button(self.master, text = "Select cc Email Address", width = 20, height = 1, \
                  font=('Helvetica', 12, "bold"), background="cyan4", borderwidth=5, command = self.select_cc_address)

            self.select_cc_list_Button.grid(row=4, column=0, sticky = NW)

            # INSERT LABEL FOR EMAIL TITLE  
            self.label_email_title = "Subject:"
            self.mylabel_email_title = Label(self.master, text = self.label_email_title, font=minilarge_font)
            self.mylabel_email_title.config(height = 1, width=25, anchor = E)
            self.mylabel_email_title.config(bg='ivory4', fg='gray25')  
            self.mylabel_email_title.grid(row=5, column=0, sticky = NW)

            # INSERT LABEL FOR EMAIL CONTENT 
            self.label_email_content = "Contact Notes / Email:"
            self.mylabel_email_content = Label(self.master, text = self.label_email_content, font=minilarge_font)
            self.mylabel_email_content.config(height = 1, width=25, anchor = E)
            self.mylabel_email_content.config(bg='ivory4', fg='gray25')  
            self.mylabel_email_content.grid(row=6, column=0, sticky = NW)

            # INSERT BUTTONS TO SAVE AND RETRIEVE CONTACT NOTES

            self.notesButton = Button(self.master, text = "SAVE\nCONTACT\nNOTES", width = 9, height = 3, \
                  font=('Verdana',14), borderwidth=10, background="turquoise4", command = self.save_contact_notes)

            self.notesButton.grid(row=6, column=0, sticky = W)

            self.retrieve_notes_Button = Button(self.master, text = "RETRIEVE\nCONTACT\nNOTES", width = 9, height = 3, \
                  font=('Verdana',14), borderwidth=10, background="turquoise4", command = self.retrieve_contact_notes)

            self.retrieve_notes_Button.grid(row=6, column=0, sticky = E)
            
            self.email_startup_user_Button = Button(self.master, text = "EMAIL STARTUP\nUSERS MANUAL", width = 25, height = 3, \
                  font=('Verdana',14), borderwidth=10, background="turquoise4", command = self.cm_app_doc_media_window_method_email_screen)

            self.email_startup_user_Button.grid(row=6, column=0, sticky = SW)

            # INSERT LABEL FOR EMAIL STATUS MESSAGES ....
            self.label_email_status = "STATUS:"
            self.mylabel_email_status = Label(self.master, text = self.label_email_status, font=minilarge_font)
            self.mylabel_email_status.config(height = 1, width=7, anchor = NE) # SE
            self.mylabel_email_status.config(bg='ivory4', fg='gray25')  
            self.mylabel_email_status.grid(row=7, column=0, sticky = E)

            #
            # LOWER WINDOW BUTTON.   
            # 
            self.lower_window_Button = Button(self.master, text = "MAIN SCREEN", width = 12, height = 1, \
                font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5, \
                activebackground="cyan", activeforeground="blue2", command = self.lower_email_WINDOW)

            self.lower_window_Button.grid(row=7, column=0, sticky = E)

            #
            # EXIT BUTTON.  
            # 
            self.quitButton = Button(self.master, text = "EXIT", width = 7, height = 1, \
                font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5, \
                activebackground="cyan", activeforeground="blue2", command = self.exit_Handler)

            self.quitButton.grid(row=7, column=0, sticky = W)

            ############################################################################ 

            self.last_widget_name_clicked = "INITIALIZE LAST WIDGET NAME CLICKED"
            
            # INSERT ENTRY WIDGET FOR SOURCE EMAIL ADDRESS 
            self.entry_SOURCE_EMAIL_ADDRESS = StringVar()
            self.source_email_address_entry = Entry(self.master, \
            textvariable = self.entry_SOURCE_EMAIL_ADDRESS, font = VERANDA_12_font, width = 50)
            self.source_email_address_entry.grid(sticky = W, row=1, column=1)
            self.source_email_address_entry.config(borderwidth=5, background="light sea green")
            self.source_email_address_entry.bind("<Button-1>",lambda event: self.src_addr_widget_function(event, "self.source_email_address_entry") )

            # INSERT ENTRY WIDGET FOR CONTACT NAME LOADED BY DICTIONARY POINTER  
            self.entry_LOADED_CONTACT_NAME = StringVar()
            self.loaded_contact_name_entry = Entry(self.master, \
            textvariable = self.entry_LOADED_CONTACT_NAME, font = VERANDA_12_font, width = 50)
            self.loaded_contact_name_entry.grid(sticky = E, row=1, column=1)
            self.loaded_contact_name_entry.config(borderwidth=5, background="DarkGoldenrod1")
            self.loaded_contact_name_entry.bind("<Button-1>",lambda event: self.clistname_widget_function(event, "self.loaded_contact_name_entry") )

            # INSERT ENTRY WIDGET FOR SOURCE EMAIL PASSWORD     
            self.entry_SOURCE_EMAIL_PASSWORD = StringVar()
            self.source_email_password_entry = Entry(self.master, \
            textvariable = self.entry_SOURCE_EMAIL_PASSWORD, font = VERANDA_12_font, width = 50)
            self.source_email_password_entry.grid(sticky = W, row=2, column=1)
            self.source_email_password_entry.config(borderwidth=5, background="light sea green", show="*")
            self.source_email_password_entry.bind("<Button-1>",lambda event: self.pwd_widget_function(event, "self.source_email_password_entry") )

            # INSERT ENTRY WIDGET FOR CONTACT LIST  
            self.entry_CONTACT_LIST_NAME_Stringvar = StringVar()
            self.CONTACT_LIST_NAME_entry = Entry(self.master, \
            textvariable = self.entry_CONTACT_LIST_NAME_Stringvar, font = VERANDA_12_font, width = 50)
            self.CONTACT_LIST_NAME_entry.grid(sticky = E, row=2, column=1)
            self.CONTACT_LIST_NAME_entry.config(borderwidth=5, background="DarkGoldenrod1")
            self.CONTACT_LIST_NAME_entry.bind("<Button-1>",lambda event: self.contact_list_widget_function(event, "self.CONTACT_LIST_NAME_entry") )
            
            # INSERT ENTRY WIDGET FOR DESTINATION 1 EMAIL ADDRESS 
            self.entry_DEST_1_EMAIL_ADDRESS = StringVar()
            self.destination_1_email_address_entry = Entry(self.master, \
            textvariable = self.entry_DEST_1_EMAIL_ADDRESS, font = VERANDA_12_font, width = 89)
            self.destination_1_email_address_entry.grid(sticky = NW, row=3, column=1)
            self.destination_1_email_address_entry.config(borderwidth=5, background="light sea green")
            self.destination_1_email_address_entry.bind("<Button-1>",lambda event: self.to_widget_function(event, "self.destination_1_email_address_entry") )

            # INSERT ENTRY WIDGET FOR DESTINATION CC EMAIL ADDRESS  
            self.entry_DEST_CC_EMAIL_ADDRESS = StringVar()
            self.destination_cc_email_address_entry = Entry(self.master, \
            textvariable = self.entry_DEST_CC_EMAIL_ADDRESS, font = VERANDA_12_font, width = 89)
            self.destination_cc_email_address_entry.grid(sticky = NW, row=4, column=1)
            self.destination_cc_email_address_entry.config(borderwidth=5, background="light sea green")
            self.destination_cc_email_address_entry.bind("<Button-1>",lambda event: self.cc_widget_function(event, "self.destination_cc_email_address_entry") )

            # NOTE: We are setting these StringVars in another Class above after we
            # select the EMAIL ADDRESS(ES) from a LISTBOX. 
            #
            # self.entry_DEST_1_EMAIL_ADDRESS.set(str(total_address_list_string_global) ) 
            # self.entry_DEST_CC_EMAIL_ADDRESS.set(str(total_address_list_string_global) )  

            # INSERT ENTRY WIDGET FOR EMAIL TITLE 
            self.entry_EMAIL_TITLE = StringVar()
            self.email_title_entry = Entry(self.master, \
                                           textvariable = self.entry_EMAIL_TITLE, font = VERANDA_12_font, width = 100)
            self.email_title_entry.grid(sticky = W, row=5, column=1)
            self.email_title_entry.config(borderwidth=5, background="light sea green")
            self.email_title_entry.bind("<Button-1>",lambda event: self.title_widget_function(event, "self.email_title_entry") )

            # INSERT TEXTBOX WIDGET FOR EMAIL CONTENT  
            self.EMAIL_Textbox = Text(self.master, height=20, width=25, font = VERANDA_12_font)
            self.EMAIL_Textbox.grid(row=6, column=1, sticky="nsew")
            self.EMAIL_Textbox.config(borderwidth=5, background="dark slate gray", fg="cyan3", wrap=WORD )
            self.EMAIL_Textbox.bind("<Button-1>",lambda event: self.content_widget_function(event, "self.EMAIL_Textbox") )
            self.master.grid_rowconfigure(0, weight=1)
            self.master.grid_columnconfigure(0, weight=1)


            # INSERT ENTRY WIDGET FOR EMAIL STATUS MESSAGES .... 
            self.entry_EMAIL_STATUS = StringVar()
            self.email_status_entry = Entry(self.master, textvariable = self.entry_EMAIL_STATUS, font = VERANDA_12_font, width = 100)
            self.email_status_entry.grid(sticky = W, row=7, column=1)
            self.email_status_entry.config(borderwidth=5, background="dark slate gray", fg="cyan3")
            self.email_status_entry.bind("<Button-1>",lambda event: self.status_widget_function(event, "self.email_status_entry") )

            # PLACE THESE TWO LINES TO SORT AND RE-WRITE DICTIONARY DATA FILES
            # WHICH UPDATES and SETS THE selected_dictionary_loaded_global GLOBAL. 

            inst_email_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
            loaded_email_contact_dict_acquired = inst_email_loaded_Process_Dict_File.read_target_dict_file()

            selected_dictionary_record_index_global = 0

            selected_dictionary_record_index_global = selected_dictionary_record_index_focus_global

            fn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )

            first_and_last_name = "  Contact Name: " + str(fn_load) + " " + str(ln_load)

            self.entry_LOADED_CONTACT_NAME.set(str(first_and_last_name) )

            self.entry_DEST_1_EMAIL_ADDRESS.set(str(em_load) )

            # Retreive from GLOBAL and Add to ENTRY WIDGET the CONTACT LIST NAME
            self.CONTACT_LIST_NAME_String = "  Contact List: " + str(master_cm_list_name_global)

            self.entry_CONTACT_LIST_NAME_Stringvar.set(str(self.CONTACT_LIST_NAME_String) )

            selected_dictionary_counter_status_display = " Contact Number: " + str(selected_dictionary_record_index_focus_global) + \
             " of " + str(num_of_dictionary_data_records_global) 

            self.entry_EMAIL_STATUS.set(str(selected_dictionary_counter_status_display) )

            if gmail_mode_global == "OAUTH2_Gmail_Mode":

                status_message_info = "Note: Your Gmail Address & Password NOT required in OAUTH2_Gmail_Mode."

                source_address_info = "Your Gmail NOT required - OAUTH2_Gmail_Mode"

                source_password_info = "Your Passward NOT required - OAUTH2_Gmail_Mode"
                 
                self.entry_EMAIL_STATUS.set(str(status_message_info) )
                self.entry_SOURCE_EMAIL_ADDRESS.set(str(source_address_info) )
                self.entry_SOURCE_EMAIL_PASSWORD.set(str(source_password_info) )

            elif gmail_mode_global == "SMTP_Gmail_Mode":

                status_message_info = "Gmail Address/Password REQUIRED and Set ALLOW LESS SECURE APPS (ON)"

                self.entry_EMAIL_STATUS.set(str(status_message_info) )
                self.entry_SOURCE_EMAIL_ADDRESS.set("")
                self.entry_SOURCE_EMAIL_PASSWORD.set("")

            else:
                pass



      ########################################################################################
      # 
      #   SELECT DEST ADDRESS(ES) from LISTBOX and return a list of selected email addresses.
      #
      #   Applicable GLOBAL:   selected_email_address_LIST_GLOBAL  
      #
      ########################################################################################
      # Method to open a new LISTBOX Window and SELECT DEST ADDRESS(ES) from LISTBOX.
      def select_dest_address(self):
          global selected_email_address_LIST_GLOBAL
          global DEST_or_CC_email_address_FLAG_GLOBAL
          global email_list_from_listbox_ready_global

          self.select_email_dest_address_Window = tk.Toplevel(self.master)
          self.select_email_dest_address_LIST_inst = Select_Email_Address_List(self.select_email_dest_address_Window)

          DEST_or_CC_email_address_FLAG_GLOBAL = "DEST_EMAIL_LIST_GEN_MODE"

          email_list_from_listbox_ready_global = False

          # Activate thread to listen for email_list_from_listbox_ready_global == True
          thread_listen_email_list_ready = threading.Thread(name="LISTEN_EMAIL_LIST_READY_THREAD", target=self.LISTEN_EMAIL_LIST_READY_THREAD_worker, daemon=True)
          thread_listen_email_list_ready.start()


      ########################################################################################
      # 
      #   SELECT CC ADDRESS(ES) from LISTBOX and return a list of selected email addresses.
      # 
      #   Applicable GLOBAL:   selected_email_address_LIST_GLOBAL    
      #
      ########################################################################################
      # Method to open a new LISTBOX Window and SELECT CC ADDRESS(ES) from LISTBOX.
      def select_cc_address(self):
          global selected_email_address_LIST_GLOBAL
          global DEST_or_CC_email_address_FLAG_GLOBAL
          global email_list_from_listbox_ready_global

          self.select_email_CC_address_Window = tk.Toplevel(self.master)
          self.select_email_CC_address_LIST_inst = Select_Email_Address_List(self.select_email_CC_address_Window)

          DEST_or_CC_email_address_FLAG_GLOBAL = "CC_EMAIL_LIST_GEN_MODE"

          email_list_from_listbox_ready_global = False

          # Activate thread to listen for email_list_from_listbox_ready_global == True
          thread_listen_email_list_ready = threading.Thread(name="LISTEN_EMAIL_LIST_READY_THREAD", target=self.LISTEN_EMAIL_LIST_READY_THREAD_worker, daemon=True)
          thread_listen_email_list_ready.start()



      def LISTEN_EMAIL_LIST_READY_THREAD_worker(self):
          global email_list_from_listbox_ready_global
      #
      # THREAD: LISTEN_EMAIL_LIST_READY_THREAD  ( email_list_from_listbox_ready_global == True  )
      #
      # Thread to check FLAG and then insert email LIST STRING into DEST or CC ENTRY WIDGET
      #
      # NOTE: We are setting these StringVars now that we have selected
      # the EMAIL ADDRESS(ES) from a LISTBOX. These StringVars are the DEST and CC ENTRY WIDGETS
      # in the EMail Class located several hundred lines below. 
      #
      # IN EMAIL CLASS: 
      # self.entry_DEST_1_EMAIL_ADDRESS.set(str(total_address_list_string_global) ) 
      # self.entry_DEST_CC_EMAIL_ADDRESS.set(str(total_address_list_string_global) )

          while 1:
#12345678901234
              if email_list_from_listbox_ready_global == True:
        
                  # Create total_address_list_string STRING from selected_email_address_LIST_GLOBAL LIST
   
                  total_address_list_string = ""

                  for each_email_address in selected_email_address_LIST_GLOBAL:  # LIST of Email Addresses

                      total_address_list_string = total_address_list_string + each_email_address + ", "

                  # remove comma and space from end of email address string
                  # because the last email does not need a comma and space.
                  if len(total_address_list_string) > 0:
                      total_address_list_string = total_address_list_string.rstrip(", ")

                  # print(".... SEE THE EMAIL STRING WE CREATED AND ABOUT TO INSERT TO ENTRY WIDGET: " + str(total_address_list_string) )

                  if DEST_or_CC_email_address_FLAG_GLOBAL == "DEST_EMAIL_LIST_GEN_MODE":

                      self.entry_DEST_1_EMAIL_ADDRESS.set(str(total_address_list_string) )

                      email_list_from_listbox_ready_global = False

                      # option to stop the thread here if there is a one liner to do so
              
                  elif DEST_or_CC_email_address_FLAG_GLOBAL == "CC_EMAIL_LIST_GEN_MODE":

                      self.entry_DEST_CC_EMAIL_ADDRESS.set(str(total_address_list_string) )

                      email_list_from_listbox_ready_global = False

                      # option to stop the thread here if there is a one liner to do so
              
                  else: pass
#12345678901234
              elif email_list_from_listbox_ready_global == False:
                  time.sleep(1)

          


          
      #####################################################################################
      # 
      #   Calls - Contact Manager Application Documentation Media Class - CM_App_Doc_Media
      #
      #####################################################################################
      #
      # Method to open new window for Application Documentation Media. 
      # 
      def cm_app_doc_media_window_method_email_screen(self):

          self.cm_app_doc_media_email_WINDOW = tk.Toplevel(self.master)
          self.cm_app_doc_media_email = CM_App_Doc_Media(self.cm_app_doc_media_email_WINDOW)



      def lower_email_WINDOW(self):
          global kick_thread_to_update_main_entry_widgets
          # update the main screen entry widgets
          # to be at the current focus dict index global
          kick_thread_to_update_main_entry_widgets = True

          # These CYCLE Buttons have been changed to
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()

          

      def exit_Handler(self):
          global kick_thread_to_update_main_entry_widgets
          # update the main screen entry widgets
          # to be at the current focus dict index global
          kick_thread_to_update_main_entry_widgets = True
          self.master.destroy()


            
            
      ######################################################################################
      #    
      # Email Mode Select Optons Menu StringVar setting ...  
      #  
      # if gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode"
      # 
      # then choose the corresponding messagebox to display to the operator.
      #
      # Default setting is gmail_mode_global = "SMTP_Gmail_Mode"
      #      
      ######################################################################################
      #
      def func_set_email_mode_select_global(self, email_mode_select_opt_menu_select):
             global gmail_mode_global

             gmail_mode_global = str(email_mode_select_opt_menu_select)

             if gmail_mode_global == "OAUTH2_Gmail_Mode":

                 status_message_info = "Note: Your Gmail Address & Password NOT required in OAUTH2_Gmail_Mode."

                 source_address_info = "Your Gmail NOT required - OAUTH2_Gmail_Mode"

                 source_password_info = "Your Passward NOT required - OAUTH2_Gmail_Mode"
                 
                 self.entry_EMAIL_STATUS.set(str(status_message_info) )
                 self.entry_SOURCE_EMAIL_ADDRESS.set(str(source_address_info) )
                 self.entry_SOURCE_EMAIL_PASSWORD.set(str(source_password_info) )

             elif gmail_mode_global == "SMTP_Gmail_Mode":

                 status_message_info = "Gmail Address/Password REQUIRED and Set ALLOW LESS SECURE APPS (ON)"

                 self.entry_EMAIL_STATUS.set(str(status_message_info) )
                 self.entry_SOURCE_EMAIL_ADDRESS.set("")
                 self.entry_SOURCE_EMAIL_PASSWORD.set("")

             else:
                 pass

  
   
#123456   save_contact_notes - Add Saving of EMail Addresses and Email Title (Subject) to this method.
      def save_contact_notes(self):
            global fullpath_prepend_cnotes_dict_file_global
            global prepend_cnotes_dict_file_global
            global fullpath_cnotes_dict_file_global

            # GET the Contact Notes from the Text Widget
            # and add a contact info section at the end
            # by building a new string called: str(build_a_string) 

            contact_notes_get = ""
            contact_notes_get = self.EMAIL_Textbox.get("1.0",END)
            two_line_space = "\n\n"
            one_line_space = "\n"
            contact_notes_date_time_label = "CONTACT NOTES DATE - TIME - "
            # Create a Time Stamp
            temp_time_string = str(datetime.datetime.now() )
            contact_notes_info_label = "CONTACT NOTES INFORMATION:"
            fn_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )
            contact_notes_line = str("_____________________________________________________________")
            contact_notes_info_line1 = str(fn_info) + " " + str(ln_info) + "\n"
            contact_notes_info_line2 = str(sa_info) + ", " + str(ct_info) + ", " + str(st_info) + ", " + str(zc_info) + "\n"
            contact_notes_info_line3 = "Phone: " + str(pn_info) + "\n"
            contact_notes_info_line4 = "Email: " + str(em_info) + "\n"
            contact_notes_info_line5 = "Website: " + str(ws_info) + "\n"

            build_a_string = []
            
            build_a_string.append(str(contact_notes_line) )
            build_a_string.append(str(two_line_space) )
            build_a_string.append(str(contact_notes_date_time_label) )
            build_a_string.append(str(temp_time_string) )
            build_a_string.append(str(two_line_space) )
            build_a_string.append(str(contact_notes_info_label) )
            build_a_string.append(str(two_line_space) )
            build_a_string.append(str(contact_notes_info_line1) )
            build_a_string.append(str(contact_notes_info_line2) )
            build_a_string.append(str(contact_notes_info_line3) )
            build_a_string.append(str(contact_notes_info_line4) )
            build_a_string.append(str(contact_notes_info_line5) )
            build_a_string.append(str(contact_notes_line) )
            build_a_string.append(str(two_line_space) )
            build_a_string.append(str(contact_notes_get) )
            build_a_string.append(str(two_line_space) )

            final_built_string = ""
            final_built_string = ''.join(build_a_string)

            #print the string to see .......
            #print("\n" + "STRING BUILT = " + "\n" )
            #print(str(final_built_string) )

            ################################################################################## 

            # Eventually, we want to change Website to LAST FOUR OF SOCIAL SECURITY Number
            # to implement this CONTACT_ID_KEY in a more conventional industry standard way.

            CONTACT_ID_KEY = ""

            CONTACT_ID_KEY = str(ln_info) + "_" + str(em_info)

            # Write contact notes data dictionary to DICTIONARY FORMAT file  
            # Note that we use the FULLPATH - fullpath_cnotes_dict_file_global

            create_the_string_1 = "CONTACT_NOTES_DATA_RECORD_DELIMITER:"
            create_the_string_2 = str(CONTACT_ID_KEY)
            create_the_string_3 = "KEY_SYNC_TARGET_NOTES_STRING:"
            create_the_string_4 = str(final_built_string)

            complete_data_block = create_the_string_1 + create_the_string_2 + \
                                  create_the_string_3 + create_the_string_4

            
            # Prepend complete_data_block to beginning of cnotes flle 
            # using fullpath_prepend_cnotes_dict_file_global        

            with open(fullpath_cnotes_dict_file_global, 'r+') as f:
                 all_notes_content = f.read()
                 f.seek(0, 0)
                 f.write(complete_data_block.rstrip('\r\n') + '\n' + all_notes_content)




      def retrieve_contact_notes(self):
            #print("..... RETRIEVING CONTACT NOTES .....")
            # INSERT CONTACT NOTES DATA LINES into TEXTBOX to VIEW the TEXTBOX
            # after loading the current LOGFILE using the full path name:
            # fullpath_cnotes_dict_file_global.
            #
            # NOTE: This is the format of the Contact Notes Data Block:
            # 
            # create_the_string_1 = "CONTACT_NOTES_DATA_RECORD_DELIMITER:"
            # create_the_string_2 = str(CONTACT_ID_KEY)
            # create_the_string_3 = "KEY_SYNC_TARGET_NOTES_STRING:"
            # create_the_string_4 = str(final_built_string)
            #
            # where the CONTACT_ID_KEY = str(ln_info) + "_" + str(em_info)
            #
            ############################################################################

            # Clear Textbox to prepare to Retrieve Contact Notes
            self.EMAIL_Textbox.delete("1.0",END)

            fn_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )

            # Eventually, we want to change Website to LAST FOUR OF SOCIAL SECURITY Number
            # to implement this CONTACT_ID_KEY in a more conventional industry standard way. 
            
            CONTACT_ID_KEY = ""

            CONTACT_ID_KEY = str(ln_info) + "_" + str(em_info)

            #print(".... RETRIEIVING DICTIONARY KEY:  Dict_KEY" + str(selected_dictionary_record_index_focus_global) )
            #print("  ")
            #print(".... selected_dictionary_record_index_focus_global = " + str(selected_dictionary_record_index_focus_global) )
            #print(".... First and Last Name = " + str(fn_info) + " " + str(ln_info) )
            #print(".... SPLIT STRING ON:  CONTACT_NOTES_DATA_RECORD_DELIMITER:  + str(CONTACT_ID_KEY) + KEY_SYNC_TARGET_NOTES_STRING: = ")
            #print(".... " + "CONTACT_NOTES_DATA_RECORD_DELIMITER:" + str(CONTACT_ID_KEY) + "KEY_SYNC_TARGET_NOTES_STRING:")

            create_the_sync_string_1 = str(CONTACT_ID_KEY)
            create_the_sync_string_2 = "KEY_SYNC_TARGET_NOTES_STRING:"

            complete_data_block_sync_string = create_the_sync_string_1 + create_the_sync_string_2

            #print(".... complete_data_block_sync_string = " + str(complete_data_block_sync_string) )

        
            self.textFile = open(fullpath_cnotes_dict_file_global, 'r')

            # This takes the file object opened with the open() and turns it into a string which 
            # you can now use textString in a text widget.
            self.textString = self.textFile.read()

            # Define Dictionaries here ....

            # Count the DATA RECORDS in the string by counting the
            # number of "CONTACT_NOTES_DATA_RECORD_DELIMITER:" patterns 
            self.num_data_records = self.textString.count("CONTACT_NOTES_DATA_RECORD_DELIMITER:")

            #print("..... NUMBER OF DATA RECORDS = " + str(self.num_data_records) )

            self.num_data_records_plus_one = self.num_data_records + 1

            track_text_widget_inserts = 0

            cummulative_notes_string = ""
            
            ####################################################################################
            #
            # Operate on the textString to search for complete_data_block_sync_string
            #
            # which is made up of the concatenation of these sub-strings:
            # 
            # 1. str(CONTACT_ID_KEY) string
            #
            # 2. "KEY_SYNC_TARGET_NOTES_STRING:" string
            #
            for record_index in range (1, self.num_data_records_plus_one):
                  
                self.data_record_string = self.textString.split("CONTACT_NOTES_DATA_RECORD_DELIMITER:")[record_index]

                #print("  ")
                #print(".... NOW PROCESSING record_index: " + str(record_index) + " of " + str(self.num_data_records) )
                #print(".... self.data_record_string = " + str(self.data_record_string) )
                
                try:
                      target_notes_string = self.data_record_string.split(str(complete_data_block_sync_string) )[1]

                      track_text_widget_inserts +=1

                      #print(".... str(complete_data_block_sync_string) = " + str(complete_data_block_sync_string) )
                      #print(".... target_notes_string = " + str(target_notes_string) )

                      temp_string_variable = ""

                      temp_string_variable = str(cummulative_notes_string) + str(target_notes_string)

                      cummulative_notes_string = temp_string_variable

                      #print(".... cummulative_notes_string = " + str(cummulative_notes_string) )


                except:
                      pass

            ##############    verifying append to string and append to TEXT WIDGET    ##############  
                
            try:
                  self.EMAIL_Textbox.insert("1.0", str(cummulative_notes_string) )
                  
                  #print("..... *** FINAL *** CUMMULATIVE NOTES STRING = " + str(cummulative_notes_string) )

                  #print("..... *** TOTAL NOTES LOCATED FOR PERSON *** track_text_widget_inserts = " + str(track_text_widget_inserts) )

            except:
                  pass
 


      ###############################################################################
      # 
      # Programming Note: 
      #
      # Note that the generic sequence of TEXT WIDGET Commands
      # are as follows:
      #
      # SAVE CONTACT NOTES:
      #
      # contact_notes_get = self.EMAIL_Textbox.get("1.0",END)
      #
      # RETRIEVE CONTACT NOTES:
      #
      # self.EMAIL_Textbox.delete("1.0",END)
      #
      # self.EMAIL_Textbox.insert(END, str(target_notes_string))
      #
      # self.EMAIL_Textbox.insert("1.0", str(target_notes_string))
      #
      ###############################################################################

           

      def src_addr_widget_function(self, event, src_addr_widget_name):
            self.last_widget_name_clicked = src_addr_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def clistname_widget_function(self, event, clist_widget_name):
            self.last_widget_name_clicked = clist_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def contact_list_widget_function(self, event, contact_list_widget_name):
            self.last_widget_name_clicked = contact_list_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )

            
      def pwd_widget_function(self, event, pwd_widget_name):
            self.last_widget_name_clicked = pwd_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def cc_widget_function(self, event, cc_widget_name):
            self.last_widget_name_clicked = cc_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def to_widget_function(self, event, to_widget_name):
            self.last_widget_name_clicked = to_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def title_widget_function(self, event, title_widget_name):
            self.last_widget_name_clicked = title_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def content_widget_function(self, event, content_widget_name):
            self.last_widget_name_clicked = content_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def status_widget_function(self, event, status_widget_name):
            self.last_widget_name_clicked = status_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )



            
      ######################################################################################
      # 
      # textbox_edit_ Mode Select Optons Menu StringVar setting ...
      #   
      # if tb_mode_select_opt_menu_select == "DROPDOWN MENU CHOICE": 
      # then execute corresponding email content textbox edit.
      #
      ######################################################################################
      #
      # IMPORTANT NOTE:  <event>  ---  Capture WIDGET NAME with print event.widget
      #
      # Update this to form and utilize a WIDGET NAME OF LAST EVENT GLOBAL
      # so that we can implement the code below with a Dynamically Changing
      # WIDGET NAME OF LAST EVENT GLOBAL where the latest curcor click happened
      # instead of the just he static self.EMAIL_Textbox implemntation. 
      #           
      ######################################################################################
      #
      def func_set_textbox_edit_mode_select_global(self, tb_mode_select_opt_menu_select):
             global textbox_edit_mode_select_global
             global fullpath_cnotes_dict_file_global

             textbox_edit_mode_select_global = str(tb_mode_select_opt_menu_select)

             self.w = self.last_widget_name_clicked

             # EDIT EMAIL DROPDOWN MENU. 
             #
             if tb_mode_select_opt_menu_select == "CLEAR Email or NOTES Content":
                   self.entry_EMAIL_STATUS.set("")
                   self.entry_EMAIL_TITLE.set("")
                   self.EMAIL_Textbox.delete('1.0', END)
                   self.EMAIL_ATTACHMENT_OPTION_FLAG = False
                   self.file_email_attachment_FULL_PATH = []

                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )

             elif tb_mode_select_opt_menu_select == "CLEAR Email STATUS Only":
                   self.entry_EMAIL_STATUS.set("")

                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )

             elif tb_mode_select_opt_menu_select == "DELETE NOTES for SELECTED CONTACT LIST":
                   # DELETE "cnotes_" NOTES FILE for the SELECTED CONTACT LIST 

                   with open(fullpath_cnotes_dict_file_global, "w") as fnotes:
                       fnotes.seek(0, 0)
                       fnotes.write("")

                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )
                   
             elif tb_mode_select_opt_menu_select == "CUT Selected Text - (CNTL-X)":
                   #print("... CUT ...")
                   
                   selected_text = "INITIALIZE SELECTED TEXT LOCAL VARIABLE"
                   
                   # ORIGINAL COMMAND 1: self.EMAIL_Textbox.clipboard_clear()
                   #
                   new_command_string_CUT_1 = self.last_widget_name_clicked + ".clipboard_clear()"
                   #print("..... new_command_string__CUT_1 = " + str(new_command_string_CUT_1) )
                   exec(new_command_string_CUT_1)  # to insert self.last_widget_name_clicked

                   # ORIGINAL COMMAND 2: selected_text = self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) )
                   #
                   # but the ENTRY WIDGET does not take any arguements for GET
                   # and the TEXT WIDGET does take arguements for GET
                   # so we must do an IF statement to discern betweem ENTRY AND TEXT WIDGETS ...
                   # to format this command accordingly ... 
                   # 
                   # get(tk.SEL_FIRST, tk.SEL_LAST) for TEXT WIDGET 
                   # get() for ENTRY WIDGET 
                   # 
                   # entry class get does not take any arguments (but text class does)
                   #
                   
                   if self.last_widget_name_clicked == "self.EMAIL_Textbox":
                         selected_text = str(self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) )
                         
                   elif self.last_widget_name_clicked == "self.source_email_address_entry":
                         selected_text = str(self.source_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.source_email_password_entry":
                         selected_text = str(self.source_email_password_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.destination_1_email_address_entry":
                         selected_text = str(self.destination_1_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.destination_cc_email_address_entry":
                         selected_text = str(self.destination_cc_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.email_title_entry":
                         selected_text = str(self.email_title_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.email_status_entry":
                         selected_text = str(self.email_status_entry.get() )


                   #print("\n")
                   #print("..... selected_text = " + str(selected_text) )
                   

                   # ORIGINAL COMMAND 3: EMAIL_Textbox.master.clipboard_append(selected_text)
                   
                   new_command_string_CUT_3 = self.last_widget_name_clicked + ".master.clipboard_append(selected_text)"

                   #print("\n")
                   #print(".... new_command_string_CUT_3 = " + str(new_command_string_CUT_3) )

                   exec(new_command_string_CUT_3)  # to insert self.last_widget_name_clicked
                   
                   # ORIGINAL COMMAND 4: self.EMAIL_Textbox.delete(tk.SEL_FIRST, tk.SEL_LAST)
                   # Now we update code to accomodate select beween TEXT Widget or ENTRY Widget 
                   # because TEXT Widget and ENTRY Widget have different commands to select text.

                   if self.last_widget_name_clicked == "self.EMAIL_Textbox":
                         self.EMAIL_Textbox.delete(tk.SEL_FIRST, tk.SEL_LAST)

                   elif self.last_widget_name_clicked == "self.source_email_address_entry":
                         self.entry_SOURCE_EMAIL_ADDRESS.set("")
                         
                   elif self.last_widget_name_clicked == "self.source_email_password_entry":
                         self.entry_SOURCE_EMAIL_PASSWORD.set("")
                         
                   elif self.last_widget_name_clicked == "self.destination_1_email_address_entry":
                         self.entry_DEST_1_EMAIL_ADDRESS.set("")
                         
                   elif self.last_widget_name_clicked == "self.destination_cc_email_address_entry":
                         self.entry_DEST_CC_EMAIL_ADDRESS.set("")
                         
                   elif self.last_widget_name_clicked == "self.email_title_entry":
                         self.entry_EMAIL_TITLE.set("")
                         
                   elif self.last_widget_name_clicked == "self.email_status_entry":
                         self.entry_EMAIL_STATUS.set("")
                         
                   else:
                         pass

                                            
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )
                   
             elif tb_mode_select_opt_menu_select == "COPY Selected Text - (CNTL-C)":
                   #print("... COPY ...")

                   selected_text = "INITIALIZE SELECTED TEXT LOCAL VARIABLE"
                   
                   # ORIGINAL COMMAND 1: self.EMAIL_Textbox.clipboard_clear()
                   new_command_string_1 = self.last_widget_name_clicked + ".clipboard_clear()"
                   #print("..... new_command_string_1 = " + str(new_command_string_1) )
                   exec(new_command_string_1)  # to insert self.last_widget_name_clicked
                   
                   # ORIGINAL COMMAND 2: selected_text = self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) )
                   # but the ENTRY WIDGET does not take any aruements for GET
                   # and the TEXT WIDGET does take argements for GET
                   # so we must do an IF statement to discern betweem ENTRY AND TEXT WIDGETS ...
                   # to format this command accordingly ... 
                   # 
                   # get(tk.SEL_FIRST, tk.SEL_LAST) for TEXT WIDGET 
                   # get() for ENTRY WIDGET 
                   # 
                   # entry class get does not take any arguments (but text class does)
                   #
                   
                   if self.last_widget_name_clicked == "self.EMAIL_Textbox":
                         selected_text = str(self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) )
                         
                   elif self.last_widget_name_clicked == "self.source_email_address_entry":
                         selected_text = str(self.source_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.source_email_password_entry":
                         selected_text = str(self.source_email_password_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.loaded_contact_name_entry":
                         selected_text = str(self.loaded_contact_name_entry.get() )

                   elif self.last_widget_name_clicked == "self.CONTACT_LIST_NAME_entry":
                         selected_text = str(self.CONTACT_LIST_NAME_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.destination_1_email_address_entry":
                         selected_text = str(self.destination_1_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.destination_cc_email_address_entry":
                         selected_text = str(self.destination_cc_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.email_title_entry":
                         selected_text = str(self.email_title_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.email_status_entry":
                         selected_text = str(self.email_status_entry.get() )
                         

                   #print("\n")
                   #print("..... selected_text = " + str(selected_text) )


                   # ORIGINAL COMMAND 3: EMAIL_Textbox.master.clipboard_append(selected_text)
                   new_command_string_3 = self.last_widget_name_clicked + ".master.clipboard_append(selected_text)"

                   #print("\n")
                   #print(".... new_command_string_3 = " + str(new_command_string_3) )

                   exec(new_command_string_3)  # to insert self.last_widget_name_clicked

                   # ORIGINAL COMMANDS WITH ONLY THE TEXT WIDGET
                   # self.EMAIL_Textbox.clipboard_clear() 
                   # selected_text = self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) 
                   # self.EMAIL_Textbox.master.clipboard_append(selected_text) 
                   
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )
                   
             elif tb_mode_select_opt_menu_select == "PASTE to Cursor - (CNTL-V)":
                   #print("... PASTE ...")  

                   selected_text = "INITIALIZE SELECTED TEXT LOCAL VARIABLE"

                   # clip_text = root.clipboard_get()
                   clip_text = self.master.clipboard_get()
                   #print("\n")
                   #print("....... clip_text = " + str(clip_text) )

                   #
                   # ORIGINAL COMMAND 1: 
                   #
                   # selected_text = self.EMAIL_Textbox.selection_get(selection='CLIPBOARD')
                   #  

                   if self.last_widget_name_clicked == "self.EMAIL_Textbox":
                         selected_text = self.EMAIL_Textbox.selection_get(selection='CLIPBOARD')
                         self.EMAIL_Textbox.insert('insert', selected_text)

                   elif self.last_widget_name_clicked == "self.source_email_address_entry":
                         self.entry_SOURCE_EMAIL_ADDRESS.set(str(clip_text) )
                         
                   elif self.last_widget_name_clicked == "self.source_email_password_entry":
                         self.entry_SOURCE_EMAIL_PASSWORD.set(str(clip_text) )
                         
                   elif self.last_widget_name_clicked == "self.destination_1_email_address_entry":
                         self.entry_DEST_1_EMAIL_ADDRESS.set(str(clip_text) )
                         
                   elif self.last_widget_name_clicked == "self.destination_cc_email_address_entry":
                         self.entry_DEST_CC_EMAIL_ADDRESS.set(str(clip_text) )
                         
                   elif self.last_widget_name_clicked == "self.email_title_entry":
                         self.entry_EMAIL_TITLE.set(str(clip_text) )
                         
                   else:
                         pass

                   # ORIGINAL COMMANDS with TEXT Widget: 
                   # selected_text = self.EMAIL_Textbox.selection_get(selection='CLIPBOARD')
                   # self.EMAIL_Textbox.insert('insert', selected_text)
                   
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )
                   
             elif tb_mode_select_opt_menu_select == "EDIT MENU":
                   return
             else:
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) ) 
                   return


                   

      def load_next_contact(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global kick_thread_to_update_main_entry_widgets

            test_forward_count = selected_dictionary_record_index_global + 1
            
            if test_forward_count <= num_of_dictionary_data_records_global:
                  pass
            elif test_forward_count > num_of_dictionary_data_records_global:
                  return

            # Increment Dictionary Contact Index. 

            selected_dictionary_record_index_global +=1
            selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global

            fn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )

            first_and_last_name = "  Contact Name: " + str(fn_load) + " " + str(ln_load)

            self.entry_LOADED_CONTACT_NAME.set(str(first_and_last_name) )

            self.entry_DEST_1_EMAIL_ADDRESS.set(str(em_load) )

            selected_dictionary_counter_status_display = " Contact Number: " + str(selected_dictionary_record_index_focus_global) + \
             " of " + str(num_of_dictionary_data_records_global) 

            self.entry_EMAIL_STATUS.set(str(selected_dictionary_counter_status_display) )

            # Each time the Email Class Instance Contact Increments or Decrements:
            # kick the main screen widgets update thread to update main screen widgets
            # by setting kick_thread_to_update_main_entry_widgets = True
            kick_thread_to_update_main_entry_widgets = True



      def load_previous_contact(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global kick_thread_to_update_main_entry_widgets

            test_backward_count = selected_dictionary_record_index_global - 1
            
            if test_backward_count >= 1:
                  pass
            elif test_backward_count < 1:
                  return
                  
            # Decrement Dictionary Contact Index.

            selected_dictionary_record_index_global -=1
            selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global

            fn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )

            first_and_last_name = "  Contact Name: " + str(fn_load) + " " + str(ln_load)

            self.entry_LOADED_CONTACT_NAME.set(str(first_and_last_name) )

            self.entry_DEST_1_EMAIL_ADDRESS.set(str(em_load) )

            selected_dictionary_counter_status_display = " Contact Number: " + str(selected_dictionary_record_index_focus_global) + \
             " of " + str(num_of_dictionary_data_records_global) 

            self.entry_EMAIL_STATUS.set(str(selected_dictionary_counter_status_display) )

            # Each time the Email Class Instance Contact Increments or Decrements:
            # kick the main screen widgets update thread to update main screen widgets
            # by setting kick_thread_to_update_main_entry_widgets = True
            kick_thread_to_update_main_entry_widgets = True




      def get_credentials(self):
          global credential_home_dir_global
          global credential_appdata_dir_global
          global credential_home_path_global
          global credential_appdata_path_global
          global client_secret_path_global
          global userprofile_global
          global gmail_oauth2_json_file_test_global
          global gmail_oauth2_status_global
          global gmail_oauth2_exceptions_status_global
          global gmail_oauth2_SPECIFIC_EXCEPTION_global
          global gmail_smtp_allow_less_secure_apps_global
          global gmail_smtp_status_global
          global gmail_smtp_exceptions_status_global
          global gmail_smtp_SPECIFIC_EXCEPTION_global
          global gmail_mode_global
          global credential_home_dir_global
          global credential_appdata_dir_global
          global credential_home_path_global
          global credential_appdata_path_global
          global client_secret_path_global
          #
          #
          # Gets valid user credentials from storage.
          # If nothing has been stored, or if the stored credentials are invalid,
          # the OAuth2 flow is completed to obtain the new credentials.
          #
          # Returns:  
          #
          # Credentials, the obtained credential (in the client_secret.json file).
          #
          # Credentials are Stored Here to save then where http will look for them:
          # credential_home_path_global = os.path.join(credential_home_dir_global, "gmail-python-quickstart.json")
          #
          # Credentials are Stored Here to save then to APPDATA Area:
          # credential_appdata_path_global = os.path.join(credential_appdata_dir_global, "gmail-python-quickstart.json")
          #
          # NOTE the following global variables in code below: (set at top of file)
          #
          # CLIENT_SECRET_FILE, SCOPES, APPLICATION_NAME
          #
          # If modifying these scopes, delete your previously saved credentials
          # at ~/.credentials/gmail-python-quickstart.json
          #
          # SCOPES = "https://mail.google.com"
          # CLIENT_SECRET_FILE = 'client_secret.json' 
          # APPLICATION_NAME = 'Gmail API Python Quickstart' 
          # 
          ###############################################################################################

          # see if our SCOPES, CLIENT_SECRET_FILE, and APPLICATION_NAME Globals are seen here
          # YES, They are printed OK. They are visible from here. 
          # These are SET at the top of this contact_management.py file.  
          #
          # print(".... APPLICATION_NAME = " + str(APPLICATION_NAME) )
          # print(".... CLIENT_SECRET_FILE = " + str(CLIENT_SECRET_FILE) )
          # print(".... SCOPES = " + str(SCOPES) )
          
          # we store credentials here because the credentials = store.get() below looks for them here. 

          # store = Storage(credential_home_path_global)  

          home_dir = userprofile_global
          credential_dir = os.path.join(home_dir, '.credentials')
          client_secret_dir = os.path.join(home_dir, '.credentials')
          if not os.path.exists(credential_dir):
              os.makedirs(credential_dir)
              
          credential_path = os.path.join(credential_dir, 'gmail-python-quickstart.json')
          client_secret_path = os.path.join(credential_dir, 'client_secret.json')

          # Test the open in read mode of client_secret.json file here
          # and if it fails then set status panel specific exception
          # gmail_oauth2_SPECIFIC_EXCEPTION_global == "FileNotFoundError"

          try:
              
              client_secret_textFile = open(client_secret_path_global, 'r')

              client_secret_textString = client_secret_textFile.read()

          except Exception:
              exc_type, exc_value, exc_traceback = sys.exc_info()
              lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
              exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

              gmail_oauth2_SPECIFIC_EXCEPTION_global = "FileNotFoundError"
                    
              # open Write_Exception_Logfile() to append logfile to update the logfile items.
              inst_Write_Exception_Logfile_open_client_secret_to_read = Write_Exception_Logfile()
              exception_logging_string_1 = "  *** OAUTH2 client_secret.json FILE NOT FOUND ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
              exception_logging_string_3 = "\n\n"
                    
              inst_Write_Exception_Logfile_open_client_secret_to_read.log_exception(str(exception_logging_string_1) )
              inst_Write_Exception_Logfile_open_client_secret_to_read.log_exception(str(exception_logging_string_2) )
              inst_Write_Exception_Logfile_open_client_secret_to_read.log_exception(str(exception_logging_string_3) )
          
          
          ###########################################################################
          #
          #    get credentials .......
          #
          # If modifying these scopes, delete your previously saved credentials
          # at ~/.credentials/gmail-python-quickstart.json
          #
          ###########################################################################
          
          SCOPES = "https://mail.google.com"
          CLIENT_SECRET_FILE = client_secret_path
          APPLICATION_NAME = 'Gmail API Python Quickstart'

          # Store the credential
          store = oauth2client.file.Storage(credential_path)

          credentials = store.get()
          
          if not credentials or credentials.invalid:
              flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
              flow.user_agent = APPLICATION_NAME
              if flags:
                  credentials = tools.run_flow(flow, store, flags)
                  storing_credentials_message = ".... WAIT 5 Seconds - Storing OAUTH2 Credentials to: " + str(credential_home_path_global)
                  self.entry_EMAIL_STATUS.set(str(storing_credentials_message) )
                  # print(str(storing_credentials_message))
                  time.sleep(5)
              else: # Needed only for compatibility with Python 2.6
                  credentials = tools.run(flow, store)
                  storing_credentials_message = ".... WAIT 5 Seconds - Storing OAUTH2 Credentials to: " + str(credential_home_path_global)
                  self.entry_EMAIL_STATUS.set(str(storing_credentials_message) )
                  # print(str(storing_credentials_message))
                  time.sleep(5)
                  
          return credentials


 

      def SendMessage(self, service, user_id, message):
          #
          # Send an email message.
          #
          #  Args:
          #   service: Authorized Gmail API service instance.
          #   user_id: User's email address. The special value "me"
          #   can be used to indicate the authenticated user. 
          #   message: Message to be sent.
          #
          #  Returns: 
          #
          #   Sent Message.
          #
          try:
                message = (service.users().messages().send(userId=user_id, body=message).execute())
                # print('Message Id: ' + str(message['id'] ) )
                return message
          
          except Exception as ex:
                temp_time_string = str(datetime.datetime.now() )
                complete_email_status_string = "OAUTH2   E M A I L   S E N D   E R R O R - TIME = " + str(temp_time_string)
                self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )
                
                # print(str(complete_email_status_string) )
                # print(ex)



      ################################################################################
      #
      # Select Gmail Mode based on GLOBAL Setting.  
      #     
      # gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode"
      # 
      # This was combined into the same METHOD controlling the
      # MIME Container building process independent of whether we are
      # gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode".
      #
      # Both gmail_mode_global settings will execute METHOD:
      #
      # self.get_Textbox_File_for_OAUTH2_Email() 
      #
      def get_decision_Textbox_File(self, event):
            global gmail_mode_global
            
            if gmail_mode_global == "OAUTH2_Gmail_Mode":
                  self.get_Textbox_File_for_OAUTH2_Email()
            elif gmail_mode_global == "SMTP_Gmail_Mode":
                  self.get_Textbox_File_for_OAUTH2_Email()
            else:
                  return
              


            
      #######################################################################
      #
      # Attention:   EMAIL ATTACHMENT OPTION  ..... 
      #
      # IF  self.EMAIL_ATTACHMENT_OPTION_FLAG == True 
      #
      # If the EMAIL ATTACHMENT OPTION FLAG is SET,
      # we add the attachment file for the EMail
      # and that attachent file name (FULL PATH)
      # was acquired using our EMAIL ATTACHMENT BUTTON
      # and this dialog_to_get_file_attachment (Dialog Method).
      #  
      #######################################################################

      def email_attachment_option_method(self, event):

          self.EMAIL_ATTACHMENT_OPTION_FLAG = True

          #
          # return_object_list: A LIST OF FILE PATHS for Each Attached File ....
          # return_object_list = file_path_list
          # return_object_list from dialog Method:    

          self.file_email_attachment_FULL_PATH = self.dialog_to_get_file_attachment()



      def dialog_to_get_file_attachment(self):
          global userprofile_global

          ###########   Select a Directory:

          root = tk.Tk()
          root.withdraw()
          home_dir = userprofile_global
          dirname = filedialog.askdirectory(parent=root,initialdir=home_dir,title='Please SELECT a Directory')

          directory_full_path = os.path.join(str(home_dir), str(dirname) )

          # print("\n\n\n")
          # print(".... DIRECTORY (FULL PATH): " + str(directory_full_path) )


          ############   Select a File for Opening:  

          # askopenfile - opens the file and returns the opened object (or Null if cancelled).

          # askopenfilename - just gets and returns the full path to the file (or empty string if cancelled).

          ftypes = [
              ('All Files', '*.*'),
              ("Microsoft Word docx Files","*.docx"),
              ("Adobe PDF Files","*.pdf"),
              ("Microsoft Excel xlsx Worksheet Files","*.xlsx"),
              ("Microsoft Excel xls Files","*.xls"),
              ("Microsoft Excel csv Files","*.csv"),
              ("Microsoft Powerpoint Files","*.pptx"),
              ("JPEG Image Files","*.jpg"),
              ("GIF Image Files","*.gif"),
              ("PNG Image Files","*.png"),
              ("Bitmap Image Files","*.bmp"),
              ("MSI Files","*.msi"),
              ("XML Files","*.xml"),
              ("HTML Files","*.html"),
              ('Text Files', '*.txt'),
              ("MIDI .mid Audio Files","*.mid"),
              ("MIDI .rmi Audio Files","*.rmi"),
              ("MP3 Audio Files","*.mp3"),
              ("Apple AIF Audio Files","*.aif"),
              ("Apple AIFC Audio Files","*.aifc"),
              ("Apple AIFF Audio Files","*.aiff"),
              ("MPEGURL Audio Files","*.m3u"),
              ("RealAudio ra Audio Files","*.ra"),
              ("RealAudio ram Audio Files","*.ram"),
              ("WAV Audio Files","*.wav"),
              ("Windows Media Audio Files","*.wma"),
              ("Apple Audio Files","*.iaff"),
              ("A/V Interleave Video File","*.avi"),
              ("Flash Video File","*.flv"),
              ("MPEG Video File","*.mpeg"),
              ("MPEG-4 Video Files","*.mp4"),
              ("Vorbis OGG Video File","*.ogv"),
              ("Vorbis OGG Video File","*.ogg"),
              ("iPhone Segment Video File","*.ts"),
              ("3GP Mobile Video File","*.3gp"),
              ("QuickTime Video File","*.qt"),
              ("QuickTime Video File","*.mov"),
              ("Web Media Video Files","*.webm"),
              ("Windows Media Video Files","*.wmv"),
              ("iPhone Index App File","*.m3u8"),
              ("Config Files","*.cfg"),
              ("Initialization Files","*.ini"),
              ('Python Code Files', '*.py'), 
              ('Perl Code Files', '*.pl;*.pm'),  # semicolon trick
              ('Java Code Files', '*.java'),
              ('Java Server Files', '*.jsp'),
              ('Java Class Files', '*.class'),
              ('JSON Files', '*.json'), 
              ('C++ Code Files', '*.cpp;*.h'),   # semicolon trick
              ("Binary Files","*.bin"),
              ("Executable Files","*.exe"),
              ("Windows System Files","*.sys"),
              ("Batch Files","*.bat"),
              ("Data Files","*.dat"),
              ("ZIP Files","*.zip"),
              ("7Z Files","*.7z"),
              ("TAR Files","*.tar")
          ]

          root = tk.Tk()
          root.withdraw()

          
          # NOTE:  
          #
          # askopenfilenames - gets and returns the full path to each file as a tuple - similar to a list.

          file_path_list=[]

          files = files = filedialog.askopenfilenames(parent=root,title='Choose a file',filetypes = ftypes)

          number_of_files = (len(files))

          # print("\n")

          # print(".... number_of_files = " + str(number_of_files) + "\n")

          for file in files:
              current_file_full_path = file
              file_path_list.append(file)
              # print(".... EACH FILE (FULL PATH): " + str(file) )
              
              current_file_name = os.path.basename(file)
              # print(".... EACH FILE (FILE NAME): " + str(current_file_name) )
              
              current_file_type = current_file_name.split(".")[1]
              # print(".... EACH FILE (FILE TYPE): " + str(current_file_type) )
              
              content_type, encoding = mimetypes.guess_type(file)

              # print(".... EACH FILE (CONTENT TYPE): " + str(content_type) )
              # print(".... EACH FILE (ENCODING): " + str(encoding) )

              main_type, sub_type = content_type.split('/', 1)

              # print(".... EACH FILE (MAIN TYPE): " + str(main_type) )
              # print(".... EACH FILE (SUB TYPE): " + str(sub_type) )

              # print("\n")

          # create and build the return_object_list, which is the file_path_list
          # because we can build everything from the file_path_list. 

          return_object_list = []

          return_object_list = file_path_list

          return return_object_list


          
      #################################################################################################
      #
      # When the Operator presses SEND EMAIL, if the gmail_mode_global = "OAUTH2_Gmail_Mode"  
      # then since the button event has a bind to the above get_decision_Textbox_File method,
      # the method above calls this get_Textbox_File_for_OAUTH2_Email method.
      #
      def get_Textbox_File_for_OAUTH2_Email(self):
            global gmail_mode_global
            global gmail_oauth2_json_file_test_global
            global gmail_oauth2_status_global
            global gmail_oauth2_exceptions_status_global
            global gmail_oauth2_SPECIFIC_EXCEPTION_global
            global textbox_edit_mode_select_global
            global gmail_smtp_allow_less_secure_apps_global
            global gmail_smtp_status_global
            global gmail_smtp_exceptions_status_global
            global gmail_smtp_SPECIFIC_EXCEPTION_global
            self.source_email_address = self.source_email_address_entry.get()
            self.source_email_password = self.source_email_password_entry.get()
            self.destination_1_email_address = self.destination_1_email_address_entry.get()
            self.destination_cc_email_address = self.destination_cc_email_address_entry.get()
            self.email_title = self.email_title_entry.get()
            self.entry_EMAIL_STATUS.set("")

            #######################################################################
            #
            # NOTE: List_of_Email_Modes = ["OAUTH2_Gmail_Mode", "SMTP_Gmail_Mode"]
            # 
            # gmail_mode_global = "SMTP_Gmail_Mode"  (Default) 
            # 
            #######################################################################
            #
            # Attention:   EMAIL ATTACHMENT OPTION  .....
            #  
            # IF  self.EMAIL_ATTACHMENT_OPTION_FLAG == True 
            #
            # If the EMAIL ATTACHMENT OPTION FLAG is SET,
            # we add the attachment file for the EMail
            # and that attachent file name (FULL PATH)
            # was acquired using our EMAIL ATTACHMENT BUTTON
            # and the dialog_to_get_file_attachment (Dialog Method).
            #
            #######################################################################
            
            # Create a Time Stamp
            temp_time_string = str(datetime.datetime.now() )

            complete_email_status_string = ""

            encode_as_bytes = ""

            COMMASPACE = ", "
            TOADDR = []
            CCADDR = []

            # TOADDR is a PYTHON LIST - use split to build this PYTHON LIST
            # from the TEXT WIDGET input get string
            # my_list = my_string.split(",")
            
            TOADDR = str(self.destination_1_email_address).split(",")
            
            # CCADDR is a PYTHON LIST - use split to build this PYTHON LIST
            # from the TEXT WIDGET input get string
            # my_list = my_string.split(",")
            
            CCADDR = str(self.destination_cc_email_address).split(",")  

            # Programming Note:  These are Python LISTS  ..... 
            #
            # TOADDR   = ["email_one@gmail.com", "email_two@outlook.com"]
            # CCADDR   = ["email_three@gmail.com", "email_four@outlook.com"] 
            #
            ####################################################################
            #
            # Create the MIME message container: 
            #
            # the correct MIME type is multipart/mixed if there is an attachment
            # or MIME type is multipart/alternative if there is NOT an attachment
            #
            #
            # print(".... self.EMAIL_ATTACHMENT_OPTION_FLAG = " + str(self.EMAIL_ATTACHMENT_OPTION_FLAG) )
            #
            if self.EMAIL_ATTACHMENT_OPTION_FLAG == True:
                message = MIMEMultipart('mixed')
            elif self.EMAIL_ATTACHMENT_OPTION_FLAG == False:
                message = MIMEMultipart('alternative')


            message['Subject'] = str(self.email_title)
            message['From']    = str(self.source_email_address)
            message['To']      = COMMASPACE.join(TOADDR)
            message['Cc']      = COMMASPACE.join(CCADDR)

            # GET the Email Content from the Text Widget
            self.email_content = self.EMAIL_Textbox.get("1.0",END)

            # print("\n" + ".... self.email_content = " + str(self.email_content) + "\n")

            body_from_textbox = str(self.email_content)

            body = MIMEText(body_from_textbox, 'plain') # convert the body to a MIME compatible string
              
            message.attach(body)

            # Load message into Class Variable Object 
            self.EMAIL_MESSAGE = message

            if ( (self.EMAIL_ATTACHMENT_OPTION_FLAG == False) and (gmail_mode_global == "OAUTH2_Gmail_Mode") ):
                # Create OAUTH2 base64.urlsafe_b64encode of message - NO Attachment - Just the message body.
                self.EMAIL_base64_urlsafe_b64encode_message = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

            elif ( (self.EMAIL_ATTACHMENT_OPTION_FLAG == False) and (gmail_mode_global == "SMTP_Gmail_Mode") ):
                # Create SMTP message - NO Attachment - Just the message body.
                self.EMAIL_SMTP_message = message

            elif self.EMAIL_ATTACHMENT_OPTION_FLAG == True:

                # Start with the Email body as the initial MIME Container Object
                # and then add all the attachments.
                # Note that this initial message container (outer MIME container)
                # for the message applies to both OAUTH2 and SMTP Modes as we
                # prepare to LOOP and add MIME inner containers for attachments.
                self.message_cummulative = self.EMAIL_MESSAGE

                ###############################################################################################
                #
                # Remember each CLASS VARIABLE is a LIST because we have ONE OR MORE Attachment Files ...
                #
                ###############################################################################################

                # self.file_email_attachment_FULL_PATH = LIST OF ATTACHMENT FILEE PATHS.

                file_path_list=[]

                file_path_list = self.file_email_attachment_FULL_PATH

                number_of_files = (len(self.file_email_attachment_FULL_PATH))

                # print("\n")

                # print(".... number_of_files - ***** Now Inside OAUTH2 METHOD *****  =  " + str(number_of_files) + "\n")

                ####################################################################
                #
                # FOR EACH ATTACHMENT FILE ..... PROCESS THE ATTACHMENT .....
                # 
                # Note that since the file full path contains all our information,
                # we can eliminate most of the variables that the dialog method
                # generates and we now just carry forward a LIST of file full paths
                # which is this LIST:  self.file_email_attachment_FULL_PATH
                #
                ####################################################################
                
                for file_count, file_item in enumerate(file_path_list):

                    self.attachment_file_index = file_count

                    the_file_full_path = file_item

                    filename = os.path.basename(the_file_full_path)

                    file_type = filename.split(".")[1]

                    content_type, encoding = mimetypes.guess_type(the_file_full_path)

                    if content_type is None or encoding is not None:
                        content_type = 'application/octet-stream'
                    
                    main_type, sub_type = content_type.split('/', 1)

                    #############################################################################################


                    ################################################################################
                    #
                    # self.file_email_attachment_FILE_TYPE acquired via dialog method:
                    #
                    #     dialog_to_get_file_attachment()
                    #
                    # and the Email attachments button press method (which calls dialog method:
                    #
                    #     email_attachment_option_method()
                    #
                    ################################################################################

                    # initialize the attachment_flow_flag.
                    attachment_flow_flag = "NO_FLOW_SET_YET"

                    if main_type == "application":
                        # print("********   Execute MIMEApplication EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEApplication_FLOW"

                    if main_type == "image":
                        # print("********   Execute MIMEImage EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEImage_FLOW"

                    if main_type == "text":
                        # print("********   Execute MIMEText EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEText_FLOW"

                    if main_type == "audio":
                        # print("********   Execute MIMEAudio EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEAudio_FLOW"

                    if main_type == "video":
                        # print("********   Execute MIMEVideo EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEVideo_FLOW"


                    if attachment_flow_flag == "MIMEApplication_FLOW":
                        self.message_cummulative = self.email_attachment_MIMEApplication()
                    elif attachment_flow_flag == "MIMEImage_FLOW":
                        self.message_cummulative = self.email_attachment_MIMEImage()
                    elif attachment_flow_flag == "MIMEText_FLOW":
                        self.message_cummulative = self.email_attachment_MIMEText()
                    elif attachment_flow_flag == "MIMEAudio_FLOW":
                        self.message_cummulative = self.email_attachment_MIMEAudio()
                    elif attachment_flow_flag == "MIMEVideo_FLOW":
                        self.message_cummulative = self.email_attachment_MIMEVideo()
                    elif attachment_flow_flag == "NO_FLOW_SET_YET":
                        self.message_cummulative = self.email_attachment_MIME_Radio_Button_Select()

#1234567890123456     
                #################################################################################
                #
                # We indent the code above for the loop processing each attached file:
                #
                # for EACH attachment  
                # for file in filenames: 
                #
                # and maintaining the CLASS VARIABLES as accumulating attachment containers
                # to process scenarios with multiple attachments of various MIME Types:
                #
                # For Example:
                #               3  .docx Attachments - MIMEApplication    (Microsoft Word Apps)
                #               3  .xlsx Attachments - MIMEApplication    (Microsoft Excel Apps)
                #               3  .mp3  Attachments - MIMEAudio          (Audio)
                #               3  .mp4  Attachments - MIMEBase           (Video)
                #               3  .ini  Attachments - MIMEText           (Text)
                #
                # Then we encode the self.MIME_message.as_string() below .... 
                # 
                #################################################################################

                #################################################################################
                #
                # NOTE: List_of_Email_Modes = ["OAUTH2_Gmail_Mode", "SMTP_Gmail_Mode"]
                # 
                # gmail_mode_global = "SMTP_Gmail_Mode"  (Default) 
                # 
                #################################################################################

                if ( (self.EMAIL_ATTACHMENT_OPTION_FLAG == True) and (gmail_mode_global == "OAUTH2_Gmail_Mode") ):
                    #############################################################################
                    #
                    # After the ATTACHMENT FILES LOOPS (above) are COMPLETE:
                    # 
                    # This (OAUTH2 Mode) Class Object will then be encoded for OAUTH2 transport below.
                    #
                    self.MIME_message = self.message_cummulative

                    # Create base64.urlsafe_b64encode of message.
                    self.EMAIL_base64_urlsafe_b64encode_message = {'raw': base64.urlsafe_b64encode(self.MIME_message.as_string().encode()).decode()}

                elif ( (self.EMAIL_ATTACHMENT_OPTION_FLAG == True) and (gmail_mode_global == "SMTP_Gmail_Mode") ):
                    #############################################################################
                    #
                    # After the ATTACHMENT FILES LOOPS (above) are COMPLETE: 
                    # 
                    # This (SMTP Mode) Class Object will then be loaded for SMTP transport below.
                    #
                    self.EMAIL_SMTP_message = self.message_cummulative

                #
                # https://developers.google.com/gmail/api/guides/sending
                #  
                # https://developers.google.com/gmail/api/quickstart/python
                #
            if (gmail_mode_global == "OAUTH2_Gmail_Mode"):
#1234567890123456
                try:

                    credentials = self.get_credentials()
                    http = credentials.authorize(httplib2.Http())
                    service = discovery.build('gmail', 'v1', http=http)

                    # SEND the EMAIL message - may have to declare message field below raw ... like str()  int() 
                    self.SendMessage(service, "me", self.EMAIL_base64_urlsafe_b64encode_message)

                    gmail_oauth2_status_global = True

                    complete_email_status_string = " ... OAUTH2  E M A I L   S E N T  ... TIME = " + str(temp_time_string)
                    self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )

                    # Email has been sent, so RESET this Attachments Flag.
                    self.EMAIL_ATTACHMENT_OPTION_FLAG = False

                    # Email has been sent, so RESET this Attachments LIST Class Variable.
                    self.file_email_attachment_FULL_PATH = []


                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                    exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

                    gmail_oauth2_exceptions_status_global = True
                    
                    complete_email_status_string = "OAUTH2  EMAIL NOT SENT : Verify OAUTH2 CREDENTIALS (JSON FILE) - See EMAIL STARTUP USERS MANUAL Button."
                    self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )

                    # open Write_Exception_Logfile() to append logfile to update the logfile items.
                    inst_Write_Exception_Logfile_for_oauth2_send = Write_Exception_Logfile()
                    exception_logging_string_1 = "OAUTH2  E M A I L   N O T   S E N T  :  Verify OAUTH2 CREDENTIALS (JSON FILE). \nSee EMAIL STARTUP USERS MANUAL Button - EXCEPTION DETAILS FOLLOW: " + "\n"
                    exception_logging_string_3 = "\n\n"
                  
                    inst_Write_Exception_Logfile_for_oauth2_send.log_exception(str(exception_logging_string_1) )
                    inst_Write_Exception_Logfile_for_oauth2_send.log_exception(str(exception_logging_string_2) )
                    inst_Write_Exception_Logfile_for_oauth2_send.log_exception(str(exception_logging_string_3) )

                    # logger.error(str(exception_logging_string), exc_info=True)

                    # Temporary command for debug that opens the exception logfile and prints the logfile 
                    # called fullpath_exception_logfile_global and prints the logfile contents acquire using read().
                    # We typically place this print of the exception logfile where exceptions are located for debug.

                    # with open(str(fullpath_exception_logfile_global) ) as exception_file_handle_var:
                    #     print(exception_file_handle_var.read() ) 

            elif (gmail_mode_global == "SMTP_Gmail_Mode"):
#1234567890123456
                #################################################################################
                #
                # NOTE: List_of_Email_Modes = ["OAUTH2_Gmail_Mode", "SMTP_Gmail_Mode"]
                # 
                # gmail_mode_global = "SMTP_Gmail_Mode"  (Default) 
                # 
                #################################################################################
#1234567890123456                     
                #############################################################################
                #
                #  EXECUTE THE SMTP Mode GMAIL SERVER COMMUNICATION SEQUENCE ..... 
                #            
                #  Note: Works with Google Setting: "Enable Less Secure Apps"  
                #        which is less secure than the additional security authentication
                #        process (OAUTH2) that meets google standards without having to
                #        change the Google Setting: "Enable Less Secure Apps"
                #        This SMTP Email Mode is a backup or alternative process
                #        until the USER gets their client_server.json file setup
                #        in their USER DIRECTORY/.credentials/client_server.json location.
                #  
                #############################################################################
              
                message = self.EMAIL_SMTP_message

                complete_email_status_string = ""

                # Send the message via the Gmail SMTP server.
                #
                # Catch Exceptions - smtplib.SMTPException 

                try:
                    
                    mail = smtplib.SMTP("smtp.gmail.com", 587)

                    mail.ehlo()

                    mail.starttls()

                    mail.ehlo()

                    mail.login(str(self.source_email_address), str(self.source_email_password) )

                    mail.sendmail(str(self.source_email_address), TOADDR+CCADDR, message.as_string() )
                    #mail.sendmail(str(self.source_email_address), str(self.destination_1_email_address), str(self.email_content) )
                    #mail.sendmail(str(self.source_email_address), str(self.destination_1_email_address), str(self.email_content) )

                    mail.close()

                    gmail_smtp_status_global = True

                    self.entry_SOURCE_EMAIL_PASSWORD.set("")

                    # CREATE A STATUS TEXTBOX FOR THE *** EMAIL STATUS MESSAGES *** smtplib.SMTPException

                    # UPDATE EMAIL STATUS MESSAGES ....  

                    complete_email_status_string = " ... SMTP  E M A I L   S E N T  ... TIME = " + str(temp_time_string)

                    self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )

                    # Email has been sent, so RESET this Attachments Flag.
                    self.EMAIL_ATTACHMENT_OPTION_FLAG = False

                    # Email has been sent, so RESET this Attachments LIST Class Variable.
                    self.file_email_attachment_FULL_PATH = []

                    #print(str(complete_email_status_string) )
                                        
                    # except smtplib.SMTPException as smtp_exception: 
                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                    exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

                    gmail_smtp_exceptions_status_global = True

                    gmail_smtp_SPECIFIC_EXCEPTION_global = "SMTPError"

                    self.entry_SOURCE_EMAIL_PASSWORD.set("")

                    complete_email_status_string = "SMTP  EMAIL NOT SENT : Set ALLOW LESS SECURE APPS to (ON) - See EMAIL STARTUP USERS MANUAL Button."

                    self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )
                    
                    #print(str(complete_email_status_string) ) 

                    # open Write_Exception_Logfile() to append logfile to update the logfile items.
                    inst_Write_Exception_Logfile_for_smtp_send = Write_Exception_Logfile()
                    exception_logging_string_1 = " ... SMTP  E M A I L   N O T   S E N T  : Set ALLOW LESS SECURE APPS (ON) \nSee EMAIL STARTUP USERS MANUAL Button - EXCEPTION DETAILS FOLLOW: " + "\n"
                    exception_logging_string_3 = "\n\n"
                    
                    inst_Write_Exception_Logfile_for_smtp_send.log_exception(str(exception_logging_string_1) )
                    inst_Write_Exception_Logfile_for_smtp_send.log_exception(str(exception_logging_string_2) )
                    inst_Write_Exception_Logfile_for_smtp_send.log_exception(str(exception_logging_string_3) )

                    # Temporary command for debug that opens the exception logfile and prints the logfile 
                    # called fullpath_exception_logfile_global and prints the logfile contents acquire using read().
                    # We typically place this print of the exception logfile where exceptions are located for debug.

                    #with open(str(fullpath_exception_logfile_global) ) as exception_file_handle_var:
                    #    print(exception_file_handle_var.read() )  

                    # logger.error(str(exception_logging_string), exc_info=True)

            

      def email_attachment_MIMEText(self):
            #####################################################################################
            #
            # if ( (selected_file_type == item) and (main_type == "application") ):
            #
            #####################################################################################
            #
            # EXAMPLE: 
            #
            # content_type = "text/plain"
            # main_type = "text" --------- REQUIRED --------
            # sub_type = "plain"
            # file_type = "txt" 
            #
            # NOTE that message = MIMEMultipart('mixed') and this is the attachment (a jpeg image)
            #
            # Now create the MIME container for the TEXT File:  
            # 
            # Note that for TEXT Files (or TEXT-like file_types), we open in "r" to avoid this error:
            # AttributeError: 'bytes' object has no attribute 'encode'
            #
            ################################################################
            #
            # Load the current state of the self.attachment_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments.  
            message_cummulative = self.message_cummulative

            the_file_full_path = self.file_email_attachment_FULL_PATH[self.attachment_file_index]

            filename = os.path.basename(the_file_full_path)

            file_type = filename.split(".")[1]

            content_type, encoding = mimetypes.guess_type(the_file_full_path)

            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'

            main_type, sub_type = content_type.split('/', 1)

            # print(".... the_file_full_path = " + str(the_file_full_path) )
            # print(".... filename = " + str(filename) )
            # print(".... content_type = " + str(content_type) )
            # print(".... main_type = " + str(main_type) )
            # print(".... sub_type = " + str(sub_type) )
            # print(".... file_type = " + str(file_type) )
            # print(".... encoding = " + str(encoding) )

            fp = open(str(the_file_full_path), 'r')
            attachment = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)

            # Attach to the current state of the self.message_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments.  
            message_cummulative.attach(attachment)
            
            # print(".... attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            return message_cummulative

                

      def email_attachment_MIMEImage(self):
            #####################################################################################
            #
            # if ( (selected_file_type == item) and (main_type == "image") ):
            #
            #####################################################################################
            #
            # EXAMPLE: 
            #
            # NOTE: 
            #
            # content_type = "image/jpeg"
            # main_type = "image" --------- REQUIRED --------
            # sub_type = "jpeg"
            # file_type = "jpg" 
            #
            #
            # NOTE that message = MIMEMultipart('mixed') and this is the attachment (a jpeg image)
            #
            # Now create the MIME container for the JPEG Image:
            #
            ################################################################
            #
            # Load the current state of the self.attachment_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments.  
            message_cummulative = self.message_cummulative

            the_file_full_path = self.file_email_attachment_FULL_PATH[self.attachment_file_index]

            filename = os.path.basename(the_file_full_path)

            file_type = filename.split(".")[1]

            content_type, encoding = mimetypes.guess_type(the_file_full_path)

            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'

            main_type, sub_type = content_type.split('/', 1)

            # print(".... the_file_full_path = " + str(the_file_full_path) )
            # print(".... filename = " + str(filename) )
            # print(".... content_type = " + str(content_type) )
            # print(".... main_type = " + str(main_type) )
            # print(".... sub_type = " + str(sub_type) )
            # print(".... file_type = " + str(file_type) )
            # print(".... encoding = " + str(encoding) )

            fp = open(str(the_file_full_path), 'rb')
            attachment = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)

            # Attach to the current state of the self.message_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments. 
            message_cummulative.attach(attachment)
            
            # print(".... attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            return message_cummulative


                    
      def email_attachment_MIMEApplication(self):
            #####################################################################################
            #
            # if ( (selected_file_type == item) and (main_type == "application") ):
            #
            #####################################################################################
            #
            #   EXAMPLE: 
            #
            #   xlsx produced THIS from content_type, encoding = mimetypes.guess_type(the_file_full_path)
            #
            #   main_type = application   --------- REQUIRED --------
            #
            #   sub_type = vnd.openxmlformats-officedocument.spreadsheetml.sheet
            #
            #       msg['Message-Id'] = make_msgid()
            #       msg['Date'] = formatdate(localtime=True)
            #
            #
            # iPhone Index    .m3u8    application/x-mpegURL
            #
            ################################################################
            #
            # Load the current state of the self.attachment_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments.  
            message_cummulative = self.message_cummulative

            the_file_full_path = self.file_email_attachment_FULL_PATH[self.attachment_file_index]

            filename = os.path.basename(the_file_full_path)

            file_type = filename.split(".")[1]

            content_type, encoding = mimetypes.guess_type(the_file_full_path)

            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'

            main_type, sub_type = content_type.split('/', 1)

            # print(".... the_file_full_path = " + str(the_file_full_path) )
            # print(".... filename = " + str(filename) )
            # print(".... content_type = " + str(content_type) )
            # print(".... main_type = " + str(main_type) )
            # print(".... sub_type = " + str(sub_type) )
            # print(".... file_type = " + str(file_type) )
            # print(".... encoding = " + str(encoding) )

            with open(the_file_full_path, "rb") as xlsx_file_handle:
                attachment = MIMEApplication(xlsx_file_handle.read(),Name=filename)
                attachment.add_header('Content-Disposition', 'attachment', filename=filename)

            # Attach to the current state of the self.message_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments. 
            message_cummulative.attach(attachment)
            
            # print(".... attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            return message_cummulative

          
                  
      def email_attachment_MIMEAudio(self):
            #############################################################################################
            #
            # if ( (selected_file_type == item) and (main_type == "audio") ):
            #
            #############################################################################################
            #
            # Note that AUDIO MIME Types are as follows: 
            #
            # Audio Type	     Extension	        MIME Type or content_type (main_type/sub_type)
            # ----------         ---------          ---------
            # MIDI	              .mid	        audio/mid
            # MIDI  	      .rmi	        audio/mid
            # MP3    	      .mp3	        audio/mpeg
            # Apple AIF           .aif	        audio/x-aiff
            # Apple AIFC	      .aifc	        audio/x-aiff
            # Apple AIFF	      .aiff	        audio/x-aiff
            # MPEGURL             .m3u	        audio/x-mpegurl
            # RealAudio	      .ra	        audio/audio/vnd.rn-realaudio
            # RealAudio	      .ram	        audio/audio/vnd.rn-realaudio
            # WAVE                .wav              audio/vnd.wav 
            # Windows Media Audio .wma              audio/x-ms-wma 
            #
            #############################################################################################
            #
            # Load the current state of the self.attachment_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments.  
            message_cummulative = self.message_cummulative

            the_file_full_path = self.file_email_attachment_FULL_PATH[self.attachment_file_index]

            filename = os.path.basename(the_file_full_path)

            file_type = filename.split(".")[1]

            content_type, encoding = mimetypes.guess_type(the_file_full_path)

            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'

            main_type, sub_type = content_type.split('/', 1)

            # print(".... the_file_full_path = " + str(the_file_full_path) )
            # print(".... filename = " + str(filename) )
            # print(".... content_type = " + str(content_type) )
            # print(".... main_type = " + str(main_type) )
            # print(".... sub_type = " + str(sub_type) )
            # print(".... file_type = " + str(file_type) )
            # print(".... encoding = " + str(encoding) )


            fp = open(str(the_file_full_path), 'rb')
            attachment = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
            
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)

            # Attach to the current state of the self.message_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments. 
            message_cummulative.attach(attachment)
            
            # print(".... attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            return message_cummulative


          
                  
      def email_attachment_MIMEVideo(self):
            #####################################################################################
            #
            # if ( (selected_file_type == item) and (main_type == "video") ):
            #
            #####################################################################################
            #
            # MPEG-4 AVC (Advanced Video Coding), MPEG LAYER 4, MPEG4 video file.
            # H.264 or MPEG-4 Part 10, Advanced Video Coding (MPEG-4 AVC).
            # H.264 is perhaps best known as being one of the video encoding standards
            # for Blu-ray Discs; all Blu-ray Disc players must be able to decode H.264.
            # It is also widely used by streaming internet sources, such as videos from Vimeo,
            # YouTube, and the iTunes Store, web software such as the Adobe Flash Player
            # and Microsoft Silverlight, and also various HDTV broadcasts over terrestrial
            # (Advanced Television Systems Committee standards, ISDB-T, DVB-T or DVB-T2),
            # cable (DVB-C), and satellite (DVB-S and DVB-S2).
            #
            # https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC  
            #
            # https://cloud.google.com/appengine/docs/standard/python/refdocs/modules/google/appengine/api/mail
            #
            # Media Container = video format (video codec) + audio format (audio codec) + subtitle
            #
            # MP4 (.mp4) = MP4 video format (.mpeg4/.h264 video codec) + audio format (mp3, aac, etc) + subtitle
            #
            # ffmpeg -i input.mp4 -vcodec copy -bsf h264_mp4toannexb -an -f h264 output.h264 works for me.
            # Credits stackoverflow.com/a/29410927/2840115
            #
            # ffmpeg -i input.mp4 -vcodec copy -bsf h264_mp4toannexb -an -f h264 output.h264
            #
            # http://www.sample-videos.com/
            #
            ##  attachment = MIMEBase(_maintype="video", _subtype="mp4")
            #
            #
            #############################################################################################
            #
            # Note that VIDEO MIME Types are as follows: 
            #
            # Video Type	     Extension	        MIME Type or content_type (main_type/sub_type)
            # ----------             ---------          ---------
            # Flash	             .flv	        video/x-flv
            # MPEG-4	             .mp4	        video/mp4
            # iPhone Segment         .ts	        video/MP2T
            # 3GP Mobile	     .3gp	        video/3gpp
            # QuickTime	             .mov	        video/quicktime
            # A/V Interleave         .avi	        video/x-msvideo
            # Windows Media	     .wmv	        video/x-ms-wmv
            # MPEG                   .mpeg              video/mpeg
            # Vorbis OGV             .ogv               video/ogg
            # WebM                   .webm              video/webm
            #
            #
            #############################################################################################
            #
            # Load the current state of the self.attachment_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments.  
            message_cummulative = self.message_cummulative

            the_file_full_path = self.file_email_attachment_FULL_PATH[self.attachment_file_index]

            filename = os.path.basename(the_file_full_path)

            file_type = filename.split(".")[1]

            content_type, encoding = mimetypes.guess_type(the_file_full_path)

            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'

            main_type, sub_type = content_type.split('/', 1)

            # print(".... the_file_full_path = " + str(the_file_full_path) )
            # print(".... filename = " + str(filename) )
            # print(".... content_type = " + str(content_type) )
            # print(".... main_type = " + str(main_type) )
            # print(".... sub_type = " + str(sub_type) )
            # print(".... file_type = " + str(file_type) )
            # print(".... encoding = " + str(encoding) )

            attachment = MIMEBase(_maintype=main_type, _subtype=sub_type)

            fp = open(str(the_file_full_path), 'rb')
        
            attachment.set_payload(fp.read())

            fp.close()

            attachment.add_header('Content-Disposition', 'attachment', filename=filename)

            # Attach to the current state of the self.message_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments. 
            message_cummulative.attach(attachment)
            
            # print(".... attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            return message_cummulative




      def email_attachment_MIME_Radio_Button_Select(self):
            ############################################################################################
            #  
            # if ( (selected_file_type != item) and (main_type != "audio", "image", "application") ):
            #
            ############################################################################################
            # 
            # Program Flow Note:
            #
            # Before we get to this Radio Button QUERY, we will see if we can initiate
            # an email attachment MIME sequence with ONLY the main_type used to route us
            # to the MIME attachment Method.
            #
            # However, if there is no file_type match and no main_type produced,
            # then we may choose to display a message to the user that the attached
            # file is UNKNOWN category sothey can SELECT the MIME Attachment Method ...
            #
            # WE NEED A DIALOG BOX TO POP-UP HERE WITH RADIO BUTTONS
            # INSTRUCTION THE USER THAT WE CANNOT RECONGIZE THE file_type
            # or the main_type AND THEY NEED TO SELECT A RADIO BUTTON FOR:
            #
            # 1.  Application Type File 
            #
            # 2.  Image Type File 
            #
            # 3   Audio Type File 
            #
            # 4.  Text or Text-like File
            #
            # 5.  Some Default Sending Method
            #
            #     attachment = MIMEBase(main_type, sub_type)
            #
            ################################################################################

            # print(".... R A D I O    B U T T O N   D E F A U L T   ....  S E L E C T I O N  .... " + "\n")
            # print(".... R A D I O    B U T T O N   D E F A U L T   ....  S E L E C T I O N  .... " + "\n")
            # print(".... R A D I O    B U T T O N   D E F A U L T   ....  S E L E C T I O N  .... " + "\n")

            #
            # Load the current state of the self.attachment_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments.  
            message_cummulative = self.message_cummulative

            the_file_full_path = self.file_email_attachment_FULL_PATH[self.attachment_file_index]

            filename = os.path.basename(the_file_full_path)

            file_type = filename.split(".")[1]

            content_type, encoding = mimetypes.guess_type(the_file_full_path)

            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'

            main_type, sub_type = content_type.split('/', 1)

            # print(".... the_file_full_path = " + str(the_file_full_path) )
            # print(".... filename = " + str(filename) )
            # print(".... content_type = " + str(content_type) )
            # print(".... main_type = " + str(main_type) )
            # print(".... sub_type = " + str(sub_type) )
            # print(".... file_type = " + str(file_type) )
            # print(".... encoding = " + str(encoding) )

            attachment = MIMEBase(_maintype=main_type, _subtype=sub_type)

            fp = open(str(the_file_full_path), 'rb')
            
            attachment.set_payload(fp.read())
            
            fp.close()

            attachment.add_header('Content-Disposition', 'attachment', filename=filename)

            # Attach to the current state of the self.message_cummulative
            # class variable that is being built as these MIME Methods
            # add the Email Attachments. 
            message_cummulative.attach(attachment)
            
            # print(".... attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            return message_cummulative




      def launch_messagebox_when_email_fails(self):
          messagebox.showinfo("Contact Manager Guide ...", \
          "............... ATTENTION: *********** USER ACTION REQUIRED ***********\n\nGMAIL ACCESS METHOD #1 - Must Set Online Switch to ALLOW LESS SECURE APPS:  (SMTP Gmail Mode)\n\nPlease VERIFY that your GMAIL SECURITY SETTINGS SWITCH is set to *** ALLOW LESS SECURE APPS *** as this will enable\nyour Gmail Account to SEND EMAIL from this Contact Management Application.\n\nTo SET the GMAIL SECURITY SWITCH to *** ALLOW LESS SECURE APPS = ON ***, login to your Gmail, and in a new Windows Window Tab, go to this LINK:\n\nhttps://myaccount.google.com/lesssecureapps\n\nand adjust the GMAIL SETTING to ALLOW LESS SECURE APPS = ON.\n\n \nGMAIL ACCESS METHOD #2 -   ADVANCED SECURITY GMAIL:  (OAUTH2 Gmail Mode)\n\nMAY REQUIRE SYSTEM ADMINISTRATOR TO PERFORM ACTIVATION OF THIS GMAIL FEATURE.\n\nTHE PROCEDURE TO ACTIVATE THIS APPLICATION FOR ADVANCED SECURITY OAUTH2 Gmail Mode is - YOU NEED TO LOGIN TO GMAIL AND THEN\nACQUIRE CREDENTIALS TO ALLOW THIS APPLICATION TO USE YOUR GMAIL ACCOUNT TO SEND GMAIL.\nCREDENTIALS ARE ACQUIRED AT THESE LINKS:   IMPORTANT - PLEASE NAME THE CLIENT:  Gmail API Python Quickstart.\n\nhttps://developers.google.com/gmail/api/quickstart/python\n\nhttps://console.developers.google.com/flows/enableapi?apiid=gmail\n\nTO ACQUIRE CREDENTIALS TO USE GMAIL, YOU MUST DOWNLOAD A DOT JSON FILE AND AFTER DOWNLOADING THAT FILE,\nRENAME THE FILE TO client_secret.json and COPY IT TO THE FOLLOWING credentials DIRECTORY PATH:\n\nC:/Users/USERNAME/.credentials/client_secret.json\n\nUpon Sending an EMail you will get a pop-up window asking you to login or approve use of your GMAIL Account by this Contact Management Application.\nThe indication that all is well is this message - The authentication flow has completed.\n\n\n..... Press OK to Continue .....\n\n(After you have completed this REQUIRED USER ACTION.)\n")

          


      
class Person(object):
      """
      This is the Person Class. 

      The Person Class is defined by the statement:  class Person(object): 

      The Person Class has the following attributes:

      self, firstname, lastname, streetadd, citytown, state, zipcode, phonenum, email, website

      """       
      def __init__(self, firstname, lastname, streetadd, citytown, state, zipcode, phonenum, email, website):
            self.firstname = firstname
            self.lastname = lastname
            self.streetadd = streetadd
            self.citytown = citytown
            self.state = state
            self.zipcode = zipcode
            self.phonenum = phonenum
            self.email = email
            self.website = website
            self.person_attribute_list = []
            self.pal = []



      person_attribute_list = ['firstname', 'lastname', 'streetadd', 'citytown', \
                                    'state', 'zipcode', 'phonenum', 'email', 'website']

      pal = ['firstname', 'lastname', 'streetadd', 'citytown', \
                  'state', 'zipcode', 'phonenum', 'email', 'website']

 
      def __name__(self):
            return 
      

      def __str__(self):
            return 'PERSON = ' + '[' + '\n' + 'FIRSTNAME = ' + str(self.firstname) + ', \n' + \
                  'LASTNAME = ' + str(self.lastname) + ', \n' + 'STREETADD = ' + str(self.streetadd) + ', \n' + \
                  'CITYTOWN = ' + str(self.citytown) + ', \n' + 'STATE = ' + str(self.state) + ', \n' + \
                  'ZIPCODE = ' + str(self.zipcode) + ', \n' + 'PHONENUM = ' + str(self.phonenum) + ', \n' + \
                  'EMAIL = ' + str(self.email) + ', \n' + 'WEBSITE = ' + str(self.website) + ', \n' + ']'

      def __repr__(self):
            return '[' + str(self.firstname) + ',' + str(self.lastname) + ',' + str(self.streetadd) + ',' + \
                  str(self.citytown) + ',' + str(self.state) + ',' + str(self.zipcode) + ',' + \
                  str(self.phonenum) + ',' + str(self.email) + ',' + str(self.website) + ',' + ']'
   

      def get_Firstname(self):
            return self.firstname

      def get_Lastname(self):
            return self.lastname

      def get_Streetadd(self):
            return self.streetadd

      def get_Citytown(self):
            return self.citytown

      def get_State(self):
            return self.state

      def get_Zipcode(self):
            return self.zipcode

      def get_Phonenum(self):
            return self.phonenum

      def get_Email(self):
            return self.email

      def get_Website(self):
            return self.website


#########################################################


      def set_Firstname(self, newFirstname):
            self.firstname = newFirstname

      def set_Lastname(self, newLastname):
            self.lastname = new

      def set_Streetadd(self, newStreetadd):
            self.streetadd = newStreetadd

      def set_Citytown(self, newCitytown):
            self.citytown = newCitytown

      def set_State(self, newState):
            self.state = newState

      def set_Zipcode(self, newZipcode):
            self.zipcode = newZipcode

      def set_Phonenum(self, newPhonenum):
            self.phonenum = newPhonenum

      def set_Email(self, newEmail):
            self.email = newEmail

      def set_Website(self, newWebsite):
            self.website = newWebsite
            


##########################################################################################
#
#     C O M I N G   S O O N   . . . 
#
##########################################################################################
#
# IMPLEMENT APPLICATION REMOTE MONITORING to privately communicate status and diagnostic
# data of this deployed Application back to the APPLICATION CLOUD COMMAND CENTER.
#
# Examples are:
#
# 1. Customer IPv4 Address (to establish communication with this deployed Application.
# 2. Number of Contact List (to help design and update customer use cases)
# 3. Application Performance on various host machines.
#  
##########################################################################################
#
# class App_Remote_Monitoring(object):  


      
##########################################################################################
#
# IMPLEMENT APPLICATION STATUS PANEL SCREEN for Contact Management Application Functions.
#  
##########################################################################################
#
class App_Status_Panel(Frame):    #( object)
    def __init__(self, master=None):
        global gmail_oauth2_json_file_test_global
        global gmail_oauth2_status_global
        global gmail_oauth2_exceptions_status_global
        global gmail_oauth2_SPECIFIC_EXCEPTION_global
        global gmail_smtp_allow_less_secure_apps_global
        global gmail_smtp_status_global
        global gmail_smtp_exceptions_status_global
        global gmail_smtp_SPECIFIC_EXCEPTION_global
        global gmail_logged_in_global
        global valid_client_secret_key_format_global
        global cm_dict_file_startup_test_global
        global cm_csv_file_startup_test_global
        global cm_notes_file_startup_test_global
        global OBJECT_toplevel_app_status_panel
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Contact Management COMMAND CENTER WORKSTATION Software - Application Status")
        
        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        OBJECT_toplevel_app_status_panel = self.master
        instance_object_LIST.append(self.master)


        self.Frame1 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame1.grid(row = 0, column = 0, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        self.Frame2 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame2.grid(row = 4, column = 0, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        self.Frame3 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame3.grid(row = 0, column = 1, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        self.Frame4 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame4.grid(row = 4, column = 1, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        self.Frame5 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame5.grid(row = 0, column = 2, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        self.Frame6 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame6.grid(row = 4, column = 2, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        
        self.Frame7 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame7.grid(row = 0, column = 3, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        self.Frame8 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame8.grid(row = 4, column = 3, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        # Instantiate GMAIL OAUTH2 Status Buttons
        for r in range(4):
            self.Frame1.rowconfigure(r, weight=1)    
            self.Frame1.columnconfigure(0, weight=1)

        self.oauth2_json_file_test_Button = Button(self.Frame1, text = "GMAIL OAUTH2\nJSON FILE STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.oauth2_json_file_test_Button.grid(row=0, column=0, padx=5, pady=5)
        self.oauth2_json_file_test_Button.config(borderwidth=5)

        self.oauth2_status_Button = Button(self.Frame1, text = "GMAIL OAUTH2\nOAUTH2 EMAIL SENT", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.oauth2_status_Button.grid(row=1, column=0, padx=5, pady=5)
        self.oauth2_status_Button.config(borderwidth=5)
        
        self.oauth2_exceptions_Button = Button(self.Frame1, text = "GMAIL OAUTH2\nOAUTH2 EMAIL NOT SENT", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.oauth2_exceptions_Button.grid(row=2, column=0, padx=5, pady=5)
        self.oauth2_exceptions_Button.config(borderwidth=5)

        self.oauth2_SPECIFIC_EXCEPTION_NAME_Button = Button(self.Frame1, text = str(gmail_oauth2_SPECIFIC_EXCEPTION_global), \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.grid(row=3, column=0, padx=5, pady=5)
        self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.config(borderwidth=5)

        # Instantiate GMAIL SMTP Status Buttons
        for r in range(4):
            self.Frame2.rowconfigure(r, weight=1)    
            self.Frame2.columnconfigure(0, weight=1)

        self.smtp_allow_less_secure_apps_Button = Button(self.Frame2, text = "GMAIL SMTP SWITCH\nALLOW LESS SECURE APPS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.smtp_allow_less_secure_apps_Button.grid(row=4, column=0, padx=5, pady=5)
        self.smtp_allow_less_secure_apps_Button.config(borderwidth=5)

        self.smtp_status_Button = Button(self.Frame2, text = "GMAIL SMTP\nSMTP EMAIL SENT", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.smtp_status_Button.grid(row=5, column=0, padx=5, pady=5)
        self.smtp_status_Button.config(borderwidth=5)
        
        self.smtp_exceptions_Button = Button(self.Frame2, text = "GMAIL SMTP\nSMTP NOT SENT", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.smtp_exceptions_Button.grid(row=6, column=0, padx=5, pady=5)
        self.smtp_exceptions_Button.config(borderwidth=5)
        
        # NOTE: This is the Exception Name that applies here: "SMTPAuthenticationError"
        
        self.smtp_SPECIFIC_EXCEPTION_NAME_Button = Button(self.Frame2, text = str(gmail_smtp_SPECIFIC_EXCEPTION_global), \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.smtp_SPECIFIC_EXCEPTION_NAME_Button.grid(row=7, column=0, padx=5, pady=5)
        self.smtp_SPECIFIC_EXCEPTION_NAME_Button.config(borderwidth=5)

        # Instantiate Thread Status Buttons  
        for r in range(4):
            self.Frame3.rowconfigure(r, weight=1)    
            self.Frame3.columnconfigure(1, weight=1)

        self.MainThread_THREAD_Button = Button(self.Frame3, text = "MainThread\nTHREAD STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.MainThread_THREAD_Button.grid(row=0, column=1, padx=5, pady=5)
        self.MainThread_THREAD_Button.config(borderwidth=5)

        self.main_Class_cm_app_THREAD_Button = Button(self.Frame3, text = "main_Class_cm_app_THREAD\nTHREAD STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.main_Class_cm_app_THREAD_Button.grid(row=1, column=1, padx=5, pady=5)
        self.main_Class_cm_app_THREAD_Button.config(borderwidth=5)
        
        self.App_Status_Class_THREAD_Button = Button(self.Frame3, text = "App_Status_Class_THREAD\nTHREAD STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.App_Status_Class_THREAD_Button.grid(row=2, column=1, padx=5, pady=5)
        self.App_Status_Class_THREAD_Button.config(borderwidth=5)

        self.client_secret_json_THREAD_Button = Button(self.Frame3, text = "client_secret_json_THREAD\nTHREAD STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.client_secret_json_THREAD_Button.grid(row=3, column=1, padx=5, pady=5)
        self.client_secret_json_THREAD_Button.config(borderwidth=5)

        # IPv4_Address, Dictionary_Database_Count, CSV_Database_Count, Spare_Col_1_Row_7 
        
        for r in range(4):
            bottom_rows = int(r + 4)
            self.Frame4.rowconfigure(bottom_rows, weight=1)    
            self.Frame4.columnconfigure(1, weight=1)

        self.IPv4_Address_Button = Button(self.Frame4, text = "IPv4 Address: " + str(ipv4_address_global), \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.IPv4_Address_Button.grid(row=4, column=1, padx=5, pady=5)
        self.IPv4_Address_Button.config(borderwidth=5)

        self.Dictionary_Database_Count_Button = Button(self.Frame4, text = "# Contact Lists (DICT): " + str(contact_lists_dict_count), \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.Dictionary_Database_Count_Button.grid(row=5, column=1, padx=5, pady=5)
        self.Dictionary_Database_Count_Button.config(borderwidth=5)
        
        self.CSV_Database_Count_Button = Button(self.Frame4, text = "# Contact Lists (CSV): " + str(contact_lists_csv_count), \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.CSV_Database_Count_Button.grid(row=6, column=1, padx=5, pady=5)
        self.CSV_Database_Count_Button.config(borderwidth=5)

        self.Spare_Col_1_Row_7_Button = Button(self.Frame4, text = "CONTACT MANAGEMENT\nSTATUS SPARE", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.Spare_Col_1_Row_7_Button.grid(row=7, column=1, padx=5, pady=5)
        self.Spare_Col_1_Row_7_Button.config(borderwidth=5)


        for r in range(4):
            self.Frame5.rowconfigure(r, weight=1)    
            self.Frame5.columnconfigure(2, weight=1)

            self.status_Button_N = Button(self.Frame5, text = "CONTACT MANAGEMENT\nSTATUS SPARE", width = 26, height = 2, \
                    font=('Helvetica', '12'), background="ivory4", fg="black")
        
            self.status_Button_N.grid(row=r, column=2, padx=5, pady=5)
            self.status_Button_N.config(borderwidth=5)


        for r in range(4):
            bottom_rows = int(r + 4)
            self.Frame6.rowconfigure(bottom_rows, weight=1)    
            self.Frame6.columnconfigure(2, weight=1)

            self.status_Button_N = Button(self.Frame6, text = "CONTACT MANAGEMENT\nSTATUS SPARE", width = 26, height = 2, \
                    font=('Helvetica', '12'), background="ivory4", fg="black")
        
            self.status_Button_N.grid(row=bottom_rows, column=2, padx=5, pady=5)
            self.status_Button_N.config(borderwidth=5)


        for r in range(4):
            self.Frame7.rowconfigure(r, weight=1)    
            self.Frame7.columnconfigure(3, weight=1)

            self.status_Button_N = Button(self.Frame7, text = "CONTACT MANAGEMENT\nSTATUS SPARE", width = 26, height = 2, \
                    font=('Helvetica', '12'), background="ivory4", fg="black")
        
            self.status_Button_N.grid(row=r, column=3, padx=5, pady=5)
            self.status_Button_N.config(borderwidth=5)


        # Instantiate Frame8 to implement status panel reset.
        for r in range(4):
            self.Frame8.rowconfigure(r, weight=1)    
            self.Frame8.columnconfigure(3, weight=1)

        self.contact_management_frame8_spare_1_Button = Button(self.Frame8, text = "CONTACT MANAGEMENT\nSTATUS SPARE", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.contact_management_frame8_spare_1_Button.grid(row=4, column=3, padx=5, pady=5)
        self.contact_management_frame8_spare_1_Button.config(borderwidth=5)

        self.contact_management_frame8_spare_2_Button = Button(self.Frame8, text = "CONTACT MANAGEMENT\nSTATUS SPARE", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.contact_management_frame8_spare_2_Button.grid(row=5, column=3, padx=5, pady=5)
        self.contact_management_frame8_spare_2_Button.config(borderwidth=5)
        
        self.contact_management_frame8_spare_3_Button = Button(self.Frame8, text = "CONTACT MANAGEMENT\nSTATUS SPARE", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.contact_management_frame8_spare_3_Button.grid(row=6, column=3, padx=5, pady=5)
        self.contact_management_frame8_spare_3_Button.config(borderwidth=5)
        
        # NOTE: This is currently the STATUS PANEL RESET BUTTON.
        
        self.status_panel_reset_Button = Button(self.Frame8, text = "STATUS PANEL\nRESET BUTTON", \
            width = 26, height = 2, font=('Helvetica', '12'), background="Midnight Blue", \
            fg="deep sky blue", command = self.reset_status_panel_method)
        self.status_panel_reset_Button.grid(row=7, column=3, padx=5, pady=5)
        self.status_panel_reset_Button.config(borderwidth=5)

        # Setting up a return to main or QUIT Button ....
        # We may want to utilize lift and lower of child windows with respect to the main App screen window
        # instead of self.master.destroy() of the status panel with threads running.
        #
        # NOTE:  self.master.lower()   # It works - It lowers the window.
        #
        # Instead of QUITING or self.master.destroy() we can set a global that requests
        # to lower or lift the window.
        #
        # window.lift()
        # window.lift(otherwin)
        # window.lower()
        # window.lower(otherwin)
        #
        # https://www.daniweb.com/programming/software-development/code/442746/toplevel-child-window-example-tkinter-python
        #
        # win1 = tk.Toplevel(bg='red')
        #
        # def lift_win1():
        #     win1.lift(aboveThis=root)
        #
        # def lower_win1(): 
        #     win1.lower(belowThis=root)  
        #
        # Note: We need to gracefully stop threads when quiting because
        # tkinter exceptions happen when this self.master.destroy() happens:
        #
        # Exception in thread App_Status_Class_THREAD
        # _tkinter.TclError: invalid command name ".!toplevel3.!frame.!button"
        #
        self.tk_lower_status_panel_Button = Button(self.master, text = "MAIN SCREEN", \
        width = 13, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.lower_the_window)
        self.tk_lower_status_panel_Button.grid(row=10, column=0, padx=5, pady=5, sticky = SE)  
        self.tk_lower_status_panel_Button.config(borderwidth=5)


        self.quit_status_panel_Button = Button(self.master, text = "EXIT", \
        width = 7, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.close_windows)
        self.quit_status_panel_Button.grid(row=10, column=0, padx=5, pady=5, sticky = SW)
        self.quit_status_panel_Button.config(borderwidth=5)
        
        
        ##########################################################
        #
        # Create and Initialize Thread Status Variables  
        #
        ##########################################################

        self.thread_list = []
        
        self.MainThread_THREAD_status = False
        self.main_Class_cm_app_THREAD_status = False
        self.App_Status_Class_THREAD_status = False
        self.client_secret_json_THREAD_status = False
            

        huge_font = ('Verdana',32)
        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')


        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        self.master.configure(background=str(config_bg_color_val_global) )

        # call THREAD method to update the app status panel widgets
        self.update_app_status_panel()

        # seperate thread to validate format of client_secret.json file
        self.json_file_validation_thread()



      
    def lower_the_window(self):
          # These CYCLE Buttons have been changed to
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()

   

    def close_windows(self):
        self.master.destroy()

        
        
    def _update_app_status_panel(self): 
        global gmail_oauth2_json_file_test_global
        global gmail_oauth2_status_global
        global gmail_oauth2_exceptions_status_global
        global gmail_oauth2_SPECIFIC_EXCEPTION_global
        global gmail_smtp_allow_less_secure_apps_global
        global gmail_smtp_status_global
        global gmail_smtp_exceptions_status_global
        global gmail_smtp_SPECIFIC_EXCEPTION_global
        global gmail_logged_in_global
        global valid_client_secret_key_format_global
        global cm_dict_file_startup_test_global
        global cm_csv_file_startup_test_global
        global cm_notes_file_startup_test_global

        while 1:

            # set the value of the client_secret.json validation status
            # determined after format validation prcoessing in
            # main() AND also periodically in a continuous thread.

            gmail_oauth2_json_file_test_global = valid_client_secret_key_format_global

            if gmail_oauth2_json_file_test_global == True:
                self.oauth2_json_file_test_Button.config(background="light sea green", fg="black")
            elif gmail_oauth2_json_file_test_global == False:
                self.oauth2_json_file_test_Button.config(background="red2", fg="black")
            elif gmail_oauth2_json_file_test_global == None:
                self.oauth2_json_file_test_Button.config(background="ivory4", fg="black")


            if gmail_oauth2_status_global == True:
                self.oauth2_status_Button.config(background="light sea green", fg="black")
            elif gmail_oauth2_status_global == False:
                self.oauth2_status_Button.config(background="red2", fg="black")
            elif gmail_oauth2_status_global == None:
                self.oauth2_status_Button.config(background="ivory4", fg="black")


            if gmail_oauth2_exceptions_status_global == True:
                self.oauth2_exceptions_Button.config(background="red2", fg="black")
            elif gmail_oauth2_exceptions_status_global == False:
                self.oauth2_exceptions_Button.config(background="ivory4", fg="black")
            elif gmail_oauth2_exceptions_status_global == None:
                self.oauth2_exceptions_Button.config(background="ivory4", fg="black")


            if gmail_oauth2_SPECIFIC_EXCEPTION_global == "Specific_OAUTH2_Exception":
                self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.config(text=str(gmail_oauth2_SPECIFIC_EXCEPTION_global), background="ivory4", fg="black")
            elif gmail_oauth2_SPECIFIC_EXCEPTION_global == "FileNotFoundError":
                self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.config(text=str(gmail_oauth2_SPECIFIC_EXCEPTION_global), background="red2", fg="black")
            elif gmail_oauth2_SPECIFIC_EXCEPTION_global == "ClientSecretValidationError":
                self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.config(text=str(gmail_oauth2_SPECIFIC_EXCEPTION_global), background="red2", fg="black")


            if gmail_smtp_allow_less_secure_apps_global == True:
                self.smtp_allow_less_secure_apps_Button.config(background="light sea green", fg="black")
            elif gmail_smtp_allow_less_secure_apps_global == False:
                self.smtp_allow_less_secure_apps_Button.config(background="red2", fg="black")
            elif gmail_smtp_allow_less_secure_apps_global == None:
                self.smtp_allow_less_secure_apps_Button.config(background="ivory4", fg="black")


            if gmail_smtp_status_global == True:
                self.smtp_status_Button.config(background="light sea green", fg="black")
            elif gmail_smtp_status_global == False:
                self.smtp_status_Button.config(background="red2", fg="black")
            elif gmail_smtp_status_global == None:
                self.smtp_status_Button.config(background="ivory4", fg="black")


            if gmail_smtp_exceptions_status_global == True:
                self.smtp_exceptions_Button.config(background="red2", fg="black")
            elif gmail_smtp_exceptions_status_global == False:
                self.smtp_exceptions_Button.config(background="ivory4", fg="black")
            elif gmail_smtp_exceptions_status_global == None:
                self.smtp_exceptions_Button.config(background="ivory4", fg="black")

            # NOTE: This is the Exception Name that applies here: "SMTPAuthenticationError" 

            if gmail_smtp_SPECIFIC_EXCEPTION_global == "Specific_SMTP_Exception":
                self.smtp_SPECIFIC_EXCEPTION_NAME_Button.config(text=str(gmail_smtp_SPECIFIC_EXCEPTION_global),  background="ivory4", fg="black")
            elif gmail_smtp_SPECIFIC_EXCEPTION_global == "SMTPError":
                self.smtp_SPECIFIC_EXCEPTION_NAME_Button.config(text="SMTPAuthenticationError",  background="red2", fg="black")

            if ipv4_address_global == "IPv4_Address_NOT_SET":
                self.IPv4_Address_Button.config(background="red2", fg="black")
            elif ipv4_address_global != "IPv4_Address_NOT_SET":
                self.IPv4_Address_Button.config(background="light sea green", fg="black")

            if contact_lists_dict_count == "Count_Not_Set":
                self.Dictionary_Database_Count_Button.config(background="red2", fg="black")
            elif contact_lists_dict_count != "Count_Not_Set":
                self.Dictionary_Database_Count_Button.config(background="light sea green", fg="black")

            if contact_lists_csv_count == "Count_Not_Set":
                self.CSV_Database_Count_Button.config(background="red2", fg="black")
            elif contact_lists_csv_count != "Count_Not_Set":
                self.CSV_Database_Count_Button.config(background="light sea green", fg="black")
                
#123456789012 
            # when the status panel tk window, class App_Status_Class, and method update_app_status_panel
            # is active, monitor and display all active threads and display each thread status on status panel. 

            for thread in threading.enumerate():

                # ADD thread.name TO LIST IF thread.name IS NOT IN LIST
                if thread.name not in self.thread_list:
                    self.thread_list.append(thread.name)

                if thread.name == "MainThread":
                    self.MainThread_THREAD_status = True

                elif thread.name == "main_Class_cm_app_THREAD":
                    self.main_Class_cm_app_THREAD_status = True

                elif thread.name == "App_Status_Class_THREAD":
                    self.App_Status_Class_THREAD_status = True

                elif thread.name == "client_secret_json_THREAD":
                    self.client_secret_json_THREAD_status = True

                else:
                    pass

                #print("\n") 
                #print(".... THREAD ENUMERATION - THREAD NAMES: ")
                #print(thread.name)

            #print("\n")
            #print(".... LIST OF THREADS: ")
            #print(self.thread_list)


            if self.MainThread_THREAD_status == True:
                self.MainThread_THREAD_Button.config(background="light sea green", fg="black")
            elif self.MainThread_THREAD_status == False:
                self.MainThread_THREAD_Button.config(background="red2", fg="black")
            elif self.MainThread_THREAD_status == None:
                self.MainThread_THREAD_Button.config(background="ivory4", fg="black")

            if self.main_Class_cm_app_THREAD_status == True:
                self.main_Class_cm_app_THREAD_Button.config(background="light sea green", fg="black")
            elif self.main_Class_cm_app_THREAD_status == False:
                self.main_Class_cm_app_THREAD_Button.config(background="red2", fg="black")
            elif self.main_Class_cm_app_THREAD_status == None:
                self.main_Class_cm_app_THREAD_Button.config(background="ivory4", fg="black")

            if self.App_Status_Class_THREAD_status == True:
                self.App_Status_Class_THREAD_Button.config(background="light sea green", fg="black")
            if self.App_Status_Class_THREAD_status == False:
                self.App_Status_Class_THREAD_Button.config(background="red2", fg="black")
            if self.App_Status_Class_THREAD_status == None:
                self.App_Status_Class_THREAD_Button.config(background="ivory4", fg="black")

            if self.client_secret_json_THREAD_status == True:
                self.client_secret_json_THREAD_Button.config(background="light sea green", fg="black")
            if self.client_secret_json_THREAD_status == False:
                self.client_secret_json_THREAD_Button.config(background="red2", fg="black")
            if self.client_secret_json_THREAD_status == None:
                self.client_secret_json_THREAD_Button.config(background="ivory4", fg="black")

            # Since this method is looping (or threaded) we manage the CPU resources
            # consumed by this method with time.sleep()
            time.sleep(.5)



    ################################################################################
    #
    # Threading INSIDE a Class:   
    #
    # def func_to_be_threaded(self):
    #     threading.Thread(target=self._func_to_be_threaded).start()
    # 
    ################################################################################


    def update_app_status_panel(self):
        global gmail_oauth2_json_file_test_global
        global gmail_oauth2_status_global
        global gmail_oauth2_exceptions_status_global
        global gmail_oauth2_SPECIFIC_EXCEPTION_global
        global gmail_smtp_allow_less_secure_apps_global
        global gmail_smtp_status_global
        global gmail_smtp_exceptions_status_global
        global gmail_smtp_SPECIFIC_EXCEPTION_global
        global gmail_logged_in_global
        global cm_dict_file_startup_test_global
        global cm_csv_file_startup_test_global
        global cm_notes_file_startup_test_global
        
        t_thread_1 = threading.Thread(name="App_Status_Class_THREAD", target=self._update_app_status_panel, daemon=True)
        t_thread_1.start()



    ################################################################################
    #
    # Threading INSIDE a Class: 
    #
    # def func_to_be_threaded(self):
    #     threading.Thread(target=self._func_to_be_threaded).start()
    # 
    ################################################################################

    def _json_file_validation_thread(self):
        global gmail_oauth2_json_file_test_global

        while 1:

            inst_comp_val_json_1 = Compute_Valid_Client_Secret_JSON_Status()
            var_to_get_method_to_run = inst_comp_val_json_1.validate_client_secret_json()

            gmail_oauth2_json_file_test_global = valid_client_secret_key_format_global

            ## print(".... Updated gmail_oauth2_json_file_test_global in THREAD .....")
            ## print(".... gmail_oauth2_json_file_test_global = " + str(gmail_oauth2_json_file_test_global) )

            # Since this method is looping (or threaded) we manage the CPU resources
            # consumed by this method with time.sleep() - updates every two seconds.
            # This controls the frequency of checking the client_secret.json file format
            # which sets the global that is used to update the status panel with
            # client_secret.json EXISTANCE and FORMAT VALID Status. 
            time.sleep(3)
            


    def json_file_validation_thread(self):
        global gmail_oauth2_json_file_test_global
        
        t_thread_json = threading.Thread(name="client_secret_json_THREAD", target=self._json_file_validation_thread, daemon=True)
        t_thread_json.start()
          
        

    def reset_status_panel_method(self):
        global gmail_oauth2_json_file_test_global
        global gmail_oauth2_status_global
        global gmail_oauth2_exceptions_status_global
        global gmail_oauth2_SPECIFIC_EXCEPTION_global
        global gmail_smtp_allow_less_secure_apps_global
        global gmail_smtp_status_global
        global gmail_smtp_exceptions_status_global
        global gmail_smtp_SPECIFIC_EXCEPTION_global
        global valid_client_secret_key_format_global

        self.MainThread_THREAD_status = None
        self.main_Class_cm_app_THREAD_status = None
        self.App_Status_Class_THREAD_status = None

        gmail_oauth2_json_file_test_global = None
        gmail_oauth2_status_global = None
        gmail_oauth2_exceptions_status_global = None
        gmail_oauth2_SPECIFIC_EXCEPTION_global = "Specific_OAUTH2_Exception"
        gmail_smtp_allow_less_secure_apps_global = None
        gmail_smtp_status_global = None
        gmail_smtp_exceptions_status_global = None
        gmail_smtp_SPECIFIC_EXCEPTION_global = "Specific_SMTP_Exception"
        valid_client_secret_key_format_global = None

        ## print(".... gmail_oauth2_json_file_test_global = " + str(gmail_oauth2_json_file_test_global) )
        



#######################################################################################
#        
# IMPLEMENT app_config.ini SETTING ..... 
#
# FIRST CONFIG ITEM - ENTER TKINTER COLOR NAMES IN A TEXTBOX FOR EACH CONFIG ITEM
#
#######################################################################################
#
class Config_Setting_Class(Frame):    #( object)
    def __init__(self, master=None):
        global listbox_color_value_global
        global listbox_color_moment_global
        global request_mainscreen_config_update_global
        global cm_listbox_file_global
        global dict_filename_global
        global master_cm_list_name_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_app_config_ini_global
        global mainscreen_bg_color_val_global
        global mainscreen_bg_color_val_global
        global viewscreen_bg_color_val_global
        global selectlist_bg_color_val_global
        global newlist_bg_color_val_global
        global usermanual_bg_color_val_global
        global config_bg_color_val_global
        global mainscreen_fg_color_val_global
        global viewscreen_fg_color_val_global
        global selectlist_fg_color_val_global
        global newlist_fg_color_val_global
        global usermanual_fg_color_val_global
        global config_fg_color_val_global
        global app_config_ini_val_global
        global app_config_request_global
        global OBJECT_toplevel_config_setting_class
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Contact Management COMMAND CENTER WORKSTATION Software - Application Configuration Command Center")
        #self.master = master
        #self.frame = tk.Frame(self.master)


        for r in range(12):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)


        # FIVE COLUMN FRAMES - EACH WITH TWELVE ROWS
        self.Frame1 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame1.grid(row = 0, column = 0, rowspan = 12, columnspan = 1, sticky = W+E+N+S) 
        self.Frame2 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame2.grid(row = 0, column = 1, rowspan = 12, columnspan = 1, sticky = W+E+N+S)
        self.Frame3 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame3.grid(row = 0, column = 2, rowspan = 12, columnspan = 1, sticky = W+E+N+S)
        self.Frame4 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame4.grid(row = 0, column = 3, rowspan = 12, columnspan = 1, sticky = W+E+N+S)
        self.Frame5 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame5.grid(row = 0, column = 4, rowspan = 12, columnspan = 1, sticky = W+E+N+S)


        huge_font = ('Verdana',32)
        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        OBJECT_toplevel_config_setting_class = self.master
        instance_object_LIST.append(self.master)

###########################################################################################
        
        self.master.configure(background=str(config_bg_color_val_global) )
        

        self.select_file_button = Button(self.master, text = "C L I C K   H E R E\nto SAVE your Settings.", width=18,height=2, font=('Helvetica', '18'), background="goldenrod", fg="black")

        self.select_file_button.grid(row=0, column=0, sticky = NW)
        self.select_file_button.bind("<Button-1>", self.get_Config_Textbox_Settings)
        

        self.select_listbox_color_button = Button(self.Frame4, text = "SELECT COLOR from LISTBOX,\nthen TOUCH BUTTONS to the LEFT\nto SET corresponding SCREEN COLOR", \
            width=32,height=3, font=('Helvetica', '12'), background="goldenrod", fg="black")
            
        self.select_listbox_color_button.grid(row=0, column=3, sticky = N)


        self.show_instructions1_button = Button(self.master, text = "\nBackground", width=15,height=2, font=('Helvetica', '18'), background="turquoise4", fg="black")
            
        self.show_instructions1_button.grid(row=0, column=1, sticky = NW)

        self.show_instructions2_button = Button(self.master, text = "\nForeground", width=15,height=2, font=('Helvetica', '18'), background="turquoise4", fg="black")
            
        self.show_instructions2_button.grid(row=0, column=2, sticky = NW)

        
        #
        # LOWER WINDOW BUTTON. 
        # 
        self.lower_window_Button = Button(self.master, text = "MAIN SCREEN", width = 15, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5, \
            activebackground="cyan", activeforeground="blue2", command = self.lower_WINDOW)

        self.lower_window_Button.grid(row=8, column=0, sticky = E)

        #
        # EXIT BUTTON.  
        # 
        self.quitButton = Button(self.master, text = "EXIT", width = 7, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5, \
            activebackground="cyan", activeforeground="blue2", command = self.exit_Handler)

        self.quitButton.grid(row=8, column=0, sticky = W)

        
############################################################################################### 
 
        # LABEL FOR NEW MAINSCREEN BACKGROUND
        self.label_main_bg = "MAIN SCREEN:"
        self.my_main_bg_label = Label(self.master, text = self.label_main_bg, font=large_font)
        self.my_main_bg_label.config(height = 1, width=15, anchor = E)
        self.my_main_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_main_bg_label.grid(row=1, column=0, sticky = N)

        # LABEL FOR VIEW CONTACTS BACKGROUND
        self.label_view_bg = "VIEW CONTACTS:"
        self.my_view_bg_label = Label(self.master, text = self.label_view_bg, font=large_font)
        self.my_view_bg_label.config(height = 1, width=15, anchor = E)
        self.my_view_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_view_bg_label.grid(row=2, column=0, sticky = N)

        # LABEL FOR SELECT LIST BACKGROUND
        self.label_select_bg = "SELECT LIST:"
        self.my_select_bg_label = Label(self.master, text = self.label_select_bg, font=large_font)
        self.my_select_bg_label.config(height = 1, width=15, anchor = E)
        self.my_select_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_select_bg_label.grid(row=3, column=0, sticky = N)

        # LABEL FOR NEW LIST BACKGROUND
        self.label_newlist_bg = "NEW LIST:"
        self.my_newlist_bg_label = Label(self.master, text = self.label_newlist_bg, font=large_font)
        self.my_newlist_bg_label.config(height = 1, width=15, anchor = E)
        self.my_newlist_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_newlist_bg_label.grid(row=4, column=0, sticky = N)

        # LABEL FOR USERS MANUAL BACKGROUND
        self.label_user_bg = "USERS MANUAL:"
        self.my_user_bg_label = Label(self.master, text = self.label_user_bg, font=large_font)
        self.my_user_bg_label.config(height = 1, width=15, anchor = E)
        self.my_user_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_user_bg_label.grid(row=5, column=0, sticky = N)

        # LABEL FOR APP CONFIG BACKGROUND
        self.label_conf_bg = "APP CONFIG:"
        self.my_conf_bg_label = Label(self.master, text = self.label_conf_bg, font=large_font)
        self.my_conf_bg_label.config(height = 1, width=15, anchor = E)
        self.my_conf_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_conf_bg_label.grid(row=6, column=0, sticky = N)

############################################################################################### 

        ##########################################################################################
        #
        # When the button is pressed, the listbox_color_moment_global selected will change
        # the color of the button widget and generate the color setting variables and globals
        # that gets saved to update the config and the corresponding screen's: 
        #   
        # 1. background   2. foreground   3. buttons   4. entry/text/list boxes
        # 
        # This will be implemented with the .config function located within the
        #
        # listbox_color_moment_global selection method: OnListBoxSelect(self, event)
        #
        ##########################################################################################
        
        self.main_bg_color_moment_button = Button(self.master, text = str(mainscreen_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(mainscreen_bg_color_val_global))
        self.main_bg_color_moment_button.grid(row=1, column=1, sticky = NW)
        self.main_bg_color_moment_button.bind("<Button-1>", self.main_bg_set_color_variables)

        self.view_bg_color_moment_button = Button(self.master, text = str(viewscreen_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(viewscreen_bg_color_val_global))
        self.view_bg_color_moment_button.grid(row=2, column=1, sticky = NW)
        self.view_bg_color_moment_button.bind("<Button-1>", self.view_bg_set_color_variables)

        self.select_bg_color_moment_button = Button(self.master, text = str(selectlist_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(selectlist_bg_color_val_global))
        self.select_bg_color_moment_button.grid(row=3, column=1, sticky = NW)
        self.select_bg_color_moment_button.bind("<Button-1>", self.select_bg_set_color_variables)

        self.newlist_bg_color_moment_button = Button(self.master, text = str(newlist_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(newlist_bg_color_val_global))
        self.newlist_bg_color_moment_button.grid(row=4, column=1, sticky = NW)
        self.newlist_bg_color_moment_button.bind("<Button-1>", self.newlist_bg_set_color_variables)

        self.usermanual_bg_color_moment_button = Button(self.master, text = str(usermanual_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(usermanual_bg_color_val_global))
        self.usermanual_bg_color_moment_button.grid(row=5, column=1, sticky = NW)
        self.usermanual_bg_color_moment_button.bind("<Button-1>", self.usermanual_bg_set_color_variables)

        self.config_bg_color_moment_button = Button(self.master, text = str(config_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(config_bg_color_val_global))
        self.config_bg_color_moment_button.grid(row=6, column=1, sticky = NW)
        self.config_bg_color_moment_button.bind("<Button-1>", self.config_bg_set_color_variables)

        ##########################################################################################

        self.main_fg_color_moment_button = Button(self.master, text = str(mainscreen_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(mainscreen_fg_color_val_global))
        self.main_fg_color_moment_button.grid(row=1, column=2, sticky = NW)
        self.main_fg_color_moment_button.bind("<Button-1>", self.main_fg_set_color_variables)

        self.view_fg_color_moment_button = Button(self.master, text = str(viewscreen_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(viewscreen_fg_color_val_global))
        self.view_fg_color_moment_button.grid(row=2, column=2, sticky = NW)
        self.view_fg_color_moment_button.bind("<Button-1>", self.view_fg_set_color_variables)

        self.select_fg_color_moment_button = Button(self.master, text = str(selectlist_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(selectlist_fg_color_val_global))
        self.select_fg_color_moment_button.grid(row=3, column=2, sticky = NW)
        self.select_fg_color_moment_button.bind("<Button-1>", self.select_fg_set_color_variables)

        self.newlist_fg_color_moment_button = Button(self.master, text = str(newlist_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(newlist_fg_color_val_global))
        self.newlist_fg_color_moment_button.grid(row=4, column=2, sticky = NW)
        self.newlist_fg_color_moment_button.bind("<Button-1>", self.newlist_fg_set_color_variables)

        self.usermanual_fg_color_moment_button = Button(self.master, text = str(usermanual_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(usermanual_fg_color_val_global))
        self.usermanual_fg_color_moment_button.grid(row=5, column=2, sticky = NW)
        self.usermanual_fg_color_moment_button.bind("<Button-1>", self.usermanual_fg_set_color_variables)

        self.config_fg_color_moment_button = Button(self.master, text = str(config_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(config_fg_color_val_global))
        self.config_fg_color_moment_button.grid(row=6, column=2, sticky = NW)
        self.config_fg_color_moment_button.bind("<Button-1>", self.config_fg_set_color_variables)

        ##########################################################################################

        self.seeColors = Text(self.Frame4, width=18, height=4)
        self.seeColors.grid(row=12, column=3, sticky = SW)
        self.seeColors.config(borderwidth=12, font=('Helvetica', '20'), background="light sea green")

        self.lbox = Listbox(self.Frame4, width=18, height=12)
        self.lbox.grid(row=10, column=3, sticky = SW)
        self.lbox.config(borderwidth=10, font=('Helvetica', '20'), background="light sea green", fg = "gray18") 
        self.lbox.bind("<<ListboxSelect>>", self.OnListBoxSelect)

        # create a Scrollbar and associate it with self.lbox 
        self.scrollb = Scrollbar(self.Frame4, command=self.lbox.yview)
        self.scrollb.grid(row=10, column=3, sticky='NSE')
        self.lbox['yscrollcommand'] = self.scrollb.set

        List_of_Colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
            'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
            'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
            'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
            'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
            'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
            'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
            'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
            'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
            'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
            'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
            'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
            'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
            'indian red', 'saddle brown', 'sandy brown',
            'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
            'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
            'pale violet red', 'maroon', 'medium violet red', 'violet red',
            'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
            'thistle', 'snow2', 'snow3',
            'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
            'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
            'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
            'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
            'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
            'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
            'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
            'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
            'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
            'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
            'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
            'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
            'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
            'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
            'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
            'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
            'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
            'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
            'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
            'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
            'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
            'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
            'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
            'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
            'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
            'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
            'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
            'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
            'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
            'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
            'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
            'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
            'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
            'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
            'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
            'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
            'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
            'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
            'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
            'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
            'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
            'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
            'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
            'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
            'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
            'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
            'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
            'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
            'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
            'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
            'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
            'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
            'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
            'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
            'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
            'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
            'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


        # Load all COLORS in LIST into the LISTBOX 
        results = []
        reversed_list = []

        # reverse the list so grays are not at beginning of LISTBOX
        reversed_list = list(reversed(List_of_Colors))

        for color in reversed_list:
              results.append(color)
              
        for color_item in results:
              self.lbox.insert(0, color_item)
              



    def lower_WINDOW(self):
          # These CYCLE Buttons have been changed to
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()



    def exit_Handler(self):
        self.master.destroy()

           
              
    def main_bg_set_color_variables(self, event):
          global mainscreen_bg_color_val_global
          global request_mainscreen_config_update_global
          mainscreen_bg_color_val_global = listbox_color_moment_global
          self.main_bg_color_moment_button.config(text = str(mainscreen_bg_color_val_global), bg = str(mainscreen_bg_color_val_global) )
          #
          # UPDATE MAINSCREEN BACKGROUND COLOR:
          #
          # Set this request_mainscreen_config_update_global GLOBAL to True 
          # to enable the IF statement in the main THREAD to perform
          # the command:
          #
          #      cm_app.config(background = str(mainscreen_bg_color_val_global)
          #
          request_mainscreen_config_update_global = True
          #
          ##########################################################################


    def view_bg_set_color_variables(self, event):
          global viewscreen_bg_color_val_global
          viewscreen_bg_color_val_global = listbox_color_moment_global
          self.view_bg_color_moment_button.config(text = str(viewscreen_bg_color_val_global), bg = str(viewscreen_bg_color_val_global) )
          

    def select_bg_set_color_variables(self, event):
          global selectlist_bg_color_val_global
          selectlist_bg_color_val_global = listbox_color_moment_global
          self.select_bg_color_moment_button.config(text = str(selectlist_bg_color_val_global), bg = str(selectlist_bg_color_val_global) )
          
    
    def newlist_bg_set_color_variables(self, event):
          global newlist_bg_color_val_global
          newlist_bg_color_val_global = listbox_color_moment_global
          self.newlist_bg_color_moment_button.config(text = str(newlist_bg_color_val_global), bg = str(newlist_bg_color_val_global) )
          

    def usermanual_bg_set_color_variables(self, event):
          global usermanual_bg_color_val_global
          usermanual_bg_color_val_global = listbox_color_moment_global
          self.usermanual_bg_color_moment_button.config(text = str(usermanual_bg_color_val_global), bg = str(usermanual_bg_color_val_global) )
          
    
    def config_bg_set_color_variables(self, event):
          global config_bg_color_val_global
          config_bg_color_val_global = listbox_color_moment_global
          self.config_bg_color_moment_button.config(text = str(config_bg_color_val_global), bg = str(config_bg_color_val_global) )


    def main_fg_set_color_variables(self, event):
          global mainscreen_fg_color_val_global
          mainscreen_fg_color_val_global = listbox_color_moment_global
          self.main_fg_color_moment_button.config(text = str(mainscreen_fg_color_val_global), bg = str(mainscreen_fg_color_val_global) )


    def view_fg_set_color_variables(self, event):
          global viewscreen_fg_color_val_global
          viewscreen_fg_color_val_global = listbox_color_moment_global
          self.view_fg_color_moment_button.config(text = str(viewscreen_fg_color_val_global), bg = str(viewscreen_fg_color_val_global) )
          

    def select_fg_set_color_variables(self, event):
          global selectlist_fg_color_val_global
          selectlist_fg_color_val_global = listbox_color_moment_global
          self.select_fg_color_moment_button.config(text = str(selectlist_fg_color_val_global), bg = str(selectlist_fg_color_val_global) )
          
    
    def newlist_fg_set_color_variables(self, event):
          global newlist_fg_color_val_global
          newlist_fg_color_val_global = listbox_color_moment_global
          self.newlist_fg_color_moment_button.config(text = str(newlist_fg_color_val_global), bg = str(newlist_fg_color_val_global) )
          

    def usermanual_fg_set_color_variables(self, event):
          global usermanual_fg_color_val_global
          usermanual_fg_color_val_global = listbox_color_moment_global
          self.usermanual_fg_color_moment_button.config(text = str(usermanual_fg_color_val_global), bg = str(usermanual_fg_color_val_global) )
          
    
    def config_fg_set_color_variables(self, event):
          global config_fg_color_val_global
          config_fg_color_val_global = listbox_color_moment_global
          self.config_fg_color_moment_button.config(text = str(config_fg_color_val_global), bg = str(config_fg_color_val_global) )
          


    def OnListBoxSelect(self, event):
        global listbox_file_capture_global
        global listbox_color_moment_global
        listbox_file_capture_global = "False"
        widget = event.widget
        selection = widget.curselection()
        listbox_color_value = widget.get(selection[0])
        listbox_color_moment_global = widget.get(selection[0])
        selection_value_tuple = [selection, listbox_color_value]
        # Change the COLOR in the Text Widget for the Viewer
        self.seeColors.config(background=str(listbox_color_value) )
        return listbox_color_value


 

    #########################################################################################
    #
    #  Use the command = func_set_xxxx_bg_textbox feature in Options Menu to acquire the
    #  xxxx_opt_menu_bg_select StringVar with the selected COLOR, then use the
    #  self.entry_xxxx_bg.set(str(xxxxscreen_bg_color_val_global) ) to set the xxxx TEXTBOX
    #  to the COLOR string value, and finally, a ways below, in get_Config_Textbox_Settings,
    #  use the self.my_xxxx_screen_bg_entry.get() to set the new COLOR value for both the
    #  GLOBAL and the app_config.ini value.   
    # 
    ######################################################################################### 
          
    def func_set_main_bg_global(self, main_opt_menu_bg_select):
          global mainscreen_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_main_bg_global feature in Options Menu to get   C O L O R  =  " + str(main_opt_menu_bg_select) )
          mainscreen_bg_color_val_global = str(main_opt_menu_bg_select)

          
    def func_set_view_bg_global(self, view_opt_menu_bg_select):
          global viewscreen_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_view_bg_global feature in Options Menu to get   C O L O R  =  " + str(view_opt_menu_bg_select) )
          viewscreen_bg_color_val_global = str(view_opt_menu_bg_select)
           

    def func_set_select_bg_global(self, select_opt_menu_bg_select):
          global selectlist_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_select_bg_global feature in Options Menu to get   C O L O R  =  " + str(select_opt_menu_bg_select) )
          selectlist_bg_color_val_global = str(select_opt_menu_bg_select)


    def func_set_newlist_bg_global(self, newlist_opt_menu_bg_select):
          global newlist_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_newlist_bg_global feature in Options Menu to get   C O L O R  =  " + str(newlist_opt_menu_bg_select) )
          newlist_bg_color_val_global = str(newlist_opt_menu_bg_select)


    def func_set_usermanual_bg_global(self, usermanual_opt_menu_bg_select):
          global usermanual_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_usermanual_bg_global feature in Options Menu to get   C O L O R  =  " + str(usermanual_opt_menu_bg_select) )
          usermanual_bg_color_val_global = str(usermanual_opt_menu_bg_select)


    def func_set_config_bg_global(self, config_opt_menu_bg_select):
          global config_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_config_bg_global feature in Options Menu to get   C O L O R  =  " + str(config_opt_menu_bg_select) )
          config_bg_color_val_global = str(config_opt_menu_bg_select)
          

#########################################################################################

    def func_set_main_fg_global(self, main_opt_menu_fg_select):
          global mainscreen_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_main_fg_global feature in Options Menu to get   C O L O R  =  " + str(main_opt_menu_fg_select) )
          mainscreen_fg_color_val_global = str(main_opt_menu_fg_select)

    def func_set_view_fg_global(self, view_opt_menu_fg_select):
          global viewscreen_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_view_fg_global feature in Options Menu to get   C O L O R  =  " + str(view_opt_menu_fg_select) )
          viewscreen_fg_color_val_global = str(view_opt_menu_fg_select)

    def func_set_select_fg_global(self, select_opt_menu_fg_select):
          global selectlist_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_select_fg_global feature in Options Menu to get   C O L O R  =  " + str(select_opt_menu_fg_select) )
          selectlist_fg_color_val_global = str(select_opt_menu_fg_select)

    def func_set_newlist_fg_global(self, newlist_opt_menu_fg_select):
          global newlist_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_newlist_fg_global feature in Options Menu to get   C O L O R  =  " + str(newlist_opt_menu_fg_select) )
          newlist_fg_color_val_global = str(newlist_opt_menu_fg_select)

    def func_set_newlist_fg_global(self, newlist_opt_menu_fg_select):
          global newlist_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_newlist_fg_global feature in Options Menu to get   C O L O R  =  " + str(newlist_opt_menu_fg_select) )
          newlist_fg_color_val_global = str(newlist_opt_menu_fg_select)

    def func_set_usermanual_fg_global(self, usermanual_opt_menu_fg_select):
          global usermanual_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_usermanual_fg_global feature in Options Menu to get   C O L O R  =  " + str(usermanual_opt_menu_fg_select) )
          usermanual_fg_color_val_global = str(usermanual_opt_menu_fg_select)

    def func_set_config_fg_global(self, config_opt_menu_fg_select):
          global config_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_config_fg_global feature in Options Menu to get   C O L O R  =  " + str(config_opt_menu_fg_select) )
          config_fg_color_val_global = str(config_opt_menu_fg_select)

          
#########################################################################################

     

    def get_Config_Textbox_Settings(self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global master_cm_list_name_global
        global listbox_file_capture_global
        global cm_textbox_newfile_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_app_config_ini_global
        global mainscreen_bg_color_val_global
        global viewscreen_bg_color_val_global
        global selectlist_bg_color_val_global
        global newlist_bg_color_val_global
        global usermanual_bg_color_val_global
        global config_bg_color_val_global
        global mainscreen_fg_color_val_global
        global viewscreen_fg_color_val_global
        global selectlist_fg_color_val_global
        global newlist_fg_color_val_global
        global usermanual_fg_color_val_global
        global config_fg_color_val_global
        global app_config_ini_val_global 
        global app_config_request_global
        ###########################################################################
        #
        # This button command gets the CONFIG VALUE from the respective
        # Config_Setting_Class OptionsMenu Selections, already upadted as
        # the corresponding CONFIG VALUE GLOBAL and then updates the
        # CONFIG INI FILE called app_config.ini
        #
        ###########################################################################
        #
        #   ******* setting NEW config settings get written here *******
        #   *******    triggered by config button    ******* 
        #
        ###########################################################################
        #
        # config settings here come from OptionsMenu Selections above where
        # the corresponding global has been set from the OptionsMenu Selections.
        #
        ###########################################################################

        # #print("\n")
        # #print(".... Verify NEW SETTING of mainscreen_bg_color_val_global =  " + str(mainscreen_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of viewscreen_bg_color_val_global =  " + str(viewscreen_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of selectlist_bg_color_val_global =  " + str(selectlist_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of newlist_bg_color_val_global =  " + str(newlist_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of usermanual_bg_color_val_global =  " + str(usermanual_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of config_bg_color_val_global =  " + str(config_bg_color_val_global) )
        # #print("\n")
        # #print(".... Verify NEW SETTING of mainscreen_fg_color_val_global =  " + str(mainscreen_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of viewscreen_fg_color_val_global =  " + str(viewscreen_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of selectlist_fg_color_val_global =  " + str(selectlist_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of newlist_fg_color_val_global =  " + str(newlist_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of usermanual_fg_color_val_global =  " + str(usermanual_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of config_fg_color_val_global =  " + str(config_fg_color_val_global) )
        # #print("\n")
        

        ########################################################################################## 
        #
        # Double Check path to app_config.ini 
        #
        # #print(".... CHECK PATH of fullpath_app_config_ini_global =  " + str(fullpath_app_config_ini_global) )
        # #print("\n")
        #
        # instantiate ConfigParser()
        config = ConfigParser()
        #
        # add new app_config.ini file data settings   
        # and re-write the app_config.ini file
        #
        config.add_section("MAIN_SCREEN_COLOR") 
        config.set("MAIN_SCREEN_COLOR", "mainscreen_bg_color_val", str(mainscreen_bg_color_val_global) )
        config.set("MAIN_SCREEN_COLOR", "mainscreen_fg_color_val", str(mainscreen_fg_color_val_global) )

        config.add_section("VIEW_SCREEN_COLOR") 
        config.set("VIEW_SCREEN_COLOR", "viewscreen_bg_color_val", str(viewscreen_bg_color_val_global) )
        config.set("VIEW_SCREEN_COLOR", "viewscreen_fg_color_val", str(viewscreen_fg_color_val_global) )

        config.add_section("SELECT_SCREEN_COLOR")
        config.set("SELECT_SCREEN_COLOR", "selectlist_bg_color_val", str(selectlist_bg_color_val_global) )
        config.set("SELECT_SCREEN_COLOR", "selectlist_fg_color_val", str(selectlist_fg_color_val_global) )

        config.add_section("NEWLIST_SCREEN_COLOR")
        config.set("NEWLIST_SCREEN_COLOR", "newlist_bg_color_val", str(newlist_bg_color_val_global) )
        config.set("NEWLIST_SCREEN_COLOR", "newlist_fg_color_val", str(newlist_fg_color_val_global) )
                   
        config.add_section("USERMANUAL_SCREEN_COLOR")
        config.set("USERMANUAL_SCREEN_COLOR", "usermanual_bg_color_val", str(usermanual_bg_color_val_global) )
        config.set("USERMANUAL_SCREEN_COLOR", "usermanual_fg_color_val", str(usermanual_fg_color_val_global) )
        
        config.add_section("CONFIG_SCREEN_COLOR")
        config.set("CONFIG_SCREEN_COLOR", "config_bg_color_val", str(config_bg_color_val_global) )
        config.set("CONFIG_SCREEN_COLOR", "config_fg_color_val", str(config_fg_color_val_global) )
                   

        # save app_config.ini file 
        with open(str(fullpath_app_config_ini_global), 'w') as configfile:
             config.write(configfile)

        # wait one fifth of a second before closing window
        time.sleep(.2)

        # pass executive window control back to App() Class and
        # create and update a CONFIG PROCESSING REQUEST GLOBAL to utilize
        # the THREAD in main() and the CONFIG PROCESSING REQUEST GLOBAL to
        # re-configure the App() Class Object with these new config settings.
        app_config_request_global = True

        # write a new logfile to update the logfile items upon Config updates.
        inst_Write_Main_Logfile_upon_config = Write_Main_Logfile()
        inst_Write_Main_Logfile_upon_config.write_update_logfile()

        self.master.destroy()


            

# SYSTEM ADMINISTRATION and DATABASE INFORMATION CLASS 
#
# Class: System_Admin_Info(Frame)
#
class System_Admin_Info(Frame):   # (object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global usermanual_bg_color_val_global
        global usermanual_fg_color_val_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_fn_cm_sw_app_logfile_global
        global OBJECT_toplevel_system_admin_info
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        
        # self.master = master
        # self.frame = tk.Frame(self.master)

        # self.master = master
        # self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice 
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above 
        # self.master.geometry("900x550")

        OBJECT_toplevel_system_admin_info = self.master
        instance_object_LIST.append(self.master)
        
        self.master.configure(background=str(usermanual_bg_color_val_global) )

        self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - SYSTEM ADMINISTRATION and DATABASE INFORMATION")

        #
        # EXIT BUTTON.    
        # 
        self.quitButton = Button(self.master, text = "EXIT", width = 7, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5, \
            activebackground="cyan", activeforeground="blue2", command = self.exit_Handler)

        self.quitButton.grid(row=3, column=0, sticky = W)

        #
        # LOWER WINDOW BUTTON. 
        # 
        self.lower_window_Button = Button(self.master, text = "MAIN SCREEN", width = 15, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5, \
            activebackground="cyan", activeforeground="blue2", command = self.lower_WINDOW)

        self.lower_window_Button.grid(row=3, column=0) 

        List_of_Sys_Admin_Modes = ["System Administration Menu", "System Administration Data", "IPCONFIG", "NETSTAT (wait 10 seconds)", "Exceptions Logfile"]

        mode_select_sysadmin_menu_global = "System Administration Menu"

        self.mode_select_sysadmin_opt_menu_select = StringVar()
        self.mode_select_sysadmin_opt_menu_select.set(str(mode_select_sysadmin_menu_global) )   # initialize OptionMenu 
        self.mode_select_sysadmin_optionsmenu_inst = OptionMenu(self.master, self.mode_select_sysadmin_opt_menu_select, \
        *List_of_Sys_Admin_Modes, command=self.set_mode_select_sysadmin_menu_global)
        self.mode_select_sysadmin_optionsmenu_inst.grid(row=3, column=0, sticky = E)
        self.mode_select_sysadmin_optionsmenu_inst.config(borderwidth=5, background="light sea green", font=('Helvetica', 14 ) )

        menu_mode_select_sysadmin = self.mode_select_sysadmin_optionsmenu_inst.nametowidget(self.mode_select_sysadmin_optionsmenu_inst.menuname) 
        menu_mode_select_sysadmin.configure(font=("Helvetica", 18), bg="light sea green")

        ###############################################################################
        #
        # Programming Note: 
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Big Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        # 
        ###############################################################################

 
        # TEXTBOX to insert TITLE at top of window and identify
        # the current Contact List File - cm_listbox_file_global  

        self.title_1_text_box = Text(self.master, width=94, height = 1)
        self.title_1_text_box.grid(row=0, column=0, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '18'), \
            fg = str(usermanual_fg_color_val_global), background=str(usermanual_bg_color_val_global) )
        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_1_TITLE = "      SYSTEM ADMINISTRATION    .....    DATABASE INFORMATION   "

        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        
        # TEXTBOX to view the USERS MANUAL and SYSTEM ADMIN INFO

        self.view_text_box = Text(self.master, width=137, height = 30)
        self.view_text_box.grid(row=2, column=0, sticky = W)
        self.view_text_box.config(borderwidth=10, font=('Helvetica', '12'), \
            fg = str(usermanual_fg_color_val_global), background=str(usermanual_bg_color_val_global) )
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        # create a Scrollbar and associate it with self.view_text_box 
        self.scrollb = Scrollbar(self.master, command=self.view_text_box.yview)
        self.scrollb.grid(row=2, column=1, sticky='NSW')
        self.view_text_box['yscrollcommand'] = self.scrollb.set

        # INSERT LOGFILE DATA LINES into TEXTBOX to VIEW the TEXTBOX
        # after loading the current LOGFILE using the full path name:
        # fullpath_fn_cm_sw_app_logfile_global
        
        self.textFile = open(fullpath_fn_cm_sw_app_logfile_global, 'r')

        with open(str(fullpath_fn_cm_sw_app_logfile_global) ) as fin:
             for line in fin:
                 self.view_text_box.insert(END, line)
        
        # Disable TEXT WIDGET for Insert 
        self.view_text_box.config(state=DISABLED)  

        ############################################################################### 
        #
        # Programming Note:     ( Reference to the code above )   
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Big Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        #
        ###############################################################################


#1234
    #     
    ######################################################################################
    #
    def set_mode_select_sysadmin_menu_global(self, mode_select_sysadmin_opt_menu_select):
        global mode_select_sysadmin_menu_global

        # Set the GLOBAL for the newly selected mode_select_sysadmin_menu_global, choices are currently:  
        # "System Administration Menu", "System Administration Data", "IPCONFIG", "NETSTAT (wait 10 seconds)", "Exceptions Logfile"
        #
        mode_select_sysadmin_menu_global = str(mode_select_sysadmin_opt_menu_select)

        if (mode_select_sysadmin_menu_global == "System Administration Menu"):

            pass

        elif (mode_select_sysadmin_menu_global == "System Administration Data"):

            # Execute updatedSYS ADMIN CLASS FILE WRITE and then display results to system administration TEXT BOX WIDGET.
            self.display_sys_admin_data()

            mode_select_sysadmin_menu_global = "System Administration Menu"
            self.mode_select_sysadmin_opt_menu_select.set(str(mode_select_sysadmin_menu_global) )   # Re-initialize OptionMenu 
            #print(".... System Administration Data .... SELECTED .... ")

        elif (mode_select_sysadmin_menu_global == "IPCONFIG"):

            # display results of os.system("ipconfig") to system administration TEXT BOX WIDGET.
            self.display_ipconfig()

            mode_select_sysadmin_menu_global = "System Administration Menu"
            self.mode_select_sysadmin_opt_menu_select.set(str(mode_select_sysadmin_menu_global) )   # Re-initialize OptionMenu 
            #print(".... ipconfig .... SELECTED .... ")

        elif (mode_select_sysadmin_menu_global == "NETSTAT (wait 10 seconds)"):

            # display results of os.system("netstat") to system administration TEXT BOX WIDGET.
            self.display_netstat()

            mode_select_sysadmin_menu_global = "System Administration Menu"
            self.mode_select_sysadmin_opt_menu_select.set(str(mode_select_sysadmin_menu_global) )   # Re-initialize OptionMenu 
            #print(".... netstat .... SELECTED .... ")

        elif (mode_select_sysadmin_menu_global == "Exceptions Logfile"):

            self.display_exceptions_logfile()

            mode_select_sysadmin_menu_global = "System Administration Menu"
            self.mode_select_sysadmin_opt_menu_select.set(str(mode_select_sysadmin_menu_global) )   # Re-initialize OptionMenu 

        else: pass



    def lower_WINDOW(self):
          # These CYCLE Buttons have been changed to 
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()



    def exit_Handler(self):
        self.master.destroy()

        
                        
    def display_sys_admin_data(self):
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert 
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        ###########################################################################
        #  
        # Update the Title Textbox to indicate IPCONFIG results are displayed.
        # 
        ###########################################################################

        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_update_TITLE = "   *****  SYSTEM ADMINISTRATION DATA DISPLAY  ***** "

        self.title_1_text_box.insert(END, text_update_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        # write a new SYS_ADMIN logfile.
        inst_Write_SYS_ADMIN_Logfile_upon_command = Write_Main_Logfile()
        inst_Write_SYS_ADMIN_Logfile_upon_command.write_update_logfile()

        with open(str(fullpath_fn_cm_sw_app_logfile_global) ) as sys_admin_file_handle_var:
             for line in sys_admin_file_handle_var:
                 self.view_text_box.insert(END, line)

        # Disable TEXT WIDGET for Insert 
        self.view_text_box.config(state=DISABLED)


        
                        
    def display_ipconfig(self):
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert 
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        ###########################################################################
        # 
        # Update the Title Textbox to indicate IPCONFIG results are displayed.
        # 
        ###########################################################################

        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_update_TITLE = "   SYSTEM ADMINISTRATION   ... IPCONFIG COMMAND ...   *** IPCONFIG DISPLAY ***"

        self.title_1_text_box.insert(END, text_update_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        # import subprocess added. 
        direct_ipconfig_output = subprocess.check_output("ipconfig", shell=True) # could be any command here.

        self.view_text_box.insert(END, direct_ipconfig_output)

        # Disable TEXT WIDGET for Insert 
        self.view_text_box.config(state=DISABLED)


        
                        
    def display_netstat(self):
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert 
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        ###########################################################################
        #
        # Update the Title Textbox to indicate IPCONFIG results are displayed.
        # 
        ###########################################################################

        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_update_TITLE = "SYSTEM ADMINISTRATION: NETSTAT COMMAND *** NETSTAT DISPLAY *** (after 10 second wait)"

        self.title_1_text_box.insert(END, text_update_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        # import subprocess added. 
        direct_netstat_output = subprocess.check_output("netstat", shell=True) # could be any command here.

        self.view_text_box.insert(END, direct_netstat_output)

        # Disable TEXT WIDGET for Insert 
        self.view_text_box.config(state=DISABLED)

        
                        
    def display_exceptions_logfile(self):
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        # open Write_Exception_Logfile() to append logfile to update the logfile items.
        inst_Write_Exception_Logfile_per_sys_admin_ping = Write_Exception_Logfile()
        
        exception_logging_string_1 = "  *** Exceptions Logfile to Capture Exceptions from PYTHON  try - except  code structure" + "\n"

        exception_logging_string_2 = "  *** Typical Format:  try:  some code   except: Exception as error_string" + "\n"
          
        exception_logging_string_3 = "\n_____________________________________________________________________________\n"
                    
        inst_Write_Exception_Logfile_per_sys_admin_ping.log_exception(str(exception_logging_string_1) )
        inst_Write_Exception_Logfile_per_sys_admin_ping.log_exception(str(exception_logging_string_2) )
        inst_Write_Exception_Logfile_per_sys_admin_ping.log_exception(str(exception_logging_string_3) )

        with open(str(fullpath_exception_logfile_global) ) as exception_file_handle_var:
             for line in exception_file_handle_var:
                 self.view_text_box.insert(END, line)

        # Disable TEXT WIDGET for Insert 
        self.view_text_box.config(state=DISABLED)

        ###########################################################################
        #
        # Update the Title Textbox to indicate EXCEPTIONS LOGFILE is displayed.
        # 
        ###########################################################################

        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_update_TITLE = "   SYSTEM ADMINISTRATION    .....    DATABASE INFORMATION   *** EXCEPTIONS LOGFILE DISPLAY ***"

        self.title_1_text_box.insert(END, text_update_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert
        





##############################################################################
#
# SELECT A CONTACT LIST FILE FROM A LISTBOX. 
#
# THEN READ IN THE CORRESPONDING DICTIONARY FILE INTO A DICTIONARY GLOBAL
# SO THAT IT CAN BE AVAILABLE TO ALL CLASSES TO BROWSE OR WHATEVER.
#
##############################################################################
#
class Select_Contact_List(Frame):  #(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global fullpath_cnotes_dict_file_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global kick_thread_to_update_main_entry_widgets
        global kick_thread_to_update_email_contact_entry_widgets
        global OBJECT_toplevel_select_contact_list
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        
        # self.master = master
        # self.frame = tk.Frame(self.master)

        # self.master = master
        # self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        OBJECT_toplevel_select_contact_list = self.master
        instance_object_LIST.append(self.master)
        
        self.master.configure(background=str(selectlist_bg_color_val_global) )

        self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - Select Contact List")
        
        self.select_file_button = Button(self.master, text = "CLICK HERE after you \nhave SELECTED \na CONTACT LIST File", \
            width=35,height=3, font=('Helvetica', '12'), background="light sea green", command = self.get_Listbox_File)
            
        self.select_file_button.grid(row=1, column=0, sticky = W)
        # self.select_file_button.bind("<Button-1>", self.get_Listbox_File)


        self.tk_lower_status_panel_Button = Button(self.master, text = "MAIN SCREEN", \
        width = 15, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.lower_the_window)
        self.tk_lower_status_panel_Button.grid(row=4, column=0, padx=5, pady=5, sticky = SE)  
        self.tk_lower_status_panel_Button.config(borderwidth=5)


        self.quit_status_panel_Button = Button(self.master, text = "EXIT", \
        width = 7, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.close_windows)
        self.quit_status_panel_Button.grid(row=4, column=0, padx=5, pady=5, sticky = SW)
        self.quit_status_panel_Button.config(borderwidth=5)

        # TEXTBOX to insert TITLE at top of window  

        self.title_1_text_box = Text(self.master, width=42, height = 1)
        self.title_1_text_box.grid(row=0, column=1, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="light sea green")

        text_1_TITLE = "Select CONTACT LIST below :  "

        self.title_1_text_box.insert(END, text_1_TITLE)


        self.lbox = Listbox(self.master, width=52, height = 22)
        self.lbox.grid(row=2, column=1, sticky = W)
        self.lbox.config(borderwidth=10, font=('Helvetica', '12'), background="light sea green") 
        self.lbox.bind("<<ListboxSelect>>", self.OnListBoxSelect)

        # create a Scrollbar and associate it with self.lbox 
        self.scrollb = Scrollbar(self.master, command=self.lbox.yview)
        self.scrollb.grid(row=2, column=2, sticky='NSEW')
        self.lbox['yscrollcommand'] = self.scrollb.set

        # Load all .txt files from cm_appdatafiles_path_global directory into the LISTBOX
        results = []

        testdir = str(cm_appdatafiles_path_global)

        for root,dirs,files in os.walk(testdir):
            for f in files:
                 if ( (f.endswith('.txt') and ("dict_file_" in str(f) ) ) ):
                       
                     try:
                           split_cm_list_see_bracket_ONE = f.split("dict_file_")[1]
                           #  print(".... f.split(cm_list_)[1] = " + str(split_cm_list_see_bracket_ONE) )
                           target_filename_string = split_cm_list_see_bracket_ONE.split(".txt")[0]
                           #  print(".... target_filename_string = " + str( target_filename_string) )

                           results.append(target_filename_string)

                     except Exception:
                           # print(".... IndexError EXCEPTION when splitting dict_file_ and dot_txt to populate LISTBOX : We Will pass")
                           pass

        # Clear Listbox and insert Contact List Names. 
        self.lbox.delete(0, END)

        # Sort the List
        results.sort()

        # Reverse the Order IF the list appears out of alphanumeric order after inserting to the LISTBOX.
        # Reversing order is not required here. 
        # results.reverse()
        
        # Insert Contact List Names.
        for fileName in results:
            self.lbox.insert(END, fileName)


    

    def get_Listbox_File(self):
        global cm_listbox_file_global
        global dict_filename_global
        global listbox_file_capture_global
        global cnotes_dict_file_global
        global fullpath_cnotes_dict_file_global
        global master_cm_list_name_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global kick_thread_to_update_main_entry_widgets
        global kick_thread_to_update_email_contact_entry_widgets
        # This button command gets the filename_value from
        # below (this Demo2 Class) and sets the 
        # CONTACT LIST ENTRY BOX in the App Class
        # USING THE GLOBAL VARIABLE cm_listbox_file_global
        # AND THE LISTBOX WIDGET METHOD:   
        #     
        # cm_filename_value = widget.get(selection[0])
        #

        ######################################################
        #
        # IMPORTANT:   *** Exception Handler ***
        #
        # This exception handler code captures the IndexError Exception that happens
        # if the USER (OPERATOR) does NOT select a Contact List
        # from the LISTBOX -- In that case:
        # we notify the operator with a messagebox and then we
        # self.master.destroy() and return to bring us back to
        # the main screen for another try. 

        verify_listbox_selection = self.lbox.curselection()

        try:
               test_cm_filename_value = str(self.lbox.get(verify_listbox_selection[0] ) )
        except IndexError as err:
               messagebox.showinfo("Contact Manager Guide ...", \
               "ATTENTION: \n\nPlease SELECT a Contact List from the LISTBOX .....\n\n")
               self.master.lift()
               return


        selection = self.lbox.curselection()
        # We must update the master_cm_list_name_global
        # This is the CONTACT LIST NAME selected from the LISTBOX.
        master_cm_list_name_global = self.lbox.get(selection[0]) # because the LISTBOX contains just LIST NAME

        # print(".... master_cm_list_name_global = " + str(master_cm_list_name_global) )
        
        # We must update the cm_list_ FILENAME GLOBAL.
        cm_filename_value = "cm_list_" + str(master_cm_list_name_global) + ".txt"
        cm_listbox_file_global = cm_filename_value

        # print(".... cm_listbox_file_global = " + str(cm_listbox_file_global) )

        # store_selected listbox filename - cm_filename_value in two classes
        lbfn_instance = Store_Lbox_Filename(selected_lbox_file = cm_filename_value)
        lbfn_instance.set_listbox_file(new_Lbox_File = cm_filename_value)
        get_lbfn_call = lbfn_instance.get_listbox_file()

        # We must update the dict_file_ FILENAME GLOBAL
        dict_filename_global = "dict_file_" + str(master_cm_list_name_global) + ".txt"

        # print(".... dict_filename_global = " + str(dict_filename_global) )

        # Set listbox_file_capture_global to trigger Contact List Entry Textbox Update 
        # as we have completed registering all the Listbox Filename variable settings
        # We will reset this listbox_file_capture_global back to False after we  
        # update the Contact List Entry Textbox with the Listbox Filename selected 
        listbox_file_capture_global = True

        # UPDATE APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
        # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
        # which gives us the FULL PATH NAME to our contact_management.py data files. 
        
        fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )

        # print(".... fullpath_fn_cm_listbox_file_global = " + str(fullpath_fn_cm_listbox_file_global) )
        
        fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )

        # print(".... fullpath_fn_dict_filename_global = " + str(fullpath_fn_dict_filename_global) )

        ###################################################################################
        # 
        # If the Contact List was created before the Contact Notes Capability Item,
        # then there will not be a fullpath_cnotes_dict_file_global FILE because
        # the fullpath_cnotes_dict_file_global FILE is created when the User creates
        # a NEW Contact List, so we must test for the existance of the FILE
        # fullpath_cnotes_dict_file_global FILE here, before we try to write to it.
        # If our test indicates that the fullpath_cnotes_dict_file_global FILE
        # does NOT exist, we must create a fullpath_cnotes_dict_file_global FILE.
        #  
        # We want to be sure that when a contact list is selected, we test for the
        # existance of the fullpath_cnotes_dict_file_global FILE, which would
        # need to be created with this code below for any Contact Lists that were
        # created previous to Version 7. And we would do this in Demo2 SELECT LIST.
        #    
        ####################################################################################

        # Build the cnotes_dict_file_global from the master_cm_list_name_global
        # that was acquired above when selcting a contact list.

        cnotes_dict_file_global = "cnotes_" + str(master_cm_list_name_global) + ".txt"

        # print("  ")
        # print(".... VERIFY master_cm_list_name_global FILENAME:  " + str(master_cm_list_name_global) )
        # print("  ")
        # print(".... VERIFY cnotes_dict_file_global FILENAME:  " + str(cnotes_dict_file_global) )
        # print("  ")

        # Build the fullpath_cnotes_dict_file_global from the cnotes_dict_file_global
        # filename that was built above.

        fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

        # print(".... VERIFY fullpath_cnotes_dict_file_global FILENAME:  " + str(fullpath_cnotes_dict_file_global) )
        # print("  ")

        if os.path.isfile(fullpath_cnotes_dict_file_global) == False:

             # Create the File for Contact NOTES DICTIONARY Filename fullpath_cnotes_dict_file_global
             with open(fullpath_cnotes_dict_file_global, 'a') as new_notes_wdictf:
                   new_notes_wdictf.flush()
                   new_notes_wdictf.write("\n")            


        # READ IN THE CORRESPONDING DICTIONARY FILE INTO A DICTIONARY GLOBAL
        # SO THAT IT CAN BE AVAILABLE TO ALL CLASSES TO BROWSE OR WHATEVER.
        # 
        # TO GET THE selected_dictionary_loaded_global GLOBAL SET .... 
        #    
        # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
        # WHICH SETS THE selected_dictionary_loaded_global GLOBAL. 

        inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        loaded_contact_dict_acquired = inst_loaded_Process_Dict_File.read_target_dict_file()

        selected_dictionary_record_index_global = 1
        selected_dictionary_record_index_focus_global = 1

        # Adding the kick_thread flags here because we created a NEW CONTACT LIST
        kick_thread_to_update_email_contact_entry_widgets = True
        kick_thread_to_update_main_entry_widgets = True

        # #print("\n")
        # #print(".... SELECTED and LOADED - selected_dictionary_loaded_global =  " + str(fullpath_fn_dict_filename_global) )
        # #print("\n")

        # write a new logfile to update the logfile items each time a new Contact List is Selected
        inst_Write_Main_Logfile_when_list_select = Write_Main_Logfile()
        inst_Write_Main_Logfile_when_list_select.write_update_logfile()
                

        # close listbox frame window after storing selected filename in Store_Lbox_Filename() Class
        self.master.destroy()
        return cm_filename_value
          


    def OnListBoxSelect(self, event):
        global listbox_file_capture_global
        listbox_file_capture_global = "False"
        widget = event.widget
        selection = widget.curselection()
        filename_value = widget.get(selection[0])
        selection_value_tuple = [selection, filename_value]
        return filename_value



    def lower_the_window(self):
          # These CYCLE Buttons have been changed to 
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()



    def close_windows(self):
        self.master.destroy()




##################################################################################################
# 
#   BUILD a NEW or EXISTING CONTACT LIST from EXISTING CONTACTS LISTS using THREE LISTBOX WIDGETS    
#
##################################################################################################
#
# Method to open new window with three LISTBOXES to BUILD a NEW or EXISTING CONTACT LIST
# from EXISTING CONTACTS LISTS using THREE LISTBOX WIDGETS.  
#
##################################################################################################
#
class List_Builder(Frame):  #(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global fullpath_cnotes_dict_file_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global kick_thread_to_update_main_entry_widgets
        global mode_select_build_list_global
        global selected_dictionary_loaded_global
        global OBJECT_toplevel_list_builder
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        
        # self.master = master
        # self.frame = tk.Frame(self.master)

        # self.master = master
        # self.frame = tk.Frame(self.master)

        huge_font = ('Verdana',32)
        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        OBJECT_toplevel_list_builder = self.master
        instance_object_LIST.append(self.master)
        
        self.master.configure(background=str(selectlist_bg_color_val_global) )

        self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - BUILD Contact List from Existing Contact List")


        # COMMAND BUTTON OVER LBOX ONE
        self.select_file_button = Button(self.master, text = "Click Here after SELECTING\nCONTACT LISTS to BUILD LIST\n(Use CNTL Select)", \
            width=43,height=3, font=('Helvetica', '12'), background="light sea green", \
            command = self.GET_LBOX_MAIN_curselection_method) 

        self.select_file_button.grid(row=0, column=0, sticky = W)
        self.select_file_button.config(borderwidth=5)


        ##########################################################################
        #
        # COMMAND BUTTON OVER LBOX TWO
        # 
        # Button Here to trigger Capture of NEW CONTACT LIST NAME.
        # Method self.capture_new_contact_list_name will then capture
        # textvariable = self.entry_CM_FILENAME from TEXTBOX Widget named
        # self.my_cm_filename_entry   (shown below)  

        self.new_list_button_text = StringVar()
        self.completed_new_contact_list_name_button = Button(self.master, textvariable=self.new_list_button_text, \
            width=43,height=3, font=('Helvetica', '12'), background="cyan4", command = self.enter_new_contact_list_name)
            
        self.completed_new_contact_list_name_button.grid(row=0, column=2, sticky = W)
        self.completed_new_contact_list_name_button.config(borderwidth=5)
        self.new_list_button_text.set("Click after Entering\nNEW Contact List Name (below)\nDefault Name = build_list_Time_Stamp")

        
        # NEW CONTACT LIST NAME ENTRY WIDGET
        # ENTRY WIDGET CREATION HERE FOR NEW CONTACT LIST FILENAME
        self.entry_CM_FILENAME = StringVar()
        self.my_cm_filename_entry = Entry(self.master, textvariable = self.entry_CM_FILENAME, font=('Helvetica', '12'), width = 42)
        self.my_cm_filename_entry.grid(sticky = W, row=1, column=2)
        self.my_cm_filename_entry.config(borderwidth=10, background="cyan4")


        # COMMAND BUTTON OVER LBOX THREE
        self.create_the_new_dictionary_button = Button(self.master, text = "Click Here when finished\nSELECTING CONTACTS\nto CREATE your NEW LIST", \
            width=43,height=3, font=('Helvetica', '12'), background="cyan4", command = self.create_the_NEW_DICTIONARY)
            
        self.create_the_new_dictionary_button.grid(row=0, column=4, sticky = W)
        self.create_the_new_dictionary_button.config(borderwidth=5)
        
        # TEXTBOX for FINAL BUILD STATUS 

        self.final_build_status_text_box = Text(self.master, width=42, height = 1)
        self.final_build_status_text_box.grid(row=1, column=4, sticky = W)
        self.final_build_status_text_box.config(borderwidth=10, font=('Helvetica', '12'), background="cyan4")

        final_build_status_TEXT = "      ***** BUILD CONTACT LIST STATUS  *****"

        self.final_build_status_text_box.insert(END, final_build_status_TEXT)

        self.tk_lower_status_panel_Button = Button(self.master, text = "MAIN SCREEN", \
        width = 15, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.lower_the_window)
        self.tk_lower_status_panel_Button.grid(row=4, column=0, padx=5, pady=5, sticky = SE)  
        self.tk_lower_status_panel_Button.config(borderwidth=5)


        self.quit_status_panel_Button = Button(self.master, text = "EXIT", \
        width = 7, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.close_windows)
        self.quit_status_panel_Button.grid(row=4, column=0, padx=5, pady=5, sticky = SW)
        self.quit_status_panel_Button.config(borderwidth=5)

        # Button to call method to get multiple DESTINATION Listbox Items  
        
        self.GET_LBOX_DESTINATION_curselection_Button = Button(self.master, text = "Select Contacts above\nthen PRESS Here\nto REMOVE from LIST\n(Shift SELECTS Group)", \
        width = 20, height = 4, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.GET_LBOX_DESTINATION_curselection_method)
        self.GET_LBOX_DESTINATION_curselection_Button.grid(row=4, column=4, padx=5, pady=5)  
        self.GET_LBOX_DESTINATION_curselection_Button.config(borderwidth=5)
        
        # Button to call method to get multiple SOURCE Listbox Items 

        self.GET_LBOX_SOURCE_curselection_Button = Button(self.master, text = "Select Contacts above\nthen PRESS Here\nto ADD to LIST\n(Shift SELECTS Group)", \
        width = 20, height =4, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.GET_LBOX_SOURCE_curselection_method)
        self.GET_LBOX_SOURCE_curselection_Button.grid(row=4, column=2, padx=5, pady=5)
        self.GET_LBOX_SOURCE_curselection_Button.config(borderwidth=5)

        # TEXTBOX for source file STATUS  

        self.source_file_status_text_box = Text(self.master, width=42, height = 1)
        self.source_file_status_text_box.grid(row=1, column=0, sticky = W)
        self.source_file_status_text_box.config(borderwidth=10, font=('Helvetica', '12'), background="cyan4")

        # Set this at Neutral initially to ficus USER on selecting BUILD MODE.
        source_file_status_TEXT = ""

        self.source_file_status_text_box.insert(END, source_file_status_TEXT)
        

        #################################################################################################

        # Copy Listbox Code to Make Three Listboxes 
        #
        # One for Existing Contact Lists
        # One that we will convert to List Contacts in that Existing Contact List
        # One that we will convert to be the Target List being Built 

        self.lbox = Listbox(self.master, width=42, height = 22, selectmode=EXTENDED)
        self.lbox.grid(row=2, column=0, sticky = W)
        self.lbox.config(borderwidth=10, font=('Helvetica', '12'), background="dark slate gray", fg="snow") 
        self.lbox.bind("<Button-1>", self.OnListBoxSelect)  #  

        # create a Scrollbar and associate it with self.lbox 
        self.scrollb = Scrollbar(self.master, command=self.lbox.yview)
        self.scrollb.grid(row=2, column=1, sticky='NSEW')
        self.lbox['yscrollcommand'] = self.scrollb.set

        # Load all .txt files from cm_appdatafiles_path_global directory into the LISTBOX
        results = []

        testdir = str(cm_appdatafiles_path_global)

        for root,dirs,files in os.walk(testdir):
            for f in files:
                 if ( (f.endswith('.txt') and ("dict_file_" in str(f) ) ) ):
                       
                     try:
                           split_cm_list_see_bracket_ONE = f.split("dict_file_")[1]
                           #  print(".... f.split(cm_list_)[1] = " + str(split_cm_list_see_bracket_ONE) )
                           target_filename_string = split_cm_list_see_bracket_ONE.split(".txt")[0]
                           #  print(".... target_filename_string = " + str( target_filename_string) )

                           results.append(target_filename_string)

                     except Exception:
                           # print(".... IndexError EXCEPTION when splitting dict_file_ and dot_txt to populate LISTBOX : We Will pass")
                           pass

        # Clear Listbox and insert Contact List Names.
        self.lbox.delete(0, END)

        # Sort the List   
        results.sort()  

        # Reverse the Order IF the list appears out of alphanumeric order after inserting to the LISTBOX.
        # Reversing order IS NOT required here.  
        # results.reverse()
        
        # Insert Contact List Names.
        for fileName in results: 
            self.lbox.insert(END, fileName)


        ################################################################################################ 

        #  Creating Our Class Variables Here ......

        self.selected_source_contact_cm_list = ""
        self.selected_source_contact_dict_list = ""

        self.SOURCE_CONTACT_LIST_NAME_ONLY = ""
        
        self.ORIGINAL_DICTIONARY_FILENAME = ""
        self.original_dict_textString = ""

        self.BUILDING_NEW_LIST_NAME_ONLY = ""
        self.button_set_filename_entry_to_status = False

        self.COPY_LIST_SOURCE_FULLPATH = ""
        self.COPY_LIST_DESTINATION_FULLPATH = ""
        
        ########################################################
        # 
        # NOTE: DICT_INDEX  = TOTAL_RECORDS - LISTBOX_SEL_LIST
        #
        ########################################################

        self.DICT_INDEX = 0
        self.TOTAL_RECORDS = 0

        self.SELECTED_DICT_OF_DICT_GLOBAL = {}

        # 
        # SINGLE (just a single choice)
        # BROWSE (same, but the selection can be moved using the mouse)
        # MULTIPLE (multiple item can be choosen, by clicking at them one at a time)
        # EXTENDED (multiple ranges of items can be chosen, using the Shift and Control keyboard modifiers).
        # The default is BROWSE. Use MULTIPLE to get "checklist" behaviour,
        # and EXTENDED when the user would usually pick only one item, but sometimes would like to select one or more ranges of items.
        #
        # lb = Listbox(selectmode=EXTENDED)  
        #
        # Declare Variables for LISTBOX DATA SELECTION for the
        # SOURCE and DESTINATION LISTBOXES to enbale us to
        # perform Contact ADD / DELETE Functions.
        #

        # This is the LIST we build with the LISTBOX INDEXES
        # so we can utilize htis LIST to index the ORIGINAL
        # Dictionary of the Selected File as we create a
        # new DICTIONARY or DICTIONARIES and our New BUILD LIST Contact List.
        # And the next LIST, self.SOURCE_LISTBOX_SEL_LIST_VALUES,
        # contains the new contact data string for the DESTINATION LISTBOX (only).
        # The complete contact data will be built from the following LIST:
        # self.SOURCE_LISTBOX_SEL_LIST as it indexes the original DICTIONARY.

        self.LISTBOX_SEL_LIST = []
        self.LISTBOX_SEL_LIST_VALUES = []
        self.MAIN_LISTBOX_SEL_LIST = []
        self.MAIN_LISTBOX_SEL_LIST_VALUES = []
        self.SOURCE_LISTBOX_SEL_LIST = []
        self.SOURCE_LISTBOX_SEL_LIST_VALUES = []

        # Maintain a DICTIONARY (MAP) of the LB2 INDEX for each LB3 INDEX.
        # This is used when we remove or delete LB3 items and then update
        # the self.SOURCE_LISTBOX_SEL_LIST (and re-write LB3 Listbox).
        self.DICT_LB3_LB2_INDEX_VALUES = {}

        # These tuples and string represent data objects corresponding
        # to *** each time *** the USER SELECTS a Contact or a Group of Contacts
        # in the SOURCE LISTBOX. 

        self.LB_1_curselection_tuple = ()
        self.LB_2_curselection_tuple = ()
        self.LB_3_curselection_tuple = ()

        self.LB_1_curselection_list = []
        self.LB_2_curselection_list = []
        self.LB_3_curselection_list = []

        ####################################################

        # Create a LIST (Class Variable):  self.save_selection_relates_to_dict_record_num = []
        # Save the selected Source Listbox Selection Numbers in this LIST (Class Variable)
        # so that we can use this LIST to open the Dictionary file 
        # in read mode and write the DATA RECORD to a NEW CONTACT LIST Dictionary
        # or append to an exisitng CONTACT LIST Dictionary.
        # using this command:  
        #
        # self.save_selection_relates_to_dict_record_num.append(str(selection[0] ) )
        #

        self.save_selection_relates_to_dict_record_num = []

        ################################################################################################# 
        #
        # FROM - self.Input_Dict_Filename_Output_Source_Contacts_to_LISTBOX() 
        #
        self.source_contacts_list_of_strings = []    # FIRST_NAME + LAST_NAME + EMAIL ...STRING 

        #################################################################################################

        self.lbox_Source_Contacts = Listbox(self.master, width=42, height = 22, selectmode=EXTENDED)
        self.lbox_Source_Contacts.grid(row=2, column=2, sticky = W)
        self.lbox_Source_Contacts.config(borderwidth=10, font=('Helvetica', '12'), background="dark slate gray", fg="snow") 
        self.lbox_Source_Contacts.bind("<<ListboxSelect>>", self.OnListBoxSelect) # <<ListboxSelect>>    <Button-1>

        # create a Scrollbar and associate it with self.lbox 
        self.scrollb_Source_Contacts = Scrollbar(self.master, command=self.lbox_Source_Contacts.yview)
        self.scrollb_Source_Contacts.grid(row=2, column=3, sticky='NSEW')
        self.lbox_Source_Contacts['yscrollcommand'] = self.scrollb_Source_Contacts.set

        # We Load Contacts into this Listbox #2 after Selecting a Contact List from Listbox #1.

        #################################################################################################

        self.lbox_Destination_Contacts = Listbox(self.master, width=42, height = 22, selectmode=EXTENDED)
        self.lbox_Destination_Contacts.grid(row=2, column=4, sticky = W)
        self.lbox_Destination_Contacts.config(borderwidth=10, font=('Helvetica', '12'), background="dark slate gray", fg="cyan") 
        self.lbox_Destination_Contacts.bind("<Button-1>", self.OnListBoxSelect)

        # create a Scrollbar and associate it with self.lbox 
        self.scrollb_Destination_Contacts = Scrollbar(self.master, command=self.lbox_Destination_Contacts.yview)
        self.scrollb_Destination_Contacts.grid(row=2, column=5, sticky='NSEW')
        self.lbox_Destination_Contacts['yscrollcommand'] = self.scrollb_Destination_Contacts.set

        # We Load Contacts into this Listbox #3 after Selecting a Contacts from Listbox #2.

        # NOTE: We are also evaluating using the get command to acquire the tuple of all
        # items in the Destination Listbox as follows: 

        # items = self.lbox_Destination_Contacts.get(0, END)   
        #     print("Using the GET to get LISTBOX ITEMS - self.lbox_Destination_Contacts.get(0, END)" + str(items) )

        ##############################################################################################

        ##########################################################################################
        #
        #  WE SWITCH THIS ON FOR **** BUILD LIST **** WORKFLOW ..... 
        #
        #self.select_file_button = Button(self.master, text = "Click Here after SELECTING\na CONTACT LIST\nto BUILD from", \
        #    width=43,height=3, font=('Helvetica', '12'), background="light sea green" ) # command = self.get_Listbox_File
            
        #self.select_file_button.grid(row=0, column=0, sticky = W)
        #self.select_file_button.bind("<Button-1>", self.get_Listbox_File)
        #self.select_file_button.config(borderwidth=5)
        
        ##########################################################################################
        #
        #  List_of_Build_List_Modes = ["Build List", "Merge List", "Copy List", "Rename List"]
        #
        #  WE INITIALIZE THE WORKFLOW CANVAS WIDGET .....  
        #
        self.draw_WorkFlow_Canvas_Widget()
        #
        #
        ##########################################################################################

        ##############################################################################################

        self.widget_ID = ""

        ##############################################################################################
        #
        #   NOTE:  The following tk GUI Signaling Sequences Guide User to NEXT STEP .....
        #
        #          These Signaling Sequences adjust the tk WIDGET Colors. 
        #
        ##############################################################################################
        #
        # set back to neutral colors
        # self.select_file_button.config(background = "cyan4")
        # self.source_file_status_text_box.config(background = "cyan4")
        # 
        # set back to neutral colors - the new filename has been set. 
        # self.my_cm_filename_entry.config(background = "cyan4")
        # self.completed_new_contact_list_name_button.config(background = "cyan4")
        #  
        # set to green to focus user on next task
        # self.create_the_new_dictionary_button.config(background = "light sea green")
        # self.final_build_status_text_box.config(background = "light sea green")
        #
        ###############################################################################################



    def func_set_mode_select_build_list_global(self, mode_select_build_opt_menu_select):
        global mode_select_build_list_global
        # print("....   BUILD LIST   M O D E   S E L E C T E D   . . . . . ")

        # List_of_Build_List_Modes = ["Build List", "Merge List", "Copy List", "Rename List"]

        # Set the GLOBAL for the newly selected mode_select_build_list_global 
        mode_select_build_list_global = str(mode_select_build_opt_menu_select)

        
        
    def start_build_list_WORKFLOW(self):
        global mode_select_build_list_global
        # print("....   S T A R T    B U I L D    L I S T    W O R K F L O W    . . . . . ")

        # List_of_Build_List_Modes = ["Build List", "Merge List", "Copy List", "Rename List"]

        ###########################################################################################
        #
        #     R E - I N I T I A L I Z E     W O R K F L O W     D A T A  
        #
        # CLEAR ALL APPLICABLE ENTRY, TEXT, and LISTBOX WIDGETS because at this method,
        # the USER has selected a new WORKFLOW and so we clear all the old data.  
        #  
        ###########################################################################################

        self.lbox_Source_Contacts.delete(0, END)
        self.lbox_Destination_Contacts.delete(0, END)

        self.LB_1_curselection_tuple = ()
        self.LB_2_curselection_tuple = ()
        self.LB_3_curselection_tuple = ()

        self.LB_1_curselection_list = []
        self.LB_2_curselection_list = []
        self.LB_3_curselection_list = []

        self.LISTBOX_SEL_LIST = []
        self.MAIN_LISTBOX_SEL_LIST = []
        self.LISTBOX_SEL_LIST_VALUES = []
        self.MAIN_LISTBOX_SEL_LIST_VALUES = []

        self.SOURCE_LISTBOX_SEL_LIST = []
        self.SOURCE_LISTBOX_SEL_LIST_VALUES = []

        self.DICT_LB3_LB2_INDEX_VALUES = {}

        self.button_set_filename_entry_to_status = False

        # Resetting this to default value in case
        # user did not select Build List Command Button.
        self.GET_LBOX_SOURCE_curselection_Button.config(background="cyan4")

        # ENTRY WIDGET OVER LBOX TWO - NEW CONTACT LIST NAME ENTRY WIDGET
        # ENTRY WIDGET CREATION HERE FOR NEW CONTACT LIST FILENAME
        self.entry_CM_FILENAME.set("")
        self.my_cm_filename_entry.config(borderwidth=10, background="cyan4")

        # STATUS TEXT WIDGET OVER LBOX THREE - TEXTBOX for FINAL BUILD STATUS 

        self.final_build_status_text_box = Text(self.master, width=42, height = 1)
        self.final_build_status_text_box.grid(row=1, column=4, sticky = W)
        self.final_build_status_text_box.config(borderwidth=10, font=('Helvetica', '12'), background="cyan4")

        final_build_status_TEXT = "      ***** BUILD CONTACT LIST STATUS  *****"

        self.final_build_status_text_box.insert(END, final_build_status_TEXT)

        ####################################################################################
        #
        #   W O R K F L O W     S E L E C T E D   -   E X E C U T E   selected   WorkFlow.
        # 
        ####################################################################################

        # Upon START, if mode_select_build_list_global == "Build List"
        # we activate our LBOX ONE select-a-list button,
        # LBOX TWO entry filename button,
        # and LBOX THREE WORKFLOW Command Button alive
        # which enables the "Build List" WORKFLOW.
        if mode_select_build_list_global == "Build List":
            #
            #  WE ACTIVATE OUR BUTTON FOR THE BUILD LIST WORKFLOW .....
            #
            #  Execute "Build List" WORKFLOW. 
            #
            # print(".... Execute ***** Build List ***** WORKFLOW")

            # STATUS TEXTBOX OVER LBOX ONE
            source_file_status_TEXT = "Select a Contact List to BUILD from .... "

            # Update the LBOX ONE Status Textbox according to the MODE.
            # See mode_select_build_list_global message above.  
            self.source_file_status_text_box.delete(1.0, END)
            self.source_file_status_text_box.insert(END, source_file_status_TEXT)

            self.source_file_status_text_box.config(background = "cyan")
            
            # COMMAND BUTTON OVER LISTBOX ONE
            self.select_file_button = Button(self.master, text = "Click Here after SELECTING\na CONTACT LIST\nto BUILD from", \
                width=43,height=3, font=('Helvetica', '12'), background="light sea green", \
                command = self.GET_LBOX_MAIN_curselection_method)  # command = self.get_Listbox_File)

            self.select_file_button.grid(row=0, column=0, sticky = W)                    
            self.select_file_button.config(borderwidth=5)

            ##########################################################################
            #
            # COMMAND BUTTON OVER LBOX TWO 
            # 
            # Button Here to trigger Capture of NEW CONTACT LIST NAME. 
            # Method self.capture_new_contact_list_name will then capture
            # textvariable = self.entry_CM_FILENAME from TEXTBOX Widget named
            # self.my_cm_filename_entry   (shown below)  

            self.new_list_button_text = StringVar()
            self.completed_new_contact_list_name_button = Button(self.master, textvariable=self.new_list_button_text, \
                width=43,height=3, font=('Helvetica', '12'), background="cyan4", command = self.enter_new_contact_list_name)

            self.completed_new_contact_list_name_button.grid(row=0, column=2, sticky = W)
            self.completed_new_contact_list_name_button.config(borderwidth=5)
            self.new_list_button_text.set("Click after Entering\nNEW Contact List Name (below)\nDefault Name = build_list_Time_Stamp")

            ##########################################################################
            #
            # COMMAND BUTTON OVER LBOX THREE
            #
            # command = self.create_the_NEW_DICTIONARY
            #
            self.create_the_new_dictionary_button = Button(self.master, text = "Click Here when finished\nSELECTING CONTACTS\nto CREATE your NEW LIST", \
                  width=43,height=3, font=('Helvetica', '12'), background="cyan4", command = self.create_the_NEW_DICTIONARY)

            self.create_the_new_dictionary_button.grid(row=0, column=4, sticky = W)
            self.create_the_new_dictionary_button.config(borderwidth=5)


        # Upon START, if mode_select_build_list_global == "Merge List"
        # we activate our LBOX ONE select-a-list button,
        # LBOX TWO entry filename button,
        # and LBOX THREE WORKFLOW Command Button alive
        # which enables the "Merge List" WORKFLOW.
        elif mode_select_build_list_global == "Merge List":
            #
            #  WE EXECUTE THE MERGE LIST WORKFLOW ..... 
            #
            #  Execute "Merge List" WORKFLOW.
            #
            # print(".... Execute ***** Merge List ***** WORKFLOW")

            
            # STATUS TEXTBOX OVER LBOX ONE
            source_file_status_TEXT = "Select Contact Lists to MERGE .... "

            # Update the LBOX ONE Status Textbox according to the MODE.
            # See mode_select_build_list_global message above.
            self.source_file_status_text_box.delete(1.0, END)
            self.source_file_status_text_box.insert(END, source_file_status_TEXT)

            self.source_file_status_text_box.config(background = "cyan")


            # COMMAND BUTTON OVER LBOX ONE
            self.select_file_button = Button(self.master, text = "Click Here after SELECTING\nCONTACT LISTS to MERGE\n(Use CNTL Select)", \
                width=43,height=3, font=('Helvetica', '12'), background="light sea green", \
                command = self.GET_LBOX_MAIN_curselection_method) 

            self.select_file_button.grid(row=0, column=0, sticky = W)
            self.select_file_button.config(borderwidth=5)

            ##########################################################################
            #
            # COMMAND BUTTON OVER LBOX TWO 
            # 
            # Button Here to trigger Capture of a MERGE CONTACT LIST NAME.
            # Method self.capture_new_contact_list_name will then capture
            # textvariable = self.entry_CM_FILENAME from TEXTBOX Widget named
            # self.my_cm_filename_entry  

            self.new_list_button_text = StringVar()
            self.completed_new_contact_list_name_button = Button(self.master, textvariable=self.new_list_button_text, \
                width=43,height=3, font=('Helvetica', '12'), background="cyan4", command = self.enter_new_contact_list_name)
            
            self.completed_new_contact_list_name_button.grid(row=0, column=2, sticky = W)
            self.completed_new_contact_list_name_button.config(borderwidth=5)
            self.new_list_button_text.set("Click after Entering\nMERGE Contact List Name (below)\nDefault Name = MERGE_list_Time_Stamp")

            ##########################################################################
            #
            # COMMAND BUTTON OVER LBOX THREE
            #
            # command = self.merge_list_of_contact_lists
            #

            self.create_the_new_dictionary_button = Button(self.master, \
                text = "Click Here\nto GENERATE your\nMERGE CONTACT LIST", \
                width=43,height=3, font=('Helvetica', '12'), background="cyan4", \
                command = self.merge_list_of_contact_lists)
            
            self.create_the_new_dictionary_button.grid(row=0, column=4, sticky = W)
            self.create_the_new_dictionary_button.config(borderwidth=5)
            
        # Upon START, if mode_select_build_list_global == "Copy List"
        # we activate our LBOX ONE select-a-list button,
        # LBOX TWO entry filename button,
        # and LBOX THREE WORKFLOW Command Button alive
        # which enables the "Copy List" WORKFLOW.
        elif mode_select_build_list_global == "Copy List":
            #
            #  Execute "Copy List" WORKFLOW. 
            #
            # print(".... Execute ***** Copy List ***** WORKFLOW")
            #
            ################################################################################################
            #
            #  Try to Copy LISTBOX ONE Selected File to Filename entered
            #  by USER to ENTRY WIDGET above LISTBOX TWO.
            #
            # try:
            #     shutil.copyfile(str(source_file_path_string), str(destination_file_path_string) )
            #
            # except:
            #     pass
            #
            ################################################################################################
            #
            # STATUS TEXTBOX OVER LBOX ONE
            source_file_status_TEXT = "Select a Contact List to COPY .... "

            # Update the LBOX ONE Status Textbox according to the MODE.
            # See mode_select_build_list_global message above.  
            self.source_file_status_text_box.delete(1.0, END)
            self.source_file_status_text_box.insert(END, source_file_status_TEXT)

            self.source_file_status_text_box.config(background = "cyan")
            
            # COMMAND BUTTON OVER LISTBOX ONE
            self.select_file_button = Button(self.master, text = "Click Here after SELECTING\na CONTACT LIST\nto COPY", \
                width=43,height=3, font=('Helvetica', '12'), background="light sea green", \
                command = self.GET_LBOX_MAIN_curselection_method)  

            self.select_file_button.grid(row=0, column=0, sticky = W)                    
            self.select_file_button.config(borderwidth=5)

            ##########################################################################
            #
            # COMMAND BUTTON OVER LBOX TWO 
            # 
            # Button Here to trigger Capture of NEW CONTACT LIST NAME. 
            # Method self.capture_new_contact_list_name will then capture
            # textvariable = self.entry_CM_FILENAME from TEXTBOX Widget named
            # self.my_cm_filename_entry   (shown below) 

            self.new_list_button_text = StringVar()
            self.completed_new_contact_list_name_button = Button(self.master, textvariable=self.new_list_button_text, \
                width=43,height=3, font=('Helvetica', '12'), background="cyan4", \
                command = self.enter_new_contact_list_name)

            self.completed_new_contact_list_name_button.grid(row=0, column=2, sticky = W)
            self.completed_new_contact_list_name_button.config(borderwidth=5)
            self.new_list_button_text.set("Click after Entering\nNEW Contact List Name (below)\nDefault Name = COPY_LIST_Time_Stamp")

            ##########################################################################
            #
            # COMMAND BUTTON OVER LBOX THREE  
            #
            # command = execute_COPY_LIST_WORKFLOW
            #
            self.create_the_new_dictionary_button = Button(self.master, \
                text = "Click Here\nto COPY your\nCONTACT LIST", \
                width=43,height=3, font=('Helvetica', '12'), background="cyan4", \
                command = self.execute_COPY_LIST_WORKFLOW)
            
            self.create_the_new_dictionary_button.grid(row=0, column=4, sticky = W)
            self.create_the_new_dictionary_button.config(borderwidth=5)

            
        # Upon START, if mode_select_build_list_global == "Rename List"
        # we activate our LBOX ONE select-a-list button,
        # LBOX TWO entry filename button,
        # and LBOX THREE WORKFLOW Command Button alive
        # which enables the "Rename List" WORKFLOW.
        elif mode_select_build_list_global == "Rename List":
            #
            #  Execute "Rename List" WORKFLOW.
            #
            # print(".... Execute ***** Rename List ***** WORKFLOW")
            #
            ################################################################################################
            #
            #  Try to Copy LISTBOX ONE Selected File to Filename entered
            #  by USER to ENTRY WIDGET above LISTBOX TWO.
            #
            # try:
            #     shutil.copyfile(str(source_file_path_string), str(destination_file_path_string) )
            #
            # except:
            #     pass
            #
            ################################################################################################
            #
            #  Then Try to remove all the LISTBOX ONE Selected Contact List Datbase Files.
            #
            #  os.remove() 
            #
            ################################################################################################

            self.lbox_Source_Contacts.delete(0, END)

            self.lbox_Source_Contacts.insert(END, " ")
            self.lbox_Source_Contacts.insert(END, "RENAME LIST")
            self.lbox_Source_Contacts.insert(END, " ")
            self.lbox_Source_Contacts.insert(END, "NOT YET IMPLEMENTED")
            self.lbox_Source_Contacts.insert(END, " ")
            self.lbox_Source_Contacts.insert(END, "USE COPY LIST")
            self.lbox_Source_Contacts.insert(END, " ")

            self.lbox_Destination_Contacts.delete(0, END)

            self.lbox_Destination_Contacts.insert(END, " ")
            self.lbox_Destination_Contacts.insert(END, "RENAME LIST")
            self.lbox_Destination_Contacts.insert(END, " ")
            self.lbox_Destination_Contacts.insert(END, "NOT YET IMPLEMENTED")
            self.lbox_Destination_Contacts.insert(END, " ")
            self.lbox_Destination_Contacts.insert(END, "USE COPY LIST")
            self.lbox_Destination_Contacts.insert(END, " ")




    ##########################################################################################
    #
    #   BEGIN OF CANVAS WIDGETS FOR BUILD LIST WORKFLOW START SEQUENCE  ......
    #
    ##########################################################################################
    #
    # This CANVAS is the START for the BUILD LIST CLASS WORKFLOW .....
    #
    # This CANVAS WIDGET will be replaced by the self.select_file_button (above)
    # when the USER selects their WORKFLOW via the OPTIONS MENU, which will
    # call self.func_set_mode_select_build_list_global and set mode_select_build_list_global.
    #
    # To put complex multi-widget objects on a canvas, you can use this method
    # to place a Frame widget on the canvas, and then place other widgets inside that frame:
    # 
    # id = C.create_window(x, y, option, ...)  
    #
    ##########################################################################################
    #  
    # WE CALL THIS THE:  WORKFLOW CANVAS WIDGET AND WE RE-PAINT IT AFTER EACH WORKFLOW TASK
    # 
    ##########################################################################################

    def draw_WorkFlow_Canvas_Widget(self):
        global mode_select_build_list_global
        
        self.select_mode_canvas = Canvas(self.master, width=384, height=57) 
        self.select_mode_canvas.grid(row=0, column=0, sticky = W)
        self.select_mode_canvas.config(background = "light sea green", borderwidth=5)

        self.radio_frame = Frame(self.select_mode_canvas, bg = "cyan4")

        self.canvas_frame = self.select_mode_canvas.create_window((0,0), window=self.radio_frame, anchor = NW)

        List_of_Build_List_Modes = ["Build List", "Merge List", "Copy List", "Rename List"]

        mode_select_build_list_global = "Build List"

        # Options Menu to Select the BUILD LIST WORKFLOW 
        self.mode_select_build_opt_menu_select = StringVar()
        self.mode_select_build_opt_menu_select.set(str(mode_select_build_list_global) )  # initialize OptionMenu for Mode Select Build List
        self.mode_select_build_optionsmenu_inst = OptionMenu(self.radio_frame, self.mode_select_build_opt_menu_select, \
            *List_of_Build_List_Modes, command=self.func_set_mode_select_build_list_global)
        self.mode_select_build_optionsmenu_inst.grid(sticky = W, row=0, column=0)
        self.mode_select_build_optionsmenu_inst.config(borderwidth=5, background="cyan4", font=('Helvetica', 14 ) )

        menu_mode_select_build = self.mode_select_build_optionsmenu_inst.nametowidget(self.mode_select_build_optionsmenu_inst.menuname) 
        menu_mode_select_build.configure(font=("Helvetica", 18), bg="light sea green")

        # Label to Start the BUILD LIST WORKFLOW
        self.label_workflow_start_text = "Select Task,\nPress START."
        self.label_workflow_start = Label(self.radio_frame, text = self.label_workflow_start_text, font=('Verdana',12) ) 
        self.label_workflow_start.config(height = 2, width=12, anchor = W)
        self.label_workflow_start.config(bg="blue2", fg='cyan')  
        self.label_workflow_start.grid(row=0, column=1)
            
        # START Button for the BUILD LIST WORKFLOW
        self.build_list_WORKFLOW_START_Button = Button(self.radio_frame, text = "START", \
        width = 7, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
           command = self.start_build_list_WORKFLOW)
        self.build_list_WORKFLOW_START_Button.grid(row=0, column=2, padx=1, pady=1, sticky = W)  
        self.build_list_WORKFLOW_START_Button.config(borderwidth=5)
        
        self.radio_frame.bind("<Configure>", self.OnFrameConfigure)
        self.select_mode_canvas.bind('<Configure>', self.FrameWidthHeight)

        # Load all .txt files from cm_appdatafiles_path_global directory into the LISTBOX
        results = []

        testdir = str(cm_appdatafiles_path_global)

        for root,dirs,files in os.walk(testdir):
            for f in files:
                 if ( (f.endswith('.txt') and ("dict_file_" in str(f) ) ) ):
                       
                     try:
                           split_cm_list_see_bracket_ONE = f.split("dict_file_")[1]
                           #  print(".... f.split(cm_list_)[1] = " + str(split_cm_list_see_bracket_ONE) )
                           target_filename_string = split_cm_list_see_bracket_ONE.split(".txt")[0]
                           #  print(".... target_filename_string = " + str( target_filename_string) )

                           results.append(target_filename_string)

                     except Exception:
                           # print(".... IndexError EXCEPTION when splitting dict_file_ and dot_txt to populate LISTBOX : We Will pass")
                           pass

        # Clear Listbox and insert Contact List Names.
        self.lbox.delete(0, END)

        # Sort the List  
        results.sort()  

        # Reverse the Order IF the list appears out of alphanumeric order after inserting to the LISTBOX.
        # Reversing order IS NOT required here.  
        # results.reverse()
        
        # Insert Contact List Names.
        for fileName in results: 
            self.lbox.insert(END, fileName)

        ##########################################################################################
        #
        #   END OF CANVAS WIDGETS FOR BUILD LIST WORKFLOW START SEQUENCE  ......   
        #
        ##########################################################################################



    def FrameWidthHeight(self, event):
        canvas_width = event.width
        canvas_height = event.height
        self.select_mode_canvas.itemconfig(self.canvas_frame, width = canvas_width)
        self.select_mode_canvas.itemconfig(self.canvas_frame, height = canvas_height)


    def OnFrameConfigure(self, event):
        self.select_mode_canvas.configure(scrollregion=self.select_mode_canvas.bbox("all"))

        

    ################################################################################
    #
    # MERGE LIST OF CONTACT LISTS.  
    # 
    # Use the Process_Dictionary Class to read in each dictionary filename
    # in the selected list of filenames, saving each dictionary (contact list).
    #
    # Merge the STRINGS for the Selected Contact Lists.
    #
    # Write the MERGED STRING to a dict_ file.
    #
    ################################################################################
    #
    def merge_list_of_contact_lists(self):
        global selected_dictionary_loaded_global
        global fullpath_fn_dict_filename_global
        global master_cm_list_name_global

        # print(".... Executing METHOD - self.merge_list_of_contact_lists ")

        ###########################################################################################
        #
        #  VERIFY that the new LISTBOX MODE doesn't break the original BUILD LIST FILE SELECT.
        #
        ###########################################################################################
        #
        #   V E R I F Y   THE OS METHOD OF MERGING TWO FILES ......
        #
        ###########################################################################################
        
        ## print(".... *** L E N *** - len(MAIN_LISTBOX_SEL_LIST_VALUES) = " + str(len(self.MAIN_LISTBOX_SEL_LIST_VALUES)) )
              
        # if len(self.MAIN_LISTBOX_SEL_LIST_VALUES) < 2:

            # print(".... **** ERROR **** NEED TWO OR MORE FILES TO MERGE **** UPDATE LBOX 2 STATUS TEXT WIDGET with COLORFUL MESSAGE")
            
        #
        # Get the LIST of Contact List Filenames from the Listbox
        # noting that to select a LIST of Files, the Listbox
        # should be in the mode:  selectmode=EXTENDED
        #
        # self.MAIN_LISTBOX_SEL_LIST_VALUES = [] 
    
        list_of_contact_lists_selected = []
        list_of_contact_lists_selected = self.MAIN_LISTBOX_SEL_LIST_VALUES

        # Create various dictionary objects and counters.
        # 
        dict_filename = ""
        dict_filename_fullpath = ""

        num_data_records = 0
        cumulative_sum_of_records = 0
        list_counter = 0

        dict_merge_result = {}

        MASTER_DICT_STRING = ""
        
        # Prepare to Write DICTIONARY RECORD COUNT TO LBOX TWO ......
        self.lbox_Source_Contacts.delete(0, END)

        # OUTPUT - MERGE FILE DEFINITION:
        #
        # Form Dictionary Filename for target MERGE File from USER input of Contact List Name
        dict_file_merge_filename = "dict_file_" + str(self.BUILDING_NEW_LIST_NAME_ONLY) + ".txt"

        dict_file_merge_fullpath = os.path.join(str(cm_appdatafiles_path_global), str(dict_file_merge_filename) )

        # Form cm_list_ Filename for target MERGE File from USER input of Contact List Name
        cm_list_file_merge_filename = "cm_list_" + str(self.BUILDING_NEW_LIST_NAME_ONLY) + ".txt"

        cm_list_file_merge_fullpath = os.path.join(str(cm_appdatafiles_path_global), str(cm_list_file_merge_filename) )

        # Form cnotes_ Filename for target MERGE File from USER input of Contact List Name
        cnotes_file_merge_filename = "cnotes_" + str(self.BUILDING_NEW_LIST_NAME_ONLY) + ".txt"

        cnotes_file_merge_fullpath = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_file_merge_filename) )
        
        # Set the global so that Dictionary Filename for target MERGE File 
        # is now the DICTIONARY GLOBAL: The Contact List viewed of the main screen.
        fullpath_fn_dict_filename_global = str(dict_file_merge_fullpath)

        fullpath_fn_cm_listbox_file_global = str(cm_list_file_merge_fullpath)

        fullpath_cnotes_dict_file_global = str(cnotes_file_merge_fullpath)

        # NOTE: DO cm_list and cnotes too .....
        #
        # fullpath_fn_dict_filename_global
        # fullpath_fn_cm_listbox_file_global
        # fullpath_cnotes_dict_file_global

        # set the new merged filename as our MASTER CONTACT LIST to appear on MAIN SCREEN
        # This will update on the MAIN SCREEN when we execute
        # kick_thread_to_update_main_entry_widgets = True
        master_cm_list_name_global = str(self.BUILDING_NEW_LIST_NAME_ONLY)
        # print("  ")
        # print(".... master_cm_list_name_global = str(self.BUILDING_NEW_LIST_NAME_ONLY) = " + str(master_cm_list_name_global) )

        # Create LIST to store fullpath of dict_files being merged.
        merging_dict_fullpath_LIST = []

        # Create LIST to store fullpath of cm_list_ files being merged.
        merging_cm_list_fullpath_LIST = []

        # Create LIST to store fullpath of cnotes_ files being merged.
        merging_cnotes_fullpath_LIST = []

        # Create LIST for all os isfile False to create status display
        OS_ISFILE_FALSE_STATUS_LIST = []
#12345678
        ####################################################################################
        # 
        #   ***** THIS IS THE CONTACT LISTS LOOP FOR CONTACT LISTS BEING MERGED ***** 
        # 
        ####################################################################################
#12345678   
        for contact_list in list_of_contact_lists_selected:

            # INPUT - FILE DEFINITION for EACH SELECTED CONTACT LIST to Merge:
            #
            # Form Dictionary Filename for each Contact List Name
            selected_contact_list_dict_filename = "dict_file_" + str(contact_list) + ".txt"

            # Form Dictionary Filename for each Contact List Name
            selected_contact_list_cm_list_filename = "cm_list_" + str(contact_list) + ".txt"

            # Form Dictionary Filename for each Contact List Name
            selected_contact_list_cnotes_filename = "cnotes_" + str(contact_list) + ".txt"

            # print("   ")
            # print(".... CONTACT LIST TO MERGE - selected_contact_list_dict_filename = " + str(selected_contact_list_dict_filename) )

            selected_contact_list_dict_fullpath = os.path.join(str(cm_appdatafiles_path_global), str(selected_contact_list_dict_filename) )

            selected_contact_list_cm_list_fullpath = os.path.join(str(cm_appdatafiles_path_global), str(selected_contact_list_cm_list_filename) )

            selected_contact_list_cnotes_fullpath = os.path.join(str(cm_appdatafiles_path_global), str(selected_contact_list_cnotes_filename) )
            ##########################################################################################
            # 
            # Here is where we must make an Executive Decision on whether to MERGE if one or more
            # or the Database File Types is not present after we perform the os isfile operation.
            # The thinking or logic is that if the Contact Management Database does NOT contain
            # each data file type: 
            #
            #      1. dict_file_
            #      2. cm_list_
            #      3. cnotes_
            #
            # then that particular contact list would need re-construction of the missing
            # data file type(s) to participate in a valid MERGE, and thus we would exclude
            # a particular contact list from the MERGE if any one (or more) of the data file
            # types (listed above) are not present as indicated by the os isfile operation.
            # Consequently, we will monitor and report the status of the os isfile operation
            # on each file type for each contact list. We gather this os isfile status in
            # this loop of the selected contact lists to MERGE. Note that because the
            # contact list selection is from LISTBOX ONE, which is formed from the dict_file_,
            # we expect all selected contact lists to have the dict_file_ type, although we
            # do check all the database file types with os isfile as a formality.
            #
            # We Gather this Status in:
            #
            # OS_ISFILE_FALSE_STATUS_LIST.append("cm_list Missing for " + str(contact_list))
            #
            # and
            #
            # OS_ISFILE_FALSE_STATUS_LIST.append("cnotes Missing for " + str(contact_list))
            #
            ##########################################################################################
            #  
            # Verify CONTACT LIST DATABASE FILES COPIED   
            # using os.path.isfile and display status in LISTBOX TWO and/or LISTBOX THREE.
#123456789012

            try:
                TF_dict_to_merge = os.path.isfile(str(selected_contact_list_dict_fullpath) )
                if TF_dict_to_merge == False:
                    OS_ISFILE_FALSE_STATUS_LIST.append("dict Missing for " + str(contact_list))
                    # print(".... ***** ERROR ***** Contact List: " + str(contact_list) + " does NOT have a dict_file_")
                          
            except Exception:
                   # print(".... EXCEPTION NoDictFile ***** ERROR ***** Contact List: " + str(contact_list) + " does NOT have a dict_file_")
                   pass
#123456789012         
            try:
                TF_cm_list_to_merge = os.path.isfile(str(selected_contact_list_cm_list_fullpath) )
                if TF_cm_list_to_merge == False:
                    OS_ISFILE_FALSE_STATUS_LIST.append("cm_list Missing for " + str(contact_list))
                    # print(".... ***** ERROR ***** Contact List: " + str(contact_list) + " does NOT have a cm_list_")                         

            except Exception:
                   # print(".... EXCEPTION NoCmListFile ***** ERROR ***** Contact List: " + str(contact_list) + " does NOT have a cm_list_")
                   pass

            try:
                TF_cnotes_to_merge = os.path.isfile(str(selected_contact_list_cnotes_fullpath) )
                if TF_cnotes_to_merge == False:
                    OS_ISFILE_FALSE_STATUS_LIST.append("cnotes Missing for " + str(contact_list))
                    # print(".... ***** ERROR ***** Contact List: " + str(contact_list) + " does NOT have a cnotes_")                        

            except Exception:
                   # print(".... EXCEPTION NoCnotesFile ***** ERROR ***** Contact List: " + str(contact_list) + " does NOT have a cnotes_")
                   pass

            all_database_files_present = TF_dict_to_merge and TF_cm_list_to_merge and TF_cnotes_to_merge

            if all_database_files_present == False:
                # print(".... MISSING DATABASE FILE(s) in " + str(contact_list) )
                pass

                
            elif all_database_files_present == True:
                                
                # Build LIST to store fullpath of dict_files being merged.
                merging_dict_fullpath_LIST.append(str(selected_contact_list_dict_fullpath) )

                # Build LIST to store fullpath of cm_listfiles being merged.
                merging_cm_list_fullpath_LIST.append(str(selected_contact_list_cm_list_fullpath) )

                # Build LIST to store fullpath of cnotes files being merged.
                merging_cnotes_fullpath_LIST.append(str(selected_contact_list_cnotes_fullpath) )

                ################################################################################### 

                # This section of code opens each Contact List Dictionary and counts the RECORDS
                # to display this to the USER in LBOX TWO for USER Feedback during MERGE WORKFLOW.

                textFile = open(selected_contact_list_dict_fullpath, 'r')

                # This takes the file object opened with the open() and turns it into a string which 
                # we can use o read the number of RECORDS in the DICTIONARY FILE.
                textString = textFile.read()

                textFile.close()

                # Count the DATA RECORDS in the string by counting the
                # number of "DATA_RECORD_DELIMITER:" patterns  
                num_data_records = textString.count("DATA_RECORD_DELIMITER:")

                cumulative_sum_of_records = cumulative_sum_of_records + num_data_records

                list_counter+=1

                # Write DICTIONARY RECORD COUNT TO LBOX TWO ...... 
                self.lbox_Source_Contacts.insert(END, "LIST # " + str(list_counter) + " RECORDS: " + str(num_data_records) + " " +  str(contact_list) )


                ####################################################################################
                ##################    GATHER DATA LOOP ENDS HERE    ################################
                ####################################################################################
                
#12345678                
#12345678  <<<---- COD INDENT GOES BACK TO HERE BECAUSE LOOP IS FINISHED.
#12345678
        ####################################################################################
        # 
        #   ***** M E R G I N G    D I C T    F I L E S   H E R E  ***** 
        #
        ####################################################################################
        # print(".... ")
        # print(".... MERGING to FILENAME:  self.BUILDING_NEW_LIST_NAME_ONLY = " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )
        # print(".... ")
        # print(".... NEW MERGED DICT GLOBAL:  fullpath_fn_dict_filename_global = \n" + str(fullpath_fn_dict_filename_global) )
        # print(".... ")


        # Execute dict_file_ MERGE 
#12345678
        with open(dict_file_merge_fullpath, 'w') as outfile:
            for fname in merging_dict_fullpath_LIST:
                with open(fname) as infile:
                    outfile.write(infile.read())

                # Execute cm_list_ MERGE                     
#12345678
        with open(cm_list_file_merge_fullpath, 'w') as outfile:
            for cm_fname in merging_cm_list_fullpath_LIST:
                with open(cm_fname) as infile:
                    outfile.write(infile.read())

#12345678
        #
        # FILTER OUT ALL ACCEPT THE TOP LINE OF THESE: 
        #
        # First Name,Last Name,Street Address,City or Town,State,Zipcode,Phone Number,Email,Website

#12345678           
        # This_SETS_A_DICTIONARY_OF_DICTIONARIES_GLOBAL given a dict_file_ as input
        # NOTE: It looks like Process_Dict_File uses the dict_file_ GLOBAL so be aware.
        inst_this_merger_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        self.SELECTED_DICT_OF_DICT_GLOBAL = inst_this_merger_loaded_Process_Dict_File.read_target_dict_file()
        # kick the main thread after the merger to update the main screen
        kick_thread_to_update_main_entry_widgets = True   # (to update main screen widgets)

        # print(".... ")
        # print(".... NEW MERGED DICT GLOBAL:  fullpath_fn_dict_filename_global = " + str(fullpath_fn_dict_filename_global) )
        # print(".... ")


        # Note for future code features:
        #
        # http://treyhunner.com/2016/02/how-to-merge-dictionaries-in-python/
        # context = defaults.copy()
        # context.update(user)

#12345678
        # Finally, we count the RECORDS in our MERGED dict_file_ to display to the USER
        # in the LBOX2 TWO for USER Feedback during the MERGE WORKFLOW:  
        #
        ###################################################################################
        # 
        # This section of code opens the MERGED dict_file and counts the RECORDS
        # to display this to the USER in LBOX TWO for USER Feedback during MERGE WORKFLOW.

        textFile_merged = open(fullpath_fn_dict_filename_global, 'r')

        # This takes the file object opened with the open() and turns it into a string which 
        # we can use o read the number of RECORDS in the DICTIONARY FILE.  
        textString_merged = textFile_merged.read()

        textFile_merged.close()

        # Count the DATA RECORDS in the string by counting the 
        # number of "DATA_RECORD_DELIMITER:" patterns  
        number_of_merged_data_records = textString_merged.count("DATA_RECORD_DELIMITER:")

        ########################################################################################################
        #
        #  D I S P L A Y    M I S S I N G     D A T A B A S E   F I L E S    S T A T U S    T O   L B O X  2
        #
        ########################################################################################################
        #
        # Write os isfile STATUS Strings List to END of LBOX TWO - - OS_ISFILE_FALSE_STATUS_LIST 
        #
        ########################################################################################################

        self.lbox_Source_Contacts.insert(END, "-----------------------------------------------------------------------" )
        self.lbox_Source_Contacts.insert(END, "                Missing Database Files Summary: " )
        self.lbox_Source_Contacts.insert(END, "-----------------------------------------------------------------------" )

        for os_isfile_status_string in OS_ISFILE_FALSE_STATUS_LIST:
            self.lbox_Source_Contacts.insert(END, str(os_isfile_status_string) )
        

        # Write DICTIONARY RECORD COUNT TO LBOX TWO ......
        self.lbox_Source_Contacts.insert(0, "-----------------------------------------------------------------------" )
        self.lbox_Source_Contacts.insert(0, "MERGED RECORDS:  " + str(number_of_merged_data_records) )
        self.lbox_Source_Contacts.insert(0, "-----------------------------------------------------------------------" )
        self.lbox_Source_Contacts.insert(0, "------------------ TOTAL_Data_Records -------------------" )
        self.lbox_Source_Contacts.insert(0, "-----------------------------------------------------------------------" )

        ###############################################################
        #
        #  WRITE MERGED CONTACT LIST to LISTBOX THREE 
        #
        ###############################################################

        # Set New MERGED dict_file file fullpath as INPUT to Contact String Generator. 
        self.selected_source_contact_dict_list = fullpath_fn_dict_filename_global

        # Generatea LIST of Contact Strings to Display in LISTBOX THREE 
        list_of_strings_for_merged_contacts = self.Input_Dict_Filename_Output_Source_Contacts_to_LISTBOX()

        for merged_contact_string in list_of_strings_for_merged_contacts:

            self.lbox_Destination_Contacts.insert(END, str(merged_contact_string) )

        self.lbox_Destination_Contacts.insert(0, "-----------------------------------------------------------------------" )
        self.lbox_Destination_Contacts.insert(0, "MERGED RECORDS:  " + str(number_of_merged_data_records) )
        self.lbox_Destination_Contacts.insert(0, "-----------------------------------------------------------------------" )
        self.lbox_Destination_Contacts.insert(0, "------------------ MERGED CONTACTS -------------------" )
        self.lbox_Destination_Contacts.insert(0, "-----------------------------------------------------------------------" )
  

        ############################################################################
        #
        #  NEW CODE TESTING HERE:
        # 
        #  Input:   contact_dict_of_dict_object   and  contact_list_name
        # 
        #  Output:  fullpath_fn_dict_filename_global  
        #
        ############################################################################
        #
        # class Write_Dict_File(object):
        #    def __init__(self, contact_dict_of_dict_object, contact_list_name):
        #
        ############################################################################
        # 
        #  NEW CODE TESTING HERE: 
        # 
        #  INPUT is  self.SELECTED_DICT_OF_DICT_GLOBAL = selected_dictionary_loaded_global
        #  This_Writes a dict_ file given a DICTIONARY_OF_DICTIONARIES_GLOBAL Object:
        #
        # inst_this_merger_Write_Dict_File = Write_Dict_File(selected_dictionary_loaded_global, self.BUILDING_NEW_LIST_NAME_ONLY)
        # writes_dict_file_sets_global = inst_this_merger_Write_Dict_File.write_target_dict_file()
        #
        ############################################################################

        # write a new logfile to update the logfile items each time a new Contact List is Created
        inst_Write_Main_Logfile_when_MERGE_new_list = Write_Main_Logfile()
        inst_Write_Main_Logfile_when_MERGE_new_list.write_update_logfile()

        # print("\n") 
        # print(".... VERIFY dict_file_GLOBAL - fullpath_fn_dict_filename_global \n.... M E R G E D   D I C T I O N A R Y   C O M P L E T E D  ....... \n.... SELECTED and LOADED - fullpath_fn_dict_filename_global =  \n" + str(fullpath_fn_dict_filename_global) )
        # print("\n")

        # print("\n") 
        # print(".... DICT FILE MERGED - dict_file_merge_fullpath  \n.... M E R G E D   D I C T I O N A R Y   C O M P L E T E D  ....... \n.... SELECTED and LOADED - fullpath_fn_dict_filename_global =  \n" + str(dict_file_merge_fullpath) )
        # print("\n")


        #######################################################################################
        #  
        # ***** Generate CONTACT LIST BUILD COMPLETE STATUS TO ENTRY WIDGET or TEXTBOX
        #  

        # print(".... str(self.BUILDING_NEW_LIST_NAME_ONLY) = " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )
        
        final_build_status_TEXT = "New List Ready: " + str(self.BUILDING_NEW_LIST_NAME_ONLY)

        self.final_build_status_text_box.delete(1.0, END)
        self.final_build_status_text_box.insert(END, final_build_status_TEXT)

        # Optionally, also Signal that the Build_List has Completed.
        self.signal_list_built_complete()

        # set back to neutral colors
        self.my_cm_filename_entry.config(background = "cyan4")
        self.completed_new_contact_list_name_button.config(background = "cyan4")

        # set to final success colors to show BUILD LIST COMPLETED
        self.create_the_new_dictionary_button.config(background = "cyan4")
        self.final_build_status_text_box.config(background = "cyan")
         
        #
        #  FINALLY, WE SWITCH BACK TO THE WORKFLOW CANVAS WIDGET ..... 
        #
        self.draw_WorkFlow_Canvas_Widget()




    ############################################################################
    #
    # Add Contact List Names selected from the MAIN Listbox to List.
    # Use Shift Key to select a group of contact lists from MAIN Listbox
    # and process their associated DICIONARY Files according to the
    # selected WORKFLOW Task.
    #
    # We save the list of indexes selected here:
    #
    # self.MAIN_LISTBOX_SEL_LIST = [] 
    #
    # We save the list of Contact List Names here:
    # 
    # self.MAIN_LISTBOX_SEL_LIST_VALUES = [] 
    #
    def GET_LBOX_MAIN_curselection_method(self):

        self.LB_1_curselection_tuple = ()
        self.LB_1_curselection_list = []


        # Test this Listbox Selection to Verify SOMETHING is actually selected.
        # If NOTHING is selected, display a messagebox to the USER. 
        verify_listbox_selection = self.lbox.curselection()

        try:
               test_cm_filename_value = str(self.lbox.get(verify_listbox_selection[0] ) )
        except IndexError as err:

            source_file_status_TEXT = "ATTENTION: SELECT Contact List from LISTBOX."

            self.source_file_status_text_box.delete(1.0, END)
            self.source_file_status_text_box.insert(END, source_file_status_TEXT)

            self.source_file_status_text_box.config(background = "goldenrod")
            self.source_file_status_text_box.after(500, lambda: self.source_file_status_text_box.config(bg="cyan")) # after 500ms
            self.source_file_status_text_box.after(1000, lambda: self.source_file_status_text_box.config(bg="goldenrod")) # after 500ms
            self.source_file_status_text_box.after(1500, lambda: self.source_file_status_text_box.config(bg="cyan")) # after 500ms
            self.source_file_status_text_box.after(2000, lambda: self.source_file_status_text_box.config(bg="goldenrod")) # after 500ms
            self.source_file_status_text_box.after(2500, lambda: self.source_file_status_text_box.config(bg="cyan")) # after 500ms
            self.source_file_status_text_box.after(3000, lambda: self.source_file_status_text_box.config(bg="goldenrod")) # after 500ms
            self.source_file_status_text_box.after(3500, lambda: self.source_file_status_text_box.config(bg="cyan")) # after 500ms
            self.source_file_status_text_box.after(4000, lambda: self.source_file_status_text_box.config(bg="goldenrod")) # after 500ms
            self.source_file_status_text_box.after(4500, lambda: self.source_file_status_text_box.config(bg="cyan")) # after 500ms
            self.source_file_status_text_box.after(5000, lambda: self.source_file_status_text_box.config(bg="goldenrod")) # after 500ms
            self.source_file_status_text_box.after(5500, lambda: self.source_file_status_text_box.config(bg="cyan")) # after 500ms
            self.source_file_status_text_box.after(6000, lambda: self.source_file_status_text_box.config(bg="goldenrod")) # after 500ms
            self.source_file_status_text_box.after(6500, lambda: self.source_file_status_text_box.config(bg="cyan")) # after 500ms
            
            return


        self.LB_1_curselection_tuple = self.lbox.curselection()
        self.LB_1_curselection_list = list(self.LB_1_curselection_tuple)

        # print(".... self.LB_1_curselection_list = " + str(self.LB_1_curselection_list) )

        # Append and then delete duplicates (using the set properties) because 
        # we are going to use this list to write our new contact list DICTIONARY.  
        self.LISTBOX_SEL_LIST.extend(self.LB_1_curselection_list)
        self.MAIN_LISTBOX_SEL_LIST.extend(self.LB_1_curselection_list)
        
        LIST_with_duplicates_removed = list(set(self.LISTBOX_SEL_LIST))
        self.LISTBOX_SEL_LIST = LIST_with_duplicates_removed
        self.MAIN_LISTBOX_SEL_LIST = LIST_with_duplicates_removed

        # NOTE: self.LISTBOX_SEL_LIST = self.MAIN_LISTBOX_SEL_LIST 

        self.LISTBOX_SEL_LIST_VALUES = []
        self.MAIN_LISTBOX_SEL_LIST_VALUES = []

        count_list_position = 0
        for item in self.MAIN_LISTBOX_SEL_LIST:

              # print(".... item in self.MAIN_LISTBOX_SEL_LIST = " + str(item) )
              self.MAIN_LISTBOX_SEL_LIST_VALUES.append(self.lbox.get(self.MAIN_LISTBOX_SEL_LIST[count_list_position]) )
              count_list_position+=1

        # print("   ")
        # print(".... self.MAIN_LISTBOX_SEL_LIST_VALUES = " + str(self.MAIN_LISTBOX_SEL_LIST_VALUES) )
        # print("   ")



        # NOTE:  List_of_Build_List_Modes = ["Build List", "Merge List", "Copy List", "Rename List"]
        # 
        # mode_select_build_list_global = .....   

        if mode_select_build_list_global == "Build List":

              source_file_status_TEXT = "Selected LIST: " + str(self.MAIN_LISTBOX_SEL_LIST_VALUES[0])

              # Update the LBOX ONE Status Textbox according to the MODE.
              # See mode_select_build_list_global message above.
              self.source_file_status_text_box.delete(1.0, END)
              self.source_file_status_text_box.insert(END, source_file_status_TEXT)

              # set back to neutral colors 
              self.select_file_button.config(background = "cyan4")

              self.source_file_status_text_box.config(background = "cyan")
              self.source_file_status_text_box.after(1000, lambda: self.source_file_status_text_box.config(bg="cyan4")) # after 1000ms

              # set entry widget to cyan to focus user on next task to enter contact list name.
              self.my_cm_filename_entry.config(background = "cyan")
              self.completed_new_contact_list_name_button.config(background = "light sea green")

              # Emphasize the color of this Button so USER knows to get SOURCE Listbox Items 

              self.GET_LBOX_SOURCE_curselection_Button.config(background="cyan")

              self.final_build_status_text_box.config(background="goldenrod")

              # Emphasize the color of this Button 
              # because the USER has NOT selected ANY CONACTS or SOURCE Listbox Items 

              self.GET_LBOX_SOURCE_curselection_Button.config(background="goldenrod")

              final_build_status_TEXT = "Use ADD to LIST Button to ADD Contacts."

              self.final_build_status_text_box.delete("1.0", END)

              self.final_build_status_text_box.insert(END, final_build_status_TEXT)

              #  EXECUTE BUILD LIST WORKFLOW .......
              self.execute_BUILD_LIST_WORKFLOW()


        elif mode_select_build_list_global == "Merge List":

              source_file_status_TEXT = "Lists to MERGE Selected ...."

              # Update the LBOX ONE Status Textbox according to the MODE.
              # See mode_select_build_list_global message above.
              self.source_file_status_text_box.delete(1.0, END)
              self.source_file_status_text_box.insert(END, source_file_status_TEXT)

              # set back to neutral colors 
              self.select_file_button.config(background = "cyan4")

              self.source_file_status_text_box.config(background = "cyan")
              self.source_file_status_text_box.after(1000, lambda: self.source_file_status_text_box.config(bg="cyan4")) # after 1000ms

              # set entry widget to cyan to focus user on next task to enter contact list name.
              self.my_cm_filename_entry.config(background = "cyan")
              self.completed_new_contact_list_name_button.config(background = "light sea green")

              # Note that the LISTBOX TWO Command Button and LISTBOX THREE Command Button
              # control the execution of the MERGE WORKFLOW of the files already acquired
              # in self.MAIN_LISTBOX_SEL_LIST_VALUES.  

              # Display the LIST of Files Selected from LISTBOX ONE, self.MAIN_LISTBOX_SEL_LIST_VALUES,
              # as a WORKFLOW FEEDBACK in LISTBOX TWO at this time in the Program Execution:

              number_of_lists_selected_for_MERGE = len(self.MAIN_LISTBOX_SEL_LIST_VALUES)

              # Clear Listbox to prepare to write MERGE WORKFLOW Feedback.
              self.lbox_Source_Contacts.delete(0, END)

              self.lbox_Source_Contacts.insert(END, "-----------------------------------------------------------------------" )

              count_each_list = 0
              count_each_list_number = 1
              for each_file_to_merge in self.MAIN_LISTBOX_SEL_LIST_VALUES:

                  # Display WORKFLOW FEEDBACK in LISTBOX TWO

                  # Form Dictionary Filename for each Contact List Name
                  merge_list_dict_filename = "dict_file_" + str(self.MAIN_LISTBOX_SEL_LIST_VALUES[count_each_list]) + ".txt"

                  merge_list_dict_fullpath = os.path.join(str(cm_appdatafiles_path_global), str(merge_list_dict_filename) )

                  with open(merge_list_dict_fullpath, "r") as read_file_handle:
                      read_file_handle.flush()
                      dict_file_TEXT_STRING = read_file_handle.read()

                  # Count the DATA RECORDS in the string by counting the
                  # number of "DATA_RECORD_DELIMITER:" patterns 
                  num_data_records = dict_file_TEXT_STRING.count("DATA_RECORD_DELIMITER:")
                    
                  # Write CONTACT LISTS READY TO MERGE USER MESSAGE TO LBOX TWO ......

                  self.lbox_Source_Contacts.insert(END, "List #" + str(count_each_list_number) + " Rec: " + str(num_data_records) + " - " + str(self.MAIN_LISTBOX_SEL_LIST_VALUES[count_each_list]) )

                  count_each_list+=1
                  count_each_list_number+=1

              # After the Loop, Write HEADING for CONTACT LISTS READY TO MERGE USER MESSAGE TO LBOX TWO ......
              self.lbox_Source_Contacts.insert(0, "-----------------------------------------------------------------------" )
              self.lbox_Source_Contacts.insert(0, "Merging " + str(number_of_lists_selected_for_MERGE) + " Contact Lists:")
              self.lbox_Source_Contacts.insert(0, "-----------------------------------------------------------------------" )
              self.lbox_Source_Contacts.insert(0, "------- CONTACT LISTS Selected to MERGE --------" )
              self.lbox_Source_Contacts.insert(0, "-----------------------------------------------------------------------" )

        elif mode_select_build_list_global == "Copy List":

              source_file_status_TEXT = "Selected LIST: " + str(self.MAIN_LISTBOX_SEL_LIST_VALUES[0])

              # Update the LBOX ONE Status Textbox according to the MODE.
              # See mode_select_build_list_global message above.
              self.source_file_status_text_box.delete(1.0, END)
              self.source_file_status_text_box.insert(END, source_file_status_TEXT)

              # set back to neutral colors 
              self.select_file_button.config(background = "cyan4")

              self.source_file_status_text_box.config(background = "cyan")
              self.source_file_status_text_box.after(1000, lambda: self.source_file_status_text_box.config(bg="cyan4")) # after 1000ms

              # set entry widget to cyan to focus user on next task to enter contact list name.
              self.my_cm_filename_entry.config(background = "cyan")
              self.completed_new_contact_list_name_button.config(background = "light sea green")



              
        ################################################################################################
        # 
        #   A T T E N T I O N   . . . . .   
        #
        # Note: Remember, the USER may do a few go arounds when selecting Contact Lists
        # from the MAIN Listbox, so we want to give USER FEEDBACK (in LISTBOX 2 for example)
        # and also in the STATUS TEXT Widget above the MAIN Listbox as to how many Contact Lists
        # they selected and what the Contact List Names are.
        #
        ################################################################################################

        return self.MAIN_LISTBOX_SEL_LIST_VALUES
        
        
    # Add Contacts to List.
    # Use Shift Key to select a group of contacts from Source Listbox and add them to
    # the new contact list in Destination Listbox.  
    # Selects from Source Listbox and Copies to Destination Listbox. 
    # We save the list of indexes selected to use when building  
    # our new DICTIONARY OF DICTIONARIES for the new contact list Database.
    def GET_LBOX_SOURCE_curselection_method(self):

        self.LB_2_curselection_tuple = ()
        self.LB_2_curselection_list = []
          
        self.LB_2_curselection_tuple = self.lbox_Source_Contacts.curselection()
        self.LB_2_curselection_list = list(self.LB_2_curselection_tuple)

        # Append and then delete duplicates (using the set properties) because 
        # we are going to use this list to write our new contact list DICTIONARY.  
        self.SOURCE_LISTBOX_SEL_LIST.extend(self.LB_2_curselection_list)
        LIST_with_duplicates_removed = list(set(self.SOURCE_LISTBOX_SEL_LIST))
        self.SOURCE_LISTBOX_SEL_LIST = LIST_with_duplicates_removed

        # Renamed this here so we update the old variable self.LISTBOX_SEL_LIST too 
        # because we are using that to build the new DICTIONARY Database.
        self.LISTBOX_SEL_LIST = self.SOURCE_LISTBOX_SEL_LIST

        # print("  ")
        # print(".... self.LB_2_curselection_list = " + str(self.LB_2_curselection_list) )
        # print("  ")
        # print(".... self.SOURCE_LISTBOX_SEL_LIST = " + str(self.SOURCE_LISTBOX_SEL_LIST) )
        # print("  ")

        # Example: self.LB_2_curselection_tuple = (3, 4, 5)   - acquired with SHIFT KEY
        # Example: self.LB_2_curselection_list = [3, 4, 5]   - converted tuple to list

        # Remember we are re-writing a NEW DESTINATION LISTBOX with this next OBJECT
        # and since we just re-calculated the indexes and removed duplicates, 
        # we start with a blank list of values and re-build our class object for
        # self.SOURCE_LISTBOX_SEL_LIST_VALUES 

        self.SOURCE_LISTBOX_SEL_LIST_VALUES = []

        count_list_position = 0
        for item in self.SOURCE_LISTBOX_SEL_LIST:

              # print(".... item in self.SOURCE_LISTBOX_SEL_LIST = " + str(item) )
              self.SOURCE_LISTBOX_SEL_LIST_VALUES.append(self.lbox_Source_Contacts.get(self.SOURCE_LISTBOX_SEL_LIST[count_list_position]) )
              count_list_position+=1

        # Notice we are DELETING all data in the LISTBOX because we have computed
        # a new list of values. Then inserting at the END of the Listbox.
        # Review all code to adjust the insert to be at the END of the Listbox.
        # ***** CLEAR THE DESINATION LISTBOX HERE, AND RE-WRITE THE DESTINATION LISTBOX
        # AS WE COMPUTED NEW LIST OF VALUES ***** 
        self.lbox_Destination_Contacts.delete(0, END)
        self.DICT_LB3_LB2_INDEX_VALUES = {}
        
        count_list_position = 0
        for item in self.SOURCE_LISTBOX_SEL_LIST:

              # Maintain (update) each time we re-write) the current KEY-VALUE DICTIONARY of the mapping 
              # of the mapping between LB2 INDEX LIST and LB3 LISTBOX ITEM: self.LB3_LB2_INDEX_VALUES
              # key = count_list_position
              # value = item
              self.DICT_LB3_LB2_INDEX_VALUES[count_list_position] = item

              self.lbox_Destination_Contacts.insert(END, self.SOURCE_LISTBOX_SEL_LIST_VALUES[count_list_position])
              count_list_position+=1

        # print("  ")
        # print(".... self.LB_2_curselection_list = " + str(self.LB_2_curselection_list ) )
        # print("  ")
        # print(".... self.SOURCE_LISTBOX_SEL_LIST = " + str(self.SOURCE_LISTBOX_SEL_LIST) )
        # print("  ")
        # print(".... self.SOURCE_LISTBOX_SEL_LIST_VALUES = " + str(self.SOURCE_LISTBOX_SEL_LIST_VALUES) )
        # print("  ")
        # print(".... self.DICT_LB3_LB2_INDEX_VALUES = " + str(self.DICT_LB3_LB2_INDEX_VALUES) )
        # print("  ")

              
#.... selection = widget.curselection() = (5,)
#.... contact_string_value = widget.get(selection[0]) = Bill8 MMM8 theirmail@gmail.com8


    # Remove or Delete Contacts from List. 
    # Use Shift Key to select a group of contacts from Destination Listbox
    # remove or delete them from the new contact list in Destination Listbox.
    # Selects from Destination Listbox and removes or deletes them from Destination Listbox.
    # At this time, we must remove these selected indexes from the Source Listbox list of indexes
    # so that they are not included or used when building our new  
    # DICTIONARY OF DICTIONARIES for the new contact list Database.
    def GET_LBOX_DESTINATION_curselection_method(self):

        self.LB_3_curselection_tuple = ()
        self.LB_3_curselection_list = []
          
        self.LB_3_curselection_tuple = self.lbox_Destination_Contacts.curselection()
        self.LB_3_curselection_list = list(self.LB_3_curselection_tuple)

        # print("  ")
        # print(".... self.LB_3_curselection_list = " + str(self.LB_3_curselection_list ) )
        # print("  ")


        REMOVE_THESE_LB2_INDEXES_LIST = []

        count_the_index = 0
        for item in self.LB_3_curselection_list:

              REMOVE_THESE_LB2_INDEXES_LIST.append(self.DICT_LB3_LB2_INDEX_VALUES[item] )

              count_the_index+=1
                    
        # Example: self.LB_3_curselection_tuple = (2, 3, 4, 5)   - acquired with SHIFT KEY
        # Example: self.LB_3_curselection_list = [2, 3, 4, 5]   - converted tuple to list

        # To remove or delete items from the DESTINATION LISTBOX, we start by
        # taking our current self.SOURCE_LISTBOX_SEL_LIST and converting it
        # to a SET so we can subtract the SET of DESTINATION (LB3) items.
        
        LB_2_Set = set(self.SOURCE_LISTBOX_SEL_LIST)
        REMOVE_THESE_LB2_INDEXES_LIST_Set = set(REMOVE_THESE_LB2_INDEXES_LIST)

        NEW_LB_2_Set = LB_2_Set - REMOVE_THESE_LB2_INDEXES_LIST_Set

        # print("  ")
        # print(".... LB_2_Set = " + str(LB_2_Set) )
        # print(".... REMOVE_THESE_LB2_INDEXES_LIST_Set = " + str(REMOVE_THESE_LB2_INDEXES_LIST_Set) )
        # print(".... NEW_LB_2_Set = " + str(NEW_LB_2_Set) )
        # print("  ")

        self.SOURCE_LISTBOX_SEL_LIST = list(NEW_LB_2_Set)

        # Renamed this here so we update the old variable self.LISTBOX_SEL_LIST too 
        # because we are using that to build the new DICTIONARY Database. 
        self.LISTBOX_SEL_LIST = self.SOURCE_LISTBOX_SEL_LIST
        
        # Remember we are re-writing a NEW DESTINATION LISTBOX with this next OBJECT
        # and since we just re-calculated the indexes and removed duplicates, 
        # we start with a blank list of values and re-build our class object for
        # self.SOURCE_LISTBOX_SEL_LIST_VALUES 

        self.SOURCE_LISTBOX_SEL_LIST_VALUES = []

        count_list_position = 0
        for item in self.SOURCE_LISTBOX_SEL_LIST:

              # print(".... item in self.SOURCE_LISTBOX_SEL_LIST = " + str(item) )
              self.SOURCE_LISTBOX_SEL_LIST_VALUES.append(self.lbox_Source_Contacts.get(self.SOURCE_LISTBOX_SEL_LIST[count_list_position]) )
              count_list_position+=1


        # Notice we are DELETING all data in the LISTBOX because we have computed
        # a new list of values. Then inserting at the END of the Listbox.
        # Review all code to adjust the insert to be at the END of the Listbox.
        # ***** CLEAR THE DESINATION LISTBOX HERE, AND RE-WRITE THE DESTINATION LISTBOX
        # AS WE COMPUTED NEW LIST OF VALUES *****  
        self.lbox_Destination_Contacts.delete(0, END)
        self.DICT_LB3_LB2_INDEX_VALUES = {}
        
        count_list_position = 0
        for item in self.SOURCE_LISTBOX_SEL_LIST:

              # Maintain (update) each time we re-write) the current KEY-VALUE DICTIONARY of the mapping 
              # of the mapping between LB2 INDEX LIST and LB3 LISTBOX ITEM: self.LB3_LB2_INDEX_VALUES
              # key = count_list_position
              # value = item
              self.DICT_LB3_LB2_INDEX_VALUES[count_list_position] = item

              self.lbox_Destination_Contacts.insert(END, self.SOURCE_LISTBOX_SEL_LIST_VALUES[count_list_position])
              count_list_position+=1


        # print("  ")
        # print(".... self.LB_3_curselection_items = " + str(self.LB_3_curselection_list ) )
        # print("  ")
        # print(".... self.SOURCE_LISTBOX_SEL_LIST = " + str(self.SOURCE_LISTBOX_SEL_LIST) )
        # print("  ")
        # print(".... self.SOURCE_LISTBOX_SEL_LIST_VALUES = " + str(self.SOURCE_LISTBOX_SEL_LIST_VALUES) )
        # print("  ")

        ###########################################################################################

        # View the self.DICT_LB3_LB2_INDEX_VALUES to see the LB2 INDEXES
        # in each LB3 potential selection (i.e. 0,1,2,3,etc).

        # VIEW_THE_LB2_INDEXES_LIST = []
        # VIEW_THE_LB3_SEL_LIST  = []
        # read_value_from_dictionary = 0

        # see_the_index = 0
        # for item in self.SOURCE_LISTBOX_SEL_LIST:

        #      read_value_from_dictionary = self.DICT_LB3_LB2_INDEX_VALUES[see_the_index]

        #      VIEW_THE_LB2_INDEXES_LIST.append(read_value_from_dictionary)

        #      VIEW_THE_LB3_SEL_LIST.append(see_the_index)

        #      see_the_index+=1

        # print(".... ****** VIEW_THE_LB3_SEL_LIST    :  " + str(VIEW_THE_LB3_SEL_LIST) )
        # print(".... ****** VIEW_THE_LB2_INDEXES_LIST:  " + str(VIEW_THE_LB2_INDEXES_LIST) )
        
        ###########################################################################################




    def execute_COPY_LIST_WORKFLOW(self):
          
        ###################################################################################
        # 
        #  METHOD:  execute_COPY_LIST_WORKFLOW 
        # 
        ###################################################################################
        #
        #  Try to Copy LISTBOX ONE Selected File to Filename entered
        #  by USER to ENTRY WIDGET above LISTBOX TWO.  
        #
        ###################################################################################


        contact_list_name = str(self.MAIN_LISTBOX_SEL_LIST_VALUES[0])

        contact_list_dict_file_name = "dict_file_" + str(contact_list_name) + ".txt"

        contact_list_cm_list_file_name = "cm_list_" + str(contact_list_name) + ".txt"

        contact_list_cnotes_file_name = "cnotes_" + str(contact_list_name) + ".txt"

        # Get New Contact List Name from enter_new_contact_list_name below. 
        dest_list_name = self.BUILDING_NEW_LIST_NAME_ONLY

        dest_list_dict_file_name = "dict_file_" + str(dest_list_name) + ".txt"

        dest_list_cm_list_file_name = "cm_list_" + str(dest_list_name) + ".txt"

        dest_list_cnotes_file_name = "cnotes_" + str(dest_list_name) + ".txt"

#12345678          
        try:
              
            self.COPY_LIST_SOURCE_FULLPATH = os.path.join(str(cm_appdatafiles_path_global), str(contact_list_dict_file_name) )

            self.COPY_LIST_DESTINATION_FULLPATH = os.path.join(str(cm_appdatafiles_path_global), str(dest_list_dict_file_name) )

            verify_dict_with_os_isfile = str(self.COPY_LIST_DESTINATION_FULLPATH)
              
            shutil.copyfile(str(self.COPY_LIST_SOURCE_FULLPATH), str(self.COPY_LIST_DESTINATION_FULLPATH) )

        except Exception:
            pass

            
            # print("   ")
            # print(".... CONTACT LIST COPY FROM:  \n" + str(self.COPY_LIST_SOURCE_FULLPATH) + "\n TO \n" + str(self.COPY_LIST_DESTINATION_FULLPATH) ) 

#12345678          
        try:
              
            self.COPY_LIST_SOURCE_FULLPATH = os.path.join(str(cm_appdatafiles_path_global), str(contact_list_cm_list_file_name) )

            self.COPY_LIST_DESTINATION_FULLPATH = os.path.join(str(cm_appdatafiles_path_global), str(dest_list_cm_list_file_name) )

            verify_cm_list_with_os_isfile = str(self.COPY_LIST_DESTINATION_FULLPATH)

            shutil.copyfile(str(self.COPY_LIST_SOURCE_FULLPATH), str(self.COPY_LIST_DESTINATION_FULLPATH) )

        except Exception:
            pass


#12345678          
        try:
              
            self.COPY_LIST_SOURCE_FULLPATH = os.path.join(str(cm_appdatafiles_path_global), str(contact_list_cnotes_file_name) )

            self.COPY_LIST_DESTINATION_FULLPATH = os.path.join(str(cm_appdatafiles_path_global), str(dest_list_cnotes_file_name) )

            verify_cnotes_with_os_isfile = str(self.COPY_LIST_DESTINATION_FULLPATH)

            shutil.copyfile(str(self.COPY_LIST_SOURCE_FULLPATH), str(self.COPY_LIST_DESTINATION_FULLPATH) )
            
        except Exception as cnotes_file_err:
            # print(".... **** ERROR **** EXCEPTION cnotes - shutil.copyfile(str(self.COPY_LIST_SOURCE_FULLPATH), str(self.COPY_LIST_DESTINATION_FULLPATH) ) \n" + str(cnotes_file_err) )  
            pass


        # Verify CONTACT LIST DATABASE FILES COPIED 
        # using os.path.isfile and display status in LISTBOX THREE.
#12345678          
        try:
            TF_dict = os.path.isfile(str(verify_dict_with_os_isfile) )
        except Exception:
            pass
#12345678          
        try:
            TF_cm_list = os.path.isfile(str(verify_cm_list_with_os_isfile) )
        except Exception:
            pass
#12345678          
        try:
            TF_cnotes = os.path.isfile(str(verify_cnotes_with_os_isfile) )
        except Exception as cnotes_err:
            # print(".... **** ERROR **** EXCEPTION cnotes - os.path.isfile(str(verify_cnotes_with_os_isfile) ) \n" + str(cnotes_err) )  
            pass
        

        self.lbox_Destination_Contacts.delete(0, END)

        self.lbox_Destination_Contacts.insert(END, " ")
        self.lbox_Destination_Contacts.insert(END, "Dictionary Database Created:  " + str(TF_dict) )
        self.lbox_Destination_Contacts.insert(END, " ")
        self.lbox_Destination_Contacts.insert(END, "CSV Database Created:  " + str(TF_cm_list) )
        self.lbox_Destination_Contacts.insert(END, " ")
        self.lbox_Destination_Contacts.insert(END, "Contact Notes Database Created:  " + str(TF_cnotes) )
        self.lbox_Destination_Contacts.insert(END, " ")

        # Write HEADING for CONTACT LISTS READY TO MERGE USER MESSAGE TO LBOX TWO ......
        self.lbox_Destination_Contacts.insert(0, "-----------------------------------------------------------------------" )
        self.lbox_Destination_Contacts.insert(0, " Database Verified with:  os.path.isfile")
        self.lbox_Destination_Contacts.insert(0, "-----------------------------------------------------------------------" )
        self.lbox_Destination_Contacts.insert(0, " L I S T:   " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )
        self.lbox_Destination_Contacts.insert(0, "-----------------------------------------------------------------------" )
        self.lbox_Destination_Contacts.insert(0, "                 CONTACT LIST COPY            " )
        self.lbox_Destination_Contacts.insert(0, "-----------------------------------------------------------------------" )

        
        final_build_status_TEXT = "New List Ready: " + str(self.BUILDING_NEW_LIST_NAME_ONLY)

        self.final_build_status_text_box.delete(1.0, END)
        self.final_build_status_text_box.insert(END, final_build_status_TEXT)

        # Optionally, also Signal that the Build_List has Completed.
        self.signal_list_built_complete()

        # set back to neutral colors
        self.my_cm_filename_entry.config(background = "cyan4")
        self.completed_new_contact_list_name_button.config(background = "cyan4")

        # set to final success colors to show BUILD LIST COMPLETED
        self.create_the_new_dictionary_button.config(background = "cyan4")
        self.final_build_status_text_box.config(background = "cyan")
         
        #######################################################################################
        # 
        #  FINALLY, WE SWITCH BACK TO THE WORKFLOW CANVAS WIDGET .....  
        #
        self.draw_WorkFlow_Canvas_Widget()

        return



    def enter_new_contact_list_name(self):
        global mode_select_build_list_global
        #########################################################################################
        # 
        # List_of_Build_List_Modes = ["Build List", "Merge List", "Copy List", "Rename List"]
        #
        # global mode_select_build_list_global
        #
        #########################################################################################
        # 
        # Introducing a FLAG called: button_set_filename_entry_to_status = True/False
        # to track and check whether the filename ENTRY WIDGET contains:
        #
        #      FILENAME (possibly)    or     STATUS   
        #
        #########################################################################################

        # print(".... RUNNING  METHOD  enter_new_contact_list_name\nwith self.button_set_filename_entry_to_status = " + str(self.button_set_filename_entry_to_status) )

        if self.button_set_filename_entry_to_status == False:

            self.button_set_filename_entry_to_status = True

            # maintain (cyan entry widget) focus on this listbox as we select contacts,
            # as the new file name has now been created, to encourage building contacts. 
            self.my_cm_filename_entry.config(background = "cyan")
            self.completed_new_contact_list_name_button.config(background = "cyan4")

            # set to light sea green on next button to indicate to user on next task
            self.create_the_new_dictionary_button.config(background = "light sea green")
            self.final_build_status_text_box.config(background = "cyan4")            

            test_entry_value = ""

            test_entry_value = self.entry_CM_FILENAME.get()  # check instance or stringvar format

            if test_entry_value != "":
                self.BUILDING_NEW_LIST_NAME_ONLY = self.entry_CM_FILENAME.get()
                self.new_list_button_text.set("Click after Entering\nNEW CONTACT LIST NAME (Optional)\nName SET to " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )
                if mode_select_build_list_global == "Build List":
                    self.final_build_status_text_box.config(background = "goldenrod")  

            elif test_entry_value == "":
                time_string = time.strftime("%m-%d-%Y-%H%M%S")
                if mode_select_build_list_global == "Build List":
                    self.BUILDING_NEW_LIST_NAME_ONLY = "BUILD_LIST_" + str(time_string)
                    self.final_build_status_text_box.config(background = "goldenrod")  
                elif mode_select_build_list_global == "Copy List":
                    self.BUILDING_NEW_LIST_NAME_ONLY = "COPY_LIST_" + str(time_string)
                elif mode_select_build_list_global == "Rename List":
                    self.BUILDING_NEW_LIST_NAME_ONLY = "RENAME_LIST_" + str(time_string)
                    
                # print(".... self.BUILDING_NEW_LIST_NAME_ONLY = " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )
                
                self.new_list_button_text.set("Click after Entering\nNEW CONTACT LIST NAME (Optional)\nDefault Name = " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )

#123456789012
            created_list_string_status = "List Name: " + str(self.BUILDING_NEW_LIST_NAME_ONLY)
            self.entry_CM_FILENAME.set(created_list_string_status)

        elif self.button_set_filename_entry_to_status == True:

            pass
              


    def execute_BUILD_LIST_WORKFLOW(self):
        global cm_listbox_file_global
        global dict_filename_global
        global listbox_file_capture_global
        global cnotes_dict_file_global
        global fullpath_cnotes_dict_file_global
        global master_cm_list_name_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global kick_thread_to_update_main_entry_widgets

        #################################################################################################
        #
        # source_file_status_TEXT = "Selected LIST: " + str(self.MAIN_LISTBOX_SEL_LIST_VALUES[0])
        # 
        # self.execute_BUILD_LIST_WORKFLOW()  
        #
        #################################################################################################
        #
        #   A T T E N T I O N  :
        #
        #   Selected CONTACT LIST:    self.MAIN_LISTBOX_SEL_LIST_VALUES[0]
        #
        #################################################################################################

        # selection = self.lbox.curselection()
        # cm_textbox_newfile_global = self.lbox.get(selection[0])
        # master_cm_list_name_global = self.lbox.get(selection[0])
        # cm_filename_value = self.lbox.get(selection[0])

        selection = self.lbox.curselection()
        cm_textbox_newfile_global = self.MAIN_LISTBOX_SEL_LIST_VALUES[0]
        master_cm_list_name_global = self.MAIN_LISTBOX_SEL_LIST_VALUES[0]
        cm_filename_value = self.MAIN_LISTBOX_SEL_LIST_VALUES[0]

        # Create NEW FILES for the cm_list_CONTACT_LIST_NAME 
        # and dict_file_CONTACT_LIST_NAME Globals filenames
        cm_listbox_file_global = "cm_list_" + str(cm_textbox_newfile_global) + ".txt"
        dict_filename_global = "dict_file_" + str(cm_textbox_newfile_global) + ".txt"
        cnotes_dict_file_global = "cnotes_" + str(cm_textbox_newfile_global) + ".txt"

        # Create APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
        # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
        # which gives us the FULL PATH NAME to our contact_management.py data files.  
       
        fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
       
        fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )

        fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

        fullpath_prepend_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )
        

        # store_selected listbox filename - cm_filename_value in two classes
        lbfn_instance = Store_Lbox_Filename(selected_lbox_file = cm_filename_value)
        lbfn_instance.set_listbox_file(new_Lbox_File = cm_filename_value)
        get_lbfn_call = lbfn_instance.get_listbox_file()


        # print(".... master_cm_list_name_global = " + str(master_cm_list_name_global) )

        self.SOURCE_CONTACT_LIST_NAME_ONLY = str(master_cm_list_name_global)

        # print(".... self.SOURCE_CONTACT_LIST_NAME_ONLY = " + str(self.SOURCE_CONTACT_LIST_NAME_ONLY) )

        source_file_status_TEXT = "Selected List: " + str(self.SOURCE_CONTACT_LIST_NAME_ONLY)

        self.source_file_status_text_box.delete(1.0, END)
        self.source_file_status_text_box.insert(END, source_file_status_TEXT)

        # set back to neutral colors 
        self.select_file_button.config(background = "cyan4")
        self.source_file_status_text_box.config(background = "cyan4")

        # set entry widget to cyan to focus user on next task to enter contact list name.
        self.my_cm_filename_entry.config(background = "cyan")
        self.completed_new_contact_list_name_button.config(background = "light sea green")
      
        # Set listbox_file_capture_global to trigger Contact List Entry Textbox Update 
        # as we have completed registering all the Listbox Filename variable settings
        # We will reset this listbox_file_capture_global back to False after we  
        # update the Contact List Entry Textbox with the Listbox Filename selected 
        listbox_file_capture_global = True

        # UPDATE APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
        # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
        # which gives us the FULL PATH NAME to our contact_management.py data files.  
        
        fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
        
        fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )

        self.ORIGINAL_DICTIONARY_FILENAME = str(fullpath_fn_dict_filename_global)

        # This_SETS_A_DICTIONARY_OF_DICTIONARIES_GLOBAL  
        inst_original_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        self.SELECTED_DICT_OF_DICT_GLOBAL = inst_original_loaded_Process_Dict_File.read_target_dict_file()

        kick_thread_to_update_main_entry_widgets = True   # (to update main screen widgets)

        # print("\n") 
        # print(".... O R I G I N A L    D I C T I O N A R Y   -   self.ORIGINAL_DICTIONARY_FILENAME  =  \n" + str(self.ORIGINAL_DICTIONARY_FILENAME) )
        # print("\n") 

        # print(".... fullpath_fn_cm_listbox_file_global = " + str(fullpath_fn_cm_listbox_file_global) )

        # print(".... fullpath_fn_dict_filename_global = " + str(fullpath_fn_dict_filename_global) )

        self.selected_source_contact_cm_list = str(fullpath_fn_cm_listbox_file_global)
        
        self.selected_source_contact_dict_list = str(fullpath_fn_dict_filename_global)

        # print(".... self.selected_source_contact_dict_list = " + str(self.selected_source_contact_dict_list) )


        # This List will now be the List (of STRINGS) for whole CONTACT LIST - FIRST_NAME + LAST_NAME + EMAIL ...STRING

        #########################################################################
        # 
        # FROM - self.Input_Dict_Filename_Output_Source_Contacts_to_LISTBOX()
        #
        # Method return build_the_list_of_strings_for_contacts
        # 
        self.source_contacts_list_of_strings = self.Input_Dict_Filename_Output_Source_Contacts_to_LISTBOX()
        
        contact_list_for_listbox = []   # LIST OF STRINGS - FIRST_NAME + LAST_NAME + EMAIL

        contact_list_for_listbox = self.source_contacts_list_of_strings
        
        # Clear Source Contacts Listbox to prepare to insert Contacts
        # in the correct order - self.lbox_Source_Contacts.insert(END, each_contact)
        self.lbox_Source_Contacts.delete(0, END)

        for each_contact in contact_list_for_listbox:
              self.lbox_Source_Contacts.insert(END, each_contact)

        # Set listbox_file_capture_global to trigger Contact List Entry Textbox Update 
        # as we have completed registering all the Listbox Filename variable settings 
        # We will reset this listbox_file_capture_global back to False after we 
        # update the Contact List Entry Textbox with the Listbox Filename selected 
        listbox_file_capture_global = True
        
        # close listbox frame window after storing selected filename in Store_Lbox_Filename() Class
        # self.master.destroy()
        return cm_filename_value
          

   

    def get_Listbox_Source_Contact(self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global listbox_file_capture_global
        global cnotes_dict_file_global
        global fullpath_cnotes_dict_file_global
        global master_cm_list_name_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global kick_thread_to_update_main_entry_widgets
        # This button command gets the filename_value from
        # below (this Demo2 Class) and sets the
        # CONTACT LIST ENTRY BOX in the App Class
        # USING THE GLOBAL VARIABLE cm_listbox_file_global
        # AND THE LISTBOX WIDGET METHOD:   
        #     
        # cm_filename_value = widget.get(selection[0])
        #

        self.selected_contacts_list_of_strings = ""

        
        ######################################################
        #
        #  def OnListBoxSelect_Source_Contacts(self, event):
        #     global listbox_file_capture_global
        #     listbox_file_capture_global = "False"
        #     widget = event.widget
        #     selection = widget.curselection()
        #     filename_value = widget.get(selection)  # modified for string not filename here 
        #     selection_value_tuple = [selection, filename_value]
        #     return filename_value
        #
        # IMPORTANT:   *** Exception Handler ***
        #
        # This exception handler code captures the IndexError Exception that happens
        # if the USER (OPERATOR) does NOT select a Contact List
        # from the LISTBOX -- In that case:
        # we notify the operator with a messagebox and then we
        # self.master.destroy() and return to bring us back to
        # the main screen for another try. 

        verify_source_listbox_selection = self.lbox_Source_Contacts.curselection()

        try:
               test_cm_filename_value = str(self.lbox_Source_Contacts.get(verify_source_listbox_selection) )
        except IndexError as err:
               messagebox.showinfo("Contact Manager Guide ...", \
               "ATTENTION: \n\nPlease SELECT a CONTACT from the LISTBOX ..... \n\n OPERATOR ERROR (Index Error): \n" + str(err) )
               self.master.destroy()
               return


        selection = self.lbox_Source_Contacts.curselection()
        cm_filename_value = self.lbox_Source_Contacts.get(selection)
        cm_listbox_file_global = self.lbox_Source_Contacts.get(selection)

        return cm_filename_value
          

  
    #################################################################
    #
    # INPUT:   self.selected_source_contact_dict_list
    #
    # OUTPUT:   build_the_list_of_strings_for_contacts
    #
    #################################################################
    def Input_Dict_Filename_Output_Source_Contacts_to_LISTBOX(self):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global viewscreen_bg_color_val_global

        ###############################################################################
        #
        # Programming Note:
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)  ... for Text Widget ... Entry and Listbox are delete(0, END) 
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert
        #
        # for Text Widget ... Entry and Listbox are delete(0, END) 
        # 
        ###############################################################################

        # VIEW the TEXTBOX after loading the current
        # DICTIONARY Contact List File - dict_file_cm_listbox_file_global
        # which is stored in APPDATA at fullpath_fn_dict_filename_global

        # print(".... OPEN THIS NOW - self.selected_source_contact_dict_list = " + str(self.selected_source_contact_dict_list) )

        # print(".... OR .. OPEN THIS NOW - fullpath_fn_dict_filename_global = " + str(fullpath_fn_dict_filename_global) )

        # self.textFile = open(fullpath_fn_dict_filename_global, 'r')
        self.textFile = open(self.selected_source_contact_dict_list, 'r')

        # This takes the file object opened with the open() and turns it into a string which 
        # you can now use textString in a text widget.
        self.textString = self.textFile.read()

        # Close the Dictionary File 
        self.textFile.close()

        # Count the DATA RECORDS in the string by counting the
        # number of "DATA_RECORD_DELIMITER:" patterns 
        self.num_data_records = self.textString.count("DATA_RECORD_DELIMITER:")

        # TEXTBOX appears to have residual data upon startup button select VIEW CONTACTS, 
        # so we may have to check to see that a dictionary global is set to
        # an actual valid dictionary after being initialized to
        # dict_filename_global = "No Contact Dictionary"
        
        self.num_data_records_plus_one = self.num_data_records + 1
        # Operate on the textString to search for DATA_RECORD_DELIMITER: and KEY_SYNC: sub-strings
        
        build_the_list_of_strings_for_contacts = []
        
        for record_index in range (1, self.num_data_records_plus_one):
             
             self.data_record_string = self.textString.split("DATA_RECORD_DELIMITER:")[record_index]

             target_contact_string = ""
             fn_sub_string = ""
             ln_sub_string = ""
             em_sub_string = ""
             
             for key_index in range (1, 10):
                   key_indexed_string = self.data_record_string.split("KEY_SYNC:")[key_index]
                   if key_index == 1:
                         fn_sub_string = key_indexed_string + str(" ")
                   if key_index == 2:
                         ln_sub_string = key_indexed_string + str(" ")
                   if key_index == 3:
                         pass
                   if key_index == 4:
                         pass
                   if key_index == 5:
                         pass
                   if key_index == 6:
                         pass
                   if key_index == 7:
                         pass
                   if key_index == 8:  # EMAIL
                         em_sub_string = key_indexed_string + str(" ")
                         # # em_sub_string = key_indexed_string + str(" ") + "data_" + str(record_index)
                   if key_index == 9:
                         pass

             target_contact_string = str(fn_sub_string) + str(ln_sub_string) + str(em_sub_string)

             build_the_list_of_strings_for_contacts.append(str(target_contact_string) )

        return build_the_list_of_strings_for_contacts

        ###############################################################################
        #
        # Programming Note:     ( Reference to the code above )   
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END) ... Note for Entry and Listbox it is (0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # For Example, A Big Text Widget will experience these commands:
        # 
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        #     
        ##############################################################################


    ###############################################
    #
    #  Usage:  self.Generate_Button_One_Event()
    #
    def Generate_Button_One_Event(self):
          self.lbox_Source_Contacts.event_generate('<Button-1>', x=0, y=0)


  
    def OnListBoxSelect(self, event):
        global listbox_file_capture_global
        
        # if event == <<VirtualEvent event x=0 y=0>>: return
        listbox_file_capture_global = "False"
        # print("   ")
        # print(".... EVENT  <Button-1>  = " + str(event) )
        widget = event.widget
        self.widget_ID = widget
        # print(".... widget = event.widget = " + str(event.widget) )
        selection = widget.curselection()

        # Catch the IndexError EXCEPTION for widget.get(selection[0])
        try:
              test_the_selection = widget.get(selection[0])
        except IndexError as err:
              # print("  ")
              # print("**** IndexError ****   widget.get(selection[0])  in OnListBoxSelect - EVENT: <Button-1> - \n\nERROR (IndexError):\n\n" + str(err) )
              pass
        
        if not len(selection):
              # print("  ")
              # print(".... not len(selection) = True")
              return

        contact_string_value = widget.get(selection[0]) 

        # selection = widget.curselection() = (17,)  

        # print(".... selection[0]  =  " + str(selection[0] ) )

        # Save the selected Source Listbox Selection Numbers in a LIST (Class Variable)
        # so that we can use this list to open the Dictionary file 
        # in read mode and write the DATA RECORD to a NEW CONTACT LIST Dictionary
        # or append to an exisitng CONTACT LIST Dictionary. 

        # print(".... selection = widget.curselection() = " + str(widget.curselection() ) )
        # print(".... contact_string_value = widget.get(selection[0]) = " + str(widget.get(selection[0]) ) )



    def capture_new_contact_list_name(self):
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global insert_first_contact_global
        global selected_dictionary_record_index_global
        global selected_dictionary_record_index_focus_global
        global kick_thread_to_update_main_entry_widgets
        global prepend_cnotes_dict_file_global
        global master_cm_list_name_global
        global listbox_file_capture_global
        global cm_textbox_newfile_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_cnotes_dict_file_global
        global fullpath_prepend_cnotes_dict_file_global
        ###################################################################################
        #
        # METHOD:  capture_new_contact_list_name
        # 
        # This method  gets the contact list name from
        # the Textbox and sets the cm_textbox_newfile_global
        # and cm_textbox_newfile_global is used in THREAD to 
        # set the CONTACT LIST ENTRY BOX in the App Class
        # USING THE GLOBAL VARIABLE cm_listbox_file_global
        # and THE SET TEXTBOX ENTRY WIDGET METHOD: 
        #
        #  cm_textbox_newfile_global = self.my_cm_filename_entry.get()
        #
        ###################################################################################
        #
        #  textbox_newfile_capture_global = False 
        # 
        #  cm_textbox_newfile_global = "Enter New Contact List Name Here"
        #
        ###################################################################################
        # 
        # Introducing a FLAG called: button_set_filename_entry_to_status = True/False
        # to track and check whether the filename ENTRY WIDGET contains:
        #
        #      FILENAME (possibly)    or     STATUS
        #
        ###################################################################################



        # print(".... RUNNING  METHOD  capture_new_contact_list_name\nwith self.button_set_filename_entry_to_status = " + str(self.button_set_filename_entry_to_status) )


#12345678
        if self.button_set_filename_entry_to_status == True:

            cm_textbox_newfile_global = self.BUILDING_NEW_LIST_NAME_ONLY
            master_cm_list_name_global = self.BUILDING_NEW_LIST_NAME_ONLY
            textbox_newfile_capture_global = True

        elif self.button_set_filename_entry_to_status == False:

            self.button_set_filename_entry_to_status = True

            # set back to neutral colors - the new filename has been set
            # and the contact building had completed.
            self.my_cm_filename_entry.config(background = "cyan4")
            self.completed_new_contact_list_name_button.config(background = "cyan4")

            # set this to neutral colors until the new contact dictionary gets
            # built and then these widgets will get set to completed build colors.
            self.create_the_new_dictionary_button.config(background = "cyan4")
            self.final_build_status_text_box.config(background = "cyan4")

            test_entry_value = ""

            test_entry_value = self.entry_CM_FILENAME.get()

            if test_entry_value != "":
                self.BUILDING_NEW_LIST_NAME_ONLY = self.entry_CM_FILENAME.get()
                self.new_list_button_text.set("Click after Entering\nNEW CONTACT LIST NAME (Optional)\nName SET to " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )

            elif test_entry_value == "":
                time_string = time.strftime("%m-%d-%Y-%H%M%S")
                self.BUILDING_NEW_LIST_NAME_ONLY = "Build_List_" + str(time_string)
                # print(".... self.BUILDING_NEW_LIST_NAME_ONLY = " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )
                self.new_list_button_text.set("Click after Entering\nNEW CONTACT LIST NAME (Optional)\nDefault Name = " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )
                
#123456789012
            cm_textbox_newfile_global = self.BUILDING_NEW_LIST_NAME_ONLY
            master_cm_list_name_global = self.BUILDING_NEW_LIST_NAME_ONLY
            created_list_string_status = "Created List: " + str(self.BUILDING_NEW_LIST_NAME_ONLY)
            self.entry_CM_FILENAME.set(created_list_string_status)
                
#12345678
        # print(".... str(self.BUILDING_NEW_LIST_NAME_ONLY) = " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )

        # Create NEW FILES for the cm_list_CONTACT_LIST_NAME  
        # and dict_file_CONTACT_LIST_NAME Globals filenames
        cm_listbox_file_global = "cm_list_" + str(cm_textbox_newfile_global) + ".txt"
        dict_filename_global = "dict_file_" + str(cm_textbox_newfile_global) + ".txt"
        cnotes_dict_file_global = "cnotes_" + str(cm_textbox_newfile_global) + ".txt"

        # Create APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
        # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
        # which gives us the FULL PATH NAME to our contact_management.py data files.  
       
        fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
       
        fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )

        fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

        fullpath_prepend_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )
        
       
        # Create the new Contact List File and add Titles 
        with open(fullpath_fn_cm_listbox_file_global, 'a') as wf_titles:
              wf_titles.flush()
              wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "\n")


        
        # Create the File for Contact DICTIONARY Filename dict_filename_global
        with open(fullpath_fn_dict_filename_global, 'a') as new_wdictf:
              new_wdictf.flush()
              new_wdictf.write("\n")


        # Create the File for Contact NOTES DICTIONARY Filename cnotes_dict_file_global
        with open(fullpath_cnotes_dict_file_global, 'a') as new_notes_wdictf:
              new_notes_wdictf.flush()
              new_notes_wdictf.write("\n")

        # Set the global - insert_first_contact_global = True
        # to add the FIRST RECORD to the New Contact List so the Database Files
        # have at least one Contact to avoid KeyError Exceptions.
        # This triggers the App Class to execute the   
        # self.first_Contact_Data_Entry() method.
        #
        
        insert_first_contact_global = True   # ADDS FIRST DICT RECORD TO AVOID KEY ERROR

        ############################################################################
        #
        #  THIS COMPLETES THE SEQUENCE OF CREATING A NEW CONTACT LIST ....
        #
        #  WE WILL NOW PROCEED TO WRITE THE SELECTED DICTIONARY RECORDS
        #  TO THE NEW CONTACT LIST DICTIONARY.
        #
        ############################################################################



        ############################################################################
        #
        #  WE WILL PROCEED TO WRITE THE SELECTED DICTIONARY RECORDS
        #  TO THE NEW CONTACT LIST DICTIONARY.   
        # 
        ############################################################################

    def create_the_NEW_DICTIONARY(self):
        global mode_select_build_list_global

        if (mode_select_build_list_global == "Build List"):

#123456789012
            if (self.SOURCE_LISTBOX_SEL_LIST == [] ):

                # print("HEY !! .... self.SOURCE_LISTBOX_SEL_LIST = " + str(self.SOURCE_LISTBOX_SEL_LIST) )

                # print("HEY !! .... self.SOURCE_LISTBOX_SEL_LIST_VALUES = " + str(self.SOURCE_LISTBOX_SEL_LIST_VALUES) )

                self.final_build_status_text_box.config(background="goldenrod")

                # Emphasize the color of this Button 
                # because the USER has NOT selected ANY CONACTS or SOURCE Listbox Items 

                self.GET_LBOX_SOURCE_curselection_Button.config(background="goldenrod")

                final_build_status_TEXT = "Use ADD to LIST Button to ADD Contacts."

                self.final_build_status_text_box.delete("1.0", END)

                self.final_build_status_text_box.insert(END, final_build_status_TEXT)

                return
            
            elif (self.SOURCE_LISTBOX_SEL_LIST != [] ):

                self.final_build_status_text_box.config(background="cyan")

                # DE-Emphasize the color of this Button 
                # because the USER has surely selected some CONACTS or SOURCE Listbox Items 

                self.GET_LBOX_SOURCE_curselection_Button.config(background="cyan4")

                # GO FORWARD and Generate Build List Dictionary
                self.create_the_NEW_DICTIONARY_after_question()

#123456789012
        else:
            # GO FORWARD and Generate Build List Dictionary
            self.create_the_NEW_DICTIONARY_after_question()


        
        
    def create_the_NEW_DICTIONARY_after_question(self):
        global mode_select_build_list_global

        # DE-Emphasize the color of this Button once the "Build List" Command is issued
        # because USER has already selected SOURCE Listbox Items 

        self.GET_LBOX_SOURCE_curselection_Button.config(background="cyan4")
        
        # print("  ")
        # print(".... create_the_NEW_DICTIONARY Method .... Display SELECTED Contacts INDEX LIST:  ")
        # print("  ") 
        # for item in self.LISTBOX_SEL_LIST:
        #     print(".... SELECTED CONTACT INDEX LIST =  " + str(item) )
        # 
        ################################################################################################

        ################################################################################################
        #
        # Initialize Database Files with New Contact List Name (or the default name if nothing entered)
        #
        self.capture_new_contact_list_name()

        ################################################################################################
        # 
        #  We use the INDEX LIST we have stored in self.LISTBOX_SEL_LIST
        #
        #  and then we compute the self.DICT_INDEX  making an integer conversion
        #
        #  self.DICT_INDEX  = self.LISTBOX_SEL
        #
        #  to  I N D E X   our  DICTIONARY  of  DICTIONARY  Variable (Object):
        #
        #  self.SELECTED_DICT_OF_DICT_GLOBAL   that was generated by
        #
        #  inst_original_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        #  self.SELECTED_DICT_OF_DICT_GLOBAL = inst_original_loaded_Process_Dict_File.read_target_dict_file()
        #
        #  This_SETS_A_DICTIONARY_OF_DICTIONARIES_GLOBAL  
        #
        #  Concurrently, we WRITE that DICTIONARY  of  DICTIONARY  Variable (Object)
        #
        #  to WRITE our NEW dict_file GLOBAL Database File .....
        #
        ################################################################################################
        # 
        # We now retreive the ORIGINAL DICTIONARY file name stored in
        # a Class Variable ... Because we have created a NEW CONTACT LIST
        # with all the respective Database Files, our dict_file GLOBAL
        # matches the NEW CONTACT LIST. 
        original_dict_filename = self.ORIGINAL_DICTIONARY_FILENAME

        # Open in READ MODE the ORIGINAL CONTACT DICTIONARY that
        # we are Building this New Dictionary from. 
        with open(original_dict_filename, 'r') as orig_rdictf:
             orig_rdictf.flush()
             self.original_dict_textString = orig_rdictf.read()
             orig_rdictf.close()

        # Count the DATA RECORDS in the string by counting the
        # number of "DATA_RECORD_DELIMITER:" patterns.
        self.TOTAL_RECORDS = self.original_dict_textString.count("DATA_RECORD_DELIMITER:")

        # print("  ")
        # print(".... self.TOTAL_RECORDS = " + str(self.TOTAL_RECORDS) )

        ###############################################################################################
        #
        # self.TOTAL_RECORDS ............ self.TOTAL_RECORDS
        # self.LISTBOX_SEL_LIST ......... self.LISTBOX_SEL_LIST
        # self.DICT_INDEX ............... self.DICT_INDEX 
        #
        # We need to verify that the contacts are written to the Listbox as follows so that the
        # Listbox Select Indexes match with the DICTIONARY Database, therefore:
        #
        # self.DICT_INDEX  = Index  to  self.LISTBOX_SEL_LIST
        #
        # WE BUILD NEW DISCTIONARY OF DICTIONARIES by Indexing:
        #
        #      self.SELECTED_DICT_OF_DICT_GLOBAL 
        #
        #
        ###############################################################################################

        # Open the NEW CONTACT DICTIONARY (global) that we
        # are Building which has already been created.
        # Note: It looks like since we open this in "w" mode that we would
        # write over any initial DATA RECORD created in the DICTIONARY Database
        # as a way to avoid KEY ERRORS. This could be why our count is one off.
        # Well it looks like this open(fullpath_fn_dict_filename_global, 'w')
        # was just writing over our initial DATA RECORD and probably causing
        # count to be one off.
        #
        # with open(fullpath_fn_dict_filename_global, 'w') as new_wdictf:
        #      new_wdictf.flush()
        #      new_wdictf.write("\n")

        #################################################################################### 
        #
        #  NOTE:  
        #
        #  Be sure the selected_loaded_dictionary_global GLOBAL has been set to make
        #  the original Store_dictionary_of_dictionaries Object available Globally.
        #  
        #  orig_selected_dictionary_loaded_global = selected_dictionary_loaded_global
        #   
        ####################################################################################
        #  
        #  This number of data records we will write is acquired by the number of
        #  contacts we selected in our LIST: self.save_selection_relates_to_dict_record_num
        #   
        #      *************  SET NUMBER OF RECORDS TO SEQUENCE THROUGH *************
        #
        ####################################################################################
        # 
        # Note:   self.LISTBOX_SEL_LIST = self.SOURCE_LISTBOX_SEL_LIST
        #  
        ####################################################################################

        # Adding this to be sure we have the correct List built by our new methods:
        self.LISTBOX_SEL_LIST = self.SOURCE_LISTBOX_SEL_LIST
        
        for listbox_index in self.LISTBOX_SEL_LIST:

             # print("  ")
             # print(".... CONVERT DICT INDEX to INTEGER:   self.DICT_INDEX  = int(listbox_index)")
             # print("  ")
             # print(".... self.TOTAL_RECORDS = " + str(self.TOTAL_RECORDS) )
             # print(".... int(listbox_index) = " + str(int(listbox_index)) )

             is_this_magic = int(listbox_index) + 1
             
             self.DICT_INDEX  = is_this_magic

             # print(".... self.DICT_INDEX  =  " + str(self.DICT_INDEX) )

             ############################################################################### 

             sdfn = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["First_Name_KEY"] )
             sdln = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["Last_Name_KEY"] )
             sdsa = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["Street_Address_KEY"] )
             sdct = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["City_Town_KEY"] )
             sdst = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["State_KEY"] )
             sdzc = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["Zip_Code_KEY"] )
             sdpn = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["Phone_Number_KEY"] )
             sdem = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["EMail_KEY"] )
             sdws = str(self.SELECTED_DICT_OF_DICT_GLOBAL["Dict_KEY" + str(self.DICT_INDEX)]["Website_KEY"] )

             # write sorted data records to cm_list_file
             # Note that we use the FULLPATH - fullpath_fn_cm_listbox_file_global

             with open(fullpath_fn_cm_listbox_file_global, 'a') as wf:
                  for x in range(0, 10):
                       if x == 0: wf.flush()
                       #--------------------------------------------------------
                       if x == 1: wf.write(sdfn + ",")
                       elif x == 2: wf.write(sdln + ",")
                       elif x == 3: wf.write(sdsa + ",")
                       elif x == 4: wf.write(sdct + ",")
                       elif x == 5: wf.write(sdst + ",")
                       elif x == 6: wf.write(sdzc + ",")
                       elif x == 7: wf.write(sdpn + ",")
                       elif x == 8: wf.write(sdem + ",")
                       elif x == 9: wf.write(sdws + "\n")
                       else: pass

             ########################################################################### 

             # Write contact data dictionary to dict_filename file from class method get_contact_dict_call
             # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
             with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                  for x in range(0, 10):
                       if x == 0:
                             wdictf.flush()
                             wdictf.write("DATA_RECORD_DELIMITER:")
                       elif x == 1: wdictf.write("KEY_SYNC:" + sdfn )
                       elif x == 2: wdictf.write("KEY_SYNC:" + sdln )
                       elif x == 3: wdictf.write("KEY_SYNC:" + sdsa )
                       elif x == 4: wdictf.write("KEY_SYNC:" + sdct )
                       elif x == 5: wdictf.write("KEY_SYNC:" + sdst )
                       elif x == 6: wdictf.write("KEY_SYNC:" + sdzc )
                       elif x == 7: wdictf.write("KEY_SYNC:" + sdpn )
                       elif x == 8: wdictf.write("KEY_SYNC:" + sdem )
                       elif x == 9: wdictf.write("KEY_SYNC:" + sdws )
                       else: pass
             
             ############################################################################

             # print(" ")
             # print(".... N E W   C O N T A C T   D A T A B A S E   B U I L D I N G   .... ")
             # print("  ")
             # print("....  self.DICT_INDEX   sdfn   sdln   sdem  =  " + str(self.DICT_INDEX) + " " + str(sdfn) + " " + str(sdln) + " " + str(sdem) )
             # print("  ")


        # ## print("\n") 
        # ## print(".... SELECTED and LOADED - selected_dictionary_loaded_global =  " + str(fullpath_fn_dict_filename_global) )
        # ## print("\n") 

        # write a new logfile to update the logfile items each time a new Contact List is Created
        inst_Write_Main_Logfile_when_BUILD_new_list = Write_Main_Logfile()
        inst_Write_Main_Logfile_when_BUILD_new_list.write_update_logfile()

        inst_newly_built_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        sets_NEW_LIST_DICTIONARY_OF_DICTIONARIES_GLOBAL = inst_newly_built_loaded_Process_Dict_File.read_target_dict_file()

        kick_thread_to_update_main_entry_widgets = True   # (to update main screen widgets)

        # print("\n") 
        # print(".... N E W   D I C T I O N A R Y   C O M P L E T E D   B U I L D  -  SELECTED and LOADED - fullpath_fn_dict_filename_global =  \n" + str(fullpath_fn_dict_filename_global) )
        # print("\n") 


        #######################################################################################
        #  
        # ***** Generate CONTACT LIST BUILD COMPLETE STATUS TO ENTRY WIDGET or TEXTBOX
        # 

        # print(".... str(self.BUILDING_NEW_LIST_NAME_ONLY) = " + str(self.BUILDING_NEW_LIST_NAME_ONLY) )
        
        final_build_status_TEXT = "New List Ready: " + str(self.BUILDING_NEW_LIST_NAME_ONLY)

        self.final_build_status_text_box.delete(1.0, END)
        self.final_build_status_text_box.insert(END, final_build_status_TEXT)

        # Optionally, also Signal that the Build_List has Completed.
        self.signal_list_built_complete()

        # set back to neutral colors
        self.my_cm_filename_entry.config(background = "cyan4")
        self.completed_new_contact_list_name_button.config(background = "cyan4")

        # set to final success colors to show BUILD LIST COMPLETED
        self.create_the_new_dictionary_button.config(background = "cyan4")
        self.final_build_status_text_box.config(background = "cyan")
         
        #
        #######################################################################################
        #
        #  NOTE:    
        #
        #  The selected_loaded_dictionary_global GLOBAL made the original
        #  Store_dictionary_of_dictionaries Object available Globally.
        #
        #  self.orig_selected_dictionary_loaded_global = selected_dictionary_loaded_global
        # 
        #######################################################################################

        # SORT our new DICTIONARY of DICTIONARIES for our new cocntact list
        # which also updates the DICTIONARY OF DICTIONARIES GLOBAL OBJECT.
        # And, finally, we kick the main() thread to update our main screen widgets.

        inst_final_built_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        sets_NEW_LIST_DICTIONARY_OF_DICTIONARIES_GLOBAL = inst_final_built_loaded_Process_Dict_File.read_target_dict_file()

        kick_thread_to_update_main_entry_widgets = True   # (to update main screen widgets)

        #
        #  FINALLY, WE SWITCH BACK TO THE WORKFLOW CANVAS WIDGET ..... 
        #
        self.draw_WorkFlow_Canvas_Widget()

        return


  
    # Modify this method to cycle a well-timed, well-designed TASK-COMPLETE SIGNAL-SEQUENCE
    # at the end of the BUILD-LIST Execution on just the ENTRY/TEXT BOXES, 
    # and not the Buttons or the Listbox. 
    #
    def signal_list_built_complete(self):

#12345678
        for count in range(0,2):

            self.select_file_button.config(background = "cyan")
            self.source_file_status_text_box.config(background = "cyan")

            self.my_cm_filename_entry.config(background = "cyan4")
            self.completed_new_contact_list_name_button.config(background = "cyan4")

            self.create_the_new_dictionary_button.config(background = "cyan4")
            self.final_build_status_text_box.config(background = "cyan4")

            self.master.update()

            time.sleep(.125)

            self.select_file_button.config(background = "cyan4")
            self.source_file_status_text_box.config(background = "cyan4")

            self.my_cm_filename_entry.config(background = "cyan")
            self.completed_new_contact_list_name_button.config(background = "cyan")

            self.create_the_new_dictionary_button.config(background = "cyan4")
            self.final_build_status_text_box.config(background = "cyan4")

            self.master.update()

            time.sleep(.125)

            self.select_file_button.config(background = "cyan4")
            self.source_file_status_text_box.config(background = "cyan4")

            self.my_cm_filename_entry.config(background = "cyan4")
            self.completed_new_contact_list_name_button.config(background = "cyan4")

            self.create_the_new_dictionary_button.config(background = "cyan")
            self.final_build_status_text_box.config(background = "cyan")

            self.master.update()

            time.sleep(.125)




    def lower_the_window(self):
          # These CYCLE Buttons have been changed to 
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()
          


    def close_windows(self):
        self.master.destroy()


     

# ENTER A NEW CONTACT LIST NAME IN A TEXTBOX
# 
class New_Contact_List(Frame):   # (object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global insert_first_contact_global
        global kick_thread_to_update_main_entry_widgets
        global kick_thread_to_update_email_contact_entry_widgets
        global selected_dictionary_record_index_global
        global selected_dictionary_record_index_focus_global
        global prepend_cnotes_dict_file_global
        global master_cm_list_name_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_cnotes_dict_file_global
        global fullpath_prepend_cnotes_dict_file_global
        global OBJECT_toplevel_new_contact_list
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        
        # self.master = master
        # self.frame = tk.Frame(self.master)

        huge_font = ('Verdana',32)
        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice 
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        OBJECT_toplevel_new_contact_list = self.master
        instance_object_LIST.append(self.master)
        
        self.master.configure(background=str(newlist_bg_color_val_global) )

        self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - Create New Contact List")

        self.select_file_button = Button(self.master, text = "CLICK HERE after you \nhave ENTERED a NEW\nCONTACT LIST NAME\nExample: sales-calls-MAY-25", \
             width=30,height=4, font=('Helvetica', '18'), background="light sea green", command = self.get_Textbox_File)
            
        self.select_file_button.grid(row=1, column=0, sticky = W)
        self.select_file_button.bind("<Button-1>", self.get_Textbox_File)

        self.quit_status_panel_Button = Button(self.master, text = "EXIT", \
        width = 7, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.close_windows)
        self.quit_status_panel_Button.grid(row=3, column=0, padx=5, pady=5, sticky = W)
        self.quit_status_panel_Button.config(borderwidth=5)

        self.tk_lower_status_panel_Button = Button(self.master, text = "MAIN SCREEN", \
        width = 15, height = 1, font=('Helvetica', '16'), \
        background="cyan4", fg="black", activebackground="cyan", activeforeground="blue2", \
        command = self.lower_the_window)
        self.tk_lower_status_panel_Button.grid(row=4, column=0, padx=5, pady=5, sticky = W) 
        self.tk_lower_status_panel_Button.config(borderwidth=5)

        # INSERT ENTRY WIDGET HERE FOR NEW CONTACT LIST FILENAME
        self.entry_CM_FILENAME = StringVar()
        self.my_cm_filename_entry = Entry(self.master, textvariable = self.entry_CM_FILENAME, font = huge_font, width = 30)
        self.my_cm_filename_entry.grid(sticky = W, row=2, column=0)
        self.my_cm_filename_entry.config(borderwidth=5, background="light sea green")
        


    def get_Textbox_File (self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global insert_first_contact_global
        global selected_dictionary_record_index_global
        global selected_dictionary_record_index_focus_global
        global kick_thread_to_update_main_entry_widgets
        global kick_thread_to_update_email_contact_entry_widgets
        global prepend_cnotes_dict_file_global
        global master_cm_list_name_global
        global listbox_file_capture_global
        global cm_textbox_newfile_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_cnotes_dict_file_global
        global fullpath_prepend_cnotes_dict_file_global
        ###########################################################################
        # This button command gets the contact list name from
        # the Demo3 Textbox and sets the cm_textbox_newfile_global
        # and cm_textbox_newfile_global is used in THREAD to 
        # set the CONTACT LIST ENTRY BOX in the App Class
        # USING THE GLOBAL VARIABLE cm_listbox_file_global
        # and THE SET TEXTBOX ENTRY WIDGET METHOD:
        #
        #  cm_textbox_newfile_global = self.my_cm_filename_entry.get()
        #
        ###########################################################################
        #
        #  textbox_newfile_capture_global = False
        #
        #  cm_textbox_newfile_global = "Enter New Contact LIst Name Here"
        #
        ###########################################################################  
        #

        # Test to see IF a CONTACT LIST NAME was ENTERED
        # IF a CONTACT LIST NAME was NOT ENTERED,  deploy a messagebox and lift the window and return.
        if self.my_cm_filename_entry.get() == "":
            messagebox.showinfo("Contact Manager Guide ...", \
            "ATTENTION: \n\nPlease ENTER a Contact LIST NAME.\n\nExample:  Northeast_SALES_TEAM")
            self.master.lift()
            return

        
        cm_textbox_newfile_global = self.my_cm_filename_entry.get()
        master_cm_list_name_global = self.my_cm_filename_entry.get()
        
        textbox_newfile_capture_global = True

        # Create NEW FILES for the cm_list_CONTACT_LIST_NAME 
        # and dict_file_CONTACT_LIST_NAME Globals filenames
        cm_listbox_file_global = "cm_list_" + str(cm_textbox_newfile_global) + ".txt"
        dict_filename_global = "dict_file_" + str(cm_textbox_newfile_global) + ".txt"
        cnotes_dict_file_global = "cnotes_" + str(cm_textbox_newfile_global) + ".txt"

        # Create APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
        # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
        # which gives us the FULL PATH NAME to our contact_management.py data files. 
       
        fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
       
        fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )

        fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

        fullpath_prepend_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )
        
       
        # Create the new Contact List File and add Titles 
        with open(fullpath_fn_cm_listbox_file_global, 'a') as wf_titles:
              wf_titles.flush()
              wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "\n")


        
        # Create the File for Contact DICTIONARY Filename dict_filename_global
        with open(fullpath_fn_dict_filename_global, 'a') as new_wdictf:
              new_wdictf.flush()
              new_wdictf.write("\n")


        # Create the File for Contact NOTES DICTIONARY Filename cnotes_dict_file_global
        with open(fullpath_cnotes_dict_file_global, 'a') as new_notes_wdictf:
              new_notes_wdictf.flush()
              new_notes_wdictf.write("\n")

        # Set the global - insert_first_contact_global = True
        # to add the FIRST RECORD to the New Contact List so the Database Files
        # have at least one Contact to avoid KeyError Exceptions. 
        # This triggers the App Class to execute the   
        # self.first_Contact_Data_Entry() method.  

        insert_first_contact_global = True

        # Adding the kick_thread flags here because we created a NEW CONTACT LIST
        kick_thread_to_update_email_contact_entry_widgets = True
        kick_thread_to_update_main_entry_widgets = True

        # #print("\n") 
        # #print(".... SELECTED and LOADED - selected_dictionary_loaded_global =  " + str(fullpath_fn_dict_filename_global) )
        # #print("\n")

        # write a new logfile to update the logfile items each time a new Contact List is Created
        inst_Write_Main_Logfile_when_new_list = Write_Main_Logfile()
        inst_Write_Main_Logfile_when_new_list.write_update_logfile()

              
        # close the Enter New Contact List File window  
        
        self.master.destroy()
        return
    


    def lower_the_window(self):
          # These CYCLE Buttons have been changed to 
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()



    def close_windows(self):
        self.master.destroy()



# VIEW A CONTACT LIST IN A LARGE SCREEN TEXTBOX 
# 
class View_Contact_List(Frame):   # (object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global viewscreen_bg_color_val_global
        global OBJECT_toplevel_view_contact_list
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
            
        #self.master = master
        #self.frame = tk.Frame(self.master) 

        #self.master = master 
        #self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice 
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        OBJECT_toplevel_view_contact_list = self.master
        instance_object_LIST.append(self.master)
        
        self.master.configure(background=str(viewscreen_bg_color_val_global) )

        self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - Contact List Display and Scroll")
          
        # self.quitButton = Button(self.master, text = 'RETURN to MAIN SCREEN', width = 30, height = 2, \
        #     font=('Helvetica', '12'), background="IndianRed1", command = self.close_windows)
        
        # self.quitButton.grid(row=3, column=0, sticky = W)

        # EXIT BUTTON.    
        # 
        self.quitButton = Button(self.master, text = "EXIT", width = 7, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5, \
            activebackground="cyan", activeforeground="blue2", command = self.exit_Handler)

        self.quitButton.grid(row=3, column=0, sticky = W)

        #
        # LOWER WINDOW BUTTON.  
        # 
        self.lower_window_Button = Button(self.master, text = "MAIN SCREEN", width = 15, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5, \
            activebackground="cyan", activeforeground="blue2", command = self.lower_WINDOW)

        self.lower_window_Button.grid(row=3, column=0) 

        ###############################################################################
        #
        # Programming Note:
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Big Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        #
        ###############################################################################

 
        # TEXTBOX to insert TITLE at top of window and identify
        # the current Contact List File - cm_listbox_file_global  

        self.title_1_text_box = Text(self.master, width=95, height = 1)
        self.title_1_text_box.grid(row=0, column=0, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '18'), \
            fg = str(viewscreen_fg_color_val_global), background=str(viewscreen_bg_color_val_global) )
        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_1_TITLE = "CONTACT LIST:  " + str(cm_listbox_file_global) + "    DICTIONARY: " + str(dict_filename_global) 

        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        
        # TEXTBOX to view the DICTIONARY FILE corresponding 
        # to the current CONTACT LIST SELECTED or CREATED 

        self.view_text_box = Text(self.master, width=95, height = 19)
        self.view_text_box.grid(row=2, column=0, sticky = W)
        self.view_text_box.config(borderwidth=10, font=('Helvetica', '18'), \
            fg = str(viewscreen_fg_color_val_global), background=str(viewscreen_bg_color_val_global) )
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        # create a Scrollbar and associate it with self.view_text_box 
        self.scrollb = Scrollbar(self.master, command=self.view_text_box.yview)
        self.scrollb.grid(row=2, column=1, sticky='NSW')
        self.view_text_box['yscrollcommand'] = self.scrollb.set

        # VIEW the TEXTBOX after loading the current
        # DICTIONARY Contact List File - dict_file_cm_listbox_file_global
        # which is stored in APPDATA at fullpath_fn_dict_filename_global

        self.textFile = open(fullpath_fn_dict_filename_global, 'r')

        # This takes the file object opened with the open() and turns it into a string which 
        # you can now use textString in a text widget.
        self.textString = self.textFile.read()

        # Close the Dictionary File
        self.textFile.close()

        # Count the DATA RECORDS in the string by counting the
        # number of "DATA_RECORD_DELIMITER:" patterns 
        self.num_data_records = self.textString.count("DATA_RECORD_DELIMITER:")

        # TEXTBOX appears to have residual data upon startup button select VIEW CONTACTS, 
        # so we may have to check to see that a dictionary global is set to
        # an actual valid dictionary after being initialized to
        # dict_filename_global = "No Contact Dictionary"
        
        self.num_data_records_plus_one = self.num_data_records + 1
        # Operate on the textString to search for DATA_RECORD_DELIMITER: and KEY_SYNC: sub-strings  
        for record_index in range (1, self.num_data_records_plus_one):
             self.view_text_box.insert(END, "\n")
             self.data_record_string = self.textString.split("DATA_RECORD_DELIMITER:")[record_index]
             for key_index in range (1, 10):
                   key_indexed_string = self.data_record_string.split("KEY_SYNC:")[key_index]
                   if key_index == 1:
                        self.view_text_box.insert(END, "NAME: ")
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, " ")
                   if key_index == 2:
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, "\n")
                   if key_index == 3:
                        self.view_text_box.insert(END, "ADDRESS: ")
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, ", ")
                   if key_index == 4:
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, ", ")
                   if key_index == 5:
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, ", ")
                   if key_index == 6:
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, "\n")
                   if key_index == 7:
                        self.view_text_box.insert(END, "PHONE: ")
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, "   ")
                   if key_index == 8:
                        self.view_text_box.insert(END, "EMAIL: ")
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, "\n")
                   if key_index == 9:
                         self.view_text_box.insert(END, "WEBSITE: ")
                         self.view_text_box.insert(END, key_indexed_string)
                         self.view_text_box.insert(END, "\n")
                   

        self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 

        ###############################################################################
        #
        # Programming Note:     ( Reference to the code above )   
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL) 
        # text.delete(1.0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Big Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        #
        ###############################################################################



    def lower_WINDOW(self):
          # These CYCLE Buttons have been changed to 
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()



    def exit_Handler(self):
        self.master.destroy()


             
          
##############################################################################
#
#   Contact Management Application USER GUI Configuration Class 
#    
#   USER_GUI_Config_Class
#
#   This USER_GUI_Config_Class allows USERS to configure a tkinter GUI template
#   consisting of: 
#
#   1. Frames
#   2. Label Widgets
#   3. Entry Widgets
#   4. Button Widgets
#   5. Text Widgets
#
# Example of three instances of this USER_GUI_Config_Class:
#
# .... str(widget_object_focus_one) = .!toplevel.!user_gui_config_class
# .... str(widget_object_focus_one.winfo_id() ) = 263122
# .... str(widget_object_focus_one.winfo_parent() ) = .!toplevel
# 
# .... str(widget_object_focus_two) = .!toplevel2.!user_gui_config_class
# .... str(widget_object_focus_two.winfo_id() ) = 66550
# .... str(widget_object_focus_two.winfo_parent() ) = .!toplevel2
# 
# .... str(widget_object_focus_three) = .!toplevel3.!user_gui_config_class
# .... str(widget_object_focus_three.winfo_id() ) = 66602
# .... str(widget_object_focus_three.winfo_parent() ) = .!toplevel3
#
##############################################################################
#
#        M E D I C A L     R E C O R D      C L A S S  
#
##############################################################################
class USER_GUI_Config_Class(Frame):    #(object)
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global master_cm_list_name_global
        global username_global
        global appdata_path_global
        global cm_appdatafiles_path_global
        global user_gui_title_value_global
        global user_gui_title_bg_color_value_global
        global user_gui_title_fg_color_value_global
        global user_gui_bg_color_value_global
        global user_gui_fg_color_value_global
        global user_gui_label_bg_color_value_global
        global user_gui_label_fg_color_value_global
        global user_gui_entry_bg_color_value_global
        global user_gui_entry_fg_color_value_global
        global user_gui_text_bg_color_value_global
        global user_gui_text_fg_color_value_global
        global USER_GUI_Config_Class_inst_LIST
        global user_defined_gui_group_one
        global user_defined_gui_group_two
        global user_defined_gui_group_three
        global fullpath_med_config_ini_global
        global user_defined_gui_instance_count_GLOBAL
        global group1_frame1_user_label
        global group1_frame1_status_text
        global group1_frame1_user_button
        global group1_frame2_user_label
        global group1_frame2_status_text
        global group1_frame2_user_button
        global group1_frame3_user_label
        global group1_frame3_status_text
        global group1_frame3_user_button
        global group1_frame4_user_label
        global group1_frame4_status_text
        global group1_frame4_user_button
        global group1_frame5_user_label
        global group1_frame5_status_text
        global group1_frame5_user_button
        global group1_frame6_user_label
        global group1_frame6_status_text
        global group1_frame6_user_button
        global group1_frame7_user_label
        global group1_frame7_status_text
        global group1_frame7_user_button
        global group1_frame8_user_label
        global group1_frame8_status_text
        global group1_frame8_user_button
        global group1_frame9_user_label
        global group1_frame9_status_text
        global group1_frame9_user_button
        global group1_frame10_user_label
        global group1_frame10_status_text
        global group1_frame10_user_button
        global group1_frame11_user_label
        global group1_frame11_status_text
        global group1_frame11_user_button
        global group1_frame12_user_label
        global group1_frame12_status_text
        global group1_frame12_user_button
        global group2_frame1_user_label
        global group2_frame1_status_text
        global group2_frame1_user_button
        global group2_frame2_user_label
        global group2_frame2_status_text
        global group2_frame2_user_button
        global group2_frame3_user_label
        global group2_frame3_status_text
        global group2_frame3_user_button
        global group2_frame4_user_label
        global group2_frame4_status_text
        global group2_frame4_user_button
        global group2_frame5_user_label
        global group2_frame5_status_text
        global group2_frame5_user_button
        global group2_frame6_user_label
        global group2_frame6_status_text
        global group2_frame6_user_button
        global group2_frame7_user_label
        global group2_frame7_status_text
        global group2_frame7_user_button
        global group2_frame8_user_label
        global group2_frame8_status_text
        global group2_frame8_user_button
        global group2_frame9_user_label
        global group2_frame9_status_text
        global group2_frame9_user_button
        global group2_frame10_user_label
        global group2_frame10_status_text
        global group2_frame10_user_button
        global group2_frame11_user_label
        global group2_frame11_status_text
        global group2_frame11_user_button
        global group2_frame12_user_label
        global group2_frame12_status_text
        global group2_frame12_user_button
        global group3_frame1_user_label
        global group3_frame1_status_text
        global group3_frame1_user_button
        global group3_frame2_user_label
        global group3_frame2_status_text
        global group3_frame2_user_button
        global group3_frame3_user_label
        global group3_frame3_status_text
        global group3_frame3_user_button
        global group3_frame4_user_label
        global group3_frame4_status_text
        global group3_frame4_user_button
        global group3_frame5_user_label
        global group3_frame5_status_text
        global group3_frame5_user_button
        global group3_frame6_user_label
        global group3_frame6_status_text
        global group3_frame6_user_button
        global group3_frame7_user_label
        global group3_frame7_status_text
        global group3_frame7_user_button
        global group3_frame8_user_label
        global group3_frame8_status_text
        global group3_frame8_user_button
        global group3_frame9_user_label
        global group3_frame9_status_text
        global group3_frame9_user_button
        global group3_frame10_user_label
        global group3_frame10_status_text
        global group3_frame10_user_button
        global group3_frame11_user_label
        global group3_frame11_status_text
        global group3_frame11_user_button
        global group3_frame12_user_label
        global group3_frame12_status_text
        global group3_frame12_user_button
        global group4_frame1_user_label
        global group4_frame1_status_text
        global group4_frame1_user_button
        global group4_frame2_user_label
        global group4_frame2_status_text
        global group4_frame2_user_button
        global group4_frame3_user_label
        global group4_frame3_status_text
        global group4_frame3_user_button
        global group4_frame4_user_label
        global group4_frame4_status_text
        global group4_frame4_user_button
        global group4_frame5_user_label
        global group4_frame5_status_text
        global group4_frame5_user_button
        global group4_frame6_user_label
        global group4_frame6_status_text
        global group4_frame6_user_button
        global group4_frame7_user_label
        global group4_frame7_status_text
        global group4_frame7_user_button
        global group4_frame8_user_label
        global group4_frame8_status_text
        global group4_frame8_user_button
        global group4_frame9_user_label
        global group4_frame9_status_text
        global group4_frame9_user_button
        global group4_frame10_user_label
        global group4_frame10_status_text
        global group4_frame10_user_button
        global group4_frame11_user_label
        global group4_frame11_status_text
        global group4_frame11_user_button
        global group4_frame12_user_label
        global group4_frame12_status_text
        global group4_frame12_user_button
        global group5_frame1_user_label
        global group5_frame1_status_text
        global group5_frame1_user_button
        global group5_frame2_user_label
        global group5_frame2_status_text
        global group5_frame2_user_button
        global group5_frame3_user_label
        global group5_frame3_status_text
        global group5_frame3_user_button
        global group5_frame4_user_label
        global group5_frame4_status_text
        global group5_frame4_user_button
        global group5_frame5_user_label
        global group5_frame5_status_text
        global group5_frame5_user_button
        global group5_frame6_user_label
        global group5_frame6_status_text
        global group5_frame6_user_button
        global group5_frame7_user_label
        global group5_frame7_status_text
        global group5_frame7_user_button
        global group5_frame8_user_label
        global group5_frame8_status_text
        global group5_frame8_user_button
        global group5_frame9_user_label
        global group5_frame9_status_text
        global group5_frame9_user_button
        global group5_frame10_user_label
        global group5_frame10_status_text
        global group5_frame10_user_button
        global group5_frame11_user_label
        global group5_frame11_status_text
        global group5_frame11_user_button
        global group5_frame12_user_label
        global group5_frame12_status_text
        global group5_frame12_user_button
        global group6_frame1_user_label
        global group6_frame1_status_text
        global group6_frame1_user_button
        global group6_frame2_user_label
        global group6_frame2_status_text
        global group6_frame2_user_button
        global group6_frame3_user_label
        global group6_frame3_status_text
        global group6_frame3_user_button
        global group6_frame4_user_label
        global group6_frame4_status_text
        global group6_frame4_user_button
        global group6_frame5_user_label
        global group6_frame5_status_text
        global group6_frame5_user_button
        global group6_frame6_user_label
        global group6_frame6_status_text
        global group6_frame6_user_button
        global group6_frame7_user_label
        global group6_frame7_status_text
        global group6_frame7_user_button
        global group6_frame8_user_label
        global group6_frame8_status_text
        global group6_frame8_user_button
        global group6_frame9_user_label
        global group6_frame9_status_text
        global group6_frame9_user_button
        global group6_frame10_user_label
        global group6_frame10_status_text
        global group6_frame10_user_button
        global group6_frame11_user_label
        global group6_frame11_status_text
        global group6_frame11_user_button
        global group6_frame12_user_label
        global group6_frame12_status_text
        global group6_frame12_user_button
        global group7_frame1_user_label
        global group7_frame1_status_text
        global group7_frame1_user_button
        global group7_frame2_user_label
        global group7_frame2_status_text
        global group7_frame2_user_button
        global group7_frame3_user_label
        global group7_frame3_status_text
        global group7_frame3_user_button
        global group7_frame4_user_label
        global group7_frame4_status_text
        global group7_frame4_user_button
        global group7_frame5_user_label
        global group7_frame5_status_text
        global group7_frame5_user_button
        global group7_frame6_user_label
        global group7_frame6_status_text
        global group7_frame6_user_button
        global group7_frame7_user_label
        global group7_frame7_status_text
        global group7_frame7_user_button
        global group7_frame8_user_label
        global group7_frame8_status_text
        global group7_frame8_user_button
        global group7_frame9_user_label
        global group7_frame9_status_text
        global group7_frame9_user_button
        global group7_frame10_user_label
        global group7_frame10_status_text
        global group7_frame10_user_button
        global group7_frame11_user_label
        global group7_frame11_status_text
        global group7_frame11_user_button
        global group7_frame12_user_label
        global group7_frame12_status_text
        global group7_frame12_user_button
        global group8_frame1_user_label
        global group8_frame1_status_text
        global group8_frame1_user_button
        global group8_frame2_user_label
        global group8_frame2_status_text
        global group8_frame2_user_button
        global group8_frame3_user_label
        global group8_frame3_status_text
        global group8_frame3_user_button
        global group8_frame4_user_label
        global group8_frame4_status_text
        global group8_frame4_user_button
        global group8_frame5_user_label
        global group8_frame5_status_text
        global group8_frame5_user_button
        global group8_frame6_user_label
        global group8_frame6_status_text
        global group8_frame6_user_button
        global group8_frame7_user_label
        global group8_frame7_status_text
        global group8_frame7_user_button
        global group8_frame8_user_label
        global group8_frame8_status_text
        global group8_frame8_user_button
        global group8_frame9_user_label
        global group8_frame9_status_text
        global group8_frame9_user_button
        global group8_frame10_user_label
        global group8_frame10_status_text
        global group8_frame10_user_button
        global group8_frame11_user_label
        global group8_frame11_status_text
        global group8_frame11_user_button
        global group8_frame12_user_label
        global group8_frame12_status_text
        global group8_frame12_user_button
        global group9_frame1_user_label
        global group9_frame1_status_text
        global group9_frame1_user_button
        global group9_frame2_user_label
        global group9_frame2_status_text
        global group9_frame2_user_button
        global group9_frame3_user_label
        global group9_frame3_status_text
        global group9_frame3_user_button
        global group9_frame4_user_label
        global group9_frame4_status_text
        global group9_frame4_user_button
        global group9_frame5_user_label
        global group9_frame5_status_text
        global group9_frame5_user_button
        global group9_frame6_user_label
        global group9_frame6_status_text
        global group9_frame6_user_button
        global group9_frame7_user_label
        global group9_frame7_status_text
        global group9_frame7_user_button
        global group9_frame8_user_label
        global group9_frame8_status_text
        global group9_frame8_user_button
        global group9_frame9_user_label
        global group9_frame9_status_text
        global group9_frame9_user_button
        global group9_frame10_user_label
        global group9_frame10_status_text
        global group9_frame10_user_button
        global group9_frame11_user_label
        global group9_frame11_status_text
        global group9_frame11_user_button
        global group9_frame12_user_label
        global group9_frame12_status_text
        global group9_frame12_user_button
        global group10_frame1_user_label
        global group10_frame1_status_text
        global group10_frame1_user_button
        global group10_frame2_user_label
        global group10_frame2_status_text
        global group10_frame2_user_button
        global group10_frame3_user_label
        global group10_frame3_status_text
        global group10_frame3_user_button
        global group10_frame4_user_label
        global group10_frame4_status_text
        global group10_frame4_user_button
        global group10_frame5_user_label
        global group10_frame5_status_text
        global group10_frame5_user_button
        global group10_frame6_user_label
        global group10_frame6_status_text
        global group10_frame6_user_button
        global group10_frame7_user_label
        global group10_frame7_status_text
        global group10_frame7_user_button
        global group10_frame8_user_label
        global group10_frame8_status_text
        global group10_frame8_user_button
        global group10_frame9_user_label
        global group10_frame9_status_text
        global group10_frame9_user_button
        global group10_frame10_user_label
        global group10_frame10_status_text
        global group10_frame10_user_button
        global group10_frame11_user_label
        global group10_frame11_status_text
        global group10_frame11_user_button
        global group10_frame12_user_label
        global group10_frame12_status_text
        global group10_frame12_user_button
        global app_config_ini_val_global
        global app_config_request_global
        global gui_group_one_object
        global gui_group_two_object
        global gui_group_three_object
        global gui_group_four_object
        global gui_group_five_object
        global gui_group_six_object
        global gui_group_seven_object
        global gui_group_eight_object
        global gui_group_nine_object
        global gui_group_ten_object
        global OBJECT_toplevel_user_gui_1_config_class
        global OBJECT_toplevel_user_gui_2_config_class
        global OBJECT_toplevel_user_gui_3_config_class
        global OBJECT_toplevel_user_gui_4_config_class
        global OBJECT_toplevel_user_gui_5_config_class
        global OBJECT_toplevel_user_gui_6_config_class
        global OBJECT_toplevel_user_gui_7_config_class
        global OBJECT_toplevel_user_gui_8_config_class
        global OBJECT_toplevel_user_gui_9_config_class
        global OBJECT_toplevel_user_gui_10_config_class
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
            
        #self.master = master
        #self.frame = tk.Frame(self.master)  

        huge_font = ('Verdana',32)
        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        OBJECT_toplevel_user_gui_config_class = self.master
        instance_object_LIST.append(self.master)

        # print("   ")
        # print(".... III-INSIDE USER-DEFINED MEDICAL RECORD CLASS .... self.master = " + str(self.master) )
        # print(".... III-INSIDE USER-DEFINED MEDICAL RECORD CLASS .... self.master = " + str(self.master) )
        # print("   ")


        if user_defined_gui_instance_count_GLOBAL == 10:
            gui_group_ten_object = self.master
            OBJECT_toplevel_user_gui_10_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_TEN"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_ten_object   " + str(gui_group_ten_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   T E N")
        elif user_defined_gui_instance_count_GLOBAL == 9:
            gui_group_nine_object = self.master
            OBJECT_toplevel_user_gui_9_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_NINE"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_nine_object   " + str(gui_group_nine_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   N I N E")
        elif user_defined_gui_instance_count_GLOBAL == 8:
            gui_group_eight_object = self.master
            OBJECT_toplevel_user_gui_8_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_EIGHT"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_eight_object   " + str(gui_group_eight_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   E I G H T")
        elif user_defined_gui_instance_count_GLOBAL == 7:
            gui_group_seven_object = self.master
            OBJECT_toplevel_user_gui_7_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_SEVEN"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_seven_object   " + str(gui_group_seven_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   S E V E N")
        elif user_defined_gui_instance_count_GLOBAL == 6:
            gui_group_six_object = self.master
            OBJECT_toplevel_user_gui_6_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_SIX"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_six_object   " + str(gui_group_six_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   S I X")
        elif user_defined_gui_instance_count_GLOBAL == 5:
            gui_group_five_object = self.master
            OBJECT_toplevel_user_gui_5_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_FIVE"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_five_object   " + str(gui_group_five_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   F I V E")
        elif user_defined_gui_instance_count_GLOBAL == 4:
            gui_group_four_object = self.master
            OBJECT_toplevel_user_gui_4_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_FOUR"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_four_object   " + str(gui_group_four_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   F O U R")
        elif user_defined_gui_instance_count_GLOBAL == 3:
            gui_group_three_object = self.master
            OBJECT_toplevel_user_gui_3_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_THREE"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_three_object   " + str(gui_group_three_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   T H R E E")
        elif user_defined_gui_instance_count_GLOBAL == 2:
            gui_group_two_object = self.master
            OBJECT_toplevel_user_gui_2_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_TWO"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_two_object   " + str(gui_group_two_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   T W O")
        elif user_defined_gui_instance_count_GLOBAL == 1:
            gui_group_one_object = self.master
            OBJECT_toplevel_user_gui_1_config_class = self.master
            self.USER_GUI_Config_Class_INSTANCE_ID = "INSTANCE_ONE"
            # print(".... INSIDE USER-DEFINED MEDICAL RECORD CLASS .... gui_group_one_object   " + str(gui_group_one_object) )
            self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - User-Defined Graphical User Interface:   M E D I C A L   R E C O R D  -  G R O U P   O N E")
        
        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")
        
        ############################################################
        #
        # If no medical_record_config.ini exists, then we call
        # self.very_first_create_medical_record_config_ini()
        #
        ############################################################

        fullpath_med_config_ini_global = os.path.join(str(cm_appdatafiles_path_global), "medical_record_config.ini" )
        
        if os.path.isfile(fullpath_med_config_ini_global) == False:
            self.very_first_create_medical_record_config_ini()

        ##############################################################################
        # 
        # Load the current medical_record.ini file to initialize all the globals
        # called here in the initialization of Class - USER_GUI_Config_Class(Frame)
        #
        ##############################################################################
        #
        self.load_medical_record_config_ini()

        #####################################################################

        user_gui_bg_color_value_global = "midnight blue"
        
        self.master.configure(background=str(user_gui_bg_color_value_global) )

        config_bg_color_val_global = "midnight blue"

        frame_highlightcolor = "cyan"

        frame_highlightbackground = "red4"
 
        self.Frame1 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame1.grid(row = 0, column = 0, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "goldenrod3"
        
        self.Frame2 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame2.grid(row = 0, column = 1, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "green4"

        self.Frame3 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame3.grid(row = 0, column = 2, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "RoyalBlue1"
        
        self.Frame4 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame4.grid(row = 0, column = 3, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "red4"
        
        self.Frame5 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame5.grid(row = 4, column = 0, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "goldenrod3"
        
        self.Frame6 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame6.grid(row = 4, column = 1, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "green4"
        
        self.Frame7 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame7.grid(row = 4, column = 2, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "RoyalBlue1"
        
        self.Frame8 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame8.grid(row = 4, column = 3, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "red4"
        
        self.Frame9 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame9.grid(row = 8, column = 0, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "goldenrod3"
        
        self.Frame10 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame10.grid(row = 8, column = 1, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "green4"
        
        self.Frame11 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame11.grid(row = 8, column = 2, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        frame_highlightbackground = "RoyalBlue1"
        
        self.Frame12 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground=frame_highlightbackground, highlightcolor=frame_highlightcolor)
        self.Frame12.grid(row = 8, column = 3, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)


        self.user_entry_1_stringvar = StringVar()
        self.user_entry_2_stringvar = StringVar()
        self.user_entry_3_stringvar = StringVar()
        self.user_entry_4_stringvar = StringVar()
        self.user_entry_5_stringvar = StringVar()
        self.user_entry_6_stringvar = StringVar()
        self.user_entry_7_stringvar = StringVar()
        self.user_entry_8_stringvar = StringVar()
        self.user_entry_9_stringvar = StringVar()
        self.user_entry_10_stringvar = StringVar()
        self.user_entry_11_stringvar = StringVar()
        self.user_entry_12_stringvar = StringVar()

        # Class variables to track instances of TEXT WIDGET and ENTRY WIDGET 
        self.text_instances = []
        self.entry_instances = []

        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame1_user_label
            group_frame_status_text = group10_frame1_status_text
            group_frame_user_button = group10_frame1_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame1_user_label
            group_frame_status_text = group9_frame1_status_text
            group_frame_user_button = group9_frame1_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame1_user_label
            group_frame_status_text = group8_frame1_status_text
            group_frame_user_button = group8_frame1_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame1_user_label
            group_frame_status_text = group7_frame1_status_text
            group_frame_user_button = group7_frame1_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame1_user_label
            group_frame_status_text = group6_frame1_status_text
            group_frame_user_button = group6_frame1_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame1_user_label
            group_frame_status_text = group5_frame1_status_text
            group_frame_user_button = group5_frame1_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame1_user_label
            group_frame_status_text = group4_frame1_status_text
            group_frame_user_button = group4_frame1_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame1_user_label
            group_frame_status_text = group3_frame1_status_text
            group_frame_user_button = group3_frame1_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame1_user_label
            group_frame_status_text = group2_frame1_status_text
            group_frame_user_button = group2_frame1_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame1_user_label
            group_frame_status_text = group1_frame1_status_text
            group_frame_user_button = group1_frame1_user_button

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame1_user_label = "Insulin - mU/L (Fasting)"
        # group1_frame1_status_text = "Enter Fasting Insulin Level below ..."
        # group1_frame1_user_button = "Record Insulin" 

        # Instantiate FIRST FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame1)   
        for r in range(4):
            self.Frame1.rowconfigure(r, weight=1)    
            self.Frame1.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame1, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_1_stringvar, group_frame_user_button)
        
        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame2_user_label = "Insulin Resistance - mU/L (2 hrs)"
        # group1_frame2_status_text = "Enter Insulin Resistance below ..."
        # group1_frame2_user_button = "Record Insulin Resistance"


        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame2_user_label
            group_frame_status_text = group10_frame2_status_text
            group_frame_user_button = group10_frame2_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame2_user_label
            group_frame_status_text = group9_frame2_status_text
            group_frame_user_button = group9_frame2_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame2_user_label
            group_frame_status_text = group8_frame2_status_text
            group_frame_user_button = group8_frame2_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame2_user_label
            group_frame_status_text = group7_frame2_status_text
            group_frame_user_button = group7_frame2_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame2_user_label
            group_frame_status_text = group6_frame2_status_text
            group_frame_user_button = group6_frame2_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame2_user_label
            group_frame_status_text = group5_frame2_status_text
            group_frame_user_button = group5_frame2_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame2_user_label
            group_frame_status_text = group4_frame2_status_text
            group_frame_user_button = group4_frame2_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame2_user_label
            group_frame_status_text = group3_frame2_status_text
            group_frame_user_button = group3_frame2_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame2_user_label
            group_frame_status_text = group2_frame2_status_text
            group_frame_user_button = group2_frame2_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame2_user_label
            group_frame_status_text = group1_frame2_status_text
            group_frame_user_button = group1_frame2_user_button

        # Instantiate SECOND FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame2)
        for r in range(4):
            self.Frame2.rowconfigure(r, weight=1)    
            self.Frame2.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame2, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_2_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame3_user_label = "Glucose - mg/dL (Fasting)"
        # group1_frame3_status_text = "Enter Glucose Level below ..."
        # group1_frame3_user_button = "Record Glucose"

        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame3_user_label
            group_frame_status_text = group10_frame3_status_text
            group_frame_user_button = group10_frame3_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame3_user_label
            group_frame_status_text = group9_frame3_status_text
            group_frame_user_button = group9_frame3_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame3_user_label
            group_frame_status_text = group8_frame3_status_text
            group_frame_user_button = group8_frame3_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame3_user_label
            group_frame_status_text = group7_frame3_status_text
            group_frame_user_button = group7_frame3_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame3_user_label
            group_frame_status_text = group6_frame3_status_text
            group_frame_user_button = group6_frame3_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame3_user_label
            group_frame_status_text = group5_frame3_status_text
            group_frame_user_button = group5_frame3_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame3_user_label
            group_frame_status_text = group4_frame3_status_text
            group_frame_user_button = group4_frame3_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame3_user_label
            group_frame_status_text = group3_frame3_status_text
            group_frame_user_button = group3_frame3_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame3_user_label
            group_frame_status_text = group2_frame3_status_text
            group_frame_user_button = group2_frame3_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame3_user_label
            group_frame_status_text = group1_frame3_status_text
            group_frame_user_button = group1_frame3_user_button
        
        # Instantiate THIRD FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame3)
        for r in range(4):
            self.Frame3.rowconfigure(r, weight=1)    
            self.Frame3.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame3, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_3_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame4_user_label = "Glucose Response - mg/dL (2 hrs)"
        # group1_frame4_status_text = "Enter Glucose Response below ..."
        # group1_frame4_user_button = "Record Glucose Response"

        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame4_user_label
            group_frame_status_text = group10_frame4_status_text
            group_frame_user_button = group10_frame4_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame4_user_label
            group_frame_status_text = group9_frame4_status_text
            group_frame_user_button = group9_frame4_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame4_user_label
            group_frame_status_text = group8_frame4_status_text
            group_frame_user_button = group8_frame4_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame4_user_label
            group_frame_status_text = group7_frame4_status_text
            group_frame_user_button = group7_frame4_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame4_user_label
            group_frame_status_text = group6_frame4_status_text
            group_frame_user_button = group6_frame4_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame4_user_label
            group_frame_status_text = group5_frame4_status_text
            group_frame_user_button = group5_frame4_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame4_user_label
            group_frame_status_text = group4_frame4_status_text
            group_frame_user_button = group4_frame4_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame4_user_label
            group_frame_status_text = group3_frame4_status_text
            group_frame_user_button = group3_frame4_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame4_user_label
            group_frame_status_text = group2_frame4_status_text
            group_frame_user_button = group2_frame4_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame4_user_label
            group_frame_status_text = group1_frame4_status_text
            group_frame_user_button = group1_frame4_user_button
        
        # Instantiate FOURTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame4) 
        for r in range(4):
            self.Frame4.rowconfigure(r, weight=1)    
            self.Frame4.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame4, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_4_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame5_user_label = "LDL-Cholesterol"
        # group1_frame5_status_text = "Enter LDL-Cholesterol below ..."
        # group1_frame5_user_button = "Record LDL-Cholesterol"

        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame5_user_label
            group_frame_status_text = group10_frame5_status_text
            group_frame_user_button = group10_frame5_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame5_user_label
            group_frame_status_text = group9_frame5_status_text
            group_frame_user_button = group9_frame5_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame5_user_label
            group_frame_status_text = group8_frame5_status_text
            group_frame_user_button = group8_frame5_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame5_user_label
            group_frame_status_text = group7_frame5_status_text
            group_frame_user_button = group7_frame5_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame5_user_label
            group_frame_status_text = group6_frame5_status_text
            group_frame_user_button = group6_frame5_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame5_user_label
            group_frame_status_text = group5_frame5_status_text
            group_frame_user_button = group5_frame5_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame5_user_label
            group_frame_status_text = group4_frame5_status_text
            group_frame_user_button = group4_frame5_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame5_user_label
            group_frame_status_text = group3_frame5_status_text
            group_frame_user_button = group3_frame5_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame5_user_label
            group_frame_status_text = group2_frame5_status_text
            group_frame_user_button = group2_frame5_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame5_user_label
            group_frame_status_text = group1_frame5_status_text
            group_frame_user_button = group1_frame5_user_button
        
        # Instantiate FIFTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame5) 
        for r in range(4):
            self.Frame5.rowconfigure(r, weight=1)    
            self.Frame5.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame5, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_5_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame6_user_label = "Total Cholesterol"
        # group1_frame6_status_text = "Enter Total Cholesterol below ..."
        # group1_frame6_user_button = "Record Total Cholesterol"


        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame6_user_label
            group_frame_status_text = group10_frame6_status_text
            group_frame_user_button = group10_frame6_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame6_user_label
            group_frame_status_text = group9_frame6_status_text
            group_frame_user_button = group9_frame6_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame6_user_label
            group_frame_status_text = group8_frame6_status_text
            group_frame_user_button = group8_frame6_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame6_user_label
            group_frame_status_text = group7_frame6_status_text
            group_frame_user_button = group7_frame6_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame6_user_label
            group_frame_status_text = group6_frame6_status_text
            group_frame_user_button = group6_frame6_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame6_user_label
            group_frame_status_text = group5_frame6_status_text
            group_frame_user_button = group5_frame6_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame6_user_label
            group_frame_status_text = group4_frame6_status_text
            group_frame_user_button = group4_frame6_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame6_user_label
            group_frame_status_text = group3_frame6_status_text
            group_frame_user_button = group3_frame6_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame6_user_label
            group_frame_status_text = group2_frame6_status_text
            group_frame_user_button = group2_frame6_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame6_user_label
            group_frame_status_text = group1_frame6_status_text
            group_frame_user_button = group1_frame6_user_button
        
        # Instantiate SIXTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame6)
        for r in range(4):
            self.Frame6.rowconfigure(r, weight=1)    
            self.Frame6.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame6, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_6_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame7_user_label = "HDL-Cholesterol"
        # group1_frame7_status_text = "Enter HDL-Cholesterol below ..."
        # group1_frame7_user_button = "Record HDL-Cholesterol"


        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame7_user_label
            group_frame_status_text = group10_frame7_status_text
            group_frame_user_button = group10_frame7_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame7_user_label
            group_frame_status_text = group9_frame7_status_text
            group_frame_user_button = group9_frame7_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame7_user_label
            group_frame_status_text = group8_frame7_status_text
            group_frame_user_button = group8_frame7_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame7_user_label
            group_frame_status_text = group7_frame7_status_text
            group_frame_user_button = group7_frame7_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame7_user_label
            group_frame_status_text = group6_frame7_status_text
            group_frame_user_button = group6_frame7_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame7_user_label
            group_frame_status_text = group5_frame7_status_text
            group_frame_user_button = group5_frame7_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame7_user_label
            group_frame_status_text = group4_frame7_status_text
            group_frame_user_button = group4_frame7_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame7_user_label
            group_frame_status_text = group3_frame7_status_text
            group_frame_user_button = group3_frame7_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame7_user_label
            group_frame_status_text = group2_frame7_status_text
            group_frame_user_button = group2_frame7_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame7_user_label
            group_frame_status_text = group1_frame7_status_text
            group_frame_user_button = group1_frame7_user_button
        
        # Instantiate SEVENTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame7)
        for r in range(4):
            self.Frame7.rowconfigure(r, weight=1)    
            self.Frame7.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame7, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_7_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame8_user_label = "Triglycerides"
        # group1_frame8_status_text = "Enter Triglycerides below ..."
        # group1_frame8_user_button = "Record Triglycerides"


        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame8_user_label
            group_frame_status_text = group10_frame8_status_text
            group_frame_user_button = group10_frame8_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame8_user_label
            group_frame_status_text = group9_frame8_status_text
            group_frame_user_button = group9_frame8_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame8_user_label
            group_frame_status_text = group8_frame8_status_text
            group_frame_user_button = group8_frame8_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame8_user_label
            group_frame_status_text = group7_frame8_status_text
            group_frame_user_button = group7_frame8_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame8_user_label
            group_frame_status_text = group6_frame8_status_text
            group_frame_user_button = group6_frame8_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame8_user_label
            group_frame_status_text = group5_frame8_status_text
            group_frame_user_button = group5_frame8_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame8_user_label
            group_frame_status_text = group4_frame8_status_text
            group_frame_user_button = group4_frame8_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame8_user_label
            group_frame_status_text = group3_frame8_status_text
            group_frame_user_button = group3_frame8_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame8_user_label
            group_frame_status_text = group2_frame8_status_text
            group_frame_user_button = group2_frame8_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame8_user_label
            group_frame_status_text = group1_frame8_status_text
            group_frame_user_button = group1_frame8_user_button
        
        # Instantiate EIGHTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame8) 
        for r in range(4):
            self.Frame8.rowconfigure(r, weight=1)    
            self.Frame8.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame8, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_8_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame9_user_label = "Body Weight"
        # group1_frame9_status_text = "Enter Body Weight below ..."
        # group1_frame9_user_button = "Record Body Weight"


        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame9_user_label
            group_frame_status_text = group10_frame9_status_text
            group_frame_user_button = group10_frame9_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame9_user_label
            group_frame_status_text = group9_frame9_status_text
            group_frame_user_button = group9_frame9_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame9_user_label
            group_frame_status_text = group8_frame9_status_text
            group_frame_user_button = group8_frame9_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame9_user_label
            group_frame_status_text = group7_frame9_status_text
            group_frame_user_button = group7_frame9_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame9_user_label
            group_frame_status_text = group6_frame9_status_text
            group_frame_user_button = group6_frame9_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame9_user_label
            group_frame_status_text = group5_frame9_status_text
            group_frame_user_button = group5_frame9_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame9_user_label
            group_frame_status_text = group4_frame9_status_text
            group_frame_user_button = group4_frame9_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame9_user_label
            group_frame_status_text = group3_frame9_status_text
            group_frame_user_button = group3_frame9_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame9_user_label
            group_frame_status_text = group2_frame9_status_text
            group_frame_user_button = group2_frame9_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame9_user_label
            group_frame_status_text = group1_frame9_status_text
            group_frame_user_button = group1_frame9_user_button
        
        # Instantiate NINTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame9)
        for r in range(4):
            self.Frame9.rowconfigure(r, weight=1)    
            self.Frame9.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame9, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_9_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame10_user_label = "Body Height" 
        # group1_frame10_status_text = "Enter Body Height below ..."
        # group1_frame10_user_button = "Record Body Height"


        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame10_user_label
            group_frame_status_text = group10_frame10_status_text
            group_frame_user_button = group10_frame10_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame10_user_label
            group_frame_status_text = group9_frame10_status_text
            group_frame_user_button = group9_frame10_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame10_user_label
            group_frame_status_text = group8_frame10_status_text
            group_frame_user_button = group8_frame10_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame10_user_label
            group_frame_status_text = group7_frame10_status_text
            group_frame_user_button = group7_frame10_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame10_user_label
            group_frame_status_text = group6_frame10_status_text
            group_frame_user_button = group6_frame10_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame10_user_label
            group_frame_status_text = group5_frame10_status_text
            group_frame_user_button = group5_frame10_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame10_user_label
            group_frame_status_text = group4_frame10_status_text
            group_frame_user_button = group4_frame10_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame10_user_label
            group_frame_status_text = group3_frame10_status_text
            group_frame_user_button = group3_frame10_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame10_user_label
            group_frame_status_text = group2_frame10_status_text
            group_frame_user_button = group2_frame10_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame10_user_label
            group_frame_status_text = group1_frame10_status_text
            group_frame_user_button = group1_frame10_user_button
        
        # Instantiate TENTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame10)
        for r in range(4):
            self.Frame10.rowconfigure(r, weight=1)    
            self.Frame10.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame10, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_10_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame11_user_label = "Resting Heart Rate"
        # group1_frame11_status_text = "Enter Resting Heart Rate below ..."
        # group1_frame11_user_button = "Record Resting Heart Rate"


        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame11_user_label
            group_frame_status_text = group10_frame11_status_text
            group_frame_user_button = group10_frame11_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame11_user_label
            group_frame_status_text = group9_frame11_status_text
            group_frame_user_button = group9_frame11_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame11_user_label
            group_frame_status_text = group8_frame11_status_text
            group_frame_user_button = group8_frame11_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame11_user_label
            group_frame_status_text = group7_frame11_status_text
            group_frame_user_button = group7_frame11_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame11_user_label
            group_frame_status_text = group6_frame11_status_text
            group_frame_user_button = group6_frame11_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame11_user_label
            group_frame_status_text = group5_frame11_status_text
            group_frame_user_button = group5_frame11_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame11_user_label
            group_frame_status_text = group4_frame11_status_text
            group_frame_user_button = group4_frame11_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame11_user_label
            group_frame_status_text = group3_frame11_status_text
            group_frame_user_button = group3_frame11_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame11_user_label
            group_frame_status_text = group2_frame11_status_text
            group_frame_user_button = group2_frame11_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame11_user_label
            group_frame_status_text = group1_frame11_status_text
            group_frame_user_button = group1_frame11_user_button
        
        # Instantiate ELEVENTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame11)  
        for r in range(4):
            self.Frame11.rowconfigure(r, weight=1)    
            self.Frame11.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame11, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_11_stringvar, group_frame_user_button)

        # NOTE: These group-frame globals are set when app_config.ini file is loaded.
        #
        # Widget Configuration (Global) Variables loaded from app_config.ini
        # group1_frame12_user_label = "Blood Press - (Sys/Dias) - mm Hg" 
        # group1_frame12_status_text = "Enter Blood Pressure below ..."
        # group1_frame12_user_button = "Record Blood Pressure"


        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            group_frame_user_label = group10_frame12_user_label
            group_frame_status_text = group10_frame12_status_text
            group_frame_user_button = group10_frame12_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            group_frame_user_label = group9_frame12_user_label
            group_frame_status_text = group9_frame12_status_text
            group_frame_user_button = group9_frame12_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            group_frame_user_label = group8_frame12_user_label
            group_frame_status_text = group8_frame12_status_text
            group_frame_user_button = group8_frame12_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            group_frame_user_label = group7_frame12_user_label
            group_frame_status_text = group7_frame12_status_text
            group_frame_user_button = group7_frame12_user_button

        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            group_frame_user_label = group6_frame12_user_label
            group_frame_status_text = group6_frame12_status_text
            group_frame_user_button = group6_frame12_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            group_frame_user_label = group5_frame12_user_label
            group_frame_status_text = group5_frame12_status_text
            group_frame_user_button = group5_frame12_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            group_frame_user_label = group4_frame12_user_label
            group_frame_status_text = group4_frame12_status_text
            group_frame_user_button = group4_frame12_user_button
        
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            group_frame_user_label = group3_frame12_user_label
            group_frame_status_text = group3_frame12_status_text
            group_frame_user_button = group3_frame12_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            group_frame_user_label = group2_frame12_user_label
            group_frame_status_text = group2_frame12_status_text
            group_frame_user_button = group2_frame12_user_button
            
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            group_frame_user_label = group1_frame12_user_label
            group_frame_status_text = group1_frame12_status_text
            group_frame_user_button = group1_frame12_user_button
        
        # Instantiate TWELVTH FRAME of FOUR USER GUI WIDGETS (Label, Entry, Text, Button)
        # using method - self.widget_group_template(self.Frame12)  
        for r in range(4):
            self.Frame12.rowconfigure(r, weight=1)    
            self.Frame12.columnconfigure(0, weight=1)

        self.widget_group_template(self.Frame12, group_frame_user_label, group_frame_status_text, \
                                   self.user_entry_12_stringvar, group_frame_user_button)
            
        #
        # Lift the MAIN SCREEN Button
        # 
        self.lift_the_main_Button = Button(self.master, text = "MAIN SCREEN", width = 15, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2", command = self.lift_the_main_WINDOW)

        self.lift_the_main_Button.grid(row=12, column=0)

        #
        # GROUP #1 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST 
        # 
        self.group_one_window_Button = Button(self.master, text = "Select\nPanel 1", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2")  
        self.group_one_window_Button.bind("<Button-1>", self.lift_group_one_WINDOW)
        self.group_one_window_Button.grid(row=12, column=1, sticky = W)

        # 
        # GROUP #1 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #1 WINDOW SELECTED.
        #  
        self.group_one_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_one_window_signal_label.grid(row=13, column=1, sticky = W)

        #
        # GROUP #2 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST 
        # 
        self.group_two_window_Button = Button(self.master, text = "Select\nPanel 2", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2") 
        self.group_two_window_Button.bind("<Button-1>", self.lift_group_two_WINDOW)
        self.group_two_window_Button.grid(row=12, column=1)

        #
        # GROUP #2 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #2 WINDOW SELECTED.
        #  
        self.group_two_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_two_window_signal_label.grid(row=13, column=1)

        #
        # GROUP #3 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST 
        # 
        self.group_three_window_Button = Button(self.master, text = "Select\nPanel 3", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2")  
        self.group_three_window_Button.bind("<Button-1>", self.lift_group_three_WINDOW)
        self.group_three_window_Button.grid(row=12, column=1, sticky = E)

        #
        # GROUP #3 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #3 WINDOW SELECTED.
        #  
        self.group_three_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_three_window_signal_label.grid(row=13, column=1, sticky = E)

        #
        # GROUP #4 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST 
        # 
        self.group_four_window_Button = Button(self.master, text = "Select\nPanel 4", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2")  
        self.group_four_window_Button.bind("<Button-1>", self.lift_group_four_WINDOW)
        self.group_four_window_Button.grid(row=12, column=2, sticky = W)

        #
        # GROUP #4 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #4 WINDOW SELECTED.
        # 
        self.group_four_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_four_window_signal_label.grid(row=13, column=2, sticky = W)

        #
        # GROUP #5 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST
        # 
        self.group_five_window_Button = Button(self.master, text = "Select\nPanel 5", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2") 
        self.group_five_window_Button.bind("<Button-1>", self.lift_group_five_WINDOW)
        self.group_five_window_Button.grid(row=12, column=2)

        #
        # GROUP #5 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #5 WINDOW SELECTED.
        # 
        self.group_five_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_five_window_signal_label.grid(row=13, column=2)

        #
        # GROUP #6 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST
        # 
        self.group_six_window_Button = Button(self.master, text = "Select\nPanel 6", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2")  
        self.group_six_window_Button.bind("<Button-1>", self.lift_group_six_WINDOW)
        self.group_six_window_Button.grid(row=12, column=2, sticky = E)

        #
        # GROUP #6 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #6 WINDOW SELECTED. 
        # 
        self.group_six_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_six_window_signal_label.grid(row=13, column=2, sticky = E)

        #
        # GROUP #7 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST
        # 
        self.group_seven_window_Button = Button(self.master, text = "Select\nPanel 7", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2")  
        self.group_seven_window_Button.bind("<Button-1>", self.lift_group_seven_WINDOW)
        self.group_seven_window_Button.grid(row=12, column=3, sticky = W)

        #
        # GROUP #7 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #7 WINDOW SELECTED.
        # 
        self.group_seven_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_seven_window_signal_label.grid(row=13, column=3, sticky = W)

        #
        # GROUP #8 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST
        # 
        self.group_eight_window_Button = Button(self.master, text = "Select\nPanel 8", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2")  
        self.group_eight_window_Button.bind("<Button-1>", self.lift_group_eight_WINDOW)
        self.group_eight_window_Button.grid(row=12, column=3)

        #
        # GROUP #8 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #8 WINDOW SELECTED.
        # 
        self.group_eight_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_eight_window_signal_label.grid(row=13, column=3)

        #
        # GROUP #9 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST 
        # 
        self.group_nine_window_Button = Button(self.master, text = "Select\nPanel 9", width = 6, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2") 
        self.group_nine_window_Button.bind("<Button-1>", self.lift_group_nine_WINDOW)
        self.group_nine_window_Button.grid(row=12, column=3, sticky = E)

        #
        # GROUP #9 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #9 WINDOW SELECTED.
        # 
        self.group_nine_window_signal_label = Label(self.master, width = 13, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_nine_window_signal_label.grid(row=13, column=3, sticky = E)

        #
        # GROUP #10 WINDOW SELECT BUTTON. global USER_GUI_Config_Class_inst_LIST 
        # 
        self.group_ten_window_Button = Button(self.master, text = "Select\nPanel 10", width = 7, height = 2, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2") 
        self.group_ten_window_Button.bind("<Button-1>", self.lift_group_ten_WINDOW)
        self.group_ten_window_Button.grid(row=12, column=4, sticky = W)

        #
        # GROUP #10 WINDOW SIGNAL BUTTON. event_generate IF self.master indicates GROUP #10 WINDOW SELECTED.
        # 
        self.group_ten_window_signal_label = Label(self.master, width = 14, height = 1, \
            font=('Helvetica', '8'), background="cyan4", fg="black", borderwidth=5, relief="raised")
        self.group_ten_window_signal_label.grid(row=13, column=4, sticky = W)
        
        
        #Class variable to track instances of TEXT WIDGET 
        frame_number = 1
        for item in self.text_instances:
            if frame_number == 1:
                self.text_widget_instance_Frame1 = item
            elif frame_number == 2:
                self.text_widget_instance_Frame2 = item
            elif frame_number == 3:
                self.text_widget_instance_Frame3 = item
            elif frame_number == 4:
                self.text_widget_instance_Frame4 = item
            elif frame_number == 5:
                self.text_widget_instance_Frame5 = item
            elif frame_number == 6:
                self.text_widget_instance_Frame6 = item
            elif frame_number == 7:
                self.text_widget_instance_Frame7 = item
            elif frame_number == 8:
                self.text_widget_instance_Frame8 = item
            elif frame_number == 9:
                self.text_widget_instance_Frame9 = item
            elif frame_number == 10:
                self.text_widget_instance_Frame10 = item
            elif frame_number == 11:
                self.text_widget_instance_Frame11 = item
            elif frame_number == 12:
                self.text_widget_instance_Frame12 = item

            frame_number+=1
            
            # print(".... self.text_instances LIST ITEM = " + str(item) )

        
        #Class variable to track instances of ENTRY WIDGET
        frame_number = 1
        for item in self.entry_instances:
            if frame_number == 1:
                self.entry_widget_instance_Frame1 = item
            elif frame_number == 2:
                self.entry_widget_instance_Frame2 = item
            elif frame_number == 3:
                self.entry_widget_instance_Frame3 = item
            elif frame_number == 4:
                self.entry_widget_instance_Frame4 = item
            elif frame_number == 5:
                self.entry_widget_instance_Frame5 = item
            elif frame_number == 6:
                self.entry_widget_instance_Frame6 = item
            elif frame_number == 7:
                self.entry_widget_instance_Frame7 = item
            elif frame_number == 8:
                self.entry_widget_instance_Frame8 = item
            elif frame_number == 9:
                self.entry_widget_instance_Frame9 = item
            elif frame_number == 10:
                self.entry_widget_instance_Frame10 = item
            elif frame_number == 11:
                self.entry_widget_instance_Frame11 = item
            elif frame_number == 12:
                self.entry_widget_instance_Frame12 = item

            frame_number+=1

        # Indicate illuminated Label under GROUP SELECT BUTTON for respective Group Window
        # so that when that GROUP WINDOW is selected, there is an illiminated Label to
        # indicate to the USER which GROUP WINDOW is selected.

        if self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TEN":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_instance = "group_ten_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_NINE":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_nine_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_EIGHT":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_eight_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SEVEN":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_seven_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_SIX":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_six_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FIVE":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_five_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_FOUR":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_four_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_THREE":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_three_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_TWO":
            self.group_one_window_signal_label.config(bg="cyan4", text="")
            self.group_two_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_two_instance"
        elif self.USER_GUI_Config_Class_INSTANCE_ID == "INSTANCE_ONE":
            self.group_one_window_signal_label.config(bg="cyan", text="ACTIVE")
            self.group_two_window_signal_label.config(bg="cyan4", text="")
            self.group_three_window_signal_label.config(bg="cyan4", text="")
            self.group_four_window_signal_label.config(bg="cyan4", text="")
            self.group_five_window_signal_label.config(bg="cyan4", text="")
            self.group_six_window_signal_label.config(bg="cyan4", text="")
            self.group_seven_window_signal_label.config(bg="cyan4", text="")
            self.group_eight_window_signal_label.config(bg="cyan4", text="")
            self.group_nine_window_signal_label.config(bg="cyan4", text="")
            self.group_ten_window_signal_label.config(bg="cyan4", text="")
            self.group_instance = "group_one_instance"

        #############################################################################
        #
        #   END of INITIALIZATION METHOD for class USER_GUI_Config_Class(Frame)
        #  
        #############################################################################
 

        #############################################################################
        #
        # Create medical_record_config.ini for the FIRST TIME 
        #
        # as we create medical_record_config.ini when it does not already exist.
        #
        #############################################################################
    def very_first_create_medical_record_config_ini(self):
        global fullpath_med_config_ini_global

        fullpath_med_config_ini_global = os.path.join(str(cm_appdatafiles_path_global), "medical_record_config.ini" )

        # print("  ") 
        # print(".... VERY FIRST .... fullpath_med_config_ini_global = " + str(fullpath_med_config_ini_global) )

        # instantiate ConfigParser() 
        very_first_medical_config = ConfigParser()

        # METHOD:  very_first_create_medical_record_config_ini .....   
        #
        # We create medical_record_config.ini for the FIRST TIME, ONLY IF it does not already exist.
        #
        # This method is called (above in initialiation) ONLY IF medical_record_config.ini does not already exist.
        #
        if os.path.isfile(fullpath_med_config_ini_global) == False:  # self.very_first_create_medical_record_config_ini()

            # print(".... VERY FIRST  medical_record_config.ini  being written .....") 

            very_first_medical_config.add_section("USER_DESIGNS_GUI")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_title", "User Designs Screen Layout and Data Name")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_title_bg_color", "cyan4")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_title_fg_color", "light sea green")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_bg_color", "dark slate gray")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_fg_color", "snow")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_label_bg_color", "cyan4")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_label_fg_color", "cyan")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_entry_bg_color", "light sea green")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_entry_fg_color", "black")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_text_bg_color", "light sea green")
            very_first_medical_config.set("USER_DESIGNS_GUI", "user_gui_text_fg_color", "black")

            ###############################################################################################
            # 
            #   M E D I C A L    P H Y S I O L O G Y   U S E R    G U I   C O N F I G U R A T I O N 
            #  
            ###############################################################################################
            #
            # USER_GUI_CONFIG Class - WIDGET Configuration - 3 Windows (Data Groups) of 12 WIDGET Frames
            #
            # Widget Configuration (Global) Variables written to app_config.ini
            #
            ###############################################################################################
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame1_user_label", "Insulin - mU/L (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame1_status_text", "Enter Fasting Insulin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame1_user_button", "Record Insulin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame2_user_label", "Insulin Resistance - mU/L (2 hrs)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame2_status_text", "Enter Insulin Resistance below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame2_user_button", "Record Insulin Resistance")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame3_user_label", "Glucose - mg/dL (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame3_status_text", "Enter Glucose Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame3_user_button", "Record Glucose")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame4_user_label", "Glucose Response - mg/dL (2 hrs)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame4_status_text", "Enter Glucose Response below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame4_user_button", "Record Glucose Response")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame5_user_label", "LDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame5_status_text", "Enter LDL-Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame5_user_button", "Record LDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame6_user_label", "Total Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame6_status_text", "Enter Total Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame6_user_button", "Record Total Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame7_user_label", "HDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame7_status_text", "Enter HDL-Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame7_user_button", "Record HDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame8_user_label", "Triglycerides")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame8_status_text", "Enter Triglycerides below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame8_user_button", "Record Triglycerides")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame9_user_label", "Body Weight")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame9_status_text", "Enter Body Weight below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame9_user_button", "Record Body Weight")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame10_user_label", "Body Height")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame10_status_text", "Enter Body Height below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame10_user_button", "Record Body Height")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame11_user_label", "Resting Heart Rate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame11_status_text", "Enter Resting Heart Rate below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame11_user_button", "Record Resting Heart Rate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame12_user_label", "Blood Press - (Sys/Dias) - mm Hg")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame12_status_text", "Enter Blood Pressure below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group1_frame12_user_button", "Record Blood Pressure")

            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame1_user_label", "Serum Creatinine - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame1_status_text", "Enter Serum Creatinine below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame1_user_button", "Record Serum Creatinine")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame2_user_label", "Blood Urea Nitrogen - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame2_status_text", "Enter Blood Urea Nitrogen below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame2_user_button", "Record Blood Urea Nitrogen")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame3_user_label", "Serum Albumin - g/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame3_status_text", "Enter Serum Albumin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame3_user_button", "Record Serum Albumin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame4_user_label", "Globulin - g/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame4_status_text", "Enter Globulin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame4_user_button", "Record Globulin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame5_user_label", "Urine Protein  - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame5_status_text", "Enter Urine Protein Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame5_user_button", "Record Urine Protein")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame6_user_label", "Total Bilirubin - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame6_status_text", "Enter Total Bilirubin below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame6_user_button", "Record Total Bilirubin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame7_user_label", "Direct Bilirubin - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame7_status_text", "Enter Direct-Bilirubin below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame7_user_button", "Record Direct-Bilirubin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame8_user_label", "AST - IU/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame8_status_text", "Enter AST below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame8_user_button", "Record AST")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame9_user_label", "ALT - IU/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame9_status_text", "Enter ALT below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame9_user_button", "Record ALT")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame10_user_label", "GGT - IU/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame10_status_text", "Enter GGT Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame10_user_button", "Record GGT")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame11_user_label", "ALP - U/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame11_status_text", "Enter ALP Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame11_user_button", "Record ALP")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame12_user_label", "25(OH)D (Vitamin D3) - ng/ml")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame12_status_text", "Enter 25(OH)D (Vitamin D3) below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group2_frame12_user_button", "Record 25(OH)D (Vitamin D3)")

            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame1_user_label", "Sodium - mmol/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame1_status_text", "Enter Sodium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame1_user_button", "Record Sodium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame2_user_label", "Potasium - mmol/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame2_status_text", "Enter Potasium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame2_user_button", "Record Potasium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame3_user_label", "Chloride - mmol/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame3_status_text", "Enter Chloride Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame3_user_button", "Record Chloride")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame4_user_label", "Bicarbonate - mmol/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame4_status_text", "Enter Bicarbonate Levels below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame4_user_button", "Record Bicarbonate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame5_user_label", "Calcium - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame5_status_text", "Enter Calium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame5_user_button", "Record Calcium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame6_user_label", "Magnesium - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame6_status_text", "Enter Magnesium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame6_user_button", "Record Magnesium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame7_user_label", "Phosphorus - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame7_status_text", "Enter Phosphorus Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame7_user_button", "Record Phosphorus")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame8_user_label", "O2 Sat - Percent")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame8_status_text", "Enter O2 Sat Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame8_user_button", "Record O2 Sat")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame9_user_label", "Troponins Test")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame9_status_text", "Enter Troponins Results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame9_user_button", "Record Troponins")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame10_user_label", "NT-proBNP - pg/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame10_status_text", "Enter NT-proBNP Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame10_user_button", "Record NT-proBNP")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame11_user_label", "Myoglobin - mcg/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame11_status_text", "Enter Myoglobin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame11_user_button", "Record Myoglobin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame12_user_label", "CKMB - ng/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame12_status_text", "Enter CKMB Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group3_frame12_user_button", "Record CKMB")

            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame1_user_label", "T3 Hormone - ng/dL (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame1_status_text", "Enter T3 Hormone Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame1_user_button", "Record T3 Hormone")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame2_user_label", "HGH - ng/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame2_status_text", "Enter HGH below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame2_user_button", "Record HGH")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame3_user_label", "IGF1 - ng/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame3_status_text", "Enter IGF1 Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame3_user_button", "Record IGF1")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame4_user_label", "Glucagon - pg/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame4_status_text", "Enter Glucagon Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame4_user_button", "Record Glucagon Level")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame5_user_label", "Testosterone - ng/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame5_status_text", "Enter Testosterone below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame5_user_button", "Record Testosterone")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame6_user_label", "Epinephrine - pg/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame6_status_text", "Enter Epinephrine below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame6_user_button", "Record Epinephrine")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame7_user_label", "Norepinephrine - pg/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame7_status_text", "Enter Norepinephrine below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame7_user_button", "Record Norepinephrine")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame8_user_label", "Dopamine - pg/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame8_status_text", "Enter Dopamine below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame8_user_button", "Record Dopamine")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame9_user_label", "Cortisol - mcg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame9_status_text", "Enter Cortisol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame9_user_button", "Record Cortisol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame10_user_label", "Insulin - mU/L (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame10_status_text", "Enter Fasting Insulin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame10_user_button", "Record Insulin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame11_user_label", "Insulin Resistance - mU/L (2 hrs)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame11_status_text", "Enter Insulin Resistance below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame11_user_button", "Record Insulin Resistance")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame12_user_label", "C-peptide - ng/mL (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame12_status_text", "Enter C-peptide below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group4_frame12_user_button", "Record C-peptide") 

            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame1_user_label", "Estradiol - pg/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame1_status_text", "Enter Estradiol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame1_user_button", "Record Estradiol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame2_user_label", "Acetone (BrAce - Breath Ketones)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame2_status_text", "Enter BrAce below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame2_user_button", "Record BrAce")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame3_user_label", "Acetoacetate (Urine Ketones)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame3_status_text", "Enter Acetoacetate below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame3_user_button", "Record Acetoacetate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame4_user_label", "Beta-Hydroxybutryate (Blood Ketones)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame4_status_text", "Enter Beta-Hydroxybutryate below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame4_user_button", "Record Beta-Hydroxybutryate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame5_user_label", "A1C - Percent")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame5_status_text", "Enter A1C Percent below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame5_user_button", "Record A1C Percent")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame6_user_label", "Antimitochondrial Antibodies (AMA)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame6_status_text", "Enter AMA Test Results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame6_user_button", "Record AMA Test Results")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame7_user_label", "Antinuclear Antibody (ANA)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame7_status_text", "Enter ANA Test Results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame7_user_button", "Record Antinuclear Antibody")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame8_user_label", "Anti-double-stranded DNA, IgG")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame8_status_text", "Enter IgG below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame8_user_button", "Record IgG")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame9_user_label", "Extractable Nuclear Antigen (ENA) Panel")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame9_status_text", "Enter ENA results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame9_user_button", "Record ENA")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame10_user_label", "APOE e4")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame10_status_text", "Enter APOE e4 results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame10_user_button", "Record APOE e4")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame11_user_label", "Tau/AB42")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame11_status_text", "Enter Tau/AB42 results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame11_user_button", "Record Tau/AB42")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame12_user_label", "PSEN1")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame12_status_text", "Enter PSEN1 results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group5_frame12_user_button", "Record PSEN1 results")

            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame1_user_label", "TOMM40 Gene (per APOE)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame1_status_text", "Enter TOMM40 results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame1_user_button", "Record TOMM40 Gene")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame2_user_label", "T4 Hormone")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame2_status_text", "Enter T4 Hormone results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame2_user_button", "Record T4 Hormone")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame3_user_label", "FT4 Hormone")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame3_status_text", "Enter FT4 Hormone below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame3_user_button", "Record FT4 Hormone")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame4_user_label", "TPM 21")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame4_status_text", "Enter TPM 21 Levels below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame4_user_button", "Record TPM 21")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame5_user_label", "Amyloid Beta-Protein - pg/ml")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame5_status_text", "Enter Amyloid Beta-Protein below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame5_user_button", "Record Amyloid Beta-Protein")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame6_user_label", "Magnesium - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame6_status_text", "Enter Magnesium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame6_user_button", "Record Magnesium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame7_user_label", "Phosphorus - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame7_status_text", "Enter Phosphorus Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame7_user_button", "Record Phosphorus")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame8_user_label", "O2 Sat - Percent")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame8_status_text", "Enter O2 Sat Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame8_user_button", "Record O2 Sat")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame9_user_label", "Troponins Test")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame9_status_text", "Enter Troponins Results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame9_user_button", "Record Troponins")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame10_user_label", "NT-proBNP - pg/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame10_status_text", "Enter NT-proBNP Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame10_user_button", "Record NT-proBNP")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame11_user_label", "Myoglobin - mcg/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame11_status_text", "Enter Myoglobin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame11_user_button", "Record Myoglobin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame12_user_label", "CKMB - ng/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame12_status_text", "Enter CKMB Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group6_frame12_user_button", "Record CKMB")

            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame1_user_label", "Insulin - mU/L (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame1_status_text", "Enter Fasting Insulin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame1_user_button", "Record Insulin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame2_user_label", "Insulin Resistance - mU/L (2 hrs)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame2_status_text", "Enter Insulin Resistance below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame2_user_button", "Record Insulin Resistance")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame3_user_label", "Glucose - mg/dL (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame3_status_text", "Enter Glucose Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame3_user_button", "Record Glucose")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame4_user_label", "Glucose Response - mg/dL (2 hrs)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame4_status_text", "Enter Glucose Response below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame4_user_button", "Record Glucose Response")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame5_user_label", "LDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame5_status_text", "Enter LDL-Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame5_user_button", "Record LDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame6_user_label", "Total Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame6_status_text", "Enter Total Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame6_user_button", "Record Total Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame7_user_label", "HDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame7_status_text", "Enter HDL-Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame7_user_button", "Record HDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame8_user_label", "Triglycerides")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame8_status_text", "Enter Triglycerides below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame8_user_button", "Record Triglycerides")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame9_user_label", "Body Weight")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame9_status_text", "Enter Body Weight below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame9_user_button", "Record Body Weight")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame10_user_label", "Body Height")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame10_status_text", "Enter Body Height below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame10_user_button", "Record Body Height")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame11_user_label", "Resting Heart Rate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame11_status_text", "Enter Resting Heart Rate below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame11_user_button", "Record Resting Heart Rate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame12_user_label", "Blood Press - (Sys/Dias) - mm Hg")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame12_status_text", "Enter Blood Pressure below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group7_frame12_user_button", "Record Blood Pressure")

            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame1_user_label", "Serum Creatinine - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame1_status_text", "Enter Serum Creatinine below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame1_user_button", "Record Serum Creatinine")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame2_user_label", "Blood Urea Nitrogen - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame2_status_text", "Enter Blood Urea Nitrogen below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame2_user_button", "Record Blood Urea Nitrogen")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame3_user_label", "Serum Albumin - g/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame3_status_text", "Enter Serum Albumin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame3_user_button", "Record Serum Albumin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame4_user_label", "Globulin - g/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame4_status_text", "Enter Globulin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame4_user_button", "Record Globulin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame5_user_label", "Urine Protein  - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame5_status_text", "Enter Urine Protein Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame5_user_button", "Record Urine Protein")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame6_user_label", "Total Bilirubin - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame6_status_text", "Enter Total Bilirubin below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame6_user_button", "Record Total Bilirubin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame7_user_label", "Direct Bilirubin - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame7_status_text", "Enter Direct-Bilirubin below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame7_user_button", "Record Direct-Bilirubin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame8_user_label", "AST - IU/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame8_status_text", "Enter AST below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame8_user_button", "Record AST")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame9_user_label", "ALT - IU/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame9_status_text", "Enter ALT below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame9_user_button", "Record ALT")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame10_user_label", "GGT - IU/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame10_status_text", "Enter GGT Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame10_user_button", "Record GGT")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame11_user_label", "ALP - U/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame11_status_text", "Enter ALP Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame11_user_button", "Record ALP")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame12_user_label", "25(OH)D (Vitamin D3) - ng/ml")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame12_status_text", "Enter 25(OH)D (Vitamin D3) below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group8_frame12_user_button", "Record 25(OH)D (Vitamin D3)")

            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame1_user_label", "Sodium - mmol/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame1_status_text", "Enter Sodium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame1_user_button", "Record Sodium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame2_user_label", "Potasium - mmol/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame2_status_text", "Enter Potasium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame2_user_button", "Record Potasium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame3_user_label", "Chloride - mmol/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame3_status_text", "Enter Chloride Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame3_user_button", "Record Chloride")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame4_user_label", "Bicarbonate - mmol/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame4_status_text", "Enter Bicarbonate Levels below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame4_user_button", "Record Bicarbonate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame5_user_label", "Calcium - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame5_status_text", "Enter Calium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame5_user_button", "Record Calcium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame6_user_label", "Magnesium - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame6_status_text", "Enter Magnesium Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame6_user_button", "Record Magnesium")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame7_user_label", "Phosphorus - mg/dL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame7_status_text", "Enter Phosphorus Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame7_user_button", "Record Phosphorus")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame8_user_label", "O2 Sat - Percent")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame8_status_text", "Enter O2 Sat Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame8_user_button", "Record O2 Sat")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame9_user_label", "Troponins Test")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame9_status_text", "Enter Troponins Results below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame9_user_button", "Record Troponins")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame10_user_label", "NT-proBNP - pg/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame10_status_text", "Enter NT-proBNP Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame10_user_button", "Record NT-proBNP")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame11_user_label", "Myoglobin - mcg/L")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame11_status_text", "Enter Myoglobin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame11_user_button", "Record Myoglobin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame12_user_label", "CKMB - ng/mL")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame12_status_text", "Enter CKMB Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group9_frame12_user_button", "Record CKMB")

            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame1_user_label", "Insulin - mU/L (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame1_status_text", "Enter Fasting Insulin Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame1_user_button", "Record Insulin")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame2_user_label", "Insulin Resistance - mU/L (2 hrs)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame2_status_text", "Enter Insulin Resistance below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame2_user_button", "Record Insulin Resistance")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame3_user_label", "Glucose - mg/dL (Fasting)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame3_status_text", "Enter Glucose Level below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame3_user_button", "Record Glucose")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame4_user_label", "Glucose Response - mg/dL (2 hrs)")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame4_status_text", "Enter Glucose Response below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame4_user_button", "Record Glucose Response")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame5_user_label", "LDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame5_status_text", "Enter LDL-Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame5_user_button", "Record LDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame6_user_label", "Total Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame6_status_text", "Enter Total Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame6_user_button", "Record Total Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame7_user_label", "HDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame7_status_text", "Enter HDL-Cholesterol below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame7_user_button", "Record HDL-Cholesterol")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame8_user_label", "Triglycerides")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame8_status_text", "Enter Triglycerides below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame8_user_button", "Record Triglycerides")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame9_user_label", "Body Weight")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame9_status_text", "Enter Body Weight below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame9_user_button", "Record Body Weight")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame10_user_label", "Body Height")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame10_status_text", "Enter Body Height below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame10_user_button", "Record Body Height")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame11_user_label", "Resting Heart Rate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame11_status_text", "Enter Resting Heart Rate below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame11_user_button", "Record Resting Heart Rate")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame12_user_label", "Blood Press - (Sys/Dias) - mm Hg")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame12_status_text", "Enter Blood Pressure below ...")
            very_first_medical_config.set("USER_DESIGNS_GUI", "group10_frame12_user_button", "Record Blood Pressure")
             
            # create / save medical_record_config.ini data
            with open(str(fullpath_med_config_ini_global), 'w') as first_configfile:
                 very_first_medical_config.write(first_configfile)



    #############################################################################
    #
    # METHOD:  load_medical_record_config_ini 
    #
    # Method to Initialize the medical_record_config.ini
    #
    # Loading the medical_record.ini file to initialize all the globals
    # as this method is called above in the initialization of
    # Class - USER_GUI_Config_Class(Frame)
    #
    #############################################################################
    #
    # CONFIGURE MEDICAL RECORD GLOBALS from
    # medical_record_config.ini EVERY TIME PROGRAM STARTS.
    #
    #  L O A D    T H E    G L O B A L S   from  medical_record_config.ini
    #
    #############################################################################
    #
    def load_medical_record_config_ini(self):
        global fullpath_med_config_ini_global
        global user_gui_title_value_global
        global user_gui_title_bg_color_value_global
        global user_gui_title_fg_color_value_global
        global user_gui_bg_color_value_global
        global user_gui_fg_color_value_global
        global user_gui_label_bg_color_value_global
        global user_gui_label_fg_color_value_global
        global user_gui_entry_bg_color_value_global
        global user_gui_entry_fg_color_value_global
        global user_gui_text_bg_color_value_global
        global user_gui_text_fg_color_value_global
        global group1_frame1_user_label
        global group1_frame1_status_text
        global group1_frame1_user_button
        global group1_frame2_user_label
        global group1_frame2_status_text
        global group1_frame2_user_button
        global group1_frame3_user_label
        global group1_frame3_status_text
        global group1_frame3_user_button
        global group1_frame4_user_label
        global group1_frame4_status_text
        global group1_frame4_user_button
        global group1_frame5_user_label
        global group1_frame5_status_text
        global group1_frame5_user_button
        global group1_frame6_user_label
        global group1_frame6_status_text
        global group1_frame6_user_button
        global group1_frame7_user_label
        global group1_frame7_status_text
        global group1_frame7_user_button
        global group1_frame8_user_label
        global group1_frame8_status_text
        global group1_frame8_user_button
        global group1_frame9_user_label
        global group1_frame9_status_text
        global group1_frame9_user_button
        global group1_frame10_user_label
        global group1_frame10_status_text
        global group1_frame10_user_button
        global group1_frame11_user_label
        global group1_frame11_status_text
        global group1_frame11_user_button
        global group1_frame12_user_label
        global group1_frame12_status_text
        global group1_frame12_user_button
        global group2_frame1_user_label
        global group2_frame1_status_text
        global group2_frame1_user_button
        global group2_frame2_user_label
        global group2_frame2_status_text
        global group2_frame2_user_button
        global group2_frame3_user_label
        global group2_frame3_status_text
        global group2_frame3_user_button
        global group2_frame4_user_label
        global group2_frame4_status_text
        global group2_frame4_user_button
        global group2_frame5_user_label
        global group2_frame5_status_text
        global group2_frame5_user_button
        global group2_frame6_user_label
        global group2_frame6_status_text
        global group2_frame6_user_button
        global group2_frame7_user_label
        global group2_frame7_status_text
        global group2_frame7_user_button
        global group2_frame8_user_label
        global group2_frame8_status_text
        global group2_frame8_user_button
        global group2_frame9_user_label
        global group2_frame9_status_text
        global group2_frame9_user_button
        global group2_frame10_user_label
        global group2_frame10_status_text
        global group2_frame10_user_button
        global group2_frame11_user_label
        global group2_frame11_status_text
        global group2_frame11_user_button
        global group2_frame12_user_label
        global group2_frame12_status_text
        global group2_frame12_user_button
        global group3_frame1_user_label
        global group3_frame1_status_text
        global group3_frame1_user_button
        global group3_frame2_user_label
        global group3_frame2_status_text
        global group3_frame2_user_button
        global group3_frame3_user_label
        global group3_frame3_status_text
        global group3_frame3_user_button
        global group3_frame4_user_label
        global group3_frame4_status_text
        global group3_frame4_user_button
        global group3_frame5_user_label
        global group3_frame5_status_text
        global group3_frame5_user_button
        global group3_frame6_user_label
        global group3_frame6_status_text
        global group3_frame6_user_button
        global group3_frame7_user_label
        global group3_frame7_status_text
        global group3_frame7_user_button
        global group3_frame8_user_label
        global group3_frame8_status_text
        global group3_frame8_user_button
        global group3_frame9_user_label
        global group3_frame9_status_text
        global group3_frame9_user_button
        global group3_frame10_user_label
        global group3_frame10_status_text
        global group3_frame10_user_button
        global group3_frame11_user_label
        global group3_frame11_status_text
        global group3_frame11_user_button
        global group3_frame12_user_label
        global group3_frame12_status_text
        global group3_frame12_user_button
        global group4_frame1_user_label
        global group4_frame1_status_text
        global group4_frame1_user_button
        global group4_frame2_user_label
        global group4_frame2_status_text
        global group4_frame2_user_button
        global group4_frame3_user_label
        global group4_frame3_status_text
        global group4_frame3_user_button
        global group4_frame4_user_label
        global group4_frame4_status_text
        global group4_frame4_user_button
        global group4_frame5_user_label
        global group4_frame5_status_text
        global group4_frame5_user_button
        global group4_frame6_user_label
        global group4_frame6_status_text
        global group4_frame6_user_button
        global group4_frame7_user_label
        global group4_frame7_status_text
        global group4_frame7_user_button
        global group4_frame8_user_label
        global group4_frame8_status_text
        global group4_frame8_user_button
        global group4_frame9_user_label
        global group4_frame9_status_text
        global group4_frame9_user_button
        global group4_frame10_user_label
        global group4_frame10_status_text
        global group4_frame10_user_button
        global group4_frame11_user_label
        global group4_frame11_status_text
        global group4_frame11_user_button
        global group4_frame12_user_label
        global group4_frame12_status_text
        global group4_frame12_user_button
        global group5_frame1_user_label
        global group5_frame1_status_text
        global group5_frame1_user_button
        global group5_frame2_user_label
        global group5_frame2_status_text
        global group5_frame2_user_button
        global group5_frame3_user_label
        global group5_frame3_status_text
        global group5_frame3_user_button
        global group5_frame4_user_label
        global group5_frame4_status_text
        global group5_frame4_user_button
        global group5_frame5_user_label
        global group5_frame5_status_text
        global group5_frame5_user_button
        global group5_frame6_user_label
        global group5_frame6_status_text
        global group5_frame6_user_button
        global group5_frame7_user_label
        global group5_frame7_status_text
        global group5_frame7_user_button
        global group5_frame8_user_label
        global group5_frame8_status_text
        global group5_frame8_user_button
        global group5_frame9_user_label
        global group5_frame9_status_text
        global group5_frame9_user_button
        global group5_frame10_user_label
        global group5_frame10_status_text
        global group5_frame10_user_button
        global group5_frame11_user_label
        global group5_frame11_status_text
        global group5_frame11_user_button
        global group5_frame12_user_label
        global group5_frame12_status_text
        global group5_frame12_user_button
        global group6_frame1_user_label
        global group6_frame1_status_text
        global group6_frame1_user_button
        global group6_frame2_user_label
        global group6_frame2_status_text
        global group6_frame2_user_button
        global group6_frame3_user_label
        global group6_frame3_status_text
        global group6_frame3_user_button
        global group6_frame4_user_label
        global group6_frame4_status_text
        global group6_frame4_user_button
        global group6_frame5_user_label
        global group6_frame5_status_text
        global group6_frame5_user_button
        global group6_frame6_user_label
        global group6_frame6_status_text
        global group6_frame6_user_button
        global group6_frame7_user_label
        global group6_frame7_status_text
        global group6_frame7_user_button
        global group6_frame8_user_label
        global group6_frame8_status_text
        global group6_frame8_user_button
        global group6_frame9_user_label
        global group6_frame9_status_text
        global group6_frame9_user_button
        global group6_frame10_user_label
        global group6_frame10_status_text
        global group6_frame10_user_button
        global group6_frame11_user_label
        global group6_frame11_status_text
        global group6_frame11_user_button
        global group6_frame12_user_label
        global group6_frame12_status_text
        global group6_frame12_user_button
        global group7_frame1_user_label
        global group7_frame1_status_text
        global group7_frame1_user_button
        global group7_frame2_user_label
        global group7_frame2_status_text
        global group7_frame2_user_button
        global group7_frame3_user_label
        global group7_frame3_status_text
        global group7_frame3_user_button
        global group7_frame4_user_label
        global group7_frame4_status_text
        global group7_frame4_user_button
        global group7_frame5_user_label
        global group7_frame5_status_text
        global group7_frame5_user_button
        global group7_frame6_user_label
        global group7_frame6_status_text
        global group7_frame6_user_button
        global group7_frame7_user_label
        global group7_frame7_status_text
        global group7_frame7_user_button
        global group7_frame8_user_label
        global group7_frame8_status_text
        global group7_frame8_user_button
        global group7_frame9_user_label
        global group7_frame9_status_text
        global group7_frame9_user_button
        global group7_frame10_user_label
        global group7_frame10_status_text
        global group7_frame10_user_button
        global group7_frame11_user_label
        global group7_frame11_status_text
        global group7_frame11_user_button
        global group7_frame12_user_label
        global group7_frame12_status_text
        global group7_frame12_user_button
        global group8_frame1_user_label
        global group8_frame1_status_text
        global group8_frame1_user_button
        global group8_frame2_user_label
        global group8_frame2_status_text
        global group8_frame2_user_button
        global group8_frame3_user_label
        global group8_frame3_status_text
        global group8_frame3_user_button
        global group8_frame4_user_label
        global group8_frame4_status_text
        global group8_frame4_user_button
        global group8_frame5_user_label
        global group8_frame5_status_text
        global group8_frame5_user_button
        global group8_frame6_user_label
        global group8_frame6_status_text
        global group8_frame6_user_button
        global group8_frame7_user_label
        global group8_frame7_status_text
        global group8_frame7_user_button
        global group8_frame8_user_label
        global group8_frame8_status_text
        global group8_frame8_user_button
        global group8_frame9_user_label
        global group8_frame9_status_text
        global group8_frame9_user_button
        global group8_frame10_user_label
        global group8_frame10_status_text
        global group8_frame10_user_button
        global group8_frame11_user_label
        global group8_frame11_status_text
        global group8_frame11_user_button
        global group8_frame12_user_label
        global group8_frame12_status_text
        global group8_frame12_user_button
        global group9_frame1_user_label
        global group9_frame1_status_text
        global group9_frame1_user_button
        global group9_frame2_user_label
        global group9_frame2_status_text
        global group9_frame2_user_button
        global group9_frame3_user_label
        global group9_frame3_status_text
        global group9_frame3_user_button
        global group9_frame4_user_label
        global group9_frame4_status_text
        global group9_frame4_user_button
        global group9_frame5_user_label
        global group9_frame5_status_text
        global group9_frame5_user_button
        global group9_frame6_user_label
        global group9_frame6_status_text
        global group9_frame6_user_button
        global group9_frame7_user_label
        global group9_frame7_status_text
        global group9_frame7_user_button
        global group9_frame8_user_label
        global group9_frame8_status_text
        global group9_frame8_user_button
        global group9_frame9_user_label
        global group9_frame9_status_text
        global group9_frame9_user_button
        global group9_frame10_user_label
        global group9_frame10_status_text
        global group9_frame10_user_button
        global group9_frame11_user_label
        global group9_frame11_status_text
        global group9_frame11_user_button
        global group9_frame12_user_label
        global group9_frame12_status_text
        global group9_frame12_user_button
        global group10_frame1_user_label
        global group10_frame1_status_text
        global group10_frame1_user_button
        global group10_frame2_user_label
        global group10_frame2_status_text
        global group10_frame2_user_button
        global group10_frame3_user_label
        global group10_frame3_status_text
        global group10_frame3_user_button
        global group10_frame4_user_label
        global group10_frame4_status_text
        global group10_frame4_user_button
        global group10_frame5_user_label
        global group10_frame5_status_text
        global group10_frame5_user_button
        global group10_frame6_user_label
        global group10_frame6_status_text
        global group10_frame6_user_button
        global group10_frame7_user_label
        global group10_frame7_status_text
        global group10_frame7_user_button
        global group10_frame8_user_label
        global group10_frame8_status_text
        global group10_frame8_user_button
        global group10_frame9_user_label
        global group10_frame9_status_text
        global group10_frame9_user_button
        global group10_frame10_user_label
        global group10_frame10_status_text
        global group10_frame10_user_button
        global group10_frame11_user_label
        global group10_frame11_status_text
        global group10_frame11_user_button
        global group10_frame12_user_label
        global group10_frame12_status_text
        global group10_frame12_user_button


        fullpath_med_config_ini_global = os.path.join(str(cm_appdatafiles_path_global), "medical_record_config.ini" )

        # print("  ")
        # print(".... fullpath_med_config_ini_global = " + str(fullpath_med_config_ini_global) )


        # instantiate ConfigParser() 
        med_startup_config = ConfigParser()


        if os.path.isfile(fullpath_med_config_ini_global) == True:

            med_startup_config.read(str(fullpath_med_config_ini_global) )

            #################################################################################################
            #
            # USER_GUI_CONFIG Class - WIDGET Configuration - 3 Windows (Data Groups) of  
            #
            # 12 WIDGET Frames Widget Configuration (Global) Variables written to medical_record_config.ini
            #
            #################################################################################################

            # read values from app_config.ini file sections
            user_gui_title_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_title")
            user_gui_title_bg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_title_bg_color")
            user_gui_title_fg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_title_fg_color")
            user_gui_bg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_bg_color")
            user_gui_fg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_fg_color")
            user_gui_label_bg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_label_bg_color")
            user_gui_label_fg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_label_fg_color")
            user_gui_entry_bg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_entry_bg_color")
            user_gui_entry_fg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_entry_fg_color")
            user_gui_text_bg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_text_bg_color")
            user_gui_text_fg_color_value = med_startup_config.get("USER_DESIGNS_GUI", "user_gui_text_fg_color")

            # set globals to communicate USER_DESIGNS_SCREEN_AND_DATA settings
            user_gui_title_value_global = str(user_gui_title_value)
            user_gui_title_bg_color_value_global = str(user_gui_title_bg_color_value)
            user_gui_title_fg_color_value_global = str(user_gui_title_fg_color_value)
            user_gui_bg_color_value_global = str(user_gui_bg_color_value)
            user_gui_fg_color_value_global = str(user_gui_fg_color_value)
            user_gui_label_bg_color_value_global = str(user_gui_label_bg_color_value)
            user_gui_label_fg_color_value_global = str(user_gui_label_fg_color_value)
            user_gui_entry_bg_color_value_global = str(user_gui_entry_bg_color_value)
            user_gui_entry_fg_color_value_global = str(user_gui_entry_fg_color_value)
            user_gui_text_bg_color_value_global = str(user_gui_text_bg_color_value)
            user_gui_text_fg_color_value_global = str(user_gui_text_fg_color_value)

            ###############################################################################################
            #
            #   M E D I C A L    P H Y S I O L O G Y   U S E R    G U I   C O N F I G U R A T I O N
            #
            ###############################################################################################
            #
            # USER_GUI_CONFIG Class - WIDGET Configuration - 3 Windows (Data Groups) of 12 WIDGET Frames
            # 
            # Widget Configuration (Global) Variables loaded from medical_record_config.ini
            #
            ###############################################################################################

            # read GROUP #1 values from app_config.ini file sections 
            group1_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame1_user_label")
            group1_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame1_status_text")
            group1_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame1_user_button")
            group1_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame2_user_label")
            group1_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame2_status_text")
            group1_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame2_user_button")
            group1_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame3_user_label")
            group1_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame3_status_text")
            group1_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame3_user_button")
            group1_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame4_user_label")
            group1_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame4_status_text")
            group1_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame4_user_button")
            group1_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame5_user_label")
            group1_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame5_status_text")
            group1_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame5_user_button")
            group1_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame6_user_label")
            group1_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame6_status_text")
            group1_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame6_user_button")
            group1_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame7_user_label")
            group1_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame7_status_text")
            group1_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame7_user_button")
            group1_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame8_user_label")
            group1_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame8_status_text")
            group1_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame8_user_button")
            group1_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame9_user_label")
            group1_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame9_status_text")
            group1_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame9_user_button")
            group1_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame10_user_label")
            group1_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame10_status_text")
            group1_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame10_user_button")
            group1_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame11_user_label")
            group1_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame11_status_text")
            group1_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame11_user_button")
            group1_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame12_user_label")
            group1_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame12_status_text")
            group1_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group1_frame12_user_button")

            # read GROUP #2 values from app_config.ini file sections  
            group2_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame1_user_label")
            group2_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame1_status_text")
            group2_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame1_user_button")
            group2_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame2_user_label")
            group2_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame2_status_text")
            group2_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame2_user_button")
            group2_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame3_user_label")
            group2_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame3_status_text")
            group2_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame3_user_button")
            group2_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame4_user_label")
            group2_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame4_status_text")
            group2_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame4_user_button")
            group2_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame5_user_label")
            group2_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame5_status_text")
            group2_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame5_user_button")
            group2_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame6_user_label")
            group2_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame6_status_text")
            group2_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame6_user_button")
            group2_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame7_user_label")
            group2_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame7_status_text")
            group2_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame7_user_button")
            group2_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame8_user_label")
            group2_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame8_status_text")
            group2_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame8_user_button")
            group2_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame9_user_label")
            group2_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame9_status_text")
            group2_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame9_user_button")
            group2_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame10_user_label")
            group2_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame10_status_text")
            group2_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame10_user_button")
            group2_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame11_user_label")
            group2_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame11_status_text")
            group2_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame11_user_button")
            group2_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame12_user_label")
            group2_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame12_status_text")
            group2_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group2_frame12_user_button")

            # read GROUP #3 values from app_config.ini file sections  
            group3_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame1_user_label")
            group3_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame1_status_text")
            group3_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame1_user_button")
            group3_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame2_user_label")
            group3_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame2_status_text")
            group3_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame2_user_button")
            group3_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame3_user_label")
            group3_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame3_status_text")
            group3_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame3_user_button")
            group3_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame4_user_label")
            group3_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame4_status_text")
            group3_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame4_user_button")
            group3_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame5_user_label")
            group3_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame5_status_text")
            group3_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame5_user_button")
            group3_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame6_user_label")
            group3_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame6_status_text")
            group3_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame6_user_button")
            group3_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame7_user_label")
            group3_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame7_status_text")
            group3_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame7_user_button")
            group3_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame8_user_label")
            group3_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame8_status_text")
            group3_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame8_user_button")
            group3_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame9_user_label")
            group3_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame9_status_text")
            group3_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame9_user_button")
            group3_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame10_user_label")
            group3_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame10_status_text")
            group3_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame10_user_button")
            group3_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame11_user_label")
            group3_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame11_status_text")
            group3_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame11_user_button")
            group3_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame12_user_label")
            group3_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame12_status_text")
            group3_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group3_frame12_user_button")

            # read GROUP #4 values from app_config.ini file sections  
            group4_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame1_user_label")
            group4_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame1_status_text")
            group4_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame1_user_button")
            group4_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame2_user_label")
            group4_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame2_status_text")
            group4_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame2_user_button")
            group4_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame3_user_label")
            group4_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame3_status_text")
            group4_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame3_user_button")
            group4_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame4_user_label")
            group4_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame4_status_text")
            group4_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame4_user_button")
            group4_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame5_user_label")
            group4_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame5_status_text")
            group4_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame5_user_button")
            group4_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame6_user_label")
            group4_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame6_status_text")
            group4_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame6_user_button")
            group4_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame7_user_label")
            group4_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame7_status_text")
            group4_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame7_user_button")
            group4_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame8_user_label")
            group4_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame8_status_text")
            group4_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame8_user_button")
            group4_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame9_user_label")
            group4_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame9_status_text")
            group4_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame9_user_button")
            group4_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame10_user_label")
            group4_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame10_status_text")
            group4_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame10_user_button")
            group4_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame11_user_label")
            group4_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame11_status_text")
            group4_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame11_user_button")
            group4_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame12_user_label")
            group4_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame12_status_text")
            group4_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group4_frame12_user_button")

            # read GROUP #5 values from app_config.ini file sections  
            group5_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame1_user_label")
            group5_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame1_status_text")
            group5_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame1_user_button")
            group5_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame2_user_label")
            group5_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame2_status_text")
            group5_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame2_user_button")
            group5_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame3_user_label")
            group5_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame3_status_text")
            group5_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame3_user_button")
            group5_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame4_user_label")
            group5_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame4_status_text")
            group5_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame4_user_button")
            group5_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame5_user_label")
            group5_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame5_status_text")
            group5_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame5_user_button")
            group5_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame6_user_label")
            group5_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame6_status_text")
            group5_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame6_user_button")
            group5_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame7_user_label")
            group5_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame7_status_text")
            group5_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame7_user_button")
            group5_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame8_user_label")
            group5_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame8_status_text")
            group5_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame8_user_button")
            group5_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame9_user_label")
            group5_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame9_status_text")
            group5_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame9_user_button")
            group5_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame10_user_label")
            group5_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame10_status_text")
            group5_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame10_user_button")
            group5_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame11_user_label")
            group5_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame11_status_text")
            group5_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame11_user_button")
            group5_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame12_user_label")
            group5_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame12_status_text")
            group5_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group5_frame12_user_button")

            # read GROUP #6 values from app_config.ini file sections  
            group6_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame1_user_label")
            group6_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame1_status_text")
            group6_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame1_user_button")
            group6_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame2_user_label")
            group6_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame2_status_text")
            group6_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame2_user_button")
            group6_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame3_user_label")
            group6_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame3_status_text")
            group6_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame3_user_button")
            group6_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame4_user_label")
            group6_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame4_status_text")
            group6_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame4_user_button")
            group6_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame5_user_label")
            group6_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame5_status_text")
            group6_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame5_user_button")
            group6_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame6_user_label")
            group6_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame6_status_text")
            group6_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame6_user_button")
            group6_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame7_user_label")
            group6_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame7_status_text")
            group6_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame7_user_button")
            group6_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame8_user_label")
            group6_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame8_status_text")
            group6_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame8_user_button")
            group6_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame9_user_label")
            group6_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame9_status_text")
            group6_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame9_user_button")
            group6_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame10_user_label")
            group6_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame10_status_text")
            group6_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame10_user_button")
            group6_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame11_user_label")
            group6_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame11_status_text")
            group6_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame11_user_button")
            group6_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame12_user_label")
            group6_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame12_status_text")
            group6_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group6_frame12_user_button")

            # read GROUP #7 values from app_config.ini file sections  
            group7_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame1_user_label")
            group7_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame1_status_text")
            group7_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame1_user_button")
            group7_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame2_user_label")
            group7_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame2_status_text")
            group7_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame2_user_button")
            group7_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame3_user_label")
            group7_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame3_status_text")
            group7_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame3_user_button")
            group7_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame4_user_label")
            group7_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame4_status_text")
            group7_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame4_user_button")
            group7_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame5_user_label")
            group7_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame5_status_text")
            group7_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame5_user_button")
            group7_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame6_user_label")
            group7_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame6_status_text")
            group7_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame6_user_button")
            group7_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame7_user_label")
            group7_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame7_status_text")
            group7_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame7_user_button")
            group7_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame8_user_label")
            group7_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame8_status_text")
            group7_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame8_user_button")
            group7_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame9_user_label")
            group7_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame9_status_text")
            group7_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame9_user_button")
            group7_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame10_user_label")
            group7_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame10_status_text")
            group7_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame10_user_button")
            group7_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame11_user_label")
            group7_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame11_status_text")
            group7_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame11_user_button")
            group7_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame12_user_label")
            group7_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame12_status_text")
            group7_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group7_frame12_user_button")

            # read GROUP #8 values from app_config.ini file sections  
            group8_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame1_user_label")
            group8_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame1_status_text")
            group8_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame1_user_button")
            group8_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame2_user_label")
            group8_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame2_status_text")
            group8_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame2_user_button")
            group8_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame3_user_label")
            group8_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame3_status_text")
            group8_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame3_user_button")
            group8_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame4_user_label")
            group8_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame4_status_text")
            group8_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame4_user_button")
            group8_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame5_user_label")
            group8_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame5_status_text")
            group8_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame5_user_button")
            group8_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame6_user_label")
            group8_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame6_status_text")
            group8_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame6_user_button")
            group8_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame7_user_label")
            group8_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame7_status_text")
            group8_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame7_user_button")
            group8_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame8_user_label")
            group8_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame8_status_text")
            group8_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame8_user_button")
            group8_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame9_user_label")
            group8_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame9_status_text")
            group8_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame9_user_button")
            group8_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame10_user_label")
            group8_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame10_status_text")
            group8_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame10_user_button")
            group8_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame11_user_label")
            group8_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame11_status_text")
            group8_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame11_user_button")
            group8_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame12_user_label")
            group8_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame12_status_text")
            group8_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group8_frame12_user_button")

            # read GROUP #9 values from app_config.ini file sections  
            group9_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame1_user_label")
            group9_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame1_status_text")
            group9_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame1_user_button")
            group9_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame2_user_label")
            group9_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame2_status_text")
            group9_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame2_user_button")
            group9_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame3_user_label")
            group9_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame3_status_text")
            group9_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame3_user_button")
            group9_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame4_user_label")
            group9_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame4_status_text")
            group9_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame4_user_button")
            group9_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame5_user_label")
            group9_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame5_status_text")
            group9_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame5_user_button")
            group9_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame6_user_label")
            group9_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame6_status_text")
            group9_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame6_user_button")
            group9_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame7_user_label")
            group9_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame7_status_text")
            group9_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame7_user_button")
            group9_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame8_user_label")
            group9_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame8_status_text")
            group9_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame8_user_button")
            group9_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame9_user_label")
            group9_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame9_status_text")
            group9_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame9_user_button")
            group9_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame10_user_label")
            group9_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame10_status_text")
            group9_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame10_user_button")
            group9_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame11_user_label")
            group9_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame11_status_text")
            group9_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame11_user_button")
            group9_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame12_user_label")
            group9_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame12_status_text")
            group9_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group9_frame12_user_button")

            # read GROUP #10 values from app_config.ini file sections  
            group10_frame1_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame1_user_label")
            group10_frame1_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame1_status_text")
            group10_frame1_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame1_user_button")
            group10_frame2_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame2_user_label")
            group10_frame2_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame2_status_text")
            group10_frame2_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame2_user_button")
            group10_frame3_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame3_user_label")
            group10_frame3_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame3_status_text")
            group10_frame3_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame3_user_button")
            group10_frame4_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame4_user_label")
            group10_frame4_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame4_status_text")
            group10_frame4_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame4_user_button")
            group10_frame5_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame5_user_label")
            group10_frame5_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame5_status_text")
            group10_frame5_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame5_user_button")
            group10_frame6_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame6_user_label")
            group10_frame6_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame6_status_text")
            group10_frame6_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame6_user_button")
            group10_frame7_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame7_user_label")
            group10_frame7_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame7_status_text")
            group10_frame7_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame7_user_button")
            group10_frame8_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame8_user_label")
            group10_frame8_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame8_status_text")
            group10_frame8_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame8_user_button")
            group10_frame9_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame9_user_label")
            group10_frame9_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame9_status_text")
            group10_frame9_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame9_user_button")
            group10_frame10_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame10_user_label")
            group10_frame10_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame10_status_text")
            group10_frame10_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame10_user_button")
            group10_frame11_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame11_user_label")
            group10_frame11_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame11_status_text")
            group10_frame11_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame11_user_button")
            group10_frame12_user_label = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame12_user_label")
            group10_frame12_status_text = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame12_status_text")
            group10_frame12_user_button = med_startup_config.get("USER_DESIGNS_GUI", "group10_frame12_user_button")

   

    # Instantiate FOUR USER GUI WIDGETS (Label, Entry, Text, Button)    
    def widget_group_template(self, Master_Frame_Object, user_label_text, status_message_text, user_entry_stringvar, user_button_text):

        self.user_label_text = user_label_text
        self.user_label = Label(Master_Frame_Object, text = self.user_label_text, font=('Helvetica', '12') )
        self.user_label.config(height = 1, width=26)
        self.user_label.config(bg="deep sky blue", fg="black")  
        self.user_label.grid(row=0, column=0, padx=5, pady=5)

        self.user_text = Text(Master_Frame_Object, width=26, height = 1)
        self.user_text.grid(row=1, column=0, padx=5, pady=5)
        self.user_text.config(borderwidth=5, font=('Helvetica', '12'), background="deep sky blue", fg ="black")
        text_STATUS = status_message_text
        self.user_text.insert(END, text_STATUS)

        # Gather Text Widget Instances to capture instance names for status update of Text Widget.
        self.text_instances.append(self.user_text)

        # widget_object_focus = self.user_text
        # print(".... str(widget_object_focus) = " + str(widget_object_focus) )
        # print(".... str(widget_object_focus.winfo_id() ) = " + str(widget_object_focus.winfo_id() ) )
        # print(".... str(widget_object_focus.winfo_parent() ) = " + str(widget_object_focus.winfo_parent() ) )
        # print("  ")
        
        self.user_entry = Entry(Master_Frame_Object, textvariable = user_entry_stringvar, font=('Helvetica', '12'), width = 26)
        self.user_entry.grid(sticky = W, row=2, column=0, padx=5, pady=5)
        self.user_entry.config(borderwidth=5, background="deep sky blue", fg ="black")

        # Gather Entry Widget Instances to capture instance names for controlled clear (delete) of the Entry Widget contents.
        self.entry_instances.append(self.user_entry)

        self.user_button = Button(Master_Frame_Object, text = user_button_text, width = 26, height = 1, \
            font=('Helvetica', '12'), background="deep sky blue", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2")  # command = self.update_user_text_status)
        self.user_button.bind("<Button-1>", self.update_user_text_status)
        self.user_button.grid(row=3, column=0, padx=5, pady=5, sticky = W)


        #######################################################################################
        # 
        # Programming Note:     ( Reference to the code above )    
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows: 
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)  # ENTRY Widget Syntax is self.user_entry.delete(0, END)
        # text.insert(END, text) 
        # text.config(state=DISABLED) 
        #
        ######################################################################################


    ###########################################################################
    #  
    # METHOD:  update_user_text_status  
    #
    # Every EVENT of the Medical Record GUI triggers this Method to update
    # the medical_record_config.ini with the NEW STATUS from the Text Widget.
    #
    # Currently there are Status TEXT WIDGETS for:
    #
    # -- Group One, Group Two, Group Three
    #
    # -- Each Group having 12 Frames of Medical Clinical Chemistry Data.
    #
    ###########################################################################
    def update_user_text_status(self, event):
        global group10_frame12_status_text
        global group9_frame12_status_text
        global group8_frame12_status_text
        global group7_frame12_status_text
        global group6_frame12_status_text
        global group5_frame12_status_text
        global group4_frame12_status_text
        global group3_frame12_status_text
        global group2_frame12_status_text
        global group1_frame12_status_text
        global group10_frame11_status_text
        global group9_frame11_status_text
        global group8_frame11_status_text
        global group7_frame11_status_text
        global group6_frame11_status_text
        global group5_frame11_status_text
        global group4_frame11_status_text
        global group3_frame11_status_text
        global group2_frame11_status_text
        global group1_frame11_status_text
        global group10_frame10_status_text
        global group9_frame10_status_text
        global group8_frame10_status_text
        global group7_frame10_status_text
        global group6_frame10_status_text
        global group5_frame10_status_text
        global group4_frame10_status_text
        global group3_frame10_status_text
        global group2_frame10_status_text
        global group1_frame10_status_text
        global group10_frame9_status_text
        global group9_frame9_status_text
        global group8_frame9_status_text
        global group7_frame9_status_text
        global group6_frame9_status_text
        global group5_frame9_status_text
        global group4_frame9_status_text
        global group3_frame9_status_text
        global group2_frame9_status_text
        global group1_frame9_status_text
        global group10_frame8_status_text
        global group9_frame8_status_text
        global group8_frame8_status_text
        global group7_frame8_status_text
        global group6_frame8_status_text
        global group5_frame8_status_text
        global group4_frame8_status_text
        global group3_frame8_status_text
        global group2_frame8_status_text
        global group1_frame8_status_text
        global group10_frame7_status_text
        global group9_frame7_status_text
        global group8_frame7_status_text
        global group7_frame7_status_text
        global group6_frame7_status_text
        global group5_frame7_status_text
        global group4_frame7_status_text
        global group3_frame7_status_text
        global group2_frame7_status_text
        global group1_frame7_status_text
        global group10_frame6_status_text
        global group9_frame6_status_text
        global group8_frame6_status_text
        global group7_frame6_status_text
        global group6_frame6_status_text
        global group5_frame6_status_text
        global group4_frame6_status_text
        global group3_frame6_status_text
        global group2_frame6_status_text
        global group1_frame6_status_text
        global group10_frame5_status_text
        global group9_frame5_status_text
        global group8_frame5_status_text
        global group7_frame5_status_text
        global group6_frame5_status_text
        global group5_frame5_status_text
        global group4_frame5_status_text
        global group3_frame5_status_text
        global group2_frame5_status_text
        global group1_frame5_status_text
        global group10_frame4_status_text
        global group9_frame4_status_text
        global group8_frame4_status_text
        global group7_frame4_status_text
        global group6_frame4_status_text
        global group5_frame4_status_text
        global group4_frame4_status_text
        global group3_frame4_status_text
        global group2_frame4_status_text
        global group1_frame4_status_text
        global group10_frame3_status_text
        global group9_frame3_status_text
        global group8_frame3_status_text
        global group7_frame3_status_text
        global group6_frame3_status_text
        global group5_frame3_status_text
        global group4_frame3_status_text
        global group3_frame3_status_text
        global group2_frame3_status_text
        global group1_frame3_status_text
        global group10_frame2_status_text
        global group9_frame2_status_text
        global group8_frame2_status_text
        global group7_frame2_status_text
        global group6_frame2_status_text
        global group5_frame2_status_text
        global group4_frame2_status_text
        global group3_frame2_status_text
        global group2_frame2_status_text
        global group1_frame2_status_text
        global group10_frame1_status_text
        global group9_frame1_status_text
        global group8_frame1_status_text
        global group7_frame1_status_text
        global group6_frame1_status_text
        global group5_frame1_status_text
        global group4_frame1_status_text
        global group3_frame1_status_text
        global group2_frame1_status_text
        global group1_frame1_status_text


        time_string = datetime.datetime.today().strftime("%m-%d-%Y")

        entry_text_data = "Data Not Set"
        
        widget_id = event.widget

        #print(".... str(event.widget) = " + str(event.widget) ) 
        #print(".... str(event.widget.winfo_id() ) = " + str(event.widget.winfo_id() ) )
        #print(".... str(event.widget.winfo_parent() ) = " + str(event.widget.winfo_parent() ) ) 
        
        if "frame12" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame12.config(state=NORMAL)
            self.text_widget_instance_Frame12.delete(1.0, END)
            entry_text_data = self.user_entry_12_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"
            
            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database. 
            if self.group_instance == "group_ten_instance": group10_frame12_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame12_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame12_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame12_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame12_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame12_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame12_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame12_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame12_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame12_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame12.insert(END, text_STATUS) # How to Address self.Frame12 WIDGET
            self.text_widget_instance_Frame12.config(state=DISABLED) # How to Address self.Frame12 WIDGET
            self.entry_widget_instance_Frame12.delete(0, END)

        elif "frame11" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame11.config(state=NORMAL)
            self.text_widget_instance_Frame11.delete(1.0, END)
            entry_text_data = self.user_entry_11_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame11_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame11_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame11_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame11_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame11_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame11_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame11_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame11_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame11_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame11_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame11.insert(END, text_STATUS) # How to Address self.Frame11 WIDGET
            self.text_widget_instance_Frame11.config(state=DISABLED) # How to Address self.Frame11 WIDGET
            self.entry_widget_instance_Frame11.delete(0, END)

        elif "frame10" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame10.config(state=NORMAL)
            self.text_widget_instance_Frame10.delete(1.0, END)
            entry_text_data = self.user_entry_10_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame10_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame10_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame10_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame10_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame10_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame10_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame10_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame10_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame10_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame10_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame10.insert(END, text_STATUS) # How to Address self.Frame10 WIDGET
            self.text_widget_instance_Frame10.config(state=DISABLED) # How to Address self.Frame10 WIDGET
            self.entry_widget_instance_Frame10.delete(0, END)

        elif "frame9" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame9.config(state=NORMAL)
            self.text_widget_instance_Frame9.delete(1.0, END)
            entry_text_data = self.user_entry_9_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame9_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame9_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame9_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame9_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame9_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame9_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame9_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame9_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame9_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame9_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame9.insert(END, text_STATUS) # How to Address self.Frame9 WIDGET
            self.text_widget_instance_Frame9.config(state=DISABLED) # How to Address self.Frame9 WIDGET
            self.entry_widget_instance_Frame9.delete(0, END)
            
        elif "frame8" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame8.config(state=NORMAL)
            self.text_widget_instance_Frame8.delete(1.0, END)
            entry_text_data = self.user_entry_8_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame8_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame8_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame8_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame8_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame8_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame8_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame8_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame8_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame8_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame8_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame8.insert(END, text_STATUS) # How to Address self.Frame8 WIDGET
            self.text_widget_instance_Frame8.config(state=DISABLED) # How to Address self.Frame8 WIDGET
            self.entry_widget_instance_Frame8.delete(0, END)

        elif "frame7" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame7.config(state=NORMAL)
            self.text_widget_instance_Frame7.delete(1.0, END)
            entry_text_data = self.user_entry_7_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame7_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame7_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame7_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame7_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame7_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame7_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame7_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame7_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame7_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame7_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame7.insert(END, text_STATUS) # How to Address self.Frame7 WIDGET
            self.text_widget_instance_Frame7.config(state=DISABLED) # How to Address self.Frame7 WIDGET
            self.entry_widget_instance_Frame7.delete(0, END)

        elif "frame6" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame6.config(state=NORMAL)
            self.text_widget_instance_Frame6.delete(1.0, END)
            entry_text_data = self.user_entry_6_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame6_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame6_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame6_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame6_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame6_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame6_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame6_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame6_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame6_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame6_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame6.insert(END, text_STATUS) # How to Address self.Frame6 WIDGET
            self.text_widget_instance_Frame6.config(state=DISABLED) # How to Address self.Frame6 WIDGET
            self.entry_widget_instance_Frame6.delete(0, END)
        
        elif "frame5" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame5.config(state=NORMAL)
            self.text_widget_instance_Frame5.delete(1.0, END)
            entry_text_data = self.user_entry_5_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame5_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame5_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame5_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame5_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame5_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame5_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame5_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame5_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame5_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame5_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame5.insert(END, text_STATUS) # How to Address self.Frame5 WIDGET
            self.text_widget_instance_Frame5.config(state=DISABLED) # How to Address self.Frame5 WIDGET
            self.entry_widget_instance_Frame5.delete(0, END)
            
        elif "frame4" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame4.config(state=NORMAL)
            self.text_widget_instance_Frame4.delete(1.0, END)
            entry_text_data = self.user_entry_4_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame4_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame4_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame4_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame4_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame4_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame4_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame4_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame4_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame4_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame4_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame4.insert(END, text_STATUS) # How to Address self.Frame4 WIDGET
            self.text_widget_instance_Frame4.config(state=DISABLED) # How to Address self.Frame4 WIDGET
            self.entry_widget_instance_Frame4.delete(0, END)

        elif "frame3" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame3.config(state=NORMAL)
            self.text_widget_instance_Frame3.delete(1.0, END)
            entry_text_data = self.user_entry_3_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame3_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame3_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame3_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame3_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame3_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame3_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame3_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame3_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame3_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame3_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame3.insert(END, text_STATUS) # How to Address self.Frame3 WIDGET
            self.text_widget_instance_Frame3.config(state=DISABLED) # How to Address self.Frame3 WIDGET
            self.entry_widget_instance_Frame3.delete(0, END)

        elif "frame2" in str(event.widget.winfo_parent() ):
            self.text_widget_instance_Frame2.config(state=NORMAL)
            self.text_widget_instance_Frame2.delete(1.0, END)
            entry_text_data = self.user_entry_2_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame2_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame2_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame2_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame2_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame2_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame2_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame2_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame2_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame2_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame2_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame2.insert(END, text_STATUS) # How to Address self.Frame2 WIDGET
            self.text_widget_instance_Frame2.config(state=DISABLED) # How to Address self.Frame2 WIDGET
            self.entry_widget_instance_Frame2.delete(0, END)

        else:
            self.text_widget_instance_Frame1.config(state=NORMAL)
            self.text_widget_instance_Frame1.delete(1.0, END)
            entry_text_data = self.user_entry_1_stringvar.get()
            text_STATUS = str(entry_text_data) + "  (" + str(time_string) + ")"

            # Determine GROUP then update corresponding status data global so we can build database med_rec_config.ini
            # that contains things like LABEL and STATUS Text in secure medical record database.
            if self.group_instance == "group_ten_instance": group10_frame1_status_text = text_STATUS
            elif self.group_instance == "group_nine_instance": group9_frame1_status_text = text_STATUS
            elif self.group_instance == "group_eight_instance": group8_frame1_status_text = text_STATUS
            elif self.group_instance == "group_seven_instance": group7_frame1_status_text = text_STATUS
            elif self.group_instance == "group_six_instance": group6_frame1_status_text = text_STATUS
            elif self.group_instance == "group_five_instance": group5_frame1_status_text = text_STATUS
            elif self.group_instance == "group_four_instance": group4_frame1_status_text = text_STATUS
            elif self.group_instance == "group_three_instance": group3_frame1_status_text = text_STATUS
            elif self.group_instance == "group_two_instance": group2_frame1_status_text = text_STATUS
            elif self.group_instance == "group_one_instance": group1_frame1_status_text = text_STATUS

            # print("  ")
            # print(".... self.group_instance = " + str(self.group_instance) + " .... STATUS UPDATED: " + str(text_STATUS) )
            
            self.text_widget_instance_Frame1.insert(END, text_STATUS) # How to Address self.Frame1 WIDGET
            self.text_widget_instance_Frame1.config(state=DISABLED) # How to Address self.Frame1 WIDGET
            self.entry_widget_instance_Frame1.delete(0, END)

        #print(".... entry_text_data = " + str(entry_text_data) )
        #print(".... text_STATUS = " + str(text_STATUS) )


        ##########################################################################################
        #
        # Create / Re-Write / Update  medical_record_config.ini with New Data from Entry Widget
        #
        ##########################################################################################

        fullpath_med_config_ini_global = os.path.join(str(cm_appdatafiles_path_global), "medical_record_config.ini" )

        # print("  ")
        # print(".... fullpath_med_config_ini_global = " + str(fullpath_med_config_ini_global) )

        # instantiate ConfigParser() 
        medical_config = ConfigParser()

        # Adjust this as required. 
        if (os.path.isfile(fullpath_med_config_ini_global) == True) or (os.path.isfile(fullpath_med_config_ini_global) == False):

            medical_config.add_section("USER_DESIGNS_GUI")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_title", "User Designs Screen Layout and Data Name")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_title_bg_color", "cyan4")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_title_fg_color", "light sea green")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_x_col_frames", "4")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_y_row_frames", "5")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_bg_color", "dark slate gray")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_fg_color", "snow")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_label_bg_color", "cyan4")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_label_fg_color", "cyan")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_entry_bg_color", "light sea green")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_entry_fg_color", "black")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_text_bg_color", "light sea green")
            medical_config.set("USER_DESIGNS_GUI", "user_gui_text_fg_color", "black")

            ###############################################################################################
            #
            #   M E D I C A L    P H Y S I O L O G Y   U S E R    G U I   C O N F I G U R A T I O N
            #
            ###############################################################################################
            #
            # USER_GUI_CONFIG Class - WIDGET Configuration - 3 Windows (Data Groups) of 12 WIDGET Frames
            #
            # Widget Configuration (Global) Variables written to medical_record_config.ini 
            #
            ###############################################################################################

            # GROUP #1 PANEL CONFIG DATA SETTINGS
            medical_config.set("USER_DESIGNS_GUI", "group1_frame1_user_label", str(group1_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame1_status_text", str(group1_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame1_user_button", str(group1_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame2_user_label", str(group1_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame2_status_text", str(group1_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame2_user_button", str(group1_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame3_user_label", str(group1_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame3_status_text", str(group1_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame3_user_button", str(group1_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame4_user_label", str(group1_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame4_status_text", str(group1_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame4_user_button", str(group1_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame5_user_label", str(group1_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame5_status_text", str(group1_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame5_user_button", str(group1_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame6_user_label", str(group1_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame6_status_text", str(group1_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame6_user_button", str(group1_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame7_user_label", str(group1_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame7_status_text", str(group1_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame7_user_button", str(group1_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame8_user_label", str(group1_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame8_status_text", str(group1_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame8_user_button", str(group1_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame9_user_label", str(group1_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame9_status_text", str(group1_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame9_user_button", str(group1_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame10_user_label", str(group1_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame10_status_text", str(group1_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame10_user_button", str(group1_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame11_user_label", str(group1_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame11_status_text", str(group1_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame11_user_button", str(group1_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame12_user_label", str(group1_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame12_status_text", str(group1_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group1_frame12_user_button", str(group1_frame12_user_button) )
            
            # GROUP #2 PANEL CONFIG DATA SETTINGS
            medical_config.set("USER_DESIGNS_GUI", "group2_frame1_user_label", str(group2_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame1_status_text", str(group2_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame1_user_button", str(group2_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame2_user_label", str(group2_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame2_status_text", str(group2_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame2_user_button", str(group2_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame3_user_label", str(group2_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame3_status_text", str(group2_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame3_user_button", str(group2_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame4_user_label", str(group2_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame4_status_text", str(group2_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame4_user_button", str(group2_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame5_user_label", str(group2_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame5_status_text", str(group2_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame5_user_button", str(group2_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame6_user_label", str(group2_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame6_status_text", str(group2_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame6_user_button", str(group2_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame7_user_label", str(group2_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame7_status_text", str(group2_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame7_user_button", str(group2_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame8_user_label", str(group2_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame8_status_text", str(group2_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame8_user_button", str(group2_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame9_user_label", str(group2_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame9_status_text", str(group2_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame9_user_button", str(group2_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame10_user_label", str(group2_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame10_status_text", str(group2_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame10_user_button", str(group2_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame11_user_label", str(group2_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame11_status_text", str(group2_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame11_user_button", str(group2_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame12_user_label", str(group2_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame12_status_text", str(group2_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group2_frame12_user_button", str(group2_frame12_user_button) )

            # GROUP #3 PANEL CONFIG DATA SETTINGS
            medical_config.set("USER_DESIGNS_GUI", "group3_frame1_user_label", str(group3_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame1_status_text", str(group3_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame1_user_button", str(group3_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame2_user_label", str(group3_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame2_status_text", str(group3_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame2_user_button", str(group3_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame3_user_label", str(group3_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame3_status_text", str(group3_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame3_user_button", str(group3_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame4_user_label", str(group3_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame4_status_text", str(group3_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame4_user_button", str(group3_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame5_user_label", str(group3_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame5_status_text", str(group3_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame5_user_button", str(group3_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame6_user_label", str(group3_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame6_status_text", str(group3_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame6_user_button", str(group3_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame7_user_label", str(group3_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame7_status_text", str(group3_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame7_user_button", str(group3_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame8_user_label", str(group3_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame8_status_text", str(group3_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame8_user_button", str(group3_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame9_user_label", str(group3_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame9_status_text", str(group3_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame9_user_button", str(group3_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame10_user_label", str(group3_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame10_status_text", str(group3_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame10_user_button", str(group3_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame11_user_label", str(group3_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame11_status_text", str(group3_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame11_user_button", str(group3_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame12_user_label", str(group3_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame12_status_text", str(group3_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group3_frame12_user_button", str(group3_frame12_user_button) )

            # GROUP #4 PANEL CONFIG DATA SETTINGS
            medical_config.set("USER_DESIGNS_GUI", "group4_frame1_user_label", str(group4_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame1_status_text", str(group4_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame1_user_button", str(group4_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame2_user_label", str(group4_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame2_status_text", str(group4_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame2_user_button", str(group4_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame3_user_label", str(group4_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame3_status_text", str(group4_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame3_user_button", str(group4_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame4_user_label", str(group4_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame4_status_text", str(group4_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame4_user_button", str(group4_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame5_user_label", str(group4_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame5_status_text", str(group4_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame5_user_button", str(group4_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame6_user_label", str(group4_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame6_status_text", str(group4_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame6_user_button", str(group4_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame7_user_label", str(group4_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame7_status_text", str(group4_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame7_user_button", str(group4_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame8_user_label", str(group4_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame8_status_text", str(group4_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame8_user_button", str(group4_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame9_user_label", str(group4_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame9_status_text", str(group4_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame9_user_button", str(group4_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame10_user_label", str(group4_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame10_status_text", str(group4_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame10_user_button", str(group4_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame11_user_label", str(group4_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame11_status_text", str(group4_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame11_user_button", str(group4_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame12_user_label", str(group4_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame12_status_text", str(group4_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group4_frame12_user_button", str(group4_frame12_user_button) )

            # GROUP #5 PANEL CONFIG DATA SETTINGS 
            medical_config.set("USER_DESIGNS_GUI", "group5_frame1_user_label", str(group5_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame1_status_text", str(group5_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame1_user_button", str(group5_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame2_user_label", str(group5_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame2_status_text", str(group5_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame2_user_button", str(group5_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame3_user_label", str(group5_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame3_status_text", str(group5_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame3_user_button", str(group5_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame4_user_label", str(group5_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame4_status_text", str(group5_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame4_user_button", str(group5_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame5_user_label", str(group5_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame5_status_text", str(group5_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame5_user_button", str(group5_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame6_user_label", str(group5_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame6_status_text", str(group5_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame6_user_button", str(group5_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame7_user_label", str(group5_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame7_status_text", str(group5_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame7_user_button", str(group5_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame8_user_label", str(group5_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame8_status_text", str(group5_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame8_user_button", str(group5_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame9_user_label", str(group5_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame9_status_text", str(group5_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame9_user_button", str(group5_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame10_user_label", str(group5_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame10_status_text", str(group5_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame10_user_button", str(group5_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame11_user_label", str(group5_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame11_status_text", str(group5_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame11_user_button", str(group5_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame12_user_label", str(group5_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame12_status_text", str(group5_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group5_frame12_user_button", str(group5_frame12_user_button) )

            # GROUP #6 PANEL CONFIG DATA SETTINGS 
            medical_config.set("USER_DESIGNS_GUI", "group6_frame1_user_label", str(group6_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame1_status_text", str(group6_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame1_user_button", str(group6_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame2_user_label", str(group6_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame2_status_text", str(group6_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame2_user_button", str(group6_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame3_user_label", str(group6_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame3_status_text", str(group6_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame3_user_button", str(group6_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame4_user_label", str(group6_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame4_status_text", str(group6_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame4_user_button", str(group6_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame5_user_label", str(group6_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame5_status_text", str(group6_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame5_user_button", str(group6_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame6_user_label", str(group6_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame6_status_text", str(group6_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame6_user_button", str(group6_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame7_user_label", str(group6_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame7_status_text", str(group6_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame7_user_button", str(group6_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame8_user_label", str(group6_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame8_status_text", str(group6_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame8_user_button", str(group6_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame9_user_label", str(group6_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame9_status_text", str(group6_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame9_user_button", str(group6_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame10_user_label", str(group6_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame10_status_text", str(group6_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame10_user_button", str(group6_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame11_user_label", str(group6_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame11_status_text", str(group6_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame11_user_button", str(group6_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame12_user_label", str(group6_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame12_status_text", str(group6_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group6_frame12_user_button", str(group6_frame12_user_button) )

            # GROUP #7 PANEL CONFIG DATA SETTINGS 
            medical_config.set("USER_DESIGNS_GUI", "group7_frame1_user_label", str(group7_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame1_status_text", str(group7_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame1_user_button", str(group7_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame2_user_label", str(group7_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame2_status_text", str(group7_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame2_user_button", str(group7_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame3_user_label", str(group7_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame3_status_text", str(group7_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame3_user_button", str(group7_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame4_user_label", str(group7_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame4_status_text", str(group7_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame4_user_button", str(group7_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame5_user_label", str(group7_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame5_status_text", str(group7_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame5_user_button", str(group7_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame6_user_label", str(group7_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame6_status_text", str(group7_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame6_user_button", str(group7_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame7_user_label", str(group7_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame7_status_text", str(group7_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame7_user_button", str(group7_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame8_user_label", str(group7_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame8_status_text", str(group7_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame8_user_button", str(group7_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame9_user_label", str(group7_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame9_status_text", str(group7_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame9_user_button", str(group7_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame10_user_label", str(group7_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame10_status_text", str(group7_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame10_user_button", str(group7_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame11_user_label", str(group7_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame11_status_text", str(group7_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame11_user_button", str(group7_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame12_user_label", str(group7_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame12_status_text", str(group7_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group7_frame12_user_button", str(group7_frame12_user_button) )

            # GROUP #8 PANEL CONFIG DATA SETTINGS 
            medical_config.set("USER_DESIGNS_GUI", "group8_frame1_user_label", str(group8_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame1_status_text", str(group8_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame1_user_button", str(group8_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame2_user_label", str(group8_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame2_status_text", str(group8_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame2_user_button", str(group8_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame3_user_label", str(group8_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame3_status_text", str(group8_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame3_user_button", str(group8_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame4_user_label", str(group8_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame4_status_text", str(group8_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame4_user_button", str(group8_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame5_user_label", str(group8_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame5_status_text", str(group8_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame5_user_button", str(group8_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame6_user_label", str(group8_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame6_status_text", str(group8_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame6_user_button", str(group8_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame7_user_label", str(group8_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame7_status_text", str(group8_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame7_user_button", str(group8_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame8_user_label", str(group8_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame8_status_text", str(group8_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame8_user_button", str(group8_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame9_user_label", str(group8_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame9_status_text", str(group8_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame9_user_button", str(group8_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame10_user_label", str(group8_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame10_status_text", str(group8_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame10_user_button", str(group8_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame11_user_label", str(group8_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame11_status_text", str(group8_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame11_user_button", str(group8_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame12_user_label", str(group8_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame12_status_text", str(group8_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group8_frame12_user_button", str(group8_frame12_user_button) )

            # GROUP #9 PANEL CONFIG DATA SETTINGS 
            medical_config.set("USER_DESIGNS_GUI", "group9_frame1_user_label", str(group9_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame1_status_text", str(group9_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame1_user_button", str(group9_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame2_user_label", str(group9_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame2_status_text", str(group9_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame2_user_button", str(group9_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame3_user_label", str(group9_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame3_status_text", str(group9_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame3_user_button", str(group9_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame4_user_label", str(group9_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame4_status_text", str(group9_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame4_user_button", str(group9_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame5_user_label", str(group9_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame5_status_text", str(group9_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame5_user_button", str(group9_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame6_user_label", str(group9_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame6_status_text", str(group9_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame6_user_button", str(group9_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame7_user_label", str(group9_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame7_status_text", str(group9_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame7_user_button", str(group9_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame8_user_label", str(group9_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame8_status_text", str(group9_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame8_user_button", str(group9_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame9_user_label", str(group9_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame9_status_text", str(group9_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame9_user_button", str(group9_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame10_user_label", str(group9_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame10_status_text", str(group9_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame10_user_button", str(group9_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame11_user_label", str(group9_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame11_status_text", str(group9_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame11_user_button", str(group9_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame12_user_label", str(group9_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame12_status_text", str(group9_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group9_frame12_user_button", str(group9_frame12_user_button) )

            # GROUP #10 PANEL CONFIG DATA SETTINGS 
            medical_config.set("USER_DESIGNS_GUI", "group10_frame1_user_label", str(group10_frame1_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame1_status_text", str(group10_frame1_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame1_user_button", str(group10_frame1_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame2_user_label", str(group10_frame2_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame2_status_text", str(group10_frame2_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame2_user_button", str(group10_frame2_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame3_user_label", str(group10_frame3_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame3_status_text", str(group10_frame3_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame3_user_button", str(group10_frame3_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame4_user_label", str(group10_frame4_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame4_status_text", str(group10_frame4_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame4_user_button", str(group10_frame4_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame5_user_label", str(group10_frame5_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame5_status_text", str(group10_frame5_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame5_user_button", str(group10_frame5_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame6_user_label", str(group10_frame6_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame6_status_text", str(group10_frame6_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame6_user_button", str(group10_frame6_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame7_user_label", str(group10_frame7_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame7_status_text", str(group10_frame7_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame7_user_button", str(group10_frame7_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame8_user_label", str(group10_frame8_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame8_status_text", str(group10_frame8_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame8_user_button", str(group10_frame8_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame9_user_label", str(group10_frame9_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame9_status_text", str(group10_frame9_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame9_user_button", str(group10_frame9_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame10_user_label", str(group10_frame10_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame10_status_text", str(group10_frame10_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame10_user_button", str(group10_frame10_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame11_user_label", str(group10_frame11_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame11_status_text", str(group10_frame11_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame11_user_button", str(group10_frame11_user_button) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame12_user_label", str(group10_frame12_user_label) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame12_status_text", str(group10_frame12_status_text) )
            medical_config.set("USER_DESIGNS_GUI", "group10_frame12_user_button", str(group10_frame12_user_button) )

             
            # save medical_record_config.ini file 
            with open(str(fullpath_med_config_ini_global), 'w') as med_configfile:
                 medical_config.write(med_configfile)
                 


    def lift_group_one_WINDOW(self, event):
        # print(" ")
        # print(".... COMMAND *** L I F T *** GROUP ONE BUTTON - gui_group_one_object.lift() - " + str(gui_group_one_object) )
        # print(" ")

        # lifts the group_one window.
        gui_group_one_object.lift()


    def lift_group_two_WINDOW(self, event):
        # print(" ")
        # print(".... COMMAND *** L I F T *** GROUP TWO BUTTON - gui_group_two_object.lift() - " + str(gui_group_two_object) )
        # print(" ")
        
        # lifts the group_two window.
        gui_group_two_object.lift()


    def lift_group_three_WINDOW(self, event):

        # lifts the group_three window. 
        gui_group_three_object.lift()


    def lift_group_four_WINDOW(self, event):
        
        # lifts the group_four window. 
        gui_group_four_object.lift()


    def lift_group_five_WINDOW(self, event):
        
        # lifts the group_five window. 
        gui_group_five_object.lift()


    def lift_group_six_WINDOW(self, event):
        
        # lifts the group_six window. 
        gui_group_six_object.lift()


    def lift_group_seven_WINDOW(self, event):
        
        # lifts the group_seven window. 
        gui_group_seven_object.lift()


    def lift_group_eight_WINDOW(self, event):
        
        # lifts the group_eight window. 
        gui_group_eight_object.lift()


    def lift_group_nine_WINDOW(self, event):
        
        # lifts the group_nine window. 
        gui_group_nine_object.lift()


    def lift_group_ten_WINDOW(self, event):
        
        # lifts the group_ten window. 
        gui_group_ten_object.lift()


        
    def lift_the_main_WINDOW(self):
          OBJECT_main.lift()



    def exit_Handler(self):
        self.master.destroy()


        

class HyperlinkManager(object):
    """A class to easily add clickable hyperlinks to Text areas.
    Usage:
      callback = lambda : webbrowser.open("http://www.google.com/")
      text = tk.Text(...)
      hyperman = tkHyperlinkManager.HyperlinkManager(text)
      text.insert(tk.INSERT, "click me", hyperman.add(callback))
    From http://effbot.org/zone/tkinter-text-hyperlink.htm
    """
    def __init__(self, text):
        self.text = text
        self.text.tag_config("hyper", foreground="snow", underline=1)
        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)
        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        """Adds an action to the manager.
        :param action: A func to call.
        :return: A clickable tag to use in the text widget.
        """
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return ("hyper", tag)

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(tk.CURRENT):
            if (tag[:6] == "hyper-"):
                self.links[tag]()
                return


          
##############################################################################
#
#   Contact Management Application Documentation Media Class 
#    
#   Multi-Media Guide to this Contact Management Application.
#
#   This CM_App_Doc_Media Class is currently being utilized
#   to give the Application Users an EMAIL STARTUP Procedure
#   for both SMTP Mode and OAUTH2 Mode Gmail Email features
#   used by this Contact Management Application. 
#
##############################################################################
class CM_App_Doc_Media(Frame):  #(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global username_global
        global userprofile_global
        global appdata_path_global
        global cm_appdatafiles_path_global
        global import_excel_csv_userprofile_global
        global import_excel_csv_cm_appdata_global
        global export_csv_excel_userprofile_global
        global export_csv_excel_cm_appdata_global
        global export_to_excel_listbox_select_fn_global
        global new_excel_file_created_global
        global client_secret_dir_global
        global credential_home_dir_global
        global client_secret_path_global
        global credential_home_path_global
        global OBJECT_toplevel_cm_app_doc_media
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        
        # self.master = master
        # self.frame = tk.Frame(self.master)

        # self.master = master
        # self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice   
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        OBJECT_toplevel_cm_app_doc_media = self.master
        instance_object_LIST.append(self.master)
        
        self.master.configure(background="dark slate gray")

        self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - EMAIL STARTUP Procedure.")

        # Button Widget for ROW ZERO to Reserve ROW ZERO for Expanded TOOLBAR Type Button Functions.
        self.reserve_row_zero_button = Button(self.master, text = "", \
            width=34,height=1, font=('Helvetica', '12'), background="dark slate gray")
        
        self.reserve_row_zero_button.grid(row=0, column=0, sticky = W)
        ## Future ROW ZERO Buttons use this line format.
        ## self.reserve_row_zero_button.bind("<Button-1>",self.some_method_here)

        # Button Widget for EXPORT METHOD.
        self.howto_activate_gmail_smtp_mode_button = Button(self.master, text = "QUICK One-Minute Option\n\nActivate Gmail (SMTP Mode)", \
            width=34,height=4, font=('Helvetica', '12'), background="dark slate gray", fg="cyan", \
            activebackground="dark slate gray", activeforeground="cyan")
        
        self.howto_activate_gmail_smtp_mode_button.grid(row=1, column=0, sticky = NW)
        self.howto_activate_gmail_smtp_mode_button.bind("<Button-1>",self.howto_activate_gmail_smtp_mode)
        
        # TEXTBOX to insert TITLE at top of window   

        self.title_1_text_box = Text(self.master, width=90, height = 29)
        self.title_1_text_box.config(state=NORMAL)  # DISABLED
        self.title_1_text_box.grid(row=1, column=1, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '12'), background="dark slate gray", fg="cyan")


      
        text_1_TITLE = "\n*********** EMAIL STARTUP Procedure *********** QUICK One-Minute Option (SMTP Mode) **********\n\nWelcome to the Contact Management EMAIL STARTUP Procedure.\n\nThis Contact Management Application is currently designed to SEND EMail using your GMAIL Email.\n\nThis EMAIL STARTUP Procedure Guides you through the steps to allow this Contact Management Application\nto SEND GMAIL using your GMAIL EMAIL.\n\nSTEP #1 is to configure your GMAIL EMAIL to give this Contact Management Application permission\nto SEND GMAIL using your GMAIL EMAIL. This requires you to login to your GMAIL EMAIL, and then,\n open another Window and Go To The Link:\n\n.............................  "

        text_1EEE_TITLE = "\n\nWhile at the Link above, scroll down to the bottom right side of the GOOGLE SECURITY WEBPAGE\nand locate a SLIDING SWITCH called:  ALLOW LESS SECURE APPS   \n\nTurn ON the  ALLOW LESS SECURE APPS  switch by SLIDING the switch to the right to set the\nswitch to the ON position.\n\nCongratulations !!  You are now ready to SEND your first GMAIL using this Contact Management Application.\n\n Note #1: Please select SMTP GMAIL MODE at the TOP RIGHT of the EMAIL SCREEN to send\nGMAIL  with this  ALLOW LESS SECURE APPS  switch  ON. In this SMTP GMAIL MODE,\nyour Gmail Username and Password must be entered when you SEND EMAIL.\n\nNote #2: Eventually, it is recommeded to configure the GMAIL EMAIL capabilities of this Contact Management \nApplication with the ADVANCED SECURITY OAUTH2 GMAIL MODE where this Application runs with\nSecurity Credentials and your GMAIL Username and Password are not required.\n"


        # Using Class: HyperlinkManager 
        GOOGLE_SECURITY_ALLOW_LESS_SECURE_APPS_LINK = lambda : webbrowser.open("https://myaccount.google.com/security")
        # text = tk.Text(...)
        hyperman = HyperlinkManager(self.title_1_text_box)

        important_client_secret_file_string = "IMPORTANT FILE #1:  " + str(client_secret_path_global) + "\n\n"

        important_credentials_file_string = "IMPORTANT FILE #2:  " + str(credential_home_path_global) + "\n\n"

        # Clear Textbox and then INSERT Text for howto_activate_gmail_smtp_mode method.
        self.title_1_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data  
        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.insert(INSERT, "https://myaccount.google.com/security", hyperman.add(GOOGLE_SECURITY_ALLOW_LESS_SECURE_APPS_LINK))
        self.title_1_text_box.insert(END, text_1EEE_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # NORMAL


        # Button Widget for METHOD: howto_activate_gmail_oauth2_mode_part_one
        # ADVANCED SECURITY Option (Part 1) - Activate Gmail (OAUTH2 Mode)  
        # Note that activebackground="dark slate gray", activeforeground="cyan")
        # were required to maintain this button's background and forground colors
        # because something makes the button "active" after the method executes.
        self.howto_activate_oauth2_part_one_button = Button(self.master, text = "ADVANCED SECURITY Option (Part 1)\n\nActivate Gmail (OAUTH2 Mode)", \
            width=34,height=4, font=('Helvetica', '12'), background="dark slate gray", fg="cyan", \
            activebackground="dark slate gray", activeforeground="cyan")
        self.howto_activate_oauth2_part_one_button.grid(row=1, column=0, sticky = W)
        self.howto_activate_oauth2_part_one_button.bind("<Button-1>",self.howto_activate_gmail_oauth2_mode_part_one)
        self.howto_activate_oauth2_part_one_button.configure(state = "normal", relief="raised", background="dark slate gray", fg="cyan")


        # Button Widget for METHOD: howto_activate_gmail_oauth2_mode_part_two
        # ADVANCED SECURITY Option (Part 2) - Verify Gmail (OAUTH2 Mode)
        # Note that activebackground="dark slate gray", activeforeground="cyan")
        # were required to maintain this button's background and forground colors
        # because something makes the button "active" after the method executes.
        self.howto_activate_oauth2_part_two_button = Button(self.master, text = "ADVANCED SECURITY Option (Part 2)\n\nVERIFY client_secret.json on the\n\nSTATUS PANEL (OAUTH2 Mode)", \
            width=34,height=6, font=('Helvetica', '12'), background="dark slate gray", fg="cyan", \
            activebackground="dark slate gray", activeforeground="cyan")
        self.howto_activate_oauth2_part_two_button.grid(row=1, column=0, sticky = SW)
        self.howto_activate_oauth2_part_two_button.bind("<Button-1>",self.howto_activate_gmail_oauth2_mode_part_two)
        self.howto_activate_oauth2_part_two_button.configure(state = "normal", relief="raised", background="dark slate gray", fg="cyan")
        
        #
        # LOWER WINDOW BUTTON.   
        # 
        self.lower_window_Button = Button(self.master, text = "MAIN SCREEN", width = 15, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2", command = self.lower_email_WINDOW)

        self.lower_window_Button.grid(row=7, column=0, sticky = E)

        #
        # EXIT BUTTON.  
        # 
        self.quitButton = Button(self.master, text = "EXIT", width = 7, height = 1, \
            font=('Helvetica', '16'), background="cyan4", fg="black", borderwidth=5,\
            activebackground="cyan",activeforeground="blue2", command = self.exit_Handler)

        self.quitButton.grid(row=7, column=0, sticky = W)




    def lower_email_WINDOW(self):
          # These CYCLE Buttons have been changed to 
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()
        


    def exit_Handler(self):
        self.master.destroy()



    #####################################################################
    #   
    #  Method to display howto_activate_gmail_smtp_mode instructions.
    #
    #####################################################################
#1234
    def howto_activate_gmail_smtp_mode(self, event):
      
        text_1_TITLE = "\n*********** EMAIL STARTUP Procedure *********** QUICK One-Minute Option (SMTP Mode) **********\n\nWelcome to the Contact Management EMAIL STARTUP Procedure.\n\nThis Contact Management Application is currently designed to SEND EMail using your GMAIL Email.\n\nThis EMAIL STARTUP Procedure Guides you through the steps to allow this Contact Management Application\nto SEND GMAIL using your GMAIL EMAIL.\n\nSTEP #1 is to configure your GMAIL EMAIL to give this Contact Management Application permission\nto SEND GMAIL using your GMAIL EMAIL. This requires you to login to your GMAIL EMAIL, and then,\n open another Window and Go To The Link:\n\n.............................  "

        text_1EEE_TITLE = "\n\nWhile at the Link above, scroll down to the bottom right side of the GOOGLE SECURITY WEBPAGE\nand locate a SLIDING SWITCH called:  ALLOW LESS SECURE APPS   \n\nTurn ON the  ALLOW LESS SECURE APPS  switch by SLIDING the switch to the right to set the\nswitch to the ON position.\n\nCongratulations !!  You are now ready to SEND your first GMAIL using this Contact Management Application.\n\n Note #1: Please select SMTP GMAIL MODE at the TOP RIGHT of the EMAIL SCREEN to send\nGMAIL  with this  ALLOW LESS SECURE APPS  switch  ON. In this SMTP GMAIL MODE,\nyour Gmail Username and Password must be entered when you SEND EMAIL.\n\nNote #2: Eventually, it is recommeded to configure the GMAIL EMAIL capabilities of this Contact Management \nApplication with the ADVANCED SECURITY OAUTH2 GMAIL MODE where this Application runs with\nSecurity Credentials and your GMAIL Username and Password are not required.\n"


        # Using Class: HyperlinkManager 
        GOOGLE_SECURITY_ALLOW_LESS_SECURE_APPS_LINK = lambda : webbrowser.open("https://myaccount.google.com/security")
        # text = tk.Text(...)
        hyperman = HyperlinkManager(self.title_1_text_box)

        important_client_secret_file_string = "IMPORTANT FILE #1:  " + str(client_secret_path_global) + "\n\n"

        important_credentials_file_string = "IMPORTANT FILE #2:  " + str(credential_home_path_global) + "\n\n"

        
        # Clear Textbox and then INSERT Text for howto_activate_gmail_smtp_mode method.
        self.title_1_text_box.config(state=NORMAL)  # DISABLED
        self.title_1_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data  
        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.insert(INSERT, "https://myaccount.google.com/security", hyperman.add(GOOGLE_SECURITY_ALLOW_LESS_SECURE_APPS_LINK))
        self.title_1_text_box.insert(END, text_1EEE_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # NORMAL
       


    ###############################################################################
    #   
    # Programming Note:     ( Reference to the code above )   
    #
    # Note that the generic sequence of TEXT WIDGET Commands to use to
    # make the TEXT WIDGET be READ ONLY is as follows:
    #
    # text.config(state=NORMAL)  # DISABLED
    # text.delete(1.0, END)
    # text.insert(END, text)
    # text.config(state=DISABLED)
    #
    ###############################################################################
    #
    # Specifically, Our Big Text Widget will experience these commands:
    #
    # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
    # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
    # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
    # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
    #
    ###############################################################################

    ################################################################################
    #     
    #  Method to display howto_activate_gmail_oauth2_mode_part_one instructions.
    #    
    ################################################################################
#1234
    def howto_activate_gmail_oauth2_mode_part_one(self, event):
        global client_secret_dir_global
        global credential_home_dir_global
        global client_secret_path_global
        global credential_home_path_global

        text_1_TITLE = "\n*********** EMAIL STARTUP Procedure *********** ADVANCED SECURITY - OAUTH2 Mode (Part 1) **********\n\nWelcome to the Contact Management EMAIL STARTUP Procedure for\nthe ADVANCED SECURITY - OAUTH2 Mode (Part 1).\n\nThis is Part 1 of the ADVANCED SECURITY OAUTH2 Mode EMAIL STARTUP Procedure.\nTypically this procedure would be executed by a trained System Administrator (a trained IT Specialist), however, \nthe Guidelines for this procedure are summarized here to allow moderately skilled computer users to execute \nthis procedure to configure their GMAIL EMAIL for ADVANCED SECURITY OAUTH2 Mode.\n\nThis Contact Management Application is currently designed to SEND EMail using your GMAIL Email.\nThis EMAIL STARTUP Procedure Guides you through the steps to allow this Contact Management Application\nto SEND GMAIL using your GMAIL EMAIL.\n\nThe process to configure your GMAIL EMAIL to give this Contact Management Application permission\nto SEND GMAIL using your GMAIL EMAIL requires you to, FIRST, LOGIN to your GMAIL EMAIL,\nand THEN, CLICK this Link:\n\n.............................  "


        text_1AAA_TITLE = "\n\nWhile viewing the LINK above, execute STEP #1 of the PYTHON QUICKSTART technical procedure\ncalled  *** TURN ON THE GMAIL API *** which eventually instructs you how to DOWNLOAD your DOT JSON file.\nAfter Downloading this DOT JSON file, rename the DOT JSON file to client_secret.json  (client_secret DOT json)\nand then copy this client_secret.json file to the following DOT CREDENTIALS DIRECTORY on your Computer:\n\n .............................  "

        text_1AAA_TWO_TITLE = "\n\nThus, the complete WINDOWS FOLDER or DIRECTORY PATH to your client_secret.json file is: \n\n.............................  "


        text_1BBB_TITLE = "\n\nNote that the SYSTEM ADMINISTRATION SCREEN of this Application also shows the exact DIRECTORY\n(or Windows Folder) where this DOT JSON file should be placed.\n\nNext, exit from this Contact Manager Application and restart the Contact Manager Application\nand press the APP STATUS button on the MAIN SCREEN of this Contact Manager Application.\nLocate the STATUS INDICATOR called GMAIL OAUTH2 JSON FILE STATUS in the top left hand corner \nof the STATUS PANEL. Verify that the GMAIL OAUTH2 JSON FILE STATUS indicator is GREEN, \nwhich means the FORMAT of your client_secret.json file is good. This GREEN status on the STATUS PANEL\nindicator for GMAIL OAUTH2 JSON FILE STATUS is required to verify that you have placed your\nclient_secret.json file in the correct DIRECTORY, and the client_secret.json file has the correct FORMAT.\n\nNext, go to the EMAIL SCREEN of this Contact Manager Application, select OAUTH2 Mode in the\ntop right hand corner EMAIL MODE SELECTOR, and carefully send a GMAIL EMAIL to yourself to activate\nyour GMAIL CREDENTIALS. You will get a pop-up window the first time to ask you for permission\nto allow this Contact Manager to use your GMAIL EMAIL. Then after sending an EMAIL, verify that\nthe following two files are present in your DOT CREDENTIALS DIRECTORY (Windows Folder):\n\n"


        text_1CCC_TITLE = "Note #1: You can always VERIFY that your client_secret.json file exists by following the next step \nand selecting the button at the left of this screen for ADVANCED SECURITY - OAUTH2 Mode (Part 2).\nADVANCED SECURITY - OAUTH2 Mode (Part 2) simply reminds you to always check the STATUS PANEL\nfor the GREEN GMAIL OAUTH2 JSON FILE STATUS indicator when executing ADVANCED SECURITY\nOAUTH2 Email. If the GMAIL OAUTH2 JSON FILE STATUS indicator on the STATUS PANEL is RED,\nyou will likely want to Download a new DOT JSON CLIENT SECRET as described above in this\nADVANCED SECURITY OAUTH2 Email Procedure.\n\nNote #2: The SYSTEMS ADMINISTRATION SCREEN on this Application also shows the \nDIRECTORY paths for the GMAIL OAUTH2 CREDENTIALS FILE (gmail-python-quickstart.json) \nand the GMAIL OAUTH2 CLIENT SECRET FILE (client_secret.json).\n\nNote #3: Please select OAUTH2 MODE at the TOP RIGHT of the EMAIL SCREEN when sending EMail \nwith this Contact Management Application.\n\nNote #4: In this ADVANCED SECURITY OAUTH2 GMAIL MODE, where this Application runs\nwith Security Credentials, your GMAIL Username and Password are not required.\n\nCongratulations !!  You are now ready to SEND GMAIL in ADVANCED SECURITY OAUTH2 Mode \nusing this Contact Management Application.\n"

        
        # Using Class: HyperlinkManager 
        PYTHON_QUICK_START_LINK = lambda : webbrowser.open("https://developers.google.com/gmail/api/quickstart/python/")
        # text = tk.Text(...)
        hyperman = HyperlinkManager(self.title_1_text_box)

        important_client_secret_file_string = "IMPORTANT FILE #1:  " + str(client_secret_path_global) + "\n\n"

        important_credentials_file_string = "IMPORTANT FILE #2:  " + str(credential_home_path_global) + "\n\n"

        # Clear Textbox and then INSERT Text for howto_activate_gmail_smtp_mode method.
        self.title_1_text_box.config(state=NORMAL)  # DISABLED
        self.title_1_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data  
        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.insert(INSERT, "https://developers.google.com/gmail/api/quickstart/python/", hyperman.add(PYTHON_QUICK_START_LINK))
        self.title_1_text_box.insert(END, text_1AAA_TITLE)
        self.title_1_text_box.insert(END, str(client_secret_dir_global))
        self.title_1_text_box.insert(END, text_1AAA_TWO_TITLE)
        self.title_1_text_box.insert(END, str(client_secret_path_global))
        self.title_1_text_box.insert(END, text_1BBB_TITLE)
        self.title_1_text_box.insert(END, str(important_client_secret_file_string))
        self.title_1_text_box.insert(END, str(important_credentials_file_string))
        self.title_1_text_box.insert(END, text_1CCC_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # NORMAL



        
    ################################################################################ 
    #       
    #  Method to display howto_activate_gmail_oauth2_mode_part_two instructions.
    # 
    ################################################################################
#1234
    def howto_activate_gmail_oauth2_mode_part_two(self, event):
        global client_secret_dir_global
        global credential_home_dir_global
        global client_secret_path_global
        global credential_home_path_global

        text_1_TITLE = "\n*********** EMAIL STARTUP Procedure *********** ADVANCED SECURITY - OAUTH2 Mode (Part 2) **********\n\nWelcome to the Contact Management EMAIL STARTUP Procedure for\nthe ADVANCED SECURITY - OAUTH2 Mode (Part 2).\n\nThis is Part 2 of the ADVANCED SECURITY OAUTH2 Mode EMAIL STARTUP Procedure explains the steps \nto VERIFY the FORMAT of your  client_secret.json  file that should be located in the DOT CREDENTIALS\nDIRECTORY on your computer (along with your gmail-python-quickstart.json CREDENTIALS JSON file) as follows:  \n\n"

        
        text_1DDD_TITLE = "On the Main Screen (top left hand corner) of this Application, select the APP STATUS button\nto display the STATUS PANEL. Locate the STATUS INDICATOR called GMAIL OAUTH2 JSON FILE STATUS\nin the top left hand corner of the STAUS PANEL. Verify that the GMAIL OAUTH2 JSON FILE STATUS indicator\nis GREEN, which means the FORMAT of your client_secret.json file is good. This GREEN status on the\nSTATUS PANEL GMAIL OAUTH2 JSON FILE STATUS indicator is required to verify that you have placed\nyour client_secret.json file in the correct DIRECTORY, and the client_secret.json file has the correct FORMAT.\n\nYou can always VERIFY that your client_secret.json file exists by checking the STATUS PANEL\nfor the GREEN GMAIL OAUTH2 JSON FILE STATUS indicator when executing ADVANCED SECURITY\nOAUTH2 Email. If the GMAIL OAUTH2 JSON FILE STATUS indicator on the STATUS PANEL is RED,\nyou will likely want to Download a new DOT JSON CLIENT SECRET as described above in Part 1 of this\nADVANCED SECURITY OAUTH2 Email Procedure.\n\nNote #1: Please select OAUTH2 MODE at the TOP RIGHT of the EMAIL SCREEN when sending EMail \nwith this Contact Management Application.\n\nNote #2: In this ADVANCED SECURITY OAUTH2 GMAIL MODE, where this Application runs\nwith Security Credentials, your GMAIL Username and Password are not required.\n\nCongratulations !!  You are now ready to SEND GMAIL in ADVANCED SECURITY OAUTH2 Mode \nusing this Contact Management Application.\n"

        
        important_client_secret_file_string = "IMPORTANT FILE #1:  " + str(client_secret_path_global) + "\n\n"

        important_credentials_file_string = "IMPORTANT FILE #2:  " + str(credential_home_path_global) + "\n\n"

        
        # Clear Textbox and then INSERT Text for howto_activate_gmail_smtp_mode method.
        self.title_1_text_box.config(state=NORMAL)  # DISABLED
        self.title_1_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data  
        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.insert(END, str(important_client_secret_file_string))
        self.title_1_text_box.insert(END, str(important_credentials_file_string))
        self.title_1_text_box.insert(END, text_1DDD_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # NORMAL



        

##############################################################################
#
#   E X P O R T  (Contact List CSV to Excel)  
#    
#   EXPORT CSV DATA for EXCEL SPREADHSEET and EXCEL WORKBOOKS.
# 
#   ----  SELECT An "EXPORT TO EXCEL" CONTACT LIST FILE FROM A LISTBOX
#
##############################################################################
#
#   I M P O R T  (Excel CSV or any CSV to Contact Management Contact List)
# 
#   IMPORT CSV FROM EXCEL TO CONTACT MANAGEMENT APP CONTACT LIST.
#
#   ----  SELECT An "IMPORT FROM CSV" CSV FILE FROM A LISTBOX (or Dialog) 
#
##############################################################################
#
class Excel_Import_Export(Frame):   #(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global username_global
        global user_profile_global
        global appdata_path_global
        global cm_appdatafiles_path_global
        global import_excel_csv_userprofile_global
        global import_excel_csv_cm_appdata_global
        global export_csv_excel_userprofile_global
        global export_csv_excel_cm_appdata_global
        global export_to_excel_listbox_select_fn_global
        global new_excel_file_created_global
        global kick_thread_to_update_main_entry_widgets
        global OBJECT_toplevel_excel_import_export
        global instance_object_LIST
        Frame.__init__(self, master)
        self.grid()
        
        # self.master = master
        # self.frame = tk.Frame(self.master)

        # self.master = master
        # self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        OBJECT_toplevel_excel_import_export = self.master
        instance_object_LIST.append(self.master)
        
        self.master.configure(background="dark slate gray")

        self.master.title("Contact Management COMMAND CENTER WORKSTATION Application Software - EXPORT Contact List to Excel - IMPORT CSV to Contact List")

        # Button Widget for ROW ZERO to Reserve ROW ZERO for Expanded TOOLBAR Type Button Functions.
        self.reserve_row_zero_button = Button(self.master, text = "", \
            width=25,height=3, font=('Helvetica', '12'), background="dark slate gray", activebackground="dark slate gray")
        
        self.reserve_row_zero_button.grid(row=0, column=0, sticky = W)
        ## Future ROW ZERO Buttons use this line format.
        ## self.reserve_row_zero_button.bind("<Button-1>",self.some_method_here)

        #   E X P O R T   D A T A   WIDGET GROUP

        # Button Widget for EXPORT METHOD.
        self.export_sign_button = Button(self.master, text = "E X P O R T  to  Excel", \
            width=25,height=3, font=('Helvetica', '12'), background="dark slate gray", fg="cyan", \
            activebackground="dark slate gray", activeforeground="cyan") 
        
        self.export_sign_button.grid(row=1, column=0, sticky = W)
        self.export_sign_button.bind("<Button-1>",self.convert_CSV_to_Excel)
        
        self.select_file_button = Button(self.master, text = "Click EXPORT to Excel (above)\nto EXPORT Contact List\nto EXCEL Spreadsheet", \
            width=25,height=3, font=('Helvetica', '12'), background="dark slate gray", fg="light sea green", \
            activebackground="dark slate gray", activeforeground="light sea green")

        self.select_file_button.grid(row=2, column=0, sticky = W)


        # TEXTBOX to insert TITLE at top of window  

        self.title_1_text_box = Text(self.master, width=90, height = 2)
        self.title_1_text_box.grid(row=1, column=1, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="cyan4")

        text_1_TITLE = "  Currently Selected CONTACT LIST\n  for EXPORT to EXCEL:   " + str(master_cm_list_name_global)

        self.title_1_text_box.insert(END, text_1_TITLE)

        # TEXTBOX to insert EXCEL FILE PATH NOTE and CONTACT LIST EXPORTED STATUS MESSAGE at top of window 

        self.title_2_text_box = Text(self.master, width=90, height = 3)
        self.title_2_text_box.grid(row=2, column=1, sticky = W)
        self.title_2_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="cyan4")

        text_2_TITLE = "  Click the EXPORT to EXCEL button to generate an Excel Spreadsheet from the selected Contact List.\n  The EXCEL Spreadsheet generated will be located in Windows Folder:\n  " + str(export_csv_excel_userprofile_global)
        self.title_2_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data
        self.title_2_text_box.insert(END, text_2_TITLE)

        # Button Widget for ROW THREE to Reserve ROW THREE for Expanded TOOLBAR Type Button Functions.
        self.reserve_row_three_button = Button(self.master, text = "", \
        width=25,height=3, font=('Helvetica', '12'), background="dark slate gray", activebackground="dark slate gray")
        
        self.reserve_row_three_button.grid(row=3, column=0, sticky = W)
        ## Future ROW THREE Buttons use this line format.   
        ## self.reserve_row_three_button.bind("<Button-1>",self.some_method_here)

        #   I M P O R T   D A T A   WIDGET GROUP 

        # Button Widget for IMPORT METHOD.
        # Note that activebackground="dark slate gray", activeforeground="cyan")
        # were required to maintain this button's background and forground colors
        # because something makes the button "active" after the method executes.
        self.import_sign_button = Button(self.master, text = "I M P O R T  from  Excel", \
            width=25,height=3, font=('Helvetica', '12'), background="dark slate gray", fg="cyan", \
            activebackground="dark slate gray", activeforeground="cyan")
        self.import_sign_button.grid(row=4, column=0, sticky = W)
        self.import_sign_button.bind("<Button-1>",self.convert_CSV_to_App_Contact_List)
        self.import_sign_button.configure(state = "normal", relief="raised", background="dark slate gray", fg="cyan", \
        activebackground="dark slate gray", activeforeground="cyan")
        
        self.select_import_file_button = Button(self.master, text = "Click IMPORT from Excel (above)\nto IMPORT Excel CSV File\nto Contact List", \
        width=25,height=3, font=('Helvetica', '12'), background="dark slate gray", fg="light sea green", \
        activebackground="dark slate gray", activeforeground="light sea green")
        self.select_import_file_button.grid(row=5, column=0, sticky = W)

        # TEXTBOX to insert TITLE at top of window 

        self.title_1_import_text_box = Text(self.master, width=90, height = 2)
        self.title_1_import_text_box.grid(row=4, column=1, sticky = W)
        self.title_1_import_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="cyan4")

        text_1_TITLE = "  Currently Selected CONTACT LIST\n  for IMPORT of CSV File:   " + str(master_cm_list_name_global)

        self.title_1_import_text_box.insert(END, text_1_TITLE)

        # TEXTBOX to insert EXCEL FILE PATH NOTE and  
        # CONTACT LIST EXPORTED STATUS MESSAGE at top of window 

        self.title_2_import_text_box = Text(self.master, width=90, height = 3)
        self.title_2_import_text_box.grid(row=5, column=1, sticky = W)
        self.title_2_import_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="cyan4")

        text_2_TITLE = "  Click the IMPORT from Excel button and Select CSV File from Dialog Windows to import to selected Contact List.\n  The Excel CSV File you SELECT to IMPORT will also be copied to Windows Folder:\n  " + str(import_excel_csv_userprofile_global)
        self.title_2_import_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data
        self.title_2_import_text_box.insert(END, text_2_TITLE)

        # Button Widget for ROW SIX to Reserve ROW SIX for Expanded TOOLBAR Type Button Functions.
        self.reserve_row_six_button = Button(self.master, text = "", \
        width=25,height=3, font=('Helvetica', '12'), background="dark slate gray", activebackground="dark slate gray")
        
        self.reserve_row_six_button.grid(row=6, column=0, sticky = W)
        ## Future ROW THREE Buttons use this line format.   
        ## self.reserve_row_six_button.bind("<Button-1>",self.some_method_here)

        # TEXTBOX to insert CSV IMPORT FORMAT EXAMPLE for User to Import from
        # Excel or whatever Database Source they are importing from. 

        self.title_1_CSV_FORMAT_text_box = Text(self.master, width=90, height = 4)
        self.title_1_CSV_FORMAT_text_box.grid(row=7, column=1, sticky = W)
        self.title_1_CSV_FORMAT_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="cyan4")

        text_1_TITLE = "  IMPORT to this Contact Management Application requires the following\n  CSV File Format or Excel Spreadhseet Headings Format: \n\n  First Name, Last Name, Street Address, City or Town, State, Zip Code, Phone Number, EMail Address, Website"

        self.title_1_CSV_FORMAT_text_box.insert(END, text_1_TITLE)

        #
        # LOWER WINDOW BUTTON.   
        # 
        self.lower_window_Button = Button(self.master, text = "MAIN SCREEN", width = 12, height = 1, \
            font=('Helvetica', '16'), background="cyan4", activebackground="cyan", \
            activeforeground="blue2", borderwidth=5, command = self.lower_email_WINDOW)

        self.lower_window_Button.grid(row=7, column=0, sticky = E)

        #
        # EXIT BUTTON.  
        # 
        self.quitButton = Button(self.master, text = "EXIT", width = 4, height = 1, \
            font=('Helvetica', '16'), background="cyan4", activebackground="cyan", \
            activeforeground="blue2", borderwidth=5, command = self.exit_Handler)

        self.quitButton.grid(row=7, column=0, sticky = W)


 

    def lower_email_WINDOW(self):
          # These CYCLE Buttons have been changed to 
          # return to the main screen by lifting the main window.
          OBJECT_main.lift()



    def exit_Handler(self):
        self.master.destroy()

     

    def convert_CSV_to_App_Contact_List(self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global username_global  
        global userprofile_global
        global appdata_path_global
        global cm_appdatafiles_path_global
        global import_excel_csv_userprofile_global
        global import_excel_csv_cm_appdata_global
        global export_csv_excel_userprofile_global
        global export_csv_excel_cm_appdata_global
        global export_to_excel_listbox_select_fn_global
        global new_excel_file_created_global
        global kick_thread_to_update_main_entry_widgets

        #####################################################################
        #
        # Open DIALOG to SELECT CSV File in Windows Folder
        # Use the Full File Path acquired from the DIALOG SELECTION
        # to copy the selected CSV File to the two 
        # IMPORT CSV File Directories (USER and APPDATA). 
        # Then, use the CSV parser Class to import the
        # CSV into a Dictionary, and then add that
        # imported Dictionary to our Contact List Database Files:
        # dict_ and cm_list_
        #
        #####################################################################

        # Use dialog to get CSV file to import.

        ###########   Select a Directory:

        root = tk.Tk()
        root.withdraw()
        home_dir = userprofile_global
        dirname = filedialog.askdirectory(parent=root,initialdir=home_dir,title='Please SELECT a Directory')

        directory_full_path = os.path.join(str(home_dir), str(dirname) )

        # print("\n\n")
        # print(".... DIRECTORY (FULL PATH): " + str(directory_full_path) )


        ############   Select a File to get CSV file to import.  

        # askopenfile - opens the file and returns the opened object (or Null if cancelled).

        # askopenfilename - just gets and returns the full path to the file (or empty string if cancelled).

        ftypes = [
            ('All Files', '*.*'),
            ("Microsoft Excel csv Files","*.csv")]

        root = tk.Tk()
        root.withdraw()

        csv_file_path = ""

        csv_file_path = filedialog.askopenfilename(parent=root,title='Choose a file',filetypes = ftypes)

        # print(".... Selected CSV File Path = " + str(csv_file_path) + "\n")

        csv_base_filename = os.path.basename(csv_file_path)

        # print(".... csv_base_filename = " + str(csv_base_filename) )

        # CSV File Full Paths that store Imported Excel CSV Files
        # that were IMPORTED to Contact Management App Contact List.
        #
        store_imported_csv_userdir_fullpath = os.path.join(str(import_excel_csv_userprofile_global), str(csv_base_filename) )
        store_imported_csv_appdata_fullpath = os.path.join(str(import_excel_csv_cm_appdata_global), str(csv_base_filename) )

        # COPY THIS CSV FILE TO OUR import_excel_csv DIRECTORY in USER PATH
        # COPY THIS CSV FILE TO OUR import_excel_csv DIRECTORY in APPDATA PATH

        # from shutil import copyfile
        # copyfile(source_path,destination_path)

        try:

            copyfile(str(csv_file_path),str(store_imported_csv_userdir_fullpath) )
            copyfile(str(csv_file_path),str(store_imported_csv_appdata_fullpath) )

        except:

            # print("  ")
            # print("  *****  copyfile FAILED  *****  CSV FILE BEING COPIED:  " + str(csv_file_path) )
            # print("  ")
            pass

        ################################################################################

        # print("  ")

        # print(".... IMPORTING CSV FILE  to  fullpath_fn_cm_listbox_file_global = " + str(fullpath_fn_cm_listbox_file_global) )

        # print("  ")
        
        # print(".... IMPORTING CSV FILE  to  fullpath_fn_dict_filename_global = " + str(fullpath_fn_dict_filename_global) )

        # print("  ")

        #################################################################################

        
        with open(str(csv_file_path), 'rt') as csv_import_fh:
            csv_import_reader = csv.reader(csv_import_fh, dialect=csv.excel)
            # print(".... I M P O R T E D    C S V    F I L E    with csv_import_reader = csv.reader(csv_import_fh, dialect=csv.excel)")

            for row in csv_import_reader:
                row_list_to_string = ""
                item_counter = 0
                item1 = ""
                item2 = ""
                item3 = ""
                item4 = ""
                item5 = ""
                item6 = ""
                item7 = ""
                item8 = ""
                item9 = ""
                for item in row:
                    item_counter += 1
                    #print(".... ITEM COUNTER = " + str(item_counter) )
                    #print(".... ITEM IN ROW = " + str(item) )
                    if item_counter == 1: item1 = str(item)
                    elif item_counter == 2: item2 = str(item)
                    elif item_counter == 3: item3 = str(item)
                    elif item_counter == 4: item4 = str(item)
                    elif item_counter == 5: item5 = str(item)
                    elif item_counter == 6: item6 = str(item)
                    elif item_counter == 7: item7 = str(item)
                    elif item_counter == 8: item8 = str(item)
                    elif item_counter == 9: item9 = str(item)

                row_list_to_string = str(item1) + "," + str(item2) + "," + str(item3) + "," + \
                                     str(item4) + "," + str(item5) + "," + str(item6) + "," + \
                                     str(item7) + "," + str(item8) + "," + str(item9) + "," + "\n"

                this_person = Person(str(item1), str(item2), str(item3), \
                            str(item4), str(item5), str(item6), str(item7), \
                            str(item8), str(item9) )

                gfn = this_person.get_Firstname()
                gln = this_person.get_Lastname()
                gsa = this_person.get_Streetadd()
                gct = this_person.get_Citytown()
                gst = this_person.get_State()
                gzc = this_person.get_Zipcode()
                gpn = this_person.get_Phonenum()
                gem = this_person.get_Email()
                gws = this_person.get_Website()

                # Create DICTIONARY to store contact data
                contact_dict = {"First_Name_KEY": str(gfn), "Last_Name_KEY": str(gln), "Street_Address_KEY": str(gsa), \
                                "City_Town_KEY": str(gct), "State_KEY": str(gst), "Zip_Code_KEY": str(gzc), \
                                "Phone_Number_KEY": str(gpn), "EMail_KEY": str(gem), "Website_KEY": str(gws) }

                # Store_Contact_Dict in Store_Contact_Dict Class 
                contact_dict_instance = Store_Contact_Dict(this_contact_dict = contact_dict)
                contact_dict_instance.set_contact_dict(new_this_contact_dict = contact_dict)
                get_contact_dict_call = contact_dict_instance.get_contact_dict()

                    
                # Write Line to CM DATABASE cm_list FILE ......
                #print(".... I M P O R T I N G    C S V    F I L E    L I N E   to   cm_list   DATABASE  FILE.")
                #print(".... row_list_to_string = " + str(row_list_to_string) )
                with open(str(fullpath_fn_cm_listbox_file_global), 'a') as cm_list_fh:
                    cm_list_fh.write(str(row_list_to_string) )

                # Write contact data dictionary to dict_filename file from class method get_contact_dict_call
                # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
                with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                      for x in range(0, 10):
                            if x == 0:
                                  wdictf.flush()
                                  wdictf.write("DATA_RECORD_DELIMITER:")
                            elif x == 1: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["First_Name_KEY"] ) )
                            elif x == 2: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Last_Name_KEY"] ) )
                            elif x == 3: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Street_Address_KEY"] ) )
                            elif x == 4: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["City_Town_KEY"] ) )
                            elif x == 5: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["State_KEY"] ) )
                            elif x == 6: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Zip_Code_KEY"] ) )
                            elif x == 7: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Phone_Number_KEY"] ) )
                            elif x == 8: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["EMail_KEY"] ) )
                            elif x == 9: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Website_KEY"] ) )
                            else: pass

        #############################################################################################################
        # 
        # Update Excel Spreadsheet STATUS TextBox with a CSV IMPORTED Message including the CONTACT LIST Name.
        text_2_import_NEW_TITLE = "  STATUS UPDATE:\n  Your Excel CSV File has been IMPORTED to the CONTACT LIST:  " + \
                                  str(master_cm_list_name_global) + "\n  Contacts Imported from Excel CSV File:  " + str(csv_file_path)
        self.title_2_import_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data
        self.title_2_import_text_box.insert(END, text_2_import_NEW_TITLE)
        self.title_2_import_text_box.config(background="turquoise")
        
        self.import_sign_button.configure(state = "normal", relief="raised", background="dark slate gray", fg="cyan")

        #############################################################################################################

        # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
        # WHICH SETS THE selected_dictionary_loaded_global GLOBAL.  

        inst_CM_IMPORT_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        updated_contact_dict_loaded_to_GLOBAL = inst_CM_IMPORT_Process_Dict_File.read_target_dict_file()

        # NOTE:
        # selected_dictionary_record_index_global = 1
        # selected_dictionary_record_index_focus_global = 1

        kick_thread_to_update_main_entry_widgets = True
                   




    def convert_CSV_to_Excel(self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global username_global
        global userprofile_global
        global appdata_path_global
        global cm_appdatafiles_path_global
        global import_excel_csv_userprofile_global
        global import_excel_csv_cm_appdata_global
        global export_csv_excel_userprofile_global
        global export_csv_excel_cm_appdata_global
        global export_to_excel_listbox_select_fn_global
        global new_excel_file_created_global


        # WE HAVE PREVIOUSLY SELECTED A CONTACT LIST for EXCEL
        # AND CAPTURED THAT INFO USING GLOBAL VARIABLES
        
        export_to_excel_filename_path = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )

        export_to_excel_workbook_filename_path = os.path.join(str(export_csv_excel_cm_appdata_global), str(master_cm_list_name_global) + ".xlsx" )
        
        export_to_excel_workbook_filename_home_path = os.path.join(str(export_csv_excel_userprofile_global), str(master_cm_list_name_global) + ".xlsx" )

        new_excel_file_created_global = str(export_to_excel_workbook_filename_home_path)

        # Update Excel Spreadsheet STATUS TextBox with PATH and FILENAME of NEW Excel Spreadsheet 
        text_2_NEW_TITLE = "  STATUS UPDATE:\n  Your NEW Excel SPREADSHEET has been CREATED in Windows Folder:\n  " + str(new_excel_file_created_global)
        self.title_2_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data
        self.title_2_text_box.insert(END, text_2_NEW_TITLE)
        self.title_2_text_box.config(background="turquoise")

        #read the csv into a pandas dataframe 
        data = pd.read_csv(str(export_to_excel_filename_path) )    
        #setup the writer
        writer = pd.ExcelWriter(str(export_to_excel_workbook_filename_path), engine='xlsxwriter')
        writer_two = pd.ExcelWriter(str(export_to_excel_workbook_filename_home_path), engine='xlsxwriter')
        #write the dataframe to an xlsx file
        data.to_excel(writer, sheet_name=str(master_cm_list_name_global), index=False)
        data.to_excel(writer_two, sheet_name=str(master_cm_list_name_global), index=False)
        writer.save()
        writer_two.save()

        #####################################################################################################
        #
        # SAVE THIS CODE SHOWING EXAMPLE OF HOW TO INSTANTIATE CLASS Process_Dict_File to create OBJECT 
        # Testing CLASS Process__Dict_File to see the INSTANTIATION and the READ of the dict_file_
        # We should see the dictionary # printed when an excel spreadsheet is generated. 
        #
        #####################################################################################################

        ######### PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
        #########
        ######### inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        ######### contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()

        #####################################################################################################
        
        #   # #print("\n" + "FROM INSTANTIATION OF CLASS :  Process_Dict_File ....... DICTIONARY GENERATED FROM dict_file_ READ:" + "\n")
        #   for key, value in contact_dict_acquired.items():
        #       # #print("\n")
        #       # #print('    ', key, 'is the INSTANTION key for the INSTANTIATION CLASS value', value)   

        ## #print("\n")
        ## #print("\n")
        #for s in sorted(contact_dict_acquired.items(), key=lambda k_v: k_v[1]["Last_Name_KEY"]):
        #      # #print(" .... **** SORTED INSTANTIATED DICTIONARY **** .... =  :  " + str(s) ) 
  

        return new_excel_file_created_global 
  

        
        

class Store_Lbox_Filename(object):
      def __init__(self, selected_lbox_file):
            self.selected_lbox_file = selected_lbox_file


      def set_listbox_file(self, new_Lbox_File):
            self.selected_lbox_file = new_Lbox_File
            return


      def get_listbox_file(self):
            return self.selected_lbox_file


        

class Store_Contact_Dict(object):
      def __init__(self, this_contact_dict):
            self.this_contact_dict = this_contact_dict


      def set_contact_dict(self, new_this_contact_dict):
            self.this_contact_dict = new_this_contact_dict
            return


      def get_contact_dict(self):
            return self.this_contact_dict



###################################################################
#
# Build a CLASS to define the DICTIONARY of DICTIONARIES
# to allow instantiation of the object to store each
# dict_file_ representing a contact list.
#
###################################################################
#
class Store_dictionary_of_dictionaries(object):
      def __init__(self, this_dict_of_dicts):
            self.this_dict_of_dicts = this_dict_of_dicts


      def set_dict_of_dicts(self, new_this_dict_of_dicts):
            self.this_dict_of_dicts = new_this_dict_of_dicts
            return


      def get_dict_of_dicts(self):
            return self.this_dict_of_dicts



  #####################################################################################################
  #
  # SAVE THIS CODE SHOWING EXAMPLE OF HOW TO INSTANTIATE CLASS Process_Dict_File to create OBJECT
  # Testing CLASS Process__Dict_File to see the INSTANTIATION and the READ of the dict_file_
  # We should see the dictionary # printed when an excel spreadsheet is generated.
  #
  #####################################################################################################
  #
  #   inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
  #   contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()
  #
  #   # #print("\n" + "FROM INSTANTIATION OF CLASS :  Process_Dict_File ....... DICTIONARY GENERATED FROM dict_file_ READ:" + "\n")
  #   for key, value in contact_dict_acquired.items():
  #       # #print("\n")
  #       # #print('    ', key, 'is the INSTANTION key for the INSTANTIATION CLASS value', value)
  #        
  #   
  #   # #print("\n")
  #   # #print("\n")
  #   for s in sorted(contact_dict_acquired.items(), key=lambda k_v: k_v[1]["Last_Name_KEY"]):
  #         # #print(" .... SORTED INSTANTIATED DICTIONARY  =  :  " + str(s) ) 
  #
  ######################################################################################################


      
#######################################################################################
#
# This Process__Dict_File Class reads in dictionary files (dict_file_) into a STRING
# and then converts STRING into a DICTIONARY and then processes the DICTIONARY
# and then converts the processed DICTIONARY to a STRING and writes out the
# processed dictionary file. 
#
# This Process_Dict_File Class and its read_target_dict_file method utilizes
# file read/write and CPU time resoures. Consequently, this Process_Dict_File
# Class and its read_target_dict_file method should be carefully utilized.
#
# Examples of the use of this Process_Dict_File Class and its
# read_target_dict_file method: 
#
#   1. WHEN A NEW CONTACT LIST IS SELECTED OR CREATED ...
#
#   2. WHEN THE SORT CONTACTS BUTTON IS PRESSED.
#
#   3. ON STARTUP TO SET THE FIRST CONTACT IS LOADED TO
#      THE cm_list and dict_file and the
#      selected dict GLOBAL NEEDS TO BE INITIALIZED.
#
#   4. WHEN CONTACT VIEW SCROLL SCREEN IS SELECTED
#      AS WE MAY ELECT TO SORT CONTACTS FIRST.
#
# This Process_Dict_File Class and its read_target_dict_file method is
# typically implemented with the following code to instantiate the
# Process__Dict_File Class that sorts and re-writes the contact list
# database as a dictionary of dictionaries:
#
# inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
# loaded_contact_dict_acquired_SETS_A_GLOBAL = inst_loaded_Process_Dict_File.read_target_dict_file()
#
# kick_thread_to_update_main_entry_widgets = True (to update main screen widgets)
#
#######################################################################################

class Process_Dict_File(object):
      def __init__(self, target_dict_file):
            global selected_dictionary_loaded_global
            global num_of_dictionary_data_records_global
            global selected_dictionary_record_index_global
            global master_cm_list_name_global
            self.target_dict_file = target_dict_file
            gfn = ''
            gln = ''
            gsa = ''
            gct = ''
            gst = ''
            gzc = ''
            gpn = ''
            gem = ''
            gws = ''
            contact_dict = {}


      ################################################################################
      #
      # Method to READ in the dict_file_ and PARSE to CREATE the
      # DICTIONARY OF DICTIONARIES - dict_of_dictionaries for selected Contact List
      # and then SORT the dict_of_dictionaries so the write_target_dict_file METHOD
      # can MAP from DICTIONARY OF DICTIONARIES to dict_file_ Format and
      # write the (eventually) newly SORTED dict_of_dictionaries to dict_file_
      #
      def read_target_dict_file(self):
              global selected_dictionary_loaded_global
              global num_of_dictionary_data_records_global
              global selected_dictionary_record_index_global
              # Read or Load DICTIONARY Contact List File - dict_file_cm_listbox_file_global
              # which is stored in APPDATA at fullpath_fn_dict_filename_global

              self.textFile = open(fullpath_fn_dict_filename_global, 'r')

              # This takes the file object opened with the open() and turns it into a string which 
              # you can now use textString in a text widget.
              self.textString = self.textFile.read()

              # Define dict_of_dictionaries and sorted_contact_dict
              dict_of_dictionaries = {}
              sorted_dict_of_dictionaries = {}
              sorted_d_of_d = {}
              get_dict_of_dicts_call = {}
              get_sorted_d_of_d_call = {}

              list_of_indexed_dictionaries = []
              new_sorted_list_of_indexed_dictionaries = []

              # Count the DATA RECORDS in the string by counting the
              # number of "DATA_RECORD_DELIMITER:" patterns 
              self.num_data_records = self.textString.count("DATA_RECORD_DELIMITER:")

              # Capture GLOBAL from the "DATA_RECORD_DELIMITER:" patterns Delimiters Counted.
              num_of_dictionary_data_records_global = self.num_data_records

              self.num_data_records_plus_one = self.num_data_records + 1
              # Operate on the textString to search for DATA_RECORD_DELIMITER: and KEY_SYNC: sub-strings  
              for record_index in range (1, self.num_data_records_plus_one):
                   d_of_d_index = record_index
                   self.data_record_string = self.textString.split("DATA_RECORD_DELIMITER:")[record_index]
                   for key_index in range (1, 10):
                         key_indexed_string = self.data_record_string.split("KEY_SYNC:")[key_index]
                         if key_index == 1: gfn = key_indexed_string
                         if key_index == 2: gln = key_indexed_string
                         if key_index == 3: gsa = key_indexed_string
                         if key_index == 4: gct = key_indexed_string
                         if key_index == 5: gst = key_indexed_string
                         if key_index == 6: gzc = key_indexed_string
                         if key_index == 7: gpn = key_indexed_string
                         if key_index == 8: gem = key_indexed_string
                         if key_index == 9: gws = key_indexed_string



                   # Since Dictionaries are immutable (cannot be changed), we could create a LIST
                   # and then SORT that list, and then RE-WRITE the dict_file_ and contact_list_ file
                   # FORMATS from the SORTED LIST, however, we have currently implemented sorting by
                   # creating a couple DICTIONARY of DICTIONARYIES to facilitate SORT Functionality ... 

                   
                   # Create DICTIONARY to store contact data 
                   contact_dict = {"First_Name_KEY": str(gfn), "Last_Name_KEY": str(gln), "Street_Address_KEY": str(gsa), \
                                   "City_Town_KEY": str(gct), "State_KEY": str(gst), "Zip_Code_KEY": str(gzc), \
                                   "Phone_Number_KEY": str(gpn), "EMail_KEY": str(gem), "Website_KEY": str(gws) }


                   # Create the {DICT_KEY: DICT_NUMBER_1} ... {DICT_KEY: DICT_NUMBER_#_of_Records} to build new NESTED dictionary
                   Dict_Key_String = "Dict_KEY" + str(record_index)

                   # dict[key] = value

                   # Define dict_of_dictionaries[str(Dict_Key_String)]
                   # and define sorted_dict_of_dictionaries[str(Dict_Key_String)]
                   dict_of_dictionaries[str(Dict_Key_String)] = {}
                   sorted_dict_of_dictionaries[str(Dict_Key_String)] = {}

                   dict_of_dictionaries[str(Dict_Key_String)]["First_Name_KEY"] = str(gfn)
                   dict_of_dictionaries[str(Dict_Key_String)]["Last_Name_KEY"] = str(gln)
                   dict_of_dictionaries[str(Dict_Key_String)]["Street_Address_KEY"] = str(gsa)
                   dict_of_dictionaries[str(Dict_Key_String)]["City_Town_KEY"] = str(gct)
                   dict_of_dictionaries[str(Dict_Key_String)]["State_KEY"] = str(gst)
                   dict_of_dictionaries[str(Dict_Key_String)]["Zip_Code_KEY"] = str(gzc)
                   dict_of_dictionaries[str(Dict_Key_String)]["Phone_Number_KEY"] = str(gpn)
                   dict_of_dictionaries[str(Dict_Key_String)]["EMail_KEY"] = str(gem)
                   dict_of_dictionaries[str(Dict_Key_String)]["Website_KEY"] = str(gws)


              # dict[key] = value             

              # Store dict_of_dictionaries to Store_dictionary_of_dictionaries Class  
              dict_of_contact_dicts_inst = Store_dictionary_of_dictionaries(this_dict_of_dicts = dict_of_dictionaries)
              dict_of_contact_dicts_inst.set_dict_of_dicts(new_this_dict_of_dicts = dict_of_dictionaries)
              get_dict_of_dicts_call = dict_of_contact_dicts_inst.get_dict_of_dicts()


              SORTED_SEQ_NUMBER = 1
              for s in sorted(dict_of_dictionaries.items(), key=lambda k_v: k_v[1]["Last_Name_KEY"]):

                    select_tuple_one = str(s[1])
                    split_on_Street_Address_KEY = select_tuple_one.split("', 'Street_Address_KEY':")[0]
                    split_on_Last_Name_KEY = split_on_Street_Address_KEY.split("'Last_Name_KEY': '")[1]
                     
                    split_on_Last_Name_KEY = select_tuple_one.split("', 'Last_Name_KEY':")[0]
                    split_on_First_Name_KEY = split_on_Last_Name_KEY.split("{'First_Name_KEY': '")[1]

                    select_tuple_zero = str(s[0])
                    split_on_dict_KEY = select_tuple_zero.split("Dict_KEY")[1]

                    old_sorted_dict_KEY_String = "Dict_KEY" + str(split_on_dict_KEY)
                    
                    new_sorted_dict_KEY_String = "Dict_KEY" + str(SORTED_SEQ_NUMBER)

                    sorted_dict_of_dictionaries[str(new_sorted_dict_KEY_String)] = get_dict_of_dicts_call[str(old_sorted_dict_KEY_String)]

                    SORTED_SEQ_NUMBER += 1
 
              ########################################################################

              # Store NEW SORTED sorted_dict_of_dictionaries to Store_dictionary_of_dictionaries Class  
              sorted_d_of_d_inst = Store_dictionary_of_dictionaries(this_dict_of_dicts = sorted_dict_of_dictionaries)
              sorted_d_of_d_inst.set_dict_of_dicts(new_this_dict_of_dicts = sorted_dict_of_dictionaries)
              get_sorted_d_of_d_call = sorted_d_of_d_inst.get_dict_of_dicts()

              ######################################################################## 
              
              # RE-Create the new Contact List File and add Titles 
              with open(fullpath_fn_cm_listbox_file_global, 'w') as wf_titles:
                   wf_titles.flush()
                   wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "\n")


        
              # RE-Create and Open the File for Contact DICTIONARY Filename dict_filename_global
              with open(fullpath_fn_dict_filename_global, 'w') as new_wdictf:
                   new_wdictf.flush()
                   new_wdictf.write("\n")
                    

              for record_index in range (1, self.num_data_records_plus_one):
              
                   ######################################################################### 

                   sdfn = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["First_Name_KEY"] )
                   sdln = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Last_Name_KEY"] )
                   sdsa = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Street_Address_KEY"] )
                   sdct = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["City_Town_KEY"] )
                   sdst = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["State_KEY"] )
                   sdzc = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Zip_Code_KEY"] )
                   sdpn = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Phone_Number_KEY"] )
                   sdem = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["EMail_KEY"] )
                   sdws = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Website_KEY"] )

                   # write sorted data records to cm_list_file
                   # Note that we use the FULLPATH - fullpath_fn_cm_listbox_file_global
            
                   with open(fullpath_fn_cm_listbox_file_global, 'a') as wf:
                        for x in range(0, 10):
                             if x == 0: wf.flush()
                             #--------------------------------------------------------
                             if x == 1: wf.write(sdfn + ",")
                             elif x == 2: wf.write(sdln + ",")
                             elif x == 3: wf.write(sdsa + ",")
                             elif x == 4: wf.write(sdct + ",")
                             elif x == 5: wf.write(sdst + ",")
                             elif x == 6: wf.write(sdzc + ",")
                             elif x == 7: wf.write(sdpn + ",")
                             elif x == 8: wf.write(sdem + ",")
                             elif x == 9: wf.write(sdws + "\n")
                             else: pass

                   ########################################################################### 

                   # Write sorted contact data dictionary to dict_filename file from class method get_contact_dict_call
                   # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
                   with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                        for x in range(0, 10):
                             if x == 0:
                                   wdictf.flush()
                                   wdictf.write("DATA_RECORD_DELIMITER:")
                             elif x == 1: wdictf.write("KEY_SYNC:" + sdfn )
                             elif x == 2: wdictf.write("KEY_SYNC:" + sdln )
                             elif x == 3: wdictf.write("KEY_SYNC:" + sdsa )
                             elif x == 4: wdictf.write("KEY_SYNC:" + sdct )
                             elif x == 5: wdictf.write("KEY_SYNC:" + sdst )
                             elif x == 6: wdictf.write("KEY_SYNC:" + sdzc )
                             elif x == 7: wdictf.write("KEY_SYNC:" + sdpn )
                             elif x == 8: wdictf.write("KEY_SYNC:" + sdem )
                             elif x == 9: wdictf.write("KEY_SYNC:" + sdws )
                             else: pass

            ####################################################################################### 

              # Set the selected_loaded_dictionary_global GLOBAL to make this current
              # Store_dictionary_of_dictionaries Object available Globally.
              # 
              selected_dictionary_loaded_global = get_sorted_d_of_d_call                         
            
              return get_sorted_d_of_d_call    # dict_of_dictionaries





#####################################################################
#
#  Input:   contact_dict_of_dict_object   and  contact_list_name
#
#  Output:  fullpath_fn_dict_filename_global
#
#####################################################################
class Write_Dict_File(object):
      def __init__(self, contact_dict_of_dict_object, contact_list_name):
            global selected_dictionary_loaded_global
            global num_of_dictionary_data_records_global
            global fullpath_fn_dict_filename_global
            self.contact_dict_of_dict_object = contact_dict_of_dict_object
            self.contact_list_name = contact_list_name 
            gfn = ''
            gln = ''
            gsa = ''
            gct = ''
            gst = ''
            gzc = ''
            gpn = ''
            gem = ''
            gws = ''
            contact_dict = {}


#####################################################################
#
#  Input:   contact_dict_of_dict_object   and  contact_list_name
#
#  Output:  fullpath_fn_dict_filename_global   
#
#####################################################################

#123456
      #
      def write_target_dict_file(self):
              global selected_dictionary_loaded_global
              global num_of_dictionary_data_records_global
              global fullpath_fn_dict_filename_global

              dict_filename = "dict_file_" + str(self.contact_list_name) + ".txt"

              # This is the path we will write the new dict_ file to.
              dict_filename_fullpath = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename) )

              # Set the DICT File GLOBAL 
              fullpath_fn_dict_filename_global = str(dict_filename_fullpath)

              # print("  ")

              # print(".... dict_filename_fullpath = " + str(dict_filename_fullpath) )

              test_len_dict = len(self.contact_dict_of_dict_object)

              # print("....  test_len_dict = " + str(test_len_dict) )
              
              # print("  ")
              
              # Count the DATA RECORDS in the DICTIONARY ......
              self.num_data_records = int(test_len_dict)

              # Capture GLOBAL from the "DATA_RECORD_DELIMITER:" patterns Delimiters Counted.
              num_of_dictionary_data_records_global = self.num_data_records

              self.num_data_records_plus_one = self.num_data_records + 1

              # dict[key] = value             

              # Store dict_of_dictionaries to Store_dictionary_of_dictionaries Class  
              dict_of_contact_dicts_inst = Store_dictionary_of_dictionaries(this_dict_of_dicts = self.contact_dict_of_dict_object)
              dict_of_contact_dicts_inst.set_dict_of_dicts(new_this_dict_of_dicts = self.contact_dict_of_dict_object)
              get_dict_of_dicts_call = dict_of_contact_dicts_inst.get_dict_of_dicts()

  
              # Create the new Contact List File and add Titles 
              with open(fullpath_fn_cm_listbox_file_global, 'w') as wf_titles:
                   wf_titles.flush()
                   wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "\n")


        
              # RE-Create and Open the File for Contact DICTIONARY Filename dict_filename_global
              with open(fullpath_fn_dict_filename_global, 'w') as new_wdictf:
                   new_wdictf.flush()
                   new_wdictf.write("\n")
                    

              for record_index in range (1, self.num_data_records_plus_one):
              
                   ######################################################################### 

                   sdfn = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["First_Name_KEY"] )
                   sdln = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["Last_Name_KEY"] )
                   sdsa = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["Street_Address_KEY"] )
                   sdct = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["City_Town_KEY"] )
                   sdst = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["State_KEY"] )
                   sdzc = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["Zip_Code_KEY"] )
                   sdpn = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["Phone_Number_KEY"] )
                   sdem = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["EMail_KEY"] )
                   sdws = str(get_dict_of_dicts_call["Dict_KEY" + str(record_index)]["Website_KEY"] )

                   # write sorted data records to cm_list_file
                   # Note that we use the FULLPATH - fullpath_fn_cm_listbox_file_global
            
                   with open(fullpath_fn_cm_listbox_file_global, 'a') as wf:
                        for x in range(0, 10):
                             if x == 0: wf.flush()
                             #--------------------------------------------------------
                             if x == 1: wf.write(sdfn + ",")
                             elif x == 2: wf.write(sdln + ",")
                             elif x == 3: wf.write(sdsa + ",")
                             elif x == 4: wf.write(sdct + ",")
                             elif x == 5: wf.write(sdst + ",")
                             elif x == 6: wf.write(sdzc + ",")
                             elif x == 7: wf.write(sdpn + ",")
                             elif x == 8: wf.write(sdem + ",")
                             elif x == 9: wf.write(sdws + "\n")
                             else: pass

                   ########################################################################### 

                   # Write sorted contact data dictionary to dict_filename file from class method get_contact_dict_call
                   # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
                   with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                        for x in range(0, 10):
                             if x == 0:
                                   wdictf.flush()
                                   wdictf.write("DATA_RECORD_DELIMITER:")
                             elif x == 1: wdictf.write("KEY_SYNC:" + sdfn )
                             elif x == 2: wdictf.write("KEY_SYNC:" + sdln )
                             elif x == 3: wdictf.write("KEY_SYNC:" + sdsa )
                             elif x == 4: wdictf.write("KEY_SYNC:" + sdct )
                             elif x == 5: wdictf.write("KEY_SYNC:" + sdst )
                             elif x == 6: wdictf.write("KEY_SYNC:" + sdzc )
                             elif x == 7: wdictf.write("KEY_SYNC:" + sdpn )
                             elif x == 8: wdictf.write("KEY_SYNC:" + sdem )
                             elif x == 9: wdictf.write("KEY_SYNC:" + sdws )
                             else: pass

            ####################################################################################### 

              # Set the selected_loaded_dictionary_global GLOBAL to make this current
              # Store_dictionary_of_dictionaries Object available Globally.
              # 
              selected_dictionary_loaded_global = get_dict_of_dicts_call                        
            
              return fullpath_fn_dict_filename_global
 



#######################################################################################
#
# class Compute_Valid_Client_Secret_JSON_Status.
#
# Sets a Global that feeds the Status Panel.
#  
#######################################################################################

class Compute_Valid_Client_Secret_JSON_Status(object):
      global valid_client_secret_key_format_global

      def validate_client_secret_json(self):
          global valid_client_secret_key_format_global

          ################################################################################################
          #
          #  VALIDATE JSON FILE EXISTANCE AND REQUIRED FILE CONTENTS .....
          #
          #  THEN, SET CORRESPONDING STATUS PANEL BUTTON.
          #
          ################################################################################################
          #
          #  {
          #    "installed": {
          #      "client_id": "837647042410-75ifg...usercontent.com",
          #      "client_secret":"asdlkfjaskd",
          #      "redirect_uris": ["http://localhost", "urn:ietf:wg:oauth:2.0:oob"],
          #      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
          #      "token_uri": "https://accounts.google.com/o/oauth2/token"
          #            }
          #  }
          #
          ################################################################################################
          #
          # Verify that a Valid JSON File -  - exists at path:   
          # by executing the following sequence:
          #
          # 1. Check for existance of the client_secrets.json JSON File at the .credentials direcory:
          #
          #    PATH OF client_secret.json in the .credentials directory: client_secret_path_global.
          #
          #    Check for existance of the client_secret.json file using os.path.isfile(path).
          #
          # 2. Read the expected client_secrets.json JSON File into a TEXT STRING VARIABLE.
          #
          #
          # 3. Use the .count method to verify each required KEY in the client_secret.json JSON File.
          #
          #    See above for the "installed application" client_secret.json format.
          #
          #    client_secret_key_count_client_id = self.client_secret_textString.count("client_id")
          #
          #    client_secret_key_count_client_secret = self.client_secret_textString.count("client_secret")
          #
          #    client_secret_key_count_redirect_uris = self.client_secret_textString.count("redirect_uris")
          #
          #    client_secret_key_count_auth_uri = self.client_secret_textString.count("auth_uri")
          #
          #    client_secret_key_count_token_uri = self.client_secret_textString.count("token_uri")
          #
          # 
          # 4. If all the required KEYs are in the client_secret.json JSON File set a GLOBAL to True.
          #
          # 5. The Status Panel while loop with use this VERIFY JSON FILE GLOBAL to
          #    set the VERIFY JSON FILE Status Button Color to GREEN. 
          #
          #################################################################################################
          
          valid_client_secret_key_format_global = None

          try:

              if not os.path.isfile(client_secret_path_global):
                  raise Exception("client_secret_FILE_NOT_FOUND")

          except Exception:
              exc_type, exc_value, exc_traceback = sys.exc_info()
              lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
              exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

              valid_client_secret_key_format_global = False

              # open Write_Exception_Logfile() to append logfile to update the logfile items.
              inst_Write_Exception_Logfile_client_secret_keys_validation = Write_Exception_Logfile()
              exception_logging_string_1 = "  *** OAUTH2 client_secret.json FILE NOT FOUND ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"

              exception_logging_string_3 = "\n\n"

              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_1) )
              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_2) )
              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_3) )

          try:

              client_secret_textFile = open(client_secret_path_global, 'r')

              client_secret_textString = client_secret_textFile.read()

          except Exception:
              exc_type, exc_value, exc_traceback = sys.exc_info()
              lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
              exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

              valid_client_secret_key_format_global = False

              # open Write_Exception_Logfile() to append logfile to update the logfile items.
              inst_Write_Exception_Logfile_client_secret_keys_validation = Write_Exception_Logfile()
              exception_logging_string_1 = "  *** OAUTH2 client_secret.json FILE NOT FOUND ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
              exception_logging_string_3 = "\n\n"

              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_1) )
              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_2) )
              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_3) )


          client_secret_key_validation_counter = 0

          if os.path.isfile(client_secret_path_global) == True:

              if "client_id" in client_secret_textString:
                  if "client_secret" in client_secret_textString:
                      if "redirect_uris" in client_secret_textString:
                          if "auth_uri" in client_secret_textString:
                              if "token_uri" in client_secret_textString:
                                  all_client_secret_json_keys_found = True


              client_secret_key_count_client_id = client_secret_textString.count("client_id")
              if client_secret_key_count_client_id == 1:
                  client_secret_key_validation_counter+=1


              client_secret_key_count_client_secret = client_secret_textString.count("client_secret")
              if client_secret_key_count_client_secret == 1:
                  client_secret_key_validation_counter+=1


              client_secret_key_count_redirect_uris = client_secret_textString.count("redirect_uris")
              if client_secret_key_count_redirect_uris == 1:
                  client_secret_key_validation_counter+=1


              client_secret_key_count_auth_uri = client_secret_textString.count("auth_uri")
              if client_secret_key_count_auth_uri == 1:
                  client_secret_key_validation_counter+=1


              client_secret_key_count_token_uri = client_secret_textString.count("token_uri")
              if client_secret_key_count_token_uri == 1:
                  client_secret_key_validation_counter+=1


              try:

                  if not ( (all_client_secret_json_keys_found) and (client_secret_key_validation_counter == 5) ):
                      raise Exception("JSON KEY VALIDATION ERROR")
                  elif ( (all_client_secret_json_keys_found) and (client_secret_key_validation_counter == 5) ):
                      valid_client_secret_key_format_global = True

              except Exception:
                  # add exception system variable acquisition code here for logging ....
                  # set STATUS GLOBAL for JSON FILE KEY VALIDATION ERROR
                  exc_type, exc_value, exc_traceback = sys.exc_info()
                  lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                  exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

                  valid_client_secret_key_format_global = False

                  # open Write_Exception_Logfile() to append logfile to update the logfile items.
                  inst_Write_Exception_Logfile_client_secret_keys_validation = Write_Exception_Logfile()
                  exception_logging_string_1 = "  *** ERROR *** INVALID client_secret.json FILE FORMAT ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
                  exception_logging_string_3 = "\n\n"

                  inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_1) )
                  inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_2) )
                  inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_3) )

              
          
            

#######################################################################################
#
# class Write_Exception_Logfile logs Exceptions during the application execution.  
#  
#######################################################################################

class Write_Exception_Logfile(object):

      def write_update_exception_logfile(self):
            with open(str(fullpath_exception_logfile_global), 'a') as exception_logfile:
                  exception_logfile.write("\n_____________________________________________________________________________\n")
                  exception_logfile.write("\n") 
                  exception_logfile.write("....   P Y T H O N    E X C E P T I O N S    L O G F I L E   ....")
                  exception_logfile.write("\n")
                  exception_logfile.write("\n_____________________________________________________________________________\n")
                  exception_logfile.write("\n" + ".... Contact  Management  Workstation  Enterprise  Cloud  Software  Application: *** Version 14.2 ***")
                  exception_logfile.write("\n" + ".... Date : Time :  " + str(datetime.datetime.now() ) )
                  exception_logfile.write("\n_____________________________________________________________________________\n")
                  exception_logfile.write("\n") 
                  


      def log_exception(self, exception_info_string):
          # Create a Time Stamp and then execute logging the exception_info_string
          time_stamp_string = str(datetime.datetime.now() )
          exception_logging_time_stamp_string = "\n" + "T I M E   S T A M P  :  " + str(time_stamp_string) + "\n"
          with open(str(fullpath_exception_logfile_global), 'a') as exception_logfile:
              exception_logfile.write(str(exception_logging_time_stamp_string) )
              exception_logfile.write(str(exception_info_string) )

              # logger.error(str(exception_logging_string), exc_info=True)
                  


            
#######################################################################################
#   
# class Write_Main_Logfile writes a new logfile replacing the previous logfile.  
#  
#######################################################################################

class Write_Main_Logfile(object):

      def write_update_logfile(self):
            with open(str(fullpath_fn_cm_sw_app_logfile_global), 'w') as cmlogfile:
                  cmlogfile.write(".... (Python) System.Version = " + str(sys.version) )
                  cmlogfile.write("\n" + ".... (tkinter Tcl) System.Version = " + str(tk.TclVersion) )
                  cmlogfile.write("\n" + ".... (tkinter Tk) System.Version = " + str(tk.TkVersion) )
                  cmlogfile.write("\n" + ".... (Windows) sys.platform = " + str(sys.platform) )
                  cmlogfile.write("\n" + ".... (Windows) platform.system = " + str(platform.system() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.machine = " + str(platform.machine() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.platform = " + str(platform.platform() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.version = " + str(platform.version() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.processor = " + str(platform.processor() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.node = " + str(platform.node() ) )
                  cmlogfile.write("\n" + ".... (Windows) IPv4 Address = " + str(ipv4_address_global) )
                  cmlogfile.write("\n_____________________________________________________________________________\n")
                  cmlogfile.write("\n" + ".... Contact  Management  Workstation  Enterprise  Cloud  Software  Application: *** Version 14.2 ***")
                  cmlogfile.write("\n" + ".... Date : Time :  " + str(datetime.datetime.now() ) )
                  cmlogfile.write("\n_____________________________________________________________________________\n")
                  cmlogfile.write("\n.... USERNAME = " + str(username_global) )
                  cmlogfile.write("\n.... USER HOME PATH = " + str(userprofile_global) )
                  cmlogfile.write("\n.... APPDATA PATH = " + str(appdata_path_global) )
                  cmlogfile.write("\n.... **********************   D_A_T_A_B_A_S_E___F_I_L_E_S    ********************")
                  cmlogfile.write("\n.... APP CONFIG INI FILE PATH = " + str(fullpath_app_config_ini_global) )
                  cmlogfile.write("\n.... MEDICAL RECORD FILE PATH = " + str(fullpath_med_config_ini_global) )
                  cmlogfile.write("\n.... EXCEPTION LOGFILE PATH = " + str(fullpath_exception_logfile_global) )
                  cmlogfile.write("\n.... CONTACT MANAGEMENT DATA PATH = " + str(cm_appdatafiles_path_global) )
                  cmlogfile.write("\n.... CSV FILENAME = " + str(fullpath_fn_cm_listbox_file_global) )
                  cmlogfile.write("\n.... DICTIONARY FILENAME = " + str(fullpath_fn_dict_filename_global) )
                  cmlogfile.write("\n.... NOTES DICT FILENAME = " + str(fullpath_cnotes_dict_file_global) )
                  cmlogfile.write("\n.... GMAIL OAUTH2 CREDENTIALS = " + str(credential_home_path_global) )
                  cmlogfile.write("\n.... GMAIL OAUTH2 CLIENT SECRET = " + str(client_secret_path_global) )
                  cmlogfile.write("\n.... THIS LOGFILE PATH = " + str(fullpath_fn_cm_sw_app_logfile_global) )
                  cmlogfile.write("\n.... EXCEL OUTPUT PATH (AppData) = " + str(export_csv_excel_cm_appdata_global) )
                  cmlogfile.write("\n.... EXCEL OUTPUT PATH (UserProfile) = " + str(export_csv_excel_userprofile_global) )
                  cmlogfile.write("\n_____________________________________________________________________________\n")
                  cmlogfile.write("\n.... mainscreen background color = " + str(mainscreen_bg_color_val_global) + \
                                  "     .... viewcreen background color = " + str(viewscreen_bg_color_val_global) )
                  cmlogfile.write("\n.... selectlist background color = " + str(selectlist_bg_color_val_global) + \
                                  "     .... newlist background color = " + str(newlist_bg_color_val_global) )
                  cmlogfile.write("\n.... usermanual background color = " + str(usermanual_bg_color_val_global) + \
                                  "     .... config background color = " + str(config_bg_color_val_global) )




def main():
      global hostname_via_socket
      global ip_address_via_socket
      global fullpath_gmail_oauth2_credentials_global
      global fullpath_exception_logfile_global
      global client_secret_dir_global
      global client_secret_path_global
      global credential_home_path_global
      global credential_home_dir_global
      global credential_appdata_dir_global
      global credential_appdata_path_global
      global valid_client_secret_key_format_global
      global gmail_oauth2_exceptions_status_global
      global gmail_oauth2_SPECIFIC_EXCEPTION_global
      global request_mainscreen_config_update_global
      global kick_thread_to_update_main_entry_widgets
      global kick_thread_to_update_email_contact_entry_widgets
      global insert_first_contact_global
      global listbox_file_capture_global
      global cm_listbox_file_global
      global mode_select_global
      global mode_select_build_list_global
      global username_global
      global userprofile_global
      global appdata_path_global
      global cm_appdatafiles_path_global
      global mainscreen_bg_color_val_global
      global viewscreen_bg_color_val_global
      global selectlist_bg_color_val_global
      global newlist_bg_color_val_global
      global usermanual_bg_color_val_global
      global config_bg_color_val_global
      global mainscreen_fg_color_val_global
      global viewscreen_fg_color_val_global
      global selectlist_fg_color_val_global
      global newlist_fg_color_val_global
      global usermanual_fg_color_val_global
      global config_fg_color_val_global
      global app_config_ini_val_global
      global app_config_request_global
      global fullpath_app_config_ini_global
      global fullpath_med_config_ini_global
      global fullpath_fn_cm_sw_app_logfile_global
      global export_csv_excel_userprofile_global
      global export_csv_excel_cm_appdata_global
      global import_excel_csv_userprofile_global
      global import_excel_csv_cm_appdata_global
      global user_gui_title_value_global
      global user_gui_title_bg_color_value_global
      global user_gui_title_fg_color_value_global
      global user_gui_x_col_frames_value_global
      global user_gui_y_row_frames_value_global
      global user_gui_bg_color_value_global
      global user_gui_fg_color_value_global
      global user_gui_label_bg_color_value_global
      global user_gui_label_fg_color_value_global
      global user_gui_entry_bg_color_value_global
      global user_gui_entry_fg_color_value_global
      global user_gui_text_bg_color_value_global
      global user_gui_text_fg_color_value_global
      global group1_frame1_user_label
      global group1_frame1_status_text
      global group1_frame1_user_button
      global group1_frame2_user_label
      global group1_frame2_status_text
      global group1_frame2_user_button
      global group1_frame3_user_label
      global group1_frame3_status_text
      global group1_frame3_user_button
      global group1_frame4_user_label
      global group1_frame4_status_text
      global group1_frame4_user_button
      global group1_frame5_user_label
      global group1_frame5_status_text
      global group1_frame5_user_button
      global group1_frame6_user_label
      global group1_frame6_status_text
      global group1_frame6_user_button
      global group1_frame7_user_label
      global group1_frame7_status_text
      global group1_frame7_user_button
      global group1_frame8_user_label
      global group1_frame8_status_text
      global group1_frame8_user_button
      global group1_frame9_user_label
      global group1_frame9_status_text
      global group1_frame9_user_button
      global group1_frame10_user_label
      global group1_frame10_status_text
      global group1_frame10_user_button
      global group1_frame11_user_label
      global group1_frame11_status_text
      global group1_frame11_user_button
      global group1_frame12_user_label
      global group1_frame12_status_text
      global group1_frame12_user_button
      global group2_frame1_user_label
      global group2_frame1_status_text
      global group2_frame1_user_button
      global group2_frame2_user_label
      global group2_frame2_status_text
      global group2_frame2_user_button
      global group2_frame3_user_label
      global group2_frame3_status_text
      global group2_frame3_user_button
      global group2_frame4_user_label
      global group2_frame4_status_text
      global group2_frame4_user_button
      global group2_frame5_user_label
      global group2_frame5_status_text
      global group2_frame5_user_button
      global group2_frame6_user_label
      global group2_frame6_status_text
      global group2_frame6_user_button
      global group2_frame7_user_label
      global group2_frame7_status_text
      global group2_frame7_user_button
      global group2_frame8_user_label
      global group2_frame8_status_text
      global group2_frame8_user_button
      global group2_frame9_user_label
      global group2_frame9_status_text
      global group2_frame9_user_button
      global group2_frame10_user_label
      global group2_frame10_status_text
      global group2_frame10_user_button
      global group2_frame11_user_label
      global group2_frame11_status_text
      global group2_frame11_user_button
      global group2_frame12_user_label
      global group2_frame12_status_text
      global group2_frame12_user_button
      global group3_frame1_user_label
      global group3_frame1_status_text
      global group3_frame1_user_button
      global group3_frame2_user_label
      global group3_frame2_status_text
      global group3_frame2_user_button
      global group3_frame3_user_label
      global group3_frame3_status_text
      global group3_frame3_user_button
      global group3_frame4_user_label
      global group3_frame4_status_text
      global group3_frame4_user_button
      global group3_frame5_user_label
      global group3_frame5_status_text
      global group3_frame5_user_button
      global group3_frame6_user_label
      global group3_frame6_status_text
      global group3_frame6_user_button
      global group3_frame7_user_label
      global group3_frame7_status_text
      global group3_frame7_user_button
      global group3_frame8_user_label
      global group3_frame8_status_text
      global group3_frame8_user_button
      global group3_frame9_user_label
      global group3_frame9_status_text
      global group3_frame9_user_button
      global group3_frame10_user_label
      global group3_frame10_status_text
      global group3_frame10_user_button
      global group3_frame11_user_label
      global group3_frame11_status_text
      global group3_frame11_user_button
      global group3_frame12_user_label
      global group3_frame12_status_text
      global group3_frame12_user_button
      global instance_object_LIST
      global instance_object_winfo_id_LIST
      global instance_object_winfo_parent_LIST
      global ipv4_address_global
      global contact_lists_dict_count
      global contact_lists_csv_count
      
######################################################################

######################################################################
#
# get ip address ... similar to windows command line: ipconfig
# 
# import socket 
# 
# hostname_via_socket = socket.gethostname()
# 
# ip_address_via_socket = socket.gethostbyname(socket.getfqdn())
# 
# https://www.youtube.com/watch?v=h-drFf4oU24
# 
#####################################################################

      # print(" ")

      try:
          hostname_via_socket = socket.gethostname()
          ipv4_address_global = socket.gethostbyname(socket.getfqdn())
          ##print("....  hostname_via_socket = " + str(hostname_via_socket) )
          ##print("....  ipv4_address_global = " + str(ipv4_address_global) )
      except Exception:
          pass

####################################################################
# 
# https://en.wikipedia.org/wiki/Netstat
#
# List of ipv6 Ports:  netstat -help
#
####################################################################


################################################################################################# 

      username_global = str(os.environ['USERNAME'])

      print("..... username_global:  " + str(username_global) )

      userprofile_global = str(os.environ['USERPROFILE'])

      print("..... userprofile_global:  " + str(userprofile_global) )

      appdata_path_global = str(os.environ['APPDATA'])

      print("..... appdata_path_global:  " + str(appdata_path_global) )

      cm_appdatafiles_path_global = os.path.join(str(appdata_path_global), "CONTACT_MANAGEMENT", str(username_global) )

      print("..... cm_appdatafiles_path_global:  " + str(cm_appdatafiles_path_global) )

      # add mkdirs here ... for cm_appdatafiles_path_global ... NOTE: this is a Version 14.2 update

      if not os.path.exists(cm_appdatafiles_path_global):
          os.makedirs(cm_appdatafiles_path_global)

      fullpath_fn_cm_sw_app_logfile_global = os.path.join(str(cm_appdatafiles_path_global), "cm_sw_app_logfile.txt" )

      fullpath_exception_logfile_global = os.path.join(str(cm_appdatafiles_path_global), "cm_app_exception_logfile.txt" )

      print("..... fullpath_exception_logfile_global:  " + str(fullpath_exception_logfile_global) )

      # start a new logfile for exceptions logging - this writes over file from previous session.
      with open(str(fullpath_exception_logfile_global), 'w') as exception_logfile_startup_new_file:
          exception_logfile_startup_new_file.write("\n\n")

      # write (append) the header for the exceptions logfile
      # that was created above - this is done once at program startup
      inst_Write_Exception_Logfile_Header_at_startup = Write_Exception_Logfile()
      inst_Write_Exception_Logfile_Header_at_startup.write_update_exception_logfile()

      fullpath_gmail_oauth2_credentials_global = os.path.join(str(cm_appdatafiles_path_global), ".credentials", 'gmail-python-quickstart.json')

      # GMAIL API OAUTH2 CLIENT CREDENTIALS .......  
      #
      # ESTABLISH client_secret.json file store paths (directories / folders) and set associated globals

      ##############################################################################
      #  
      # If modifying these scopes, delete your previously saved credentials
      # at ~/.credentials/gmail-python-quickstart.json
      #
      # SCOPES = "https://mail.google.com"
      # CLIENT_SECRET_FILE = 'client_secret.json'
      # APPLICATION_NAME = 'Gmail API Python Quickstart'
      #
      ##############################################################################

      # we create credentials here because we want to also maintain a copy of the credentials in APPDATA area.
      credential_appdata_dir = os.path.join(str(cm_appdatafiles_path_global), ".credentials")
      credential_appdata_dir_global = os.path.join(str(cm_appdatafiles_path_global), ".credentials")
      if not os.path.exists(credential_appdata_dir):
            os.makedirs(credential_appdata_dir)

      credential_appdata_path = os.path.join(credential_appdata_dir, 'gmail-python-quickstart.json')
      credential_appdata_path_global = os.path.join(credential_appdata_dir, 'gmail-python-quickstart.json')
      
      # we create credentials here because the http routine looks for them here. 
      home_dir = userprofile_global 
      client_secret_dir = os.path.join(home_dir, '.credentials')
      client_secret_dir_global = os.path.join(home_dir, '.credentials')
      credential_home_dir = os.path.join(home_dir, '.credentials')
      credential_home_dir_global = os.path.join(home_dir, '.credentials')
      if not os.path.exists(credential_home_dir):
            os.makedirs(credential_home_dir)

      credential_home_path = os.path.join(credential_home_dir, 'gmail-python-quickstart.json')
      credential_home_path_global = os.path.join(credential_home_dir, 'gmail-python-quickstart.json')
      client_secret_path = os.path.join(credential_home_dir, 'client_secret.json')
      client_secret_path_global = os.path.join(credential_home_dir, 'client_secret.json')

      ################################################################################################
      #
      #  VALIDATE JSON FILE EXISTANCE AND REQUIRED FILE CONTENTS .....
      #
      #  THEN, SET CORRESPONDING STATUS PANEL BUTTON.
      #
      ################################################################################################
      #
      #  {
      #    "installed": {
      #      "client_id": "837647042410-75ifg...usercontent.com",
      #      "client_secret":"asdlkfjaskd",
      #      "redirect_uris": ["http://localhost", "urn:ietf:wg:oauth:2.0:oob"],
      #      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      #      "token_uri": "https://accounts.google.com/o/oauth2/token"
      #            }
      #  }
      #
      ################################################################################################
      #
      # Verify that a Valid JSON File -  - exists at path:   
      # by executing the following sequence:
      #
      # 1. Check for existance of the client_secrets.json JSON File at the .credentials direcory:
      #
      #    PATH OF client_secret.json in the .credentials directory: client_secret_path_global.
      #
      #    Check for existance of the client_secret.json file using os.path.isfile(path).
      #
      # 2. Read the expected client_secrets.json JSON File into a TEXT STRING VARIABLE.
      #
      #
      # 3. Use the .count method to verify each required KEY in the client_secret.json JSON File.
      #
      #    See above for the "installed application" client_secret.json format.
      #
      #    client_secret_key_count_client_id = self.client_secret_textString.count("client_id")
      #
      #    client_secret_key_count_client_secret = self.client_secret_textString.count("client_secret")
      #
      #    client_secret_key_count_redirect_uris = self.client_secret_textString.count("redirect_uris")
      #
      #    client_secret_key_count_auth_uri = self.client_secret_textString.count("auth_uri")
      #
      #    client_secret_key_count_token_uri = self.client_secret_textString.count("token_uri")
      #
      # 
      # 4. If all the required KEYs are in the client_secret.json JSON File set a GLOBAL to True.
      #
      # 5. The Status Panel while loop with use this VERIFY JSON FILE GLOBAL to
      #    set the VERIFY JSON FILE Status Button Color to GREEN. 
      #
      #################################################################################################

      valid_client_secret_key_format_global = None

      try:

          if not os.path.isfile(client_secret_path_global):
              raise Exception("client_secret_FILE_NOT_FOUND")

      except Exception:
          exc_type, exc_value, exc_traceback = sys.exc_info()
          lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
          exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

          valid_client_secret_key_format_global = False
                    
          # open Write_Exception_Logfile() to append logfile to update the logfile items.
          inst_Write_Exception_Logfile_client_secret_keys_validation = Write_Exception_Logfile()
          exception_logging_string_1 = "  *** OAUTH2 client_secret.json FILE NOT FOUND ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
          
          exception_logging_string_3 = "\n\n"
                    
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_1) )
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_2) )
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_3) )


      try:
              
          client_secret_textFile = open(client_secret_path_global, 'r')

          client_secret_textString = client_secret_textFile.read()

      except Exception:
          exc_type, exc_value, exc_traceback = sys.exc_info()
          lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
          exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

          valid_client_secret_key_format_global = False
                    
          # open Write_Exception_Logfile() to append logfile to update the logfile items.
          inst_Write_Exception_Logfile_client_secret_keys_validation = Write_Exception_Logfile()
          exception_logging_string_1 = "  *** OAUTH2 client_secret.json FILE NOT FOUND ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
          exception_logging_string_3 = "\n\n"
                    
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_1) )
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_2) )
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_3) )

          
      client_secret_key_validation_counter = 0

      if os.path.isfile(client_secret_path_global) == True:

          if "client_id" in client_secret_textString:
              if "client_secret" in client_secret_textString:
                  if "redirect_uris" in client_secret_textString:
                      if "auth_uri" in client_secret_textString:
                          if "token_uri" in client_secret_textString:
                              all_client_secret_json_keys_found = True
              
              
          client_secret_key_count_client_id = client_secret_textString.count("client_id")
          if client_secret_key_count_client_id == 1:
              client_secret_key_validation_counter+=1
              

          client_secret_key_count_client_secret = client_secret_textString.count("client_secret")
          if client_secret_key_count_client_secret == 1:
              client_secret_key_validation_counter+=1
              

          client_secret_key_count_redirect_uris = client_secret_textString.count("redirect_uris")
          if client_secret_key_count_redirect_uris == 1:
              client_secret_key_validation_counter+=1
              

          client_secret_key_count_auth_uri = client_secret_textString.count("auth_uri")
          if client_secret_key_count_auth_uri == 1:
              client_secret_key_validation_counter+=1
              

          client_secret_key_count_token_uri = client_secret_textString.count("token_uri")
          if client_secret_key_count_token_uri == 1:
              client_secret_key_validation_counter+=1
              

          try:

              if not ( (all_client_secret_json_keys_found) and (client_secret_key_validation_counter == 5) ):
                  raise Exception("JSON KEY VALIDATION ERROR")
              elif ( (all_client_secret_json_keys_found) and (client_secret_key_validation_counter == 5) ):
                  valid_client_secret_key_format_global = True

          except Exception:
              exc_type, exc_value, exc_traceback = sys.exc_info()
              lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
              exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

              valid_client_secret_key_format_global = False

              # open Write_Exception_Logfile() to append logfile to update the logfile items.
              inst_Write_Exception_Logfile_client_secret_keys_validation = Write_Exception_Logfile()
              exception_logging_string_1 = "  *** ERROR *** INVALID client_secret.json FILE FORMAT ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
              exception_logging_string_3 = "\n\n"

              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_1) )
              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_2) )
              inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_3) )

          
      ################################################################################################
      #
      # NOTE:    
      #
      # If modifying these scopes, delete your previously saved credentials
      # at ~/.credentials/gmail-python-quickstart.json
      #
      # SCOPES = "https://mail.google.com"
      # CLIENT_SECRET_FILE = client_secret_path
      # APPLICATION_NAME = 'Gmail API Python Quickstart'
      #
      ################################################################################################
      #
      # Try to Copy CM-APP-CLIENT JSON FILE TO APPDATA .credentials AREA - cm_appdatafiles_path_global
      #
      try:
          shutil.copyfile(str(credential_home_path_global), str(credential_appdata_path_global) )

      except:
          pass

      ################################################################################################
      #
      #  Count the Dictionary and CSV Database Files for the Status Panel GLOBALS:
      #
      #  contact_lists_dict_count (dict_file)      contact_lists_csv_count (cm_list)
      #
      #  e.g.  import glob  
      #
      #        tifCounter = len(glob.glob1(myPath,"*.tif"))
      #
      ################################################################################################

      contact_lists_dict_count = len(glob.glob1(str(cm_appdatafiles_path_global),"dict_file_*"))

      contact_lists_csv_count = len(glob.glob1(str(cm_appdatafiles_path_global),"cm_list_*"))

      ## print(".... contact_lists_dict_count = " + str(contact_lists_dict_count) )
      ## print(".... contact_lists_csv_count = " + str(contact_lists_csv_count) )

      ####################################################################################################
      #
      # Begin app_config.ini processing and medical_record_config.ini path definition upon startup .....
      #
      ####################################################################################################

      fullpath_app_config_ini_global = os.path.join(str(cm_appdatafiles_path_global), "app_config.ini" )

      fullpath_med_config_ini_global = os.path.join(str(cm_appdatafiles_path_global), "medical_record_config.ini" )

      # Note:  str(master_cm_list_name_global) - When Contact List Selected.

      # instantiate ConfigParser() 
      config = ConfigParser()

      #
      # IF the app_config.ini file DOES NOT EXIST, Create-Initialize-Write app_config.ini file to CONFIGURE APP SETTINGS
      #     
      # #print("\n") 
      # #print(".... IF app_config.ini file DOES NOT EXIST, Create-Initialize-Write app_config.ini file to CONFIGURE APP SETTINGS")
      # #print("\n")
      # add app_config.ini file section(s) and some default values 
      # to create an app_config.ini file 
      if os.path.isfile(fullpath_app_config_ini_global) == False:
            config.add_section("MAIN_SCREEN_COLOR")
            config.set("MAIN_SCREEN_COLOR", "mainscreen_bg_color_val", "dark slate gray")
            config.set("MAIN_SCREEN_COLOR", "mainscreen_fg_color_val", "snow")

            config.add_section("VIEW_SCREEN_COLOR")
            config.set("VIEW_SCREEN_COLOR", "viewscreen_bg_color_val", "dark slate gray")
            config.set("VIEW_SCREEN_COLOR", "viewscreen_fg_color_val", "snow")

            config.add_section("SELECT_SCREEN_COLOR")
            config.set("SELECT_SCREEN_COLOR", "selectlist_bg_color_val", "dark slate gray")
            config.set("SELECT_SCREEN_COLOR", "selectlist_fg_color_val", "snow")

            config.add_section("NEWLIST_SCREEN_COLOR")
            config.set("NEWLIST_SCREEN_COLOR", "newlist_bg_color_val", "dark slate gray")
            config.set("NEWLIST_SCREEN_COLOR", "newlist_fg_color_val", "snow")

            config.add_section("USERMANUAL_SCREEN_COLOR")
            config.set("USERMANUAL_SCREEN_COLOR", "usermanual_bg_color_val", "dark slate gray")
            config.set("USERMANUAL_SCREEN_COLOR", "usermanual_fg_color_val", "snow")

            config.add_section("CONFIG_SCREEN_COLOR")
            config.set("CONFIG_SCREEN_COLOR", "config_bg_color_val", "dark slate gray")
            config.set("CONFIG_SCREEN_COLOR", "config_fg_color_val", "snow")

            # save app_config.ini file 
            with open(str(fullpath_app_config_ini_global), 'w') as configfile:
                 config.write(configfile)
                 
############################# CONFIGURE APP EVERY TIME PROGRAM STARTS ########################### 

      if os.path.isfile(fullpath_app_config_ini_global) == True:
            # #print("\n") 
            # #print(".... READ the app_config.ini file to initialize the APP - CONFIGURE APP SETTINGS and set corresponding config GLOBALS")
            # #print("\n")
            # read app_config.ini file
            config.read(str(fullpath_app_config_ini_global) )
            
            # read values from app_config.ini file sections
            mainscreen_bg_color_val = config.get("MAIN_SCREEN_COLOR", "mainscreen_bg_color_val")
            viewscreen_bg_color_val = config.get("VIEW_SCREEN_COLOR", "viewscreen_bg_color_val")
            selectlist_bg_color_val = config.get("SELECT_SCREEN_COLOR", "selectlist_bg_color_val")
            newlist_bg_color_val = config.get("NEWLIST_SCREEN_COLOR", "newlist_bg_color_val")
            usermanual_bg_color_val = config.get("USERMANUAL_SCREEN_COLOR", "usermanual_bg_color_val")
            config_bg_color_val = config.get("CONFIG_SCREEN_COLOR", "config_bg_color_val")
            
#################################################################################################
            # read values from app_config.ini file sections
            mainscreen_fg_color_val = config.get("MAIN_SCREEN_COLOR", "mainscreen_fg_color_val")
            viewscreen_fg_color_val = config.get("VIEW_SCREEN_COLOR", "viewscreen_fg_color_val")
            selectlist_fg_color_val = config.get("SELECT_SCREEN_COLOR", "selectlist_fg_color_val")
            newlist_fg_color_val = config.get("NEWLIST_SCREEN_COLOR", "newlist_fg_color_val")
            usermanual_fg_color_val = config.get("USERMANUAL_SCREEN_COLOR", "usermanual_fg_color_val")
            config_fg_color_val = config.get("CONFIG_SCREEN_COLOR", "config_fg_color_val")
            
#################################################################################################
            
            # set globals to communicate color settings
            mainscreen_bg_color_val_global = str(mainscreen_bg_color_val)
            viewscreen_bg_color_val_global = str(viewscreen_bg_color_val)
            selectlist_bg_color_val_global = str(selectlist_bg_color_val)
            newlist_bg_color_val_global = str(newlist_bg_color_val)
            usermanual_bg_color_val_global = str(usermanual_bg_color_val)
            config_bg_color_val_global = str(config_bg_color_val)
            
#################################################################################################

            # set globals to communicate color settings
            mainscreen_fg_color_val_global = str(mainscreen_fg_color_val)
            viewscreen_fg_color_val_global = str(viewscreen_fg_color_val)
            selectlist_fg_color_val_global = str(selectlist_fg_color_val)
            newlist_fg_color_val_global = str(newlist_fg_color_val)
            usermanual_fg_color_val_global = str(usermanual_fg_color_val)
            config_fg_color_val_global = str(config_fg_color_val)
            
################################################################################################# 
      appdata_cm_then_user_dir = (str(cm_appdatafiles_path_global) )     
      if not os.path.isdir(appdata_cm_then_user_dir):
          os.makedirs(appdata_cm_then_user_dir)
#################################################################################################

      # Create Directory Paths for Exporting Contact Management App Contact List to Excel.
      #
      export_csv_excel_userprofile_global = os.path.join(str(userprofile_global), "export_csv_excel" )
      export_csv_excel_cm_appdata_global = os.path.join(str(cm_appdatafiles_path_global), "export_csv_excel" )
      
      if not os.path.isdir(export_csv_excel_userprofile_global):
          os.makedirs(export_csv_excel_userprofile_global)

      if not os.path.isdir(export_csv_excel_cm_appdata_global):
          os.makedirs(export_csv_excel_cm_appdata_global)
          
      # Create Directory Paths for Importing Excel CSV to Contact Management App Contact List.
      #
      import_excel_csv_userprofile_global = os.path.join(str(userprofile_global), "import_excel_csv" )
      import_excel_csv_cm_appdata_global = os.path.join(str(cm_appdatafiles_path_global), "import_excel_csv" )
      
      if not os.path.isdir(import_excel_csv_userprofile_global):
          os.makedirs(import_excel_csv_userprofile_global)

      if not os.path.isdir(import_excel_csv_cm_appdata_global):
          os.makedirs(import_excel_csv_cm_appdata_global)
          
################################################################################################# 

      # Opens a Logfile every session which we can append to from anywhere 
      # in the program execution to monitor or debug. However, please note
      # that this logfile is being used to create a system administration screen
      # and therefore this logfile is re-written upon every new or selected
      # contact list Class/Method call. 

      # write a new logfile to update the logfile items upon program startup.
      inst_Write_Main_Logfile_upon_startup = Write_Main_Logfile()
      inst_Write_Main_Logfile_upon_startup.write_update_logfile()

 
      root = tk.Tk()
      cm_app = App(root)

      this_person = []

      # This is the cm_filename_worker_THREAD to maintain the Contact List Entry Widget filename String 
      # that we selected from LISTBOX to create CONTACT LIST FILENAME GLOBAL - str(cm_listbox_file_global)
      # Execute thread is a daeon thread that must run in a loop to always update the  
      # Contact List Entry Widget with the currently selected Contact List Filename: cm_listbox_file_global.
      # This thread is implemented as a continuous loop (with sleep) because if we let thr thread stop,
      # then we would have to instantiate it again to start another instance of the thread. 
      # The global variable, listbox_file_capture_global = False, resets the global variable 
      # that shows the STATUS of 1. Button Selects Contact List File 2. Update Entry Widget Textbox
      def cm_filename_worker():
           """Thread to UPDATE Contact List Entry Widgetthread - cm_filename_worker function"""
           
           global selected_dictionary_record_index_focus_global
           global kick_thread_to_update_main_entry_widgets
           global kick_thread_to_update_email_contact_entry_widgets
           global request_mainscreen_config_update_global
           global mainscreen_bg_color_val_global
           global insert_first_contact_global
           while 1:
                 
                 # Update the Main Screen Background Color per the latest GLOBAL setting
                 # so when User changes it, the new color appears instantly.
                 if request_mainscreen_config_update_global == True:
                     cm_app.master.config(background = str(mainscreen_bg_color_val_global) )
                     request_mainscreen_config_update_global = False

                 # #print("...... W H A T   I S   kick_thread_to_update_main_entry_widgets = " + str(kick_thread_to_update_main_entry_widgets) )

                 if (mode_select_global == "Browse Mode") and (str(dict_filename_global) != "No Contact Dictionary") and (kick_thread_to_update_main_entry_widgets == True):
#123456789012345678901
                     try:
                         # Utilize this try to Avoid a KeyError if there is an EMPTY DICTIONARY where no contacts were added.

                         # #print("...... DO WE EVER INITIATE kick_thread_to_update_main_entry_widgets = True ??? " + str(kick_thread_to_update_main_entry_widgets) )
                         fn_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
                         ln_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
                         sa_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
                         ct_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
                         st_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
                         zc_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
                         pn_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
                         em_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
                         ws_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] ) 
                         cm_app.entry_first.set(str(fn_browse) )
                         cm_app.entry_last.set(str(ln_browse) )
                         cm_app.entry_streetadd.set(str(sa_browse) )
                         cm_app.entry_citytown.set(str(ct_browse) )
                         cm_app.entry_state.set(str(st_browse) )
                         cm_app.entry_zipcode.set(str(zc_browse) )
                         cm_app.entry_phonenum.set(str(pn_browse) )
                         cm_app.entry_email.set(str(em_browse) )
                         cm_app.entry_website.set(str(ws_browse) )
                         selected_dictionary_counter_status_display = "Contact # " + str(selected_dictionary_record_index_focus_global) + \
                         " of " + str(num_of_dictionary_data_records_global)
                         
                         cm_app.contact_dict_count_status.set(str(selected_dictionary_counter_status_display) )

                         time.sleep(.15)
                      
                         # reset the kick_thread_to_update_main_entry_widgets = False 
                         kick_thread_to_update_main_entry_widgets = False
#123456789012345678901
                     except:
                         # reset the kick_thread_to_update_main_entry_widgets = False
                         kick_thread_to_update_main_entry_widgets = False
                             
                         # # print(".... LIKELY DETECTED KEY ERROR due to empty DICTIONARY, thus no need to update main screen")

                 if (mode_select_global == "Browse Mode") and (str(dict_filename_global) != "No Contact Dictionary") and (kick_thread_to_update_email_contact_entry_widgets == True):
#123456789012345678901
                     try:
                         # Utilize this try to Avoid a KeyError if there is an EMPTY DICTIONARY where no contacts were added.

                         # print("...... DO WE EVER INITIATE kick_thread_to_update_email_contact_entry_widgets = True ??? " + str(kick_thread_to_update_email_contact_entry_widgets) )
                             
                         fn_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
                         ln_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
                         em_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] )
                         # update the specific email screen widgets that are updated
                         # when contact increment or decrement button is clicked 

                         first_and_last_name = "  Contact Name: " + str(fn_browse) + " " + str(ln_browse)

                         # Verify Instance Path to these three EMAIL CLASS WIDGETS: 
                         #
                         # cm_app.cm_app_email.entry_LOADED_CONTACT_NAME.set(str(first_and_last_name) )
                         # cm_app.cm_app_email.entry_DEST_1_EMAIL_ADDRESS.set(str(em_browse) )    
                         # cm_app.cm_app_email.entry_EMAIL_STATUS.set(str(selected_dictionary_counter_status_display) )

                         cm_app.cm_app_email.entry_LOADED_CONTACT_NAME.set(str(first_and_last_name) )

                         cm_app.cm_app_email.entry_DEST_1_EMAIL_ADDRESS.set(str(em_browse) )

                         # PING IF YOU ARE IN THIS THREAD
                         # print("..... I AM IN THE MAIN THREAD ... UPDATING EMAIL ENTRY WIDGETS  !!!! ") 
                         
                         # Retreive from GLOBAL and Add to ENTRY WIDGET the CONTACT LIST NAME
                         new_CONTACT_LIST_NAME_String = "  Contact List: " + str(master_cm_list_name_global)

                         cm_app.cm_app_email.entry_CONTACT_LIST_NAME_Stringvar.set(str(new_CONTACT_LIST_NAME_String) )

                         selected_dictionary_counter_status_display = " Contact Number " + str(selected_dictionary_record_index_focus_global) + \
                         " of " + str(num_of_dictionary_data_records_global) 

                         cm_app.cm_app_email.entry_EMAIL_STATUS.set(str(selected_dictionary_counter_status_display) )

                         time.sleep(.15)
                         
                         # reset the kick_thread_to_update_email_contact_entry_widgets = False
                         kick_thread_to_update_email_contact_entry_widgets = False
#123456789012345678901
                     except AttributeError:
                         exc_type, exc_value, exc_traceback = sys.exc_info()
                         lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                         exception_AttributeError_string = ''.join('Exception Info: ' + line for line in lines)
                         
                         # reset the kick_thread_to_update_email_contact_entry_widgets = False
                         # Note that we CATCH THIS AttributeError EXCEPTION when the EMAIL TK WINDOW has not yet been activated.
                         kick_thread_to_update_email_contact_entry_widgets = False

                         # print(".... AttributeError  ....  E X C E P T I O N  in  THREAD  while attempting update of NOT YET ACTIVATED EMAIL CLASS WIDGETS: " + str("\n") )
                         # print(str(exception_AttributeError_string) )

#123456789012345678901
                     except:
                         exc_type, exc_value, exc_traceback = sys.exc_info()
                         lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                         exception_string_debug_this = ''.join('Exception Info: ' + line for line in lines)
                         
                         # reset the kick_thread_to_update_email_contact_entry_widgets = False
                         kick_thread_to_update_email_contact_entry_widgets = False

                         # print(".... E X C E P T I O N  in  THREAD  while attempting update of EMAIL CLASS WIDGETS: " + str("\n") )
                         # print(str(exception_string_debug_this) )
                             
                         # # print(".... LIKELY DETECTED KEY ERROR due to empty DICTIONARY, thus no need to update main screen")
                             
                 # Keep this master_cm_list_name_global data entry widget assertion     
                 # setting Contact List Entry Widget String from LISTBOX FILE GLOBAL - str(cm_listbox_file_global)
                 # cm_app.entry_buildlist.set(str(master_cm_list_name_global) )
                 
                 listbox_file_capture_global = False

                 # When each New Contact List is created, we will
                 # execute this method to insert the first contact  
                 # and then reset the insert_first_contact_global flag: 
                 if insert_first_contact_global == True:
                     
                     # cm_app.first_Contact_Data_Entry()
            
                     # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
                     # WHICH SETS THE selected_dictionary_loaded_global GLOBAL.  

                     inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
                     loaded_contact_dict_acquired_GLOBAL = inst_loaded_Process_Dict_File.read_target_dict_file()

                     # NOTE:
                     # selected_dictionary_record_index_global = 1
                     # selected_dictionary_record_index_focus_global = 1

                     kick_thread_to_update_main_entry_widgets = True
                     insert_first_contact_global = False

                 # manage this thread CPU usage but keep updates executed
                 # in the thread fast enough for human perception.
                 time.sleep(.05)

      t = threading.Thread(name="main_Class_cm_app_THREAD", target=cm_filename_worker, daemon=True)
      t.start()

      root.mainloop()


    

if __name__ == '__main__':
    main()
        
                       

