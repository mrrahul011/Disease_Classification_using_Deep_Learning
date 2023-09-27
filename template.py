import os
import pathlib
#form pathlib import Path
import logging

#to log basic information when running template.py
logging.basicConfig(level=logging.INFO, format='[%(asctime)]: %(message)s:') 

#define the project name
project_name = "CNN_Classifier"

#list of file and folder to be created
list_of_files = [
    ".github/workflows/.gitkeep",                               #for deployemed, all ci/cd related file are stored here in yaml format
    f"src/{project_name}/__init__.py",                          #src folder with project name, with local package, ie the constructor file (__init__.py)                 
    f"src/{project_name}/components/__init__.py",               #create folder inside src called components with a constructor file               
    f"src/{project_name}/utils/__init__.py",    
    f"src/{project_name}/config/__init__.py"
    f"src/{project_name}/config/configuration.py",              #
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",                                       #create config folder with config.yaml file in it.
    "dvc.yaml",
    "params.yaml",
    "requirments.txt",
    "setup.py",
    "research/trials.ipynb"                                 #research folder with trials.py file which is used for trial experiment
]

for filepath in list_of_files:
    filepath = pathlib.Path(filepath)                           #the file path have forward slash whereas in windows it is backward slash, it considers as windows path
    filedir, filename  = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exist")


