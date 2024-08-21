import os
import re

def build_cms():
    list_of_files = [file for file in os.listdir("md_files") if file.endswith(".md") and file != "README.md"]
    print("\n", "list of files:", list_of_files) 
    data = [] # one item is one file and inside they will have a list corresponding to the settings which will later be transfered to a cms builder function
    for file in list_of_files:
        print("file:", file)
        with open(f"md_files/{file}", "r") as f:
            content = f.read()
            content_list = content.splitlines()
            file_settings = []
            data_mode = False
            publish = False
            for line in content_list:
                if line.startswith("---"):
                    if data_mode == True:
                        break
                    if data_mode == False:
                        data_mode = True
                if line.startswith("author:"):
                    file_settings.append(["author", line.split(":")[1].strip()])
                if line.startswith("date:"):
                    file_settings.append(["date", line.split(":")[1].strip()])
                if line.startswith("title:"):
                    file_settings.append(["title", line.split(":")[1].strip()])
                if line.startswith("tags:"):
                    file_settings.append(["tags", line.split(":")[1].strip()])    
                if line.startswith("description:"):
                    file_settings.append(["description", line.split(":")[1].strip()])
                if line.startswith("number:"):
                    file_settings.append(["number", float(line.split(":")[1].strip())])
                if line.startswith("publish:"):
                    if (line.split(":")[1].strip().lower()) == "true":
                        publish = True
                    elif (line.split(":")[1].strip().lower()) == "false":
                        publish = True
                    else:
                        print("publish should be either true or false")
                        print("file:", file)
                        exit()
                        
            if publish == True:
                data.append(file_settings)
    print("data:", data)

build_cms()
