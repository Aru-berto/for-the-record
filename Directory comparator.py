import os
from os import listdir
from os.path import isfile, join
import zipfile
import shutil
from pathlib import Path
import customtkinter
from tkinter import filedialog
from datetime import datetime


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Done")
        self.geometry(self.CenterWindowToDisplay(260, 100, self._get_window_scaling()))
        self.after(0, self.grab_set())
        self.resizable(False, False)
        self.bell()

        self.label10_completion_window = customtkinter.CTkLabel(
            self, text="All done boss!", font=("Arial", 28)
        )
        self.label10_completion_window.pack(pady=(30, 10))

    def CenterWindowToDisplay(
        Screen: customtkinter.CTkToplevel,
        width: int,
        height: int,
        scale_factor: float = 1.0,
    ):
        screen_width = Screen.winfo_screenwidth()
        screen_height = Screen.winfo_screenheight()
        x = int(((screen_width / 2) - (width / 1.6)) * scale_factor)
        y = int(((screen_height / 2) - (height / 1.8)) * scale_factor)

        return f"{width}x{height}+{x}+{y}"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # ------------------------------------------------------------------------------------
        # Attributes
        self.folder01 = ""
        self.folder02 = ""

        # ------------------------------------------------------------------------------------
        # Window
        self.app_width = 1200
        self.app_height = 780

        self.geometry(
            self.CenterWindowToDisplay(
                self.app_width, self.app_height, self._get_window_scaling()
            )
        )
        self.title("Directory comparator (For the record 01 and 02)")

        self.toplevel_window = None

        # ------------------------------------------------------------------------------------
        # Buttons
        self.button_select_folder1 = customtkinter.CTkButton(
            self,
            text="Select",
            command=self.button_select_folder01,
            font=("Arial", 16),
        )
        self.button_select_folder2 = customtkinter.CTkButton(
            self,
            text="Select",
            command=self.button_select_folder02,
            font=("Arial", 16),
        )
        self.button_confirm1 = customtkinter.CTkButton(
            self,
            text="Start",
            command=self.confirm,
            state="disabled",
            font=("Arial", 16),
        )

        # ------------------------------------------------------------------------------------
        # Progress bar
        self.progressbar = customtkinter.CTkProgressBar(master=self)
        self.progressbar.set(0)

        # ------------------------------------------------------------------------------------
        # Frames
        self.scrollable_frame01 = customtkinter.CTkScrollableFrame(
            self, width=500, height=300
        )
        self.scrollable_frame02 = customtkinter.CTkScrollableFrame(
            self, width=500, height=300
        )

        # ------------------------------------------------------------------------------------
        # Labels
        self.label1_title = customtkinter.CTkLabel(
            self,
            text="Directory comparator",
            fg_color="transparent",
            anchor="w",
            font=("Arial", 42),
        )
        self.label2_first_folder_name = customtkinter.CTkLabel(
            self,
            text="01. Master Fabrication Orders",
            fg_color="transparent",
            font=("Arial", 18),
        )
        self.label3_first_path = customtkinter.CTkLabel(
            self,
            text="",
            fg_color="transparent",
            wraplength=550,
            font=("Arial", 12),
        )
        self.label4_second_folder_name = customtkinter.CTkLabel(
            self,
            text="02. Master Document Control PDF",
            fg_color="transparent",
            font=("Arial", 18),
        )
        self.label5_second_path = customtkinter.CTkLabel(
            self,
            text="",
            fg_color="transparent",
            wraplength=550,
            font=("Arial", 12),
        )
        self.label6_to_do_first_dir = customtkinter.CTkLabel(
            self,
            text="Only in 01 -> Creating in 02",
            fg_color="transparent",
            font=("Arial", 18),
        )
        self.label7_to_do_second_dir = customtkinter.CTkLabel(
            self,
            text="Only in 02 -> Moving to Complete",
            fg_color="transparent",
            font=("Arial", 18),
        )

        self.label8_frame1_text = customtkinter.CTkLabel(
            master=self.scrollable_frame01,
            text="",
            fg_color="transparent",
            font=("Arial", 12),
            wraplength=400,
            justify="left",
        )
        self.label9_frame2_text = customtkinter.CTkLabel(
            master=self.scrollable_frame02,
            text="",
            fg_color="transparent",
            font=("Arial", 12),
            wraplength=400,
            justify="left",
        )

        # ------------------------------------------------------------------------------------
        # Grid
        self.label1_title.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 20),
            sticky=customtkinter.W,
            columnspan=2,
        )
        # ------------------------
        self.label2_first_folder_name.grid(
            row=1, column=0, padx=20, pady=(5, 5), sticky=customtkinter.W
        )
        self.button_select_folder1.grid(
            row=2, column=0, padx=20, pady=(5, 5), sticky=customtkinter.W
        )
        self.label3_first_path.grid(
            row=2, column=1, padx=20, pady=(5, 30), sticky=customtkinter.W
        )
        # ------------------------
        self.label4_second_folder_name.grid(
            row=4, column=0, padx=20, pady=(5, 5), sticky=customtkinter.W
        )
        self.button_select_folder2.grid(
            row=5, column=0, padx=20, pady=(5, 5), sticky=customtkinter.W
        )
        self.label5_second_path.grid(
            row=5, column=1, padx=20, pady=(5, 30), sticky=customtkinter.W
        )

        # ------------------------
        self.label6_to_do_first_dir.grid(
            row=7, column=0, padx=20, pady=(5, 5), sticky=customtkinter.W
        )
        self.scrollable_frame01.grid(
            row=8, column=0, padx=20, pady=(5, 5), sticky=customtkinter.W
        )
        self.label8_frame1_text.grid(
            row=8,
            column=0,
            padx=20,
            pady=(5, 5),
            sticky=customtkinter.W + customtkinter.N,
        )

        self.label7_to_do_second_dir.grid(
            row=7, column=1, padx=20, pady=(5, 5), sticky=customtkinter.W
        )
        self.scrollable_frame02.grid(
            row=8, column=1, padx=20, pady=(5, 5), sticky=customtkinter.W
        )
        self.label9_frame2_text.grid(
            row=8,
            column=1,
            padx=20,
            pady=(5, 5),
            sticky=customtkinter.W + customtkinter.N,
        )
        # ------------------------

        self.progressbar.grid(
            row=10,
            column=0,
            padx=20,
            pady=(30, 5),
            sticky=customtkinter.W + customtkinter.E,
            columnspan=2,
        )

        self.button_confirm1.grid(
            row=11, column=1, padx=20, pady=(30, 5), sticky=customtkinter.E
        )

    # ------------------------------------------------------------------------------------
    # Methods

    def CenterWindowToDisplay(
        Screen: customtkinter.CTk, width: int, height: int, scale_factor: float = 1.0
    ):
        screen_width = Screen.winfo_screenwidth()
        screen_height = Screen.winfo_screenheight()
        x = int(((screen_width / 2) - (width / 2)) * scale_factor)
        y = int(((screen_height / 2) - (height / 2)) * scale_factor)

        return f"{width}x{height}+{x}+{y}"

    def change_frames_and_button(self):
        diff = self.what_is_different()

        what_to_write_on_first_frame = str = "\n\n".join(diff["files_only_in_x"])
        what_to_write_on_second_frame = str = "\n\n".join(diff["files_only_in_y"])

        if what_to_write_on_first_frame == "":
            self.label8_frame1_text.configure(
                text="(No new folders but will check zip files for updates)"
            )
        else:
            self.label8_frame1_text.configure(text=what_to_write_on_first_frame)

        if what_to_write_on_second_frame == "":
            self.label9_frame2_text.configure(text="(Nothing to move to Complete)")
        else:
            self.label9_frame2_text.configure(text=what_to_write_on_second_frame)

        self.button_confirm1.configure(state="normal")

    def button_select_folder01(self):
        dir = filedialog.askdirectory()
        self.label3_first_path.configure(text=dir)
        self.folder01 = dir

        if self.folder01 != "" and self.folder02 != "":
            self.change_frames_and_button()
        else:
            self.label8_frame1_text.configure(text="")
            self.label9_frame2_text.configure(text="")
            self.button_confirm1.configure(state="disabled")

    # ------------------------

    def button_select_folder02(self):
        dir = filedialog.askdirectory()
        self.label5_second_path.configure(text=dir)
        self.folder02 = dir

        if self.folder01 != "" and self.folder02 != "":
            self.change_frames_and_button()
        else:
            self.label8_frame1_text.configure(text="")
            self.label9_frame2_text.configure(text="")
            self.button_confirm1.configure(state="disabled")

    # ------------------------

    def confirm(self):
        self.what_to_log = []

        self.do_the_extraction()

        self.copy_folder_without_zip_file()

        self.move_to_complete()

        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)

        os.makedirs("Directory comparator logs", exist_ok=True)

        file_name = f"Directory comparator logs\\log {str_current_datetime}.txt"

        with open(file_name, "a") as f:  # Open the file in append mode
            for line in self.what_to_log:
                f.write(f"{line}\n")  # Write each line with a newline character

        self.button_confirm1.configure(state="disabled", text="Done!")

        self.open_toplevel()
        self.protocol("WM_DELETE_WINDOW", lambda: self.destroy())

    # ------------------------

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            self.toplevel_window.protocol("WM_DELETE_WINDOW", lambda: self.destroy())
        else:
            self.toplevel_window.focus()

    # ------------------------

    def listfolders(self, path):
        onlyfolders = [f for f in listdir(path)]
        if "Complete" in onlyfolders:
            onlyfolders.remove("Complete")
        return onlyfolders

    # ------------------------

    def listzipfiles(self, path):
        zipfiles = []
        for dirName, subdirList, fileList in os.walk(path):
            dir = dirName.replace(path, "")
            for fname in fileList:
                if fname.endswith(".zip"):
                    zipfiles.append([dir, os.path.join(dir, fname)])
        return zipfiles

    # ------------------------

    def extract_files(self, zip_file_path, target_directory):
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

    # ------------------------

    def what_is_different(self):
        f01 = self.listfolders(self.folder01)
        f02 = self.listfolders(self.folder02)
        diff = {
            "files_only_in_x": set(f01) - set(f02),
            "files_only_in_y": set(f02) - set(f01),
            "files_only_in_either": set(f01) ^ set(f02),
            "files_in_both": set(f01) & set(f02),
            "all_files": set(f01) | set(f02),
        }
        return diff

    # ------------------------

    def do_the_extraction(self):
        diff = self.what_is_different()

        for folder_without_zip_file in diff["files_only_in_x"]:
            self.what_to_log.append(
                f"New folder only in 01 created in 02 successfully: {folder_without_zip_file}"
            )
        self.what_to_log.append(f"")

        self.button_confirm1.configure(state="disabled", text="Working...")
        self.progressbar.set(0.25)
        zipfiles = self.listzipfiles(self.folder01)
        for current_zipfile in zipfiles:
            where_is_the_zip_file = self.folder01 + current_zipfile[1]
            target_directory = self.folder02 + current_zipfile[0]
            os.makedirs(target_directory, exist_ok=True)
            self.extract_files(where_is_the_zip_file, target_directory)
            self.what_to_log.append(
                f"Folder WITH zip file updated successfully: {current_zipfile[0]}"
            )
        self.what_to_log.append(f"")

    # ------------------------

    def copy_folder_without_zip_file(self):
        diff = self.what_is_different()
        self.progressbar.set(0.50)

        for folder_without_zip_file in diff["files_only_in_x"]:
            # Specify the paths
            source_folder_path = self.folder01 + "\\" + folder_without_zip_file
            target_directory_path = self.folder02 + "\\" + folder_without_zip_file

            # Copy the folder, overwriting existing files if necessary
            shutil.copytree(
                source_folder_path, target_directory_path, dirs_exist_ok=True
            )
            self.what_to_log.append(
                f"Folder WITHOUT zip file copied successfully: {folder_without_zip_file}"
            )
        self.what_to_log.append(f"")

    # ------------------------

    def move_to_complete(self):
        diff = self.what_is_different()
        self.progressbar.set(1)

        for folder_moving_to_complete in diff["files_only_in_y"]:
            if folder_moving_to_complete != "Complete":
                # Specify the paths
                folder_to_move = self.folder02 + "\\" + folder_moving_to_complete
                complete_directory = self.folder02 + "\\" + "Complete"

                # Create the "Complete" directory if it doesn't exist
                os.makedirs(
                    complete_directory, exist_ok=True
                )  # Ensures it's created only if needed

                # Move the folder
                shutil.move(folder_to_move, complete_directory)

                self.what_to_log.append(
                    f"Folder moved successfully to Complete: {folder_moving_to_complete}"
                )
        self.what_to_log.append(f"")

    # ------------------------


# ------------------------------------------------------------------------------------
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = App()
app.mainloop()
