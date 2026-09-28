#!/bin/bash

# Uncomment the !! because the editor screen color hides comments

echo "  "
echo "start_windows_python_script ... export DISPLAY CHIPCODER:0.0  in bashrc ... "
echo "start_windows_python_script ... export DISPLAY CHIPCODER:0.0  in bashrc ... "
echo "start_windows_python_script ... export DISPLAY CHIPCODER:0.0  in bashrc ... "
export DISPLAY=CHIPCODER:0.0
echo "  "
echo "start_windows_python_script echo DISPLAY Setting:  "
echo $DISPLAY
echo "  "
echo "start_windows_python_script ... export PATH=$PATH:\\root\\intelFPGA\\20.1\\modelsim_ase\\bin"
echo "start_windows_python_script ... export PATH=$PATH:\\root\\intelFPGA\\20.1\\modelsim_ase\\linuxaloem"
echo "  "
export PATH=$PATH:\\root\\intelFPGA\\20.1\\modelsim_ase\\bin
export PATH=$PATH:\\root\\intelFPGA\\20.1\\modelsim_ase\\linuxaloem
echo "  "
echo "start_windows_python_script ATTENTION: Verify updated exported linuxaloem linux modelsim . . . . ."
echo "  "
echo $PATH
echo "  "

# Generate the directory name in the format "workpython-YEAR-MONTH-DAY"

LINUX_DIRECTORY_NAME="LINUX_DIRECTORY_NAME"
MACOS_DIRECTORY_NAME="MACOS_DIRECTORY_NAME"
WINDOWS_DIRECTORY_NAME="WINDOWS_DIRECTORY_NAME"

DATE_VAR="Date: $(date +%Y-%m-%d)"
echo "-------------------------------"
echo "$DATE_VAR"
echo "-------------------------------"
echo "   "
echo $PATH
echo "   "
echo "-------------------------------"
echo "$LINUX_DIRECTORY_NAME"
echo "$MACOS_DIRECTORY_NAME"
echo "$WINDOWS_DIRECTORY_NAME"
echo "-------------------------------"
echo "$DATE_VAR"
echo "-------------------------------"
pwd
echo "  "
echo "-------------------------------"
echo "   View python Files: "
echo "-------------------------------"
echo "  "
ls *.py
echo "  "
echo "-------------------------------"
pwd
# Display python version
echo "PYTHON VERSION:  "
echo "  "
python3 --version
echo "  "
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
echo "Run the uvm_builder_python_linux_ubuntu.py script from start_windows_python_script.sh"
echo "Run the uvm_builder_python_linux_ubuntu.py script from start_windows_python_script.sh"
echo "Run the uvm_builder_python_linux_ubuntu.py script from start_windows_python_script.sh"
# Run the Python script
# python3 uvm_builder_python.py
# python3 uvm_builder_python_linux.py
python3 uvm_builder_python_linux_ubuntu.py
pwd
echo "-------------------------------"

