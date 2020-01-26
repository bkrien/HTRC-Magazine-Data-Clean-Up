#This script creates new subdirectories for each of the zipped
#HTRC files and moves the zipped files into the correct subdirectories
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import glob, os, shutil

folder = filedialog.askdirectory()

for file_path in glob.glob(os.path.join(folder, '*.zip')):
    new_dir = file_path.rsplit('.', 1)[0]
    print(new_dir)
    os.mkdir(os.path.join(folder, new_dir))
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))
