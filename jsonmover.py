#After adding the json folders to the same directory as the zipped files
#After creating the subdirectories for each of the json files with
#fileadder.py, run this script to move the jsons into the correct subdirectory
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import glob, os, shutil

folder = filedialog.askdirectory()

for file_path in glob.glob(os.path.join(folder, '*.json')):
    move_file = file_path.rsplit('.',1)[0]
    shutil.move(file_path, os.path.join(move_file, os.path.basename(file_path)))
