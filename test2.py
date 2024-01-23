import os
from os import listdir
from os.path import isfile, join
import zipfile
import shutil
from pathlib import Path

folder01 = "01. Master Fabrication Orders"
folder02 = "y"


def listfolders(path):
    onlyfolders = [f for f in listdir(path)]
    return onlyfolders


def listzipfiles(path):
    zipfiles = []
    for dirName, subdirList, fileList in os.walk(path):
        dir = dirName.replace(path, "")
        for fname in fileList:
            if fname.endswith(".zip"):
                zipfiles.append([dir, os.path.join(dir, fname)])
    return zipfiles


zipfiles = listzipfiles(folder01)

for current_zipfile in zipfiles:
    where_is_the_zip_file = folder01 + current_zipfile[1]
    directory_where_we_will_extract = folder02 + current_zipfile[0]
    with zipfile.ZipFile(where_is_the_zip_file, "r") as zip_ref:
        zip_ref.extractall(directory_where_we_will_extract)

    Assembly_GA_or_Single_part = listfolders(directory_where_we_will_extract)
    print(Assembly_GA_or_Single_part)

    # heres the problem right now, i have to rename the folders to the corret ones, right now the path doesnt want to show the main folder for each directory
    if "Assembly" in Assembly_GA_or_Single_part:
        where_to_move = folder02 + "\\" + current_zipfile[0] + "\\\\ASSY"
        Path(where_to_move).mkdir(parents=True, exist_ok=True)
        src = folder02 + "\\" + current_zipfile[0] + "\\\\Assembly"
        print(src)
        print(where_to_move)
        os.rename(src, where_to_move)

    if "Single part" in Assembly_GA_or_Single_part:
        where_to_move = folder02 + "\\" + current_zipfile[0] + "\\\\SP"
        Path(where_to_move).mkdir(parents=True, exist_ok=True)
        src = folder02 + "\\" + current_zipfile[0] + "\\\\Single part"
        print(src)
        print(where_to_move)
        os.rename(src, where_to_move)


x = listfolders(folder01)
y = listfolders(folder02)

files_only_in_x = set(x) - set(y)
files_only_in_y = set(y) - set(x)
files_only_in_either = set(x) ^ set(y)
files_in_both = set(x) & set(y)
all_files = set(x) | set(y)
