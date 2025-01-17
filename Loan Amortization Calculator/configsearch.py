import os
import yaml
from tkinter import Tk
from tkinter.filedialog import askdirectory

def loadYaml(file_path):
#to-do: load yml file, or create a default file if the file doesn't exist
    return {}

def saveYaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def directorySelect():
    Tk().withdraw() # hide the root window
    directory = askdirectory(title="Select a directory for the yaml file ")
    return directory

