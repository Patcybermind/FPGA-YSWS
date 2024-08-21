# this will be to transform markdown files to html files with our own styling and our own rules, the reason for this is that we might one day need more customisation options and it cant be that hard to make our own md to html
# when running this script you must be in the website directory and if you are on vscode you working terminal directory must be FPGA-YSWS/website
import os
import re
import md_to_html
import build_cms

current_directory = os.getcwd()
if not current_directory.endswith("website"):
    print("Please make sure you are in the 'website' directory before running this script.")
    print("Current directory:", current_directory)
    exit()


generate_html()
