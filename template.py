import os
from pathlib import Path

"""
This python script will create the architecure/template for the Network Security Project

"""
main_folder = "NetworkSecurity"
folder_list = [
    f"{main_folder}/__init__.py",
    f"{main_folder}/components/__init__.py",
    f"{main_folder}/utils.py",
    f"{main_folder}/logging.py",
    f"{main_folder}/exception.py",
    f"{main_folder}/constants",
    f"{main_folder}/pipeline/__init__.py",
    "NetworkData",
    "notebooks",
    "config/config.yaml",
    "params.yaml",
    "templates/index.html",
    "app.py",
    "setup.py",
    "requirements.txt"
]


for filepath in folder_list:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        print(f"Creating directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            print(f"{filepath} doesn't exist")
    else:
        print(f"{filepath} already exist")