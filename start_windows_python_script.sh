#!/bin/bash

# Uncomment the !! because the editor screen color hides comments

# Generate the directory name in the format "workpython-YEAR-MONTH-DAY"

LINUX_DIRECTORY_NAME="LINUX_DIRECTORY_NAME"
MACOS_DIRECTORY_NAME="MACOS_DIRECTORY_NAME"
WINDOWS_DIRECTORY_NAME="WINDOWS_DIRECTORY_NAME"

DATE_VAR="Date: $(date +%Y-%m-%d)"

echo "   "
echo "-------------------------------"
echo "$LINUX_DIRECTORY_NAME"
echo "$MACOS_DIRECTORY_NAME"
echo "$WINDOWS_DIRECTORY_NAME"
echo "$DATE_VAR"
echo "-------------------------------"
pwd
ls
pwd
# Display python version
python3 --version
pwd
echo "-------------------------------"
pwd
# Run the tk_test1 script
# echo "Run the tk_test1 script from start_windows_python_script.sh"
# echo "Run the tk_test1 script from start_windows_python_script.sh"
# echo "Run the tk_test1 script from start_windows_python_script.sh"
# python3 tk_test1.py
echo "-------------------------------"
pwd
echo "-------------------------------"
echo "Run the uvm_builder_python.py script from start_windows_python_script.sh"
echo "Run the uvm_builder_python.py script from start_windows_python_script.sh"
echo "Run the uvm_builder_python.py script from start_windows_python_script.sh"
# Run the Python script
# python3 uvm_builder_python.py
# python3 uvm_builder_python_linux.py
python3 uvm_builder_python_linux_ubuntu.py
pwd
echo "-------------------------------"

