import os
from os import listdir
from os.path import isfile, join
import zipfile
import shutil
from pathlib import Path
import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("For the record")

label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack()

root.mainloop()


# -----------------------------------------------------------------------------------------
# Folder names
folder01 = "01. Master Fabrication Orders"
folder02 = "y"

# -----------------------------------------------------------------------------------------
# Functions


def listfolders(path):
    onlyfolders = [f for f in listdir(path)]
    if "Complete" in onlyfolders:
        onlyfolders.remove("Complete")
    return onlyfolders


def listzipfiles(path):
    zipfiles = []
    for dirName, subdirList, fileList in os.walk(path):
        dir = dirName.replace(path, "")
        for fname in fileList:
            if fname.endswith(".zip"):
                zipfiles.append([dir, os.path.join(dir, fname)])
    return zipfiles


def extract_files(zip_file_path, target_directory):
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        # Dictionary for mapping old folder names to new names
        folder_rename_map = {
            "Assembly": "ASSY",
            "GA": "GA",
            "Single part": "SP",
        }

        # Iterate through the files in the zip archive
        for info in zip_ref.infolist():
            # Extract the filename and its parent directory
            file_path = info.filename
            parent_dir = os.path.dirname(file_path)

            # Check for folders and rename if needed
            if parent_dir:  # Non-empty parent directory indicates a folder
                old_folder_name = os.path.basename(parent_dir)
                if old_folder_name in folder_rename_map:
                    new_folder_name = folder_rename_map[old_folder_name]
                    # Update the filename to reflect the renamed folder
                    new_file_path = os.path.join(
                        new_folder_name, os.path.relpath(file_path, parent_dir)
                    )
                    info.filename = new_file_path

            # Extract the file with the updated filename
            zip_ref.extract(info, target_directory)


# -----------------------------------------------------------------------------------------
# Zip files

zipfiles = listzipfiles(folder01)
for current_zipfile in zipfiles:
    where_is_the_zip_file = folder01 + current_zipfile[1]
    target_directory = folder02 + current_zipfile[0]
    os.makedirs(target_directory, exist_ok=True)
    extract_files(where_is_the_zip_file, target_directory)
    print(f"Files extracted and folders renamed successfully! ({current_zipfile[0]})")
print()

# -----------------------------------------------------------------------------------------
# What is different

x = listfolders(folder01)
y = listfolders(folder02)

files_only_in_x = set(x) - set(y)
files_only_in_y = set(y) - set(x)
files_only_in_either = set(x) ^ set(y)
files_in_both = set(x) & set(y)
all_files = set(x) | set(y)

print(f"Only in 01: {files_only_in_x}")
print()
print(f"Only in 02: {files_only_in_y}")

for folder_without_zip_file in files_only_in_x:
    # Specify the paths
    source_folder_path = folder01 + "\\" + folder_without_zip_file
    target_directory_path = folder02 + "\\" + folder_without_zip_file

    # Copy the folder, overwriting existing files if necessary
    shutil.copytree(source_folder_path, target_directory_path, dirs_exist_ok=True)

    print(f"Folder without zip file copied successfully! ({folder_without_zip_file})")
print()

x = listfolders(folder01)
y = listfolders(folder02)

files_only_in_x = set(x) - set(y)
files_only_in_y = set(y) - set(x)
files_only_in_either = set(x) ^ set(y)
files_in_both = set(x) & set(y)
all_files = set(x) | set(y)

print(f"Only in 01: {files_only_in_x}")
print()
print(f"Only in 02: {files_only_in_y}")


for folder_moving_to_complete in files_only_in_y:
    if folder_moving_to_complete != "Complete":
        # Specify the paths
        folder_to_move = folder02 + "\\" + folder_moving_to_complete
        complete_directory = folder02 + "\\" + "Complete"

        # Create the "Complete" directory if it doesn't exist
        os.makedirs(
            complete_directory, exist_ok=True
        )  # Ensures it's created only if needed

        # Move the folder
        shutil.move(folder_to_move, complete_directory)

        print(f"Folder moved successfully to Complete! ({folder_moving_to_complete})")

x = listfolders(folder01)
y = listfolders(folder02)

files_only_in_x = set(x) - set(y)
files_only_in_y = set(y) - set(x)
files_only_in_either = set(x) ^ set(y)
files_in_both = set(x) & set(y)
all_files = set(x) | set(y)

print(f"Only in 01: {files_only_in_x}")
print()
print(f"Only in 02: {files_only_in_y}")
