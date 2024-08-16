# this will be to transform markdown files to html files with our own styling and our own rules, the reason for this is that we might one day need more customisation options and it cant be that hard to make our own md to html
# when running this script you must be in the website directory and if you are on vscode you working terminal directory must be FPGA-YSWS/website
import os

def generate_html():
    list_of_files = [file for file in os.listdir("md_files") if file.endswith(".md") and file != "README.md"]
    print(list_of_files)
    

generate_html()
