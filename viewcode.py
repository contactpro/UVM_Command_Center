##########################################################################
#
# Author: Michael Hughes
# 
# Program: viewcode.py 
#
# Version: 1.0
#    
# Date: November 6, 2017 
#
# Description:
#
# viewcode command line script to show Python Module CLASSES and METHODS.
#
# Parses classes and methods to view python code.
#
# Usage:  viewcode.py  filename.py 
#
# Language: Python 3.6.2 
#
########################################################################## 

import re
import os
import argparse

def main():

    print("\n\n")

    parser = argparse.ArgumentParser(description="The viewcode command line script displays Python Module CLASSES and METHODS.\nResults are also written to a file named: viewcode_report.txt\n", usage="viewcode filename.py  or  viewcode filename.py -c  or  viewcode -h\n\nThe viewcode command line script displays Python Module CLASSES and METHODS.\nResults are also written to a file named: viewcode_report.txt\n\nExample Use Cases:  viewcode filename.py  or  viewcode filename.py -c  to include code lines with # comments, or  viewcode -h  for help.\n\n")
    
    parser.add_argument("filename", type=str, help="filename - Example Use Case:  viewcode filename.py")
    parser.add_argument("--comments", "-c", action="store_true", default=False, help="Commments Option -comments or -c adds code lines with #")
    
    args = parser.parse_args()

    filename = args.filename

    python_file = open(str(filename), "r")
    viewcode_report = open("viewcode_report.txt", "w")

    for line in python_file:
        if re.search("class ", line):
            viewcode_report.write(line)
        if re.search("def ", line):
            viewcode_report.write(line)
        if args.comments==True:
            if re.search("#", line):
                viewcode_report.write(line)
            
    python_file.close()
    viewcode_report.close()

    viewcode_report = open("viewcode_report.txt", "r")

    for line in viewcode_report:
        print(line, end="")

    viewcode_report.close()

    print("\n\n")

    print("The viewcode command line script has executed to show Python Module CLASSES and METHODS, and optionally, COMMENTS." + str("\n\n") + "The viewcode command line script has completed parsing this file: " + str(filename) + str("\n\n") + "Results are also written to a file named:  viewcode_report.txt" + str("\n\n") + "NOTE:  Add the -comments or -c option to include all lines of python code containing the # comment delimiter." + str("\n\n") + "NOTE:  Type  viewcode -h  for help.")

    print("\n\n")


if __name__ == '__main__':
    main()


