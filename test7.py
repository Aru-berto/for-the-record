import os
from os import listdir
from os.path import isfile, join
import zipfile
import shutil
from pathlib import Path
import customtkinter
from tkinter import filedialog


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # ------------------------------------------------------------------------------------
        # Attributes
        self.folder01 = "..."
        self.folder02 = "..."

        # ------------------------------------------------------------------------------------
        # Window
        self.geometry("1000x800")
        self.title("For the record")

        # ------------------------------------------------------------------------------------
        # Buttons
        self.button_select_folder1 = customtkinter.CTkButton(
            self,
            text="Select",
            command=self.button_select_folder01,
            font=("Arial", 14),
        )
        self.button_select_folder2 = customtkinter.CTkButton(
            self,
            text="Select",
            command=self.button_select_folder02,
            font=("Arial", 14),
        )
        self.button_confirm1 = customtkinter.CTkButton(
            self,
            text="Start",
            command=self.confirm,
            state="disabled",
            font=("Arial", 14),
        )

        # ------------------------------------------------------------------------------------
        # Frames
        self.scrollable_frame01 = customtkinter.CTkScrollableFrame(
            self, width=400, height=300
        )
        self.scrollable_frame02 = customtkinter.CTkScrollableFrame(
            self, width=400, height=300
        )

        # ------------------------------------------------------------------------------------
        # Labels
        self.label1_title = customtkinter.CTkLabel(
            self,
            text="For the record",
            fg_color="transparent",
            anchor="w",
            font=("Arial", 46),
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
            font=("Arial", 18),
            wraplength=300,
            justify="left",
        )
        self.label9_frame2_text = customtkinter.CTkLabel(
            master=self.scrollable_frame02,
            text="",
            fg_color="transparent",
            font=("Arial", 18),
            wraplength=300,
            justify="left",
        )

        # ------------------------------------------------------------------------------------
        # Grid
        self.label1_title.grid(
            row=0, column=0, padx=20, pady=(10, 20), sticky=customtkinter.W
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
        self.button_confirm1.grid(
            row=11, column=0, padx=20, pady=(30, 5), sticky=customtkinter.W
        )

    # ------------------------------------------------------------------------------------
    # Methods
    def change_frames_and_button(self):
        self.label8_frame1_text.configure(
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam purus metus, eleifend eget lacus in, iaculis malesuada lectus. Aenean laoreet arcu sed augue efficitur, sit amet sagittis ligula mattis. Fusce ultricies rutrum augue vel volutpat. Proin efficitur ac neque id elementum. Vestibulum auctor ex sit amet auctor dapibus. Sed interdum eros in velit sagittis tincidunt. Praesent sagittis lacinia ligula a vehicula. Aliquam lacinia urna ac quam aliquet, et tristique ante suscipit. Pellentesque sit amet ullamcorper purus. In a viverra diam. Nulla at nibh porttitor, vestibulum nunc faucibus, malesuada orci. Fusce elementum rutrum lacus, at efficitur tortor ultricies quis. \n Ut tempus, massa in porta hendrerit, nulla mauris placerat dolor, in tincidunt urna justo vitae ipsum. Aenean a nunc et neque commodo congue. Etiam dignissim lorem interdum risus cursus, eu blandit dui tincidunt. Quisque vulputate arcu eu nisl interdum, sit amet suscipit nisi auctor. Integer augue ex, ultrices id iaculis vel, dignissim sed purus. Aliquam nunc arcu, luctus convallis dignissim eu, pulvinar sagittis tellus. Aliquam vestibulum justo nibh, sed hendrerit erat tincidunt ullamcorper. Morbi diam eros, interdum ac iaculis rhoncus, porta in ipsum. Aenean lobortis maximus aliquam. Sed imperdiet posuere enim at pretium. \nVivamus in varius nulla, non tincidunt urna. Vestibulum sit amet sem vel arcu mollis pharetra vitae a eros. Aliquam arcu leo, vestibulum nec condimentum in, maximus quis dolor. Nulla magna odio, vestibulum sit amet hendrerit vel, mattis ut felis. Etiam venenatis in libero rutrum finibus. Etiam tempor porta pellentesque. Nunc et massa id nulla iaculis ultrices in ac lacus. Nam a venenatis nisi, in posuere magna. Morbi vehicula consectetur tincidunt. Nunc sit amet ex suscipit ex consequat tempor. Phasellus laoreet sed tortor a dapibus. Duis non nulla ipsum. Integer imperdiet dignissim enim id ultrices.\nMorbi porta hendrerit lectus, nec faucibus lectus molestie eu. Aenean est arcu, mattis vel nulla vel, mattis vulputate ligula. Maecenas sit amet turpis sodales erat tincidunt ultricies. Vivamus eget urna tincidunt, egestas arcu ut, tempor nunc. Cras venenatis dapibus turpis, a bibendum leo hendrerit ac. Pellentesque efficitur pretium est sed molestie. Sed pretium, orci sed semper elementum, nunc odio aliquam lacus, nec rhoncus dolor leo id justo. Nulla bibendum turpis nunc, vel luctus augue cursus congue. Duis porttitor venenatis eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut feugiat, lacus quis consequat viverra, metus lacus tempor diam, vel dictum justo justo et metus. Praesent augue ipsum, ultrices eu libero faucibus, tristique laoreet quam. Donec pretium malesuada placerat. Integer quis dignissim risus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\nPraesent interdum dignissim lacus, sit amet ullamcorper odio iaculis a. Pellentesque euismod est vel quam malesuada vulputate. Integer tristique libero justo, sed aliquet sapien volutpat sed. Mauris at finibus neque. Pellentesque quam quam, volutpat at sagittis a, fringilla eu est. Etiam vel orci at metus vestibulum accumsan. In posuere, lacus eget lacinia ornare, felis ligula tempus lacus, ut vehicula est enim nec mi. Maecenas interdum tempus mollis. In hac habitasse platea dictumst. "
        )
        self.label9_frame2_text.configure(
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam purus metus, eleifend eget lacus in, iaculis malesuada lectus. Aenean laoreet arcu sed augue efficitur, sit amet sagittis ligula mattis. Fusce ultricies rutrum augue vel volutpat. Proin efficitur ac neque id elementum. Vestibulum auctor ex sit amet auctor dapibus. Sed interdum eros in velit sagittis tincidunt. Praesent sagittis lacinia ligula a vehicula. Aliquam lacinia urna ac quam aliquet, et tristique ante suscipit. Pellentesque sit amet ullamcorper purus. In a viverra diam. Nulla at nibh porttitor, vestibulum nunc faucibus, malesuada orci. Fusce elementum rutrum lacus, at efficitur tortor ultricies quis. \n Ut tempus, massa in porta hendrerit, nulla mauris placerat dolor, in tincidunt urna justo vitae ipsum. Aenean a nunc et neque commodo congue. Etiam dignissim lorem interdum risus cursus, eu blandit dui tincidunt. Quisque vulputate arcu eu nisl interdum, sit amet suscipit nisi auctor. Integer augue ex, ultrices id iaculis vel, dignissim sed purus. Aliquam nunc arcu, luctus convallis dignissim eu, pulvinar sagittis tellus. Aliquam vestibulum justo nibh, sed hendrerit erat tincidunt ullamcorper. Morbi diam eros, interdum ac iaculis rhoncus, porta in ipsum. Aenean lobortis maximus aliquam. Sed imperdiet posuere enim at pretium. \nVivamus in varius nulla, non tincidunt urna. Vestibulum sit amet sem vel arcu mollis pharetra vitae a eros. Aliquam arcu leo, vestibulum nec condimentum in, maximus quis dolor. Nulla magna odio, vestibulum sit amet hendrerit vel, mattis ut felis. Etiam venenatis in libero rutrum finibus. Etiam tempor porta pellentesque. Nunc et massa id nulla iaculis ultrices in ac lacus. Nam a venenatis nisi, in posuere magna. Morbi vehicula consectetur tincidunt. Nunc sit amet ex suscipit ex consequat tempor. Phasellus laoreet sed tortor a dapibus. Duis non nulla ipsum. Integer imperdiet dignissim enim id ultrices.\nMorbi porta hendrerit lectus, nec faucibus lectus molestie eu. Aenean est arcu, mattis vel nulla vel, mattis vulputate ligula. Maecenas sit amet turpis sodales erat tincidunt ultricies. Vivamus eget urna tincidunt, egestas arcu ut, tempor nunc. Cras venenatis dapibus turpis, a bibendum leo hendrerit ac. Pellentesque efficitur pretium est sed molestie. Sed pretium, orci sed semper elementum, nunc odio aliquam lacus, nec rhoncus dolor leo id justo. Nulla bibendum turpis nunc, vel luctus augue cursus congue. Duis porttitor venenatis eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut feugiat, lacus quis consequat viverra, metus lacus tempor diam, vel dictum justo justo et metus. Praesent augue ipsum, ultrices eu libero faucibus, tristique laoreet quam. Donec pretium malesuada placerat. Integer quis dignissim risus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\nPraesent interdum dignissim lacus, sit amet ullamcorper odio iaculis a. Pellentesque euismod est vel quam malesuada vulputate. Integer tristique libero justo, sed aliquet sapien volutpat sed. Mauris at finibus neque. Pellentesque quam quam, volutpat at sagittis a, fringilla eu est. Etiam vel orci at metus vestibulum accumsan. In posuere, lacus eget lacinia ornare, felis ligula tempus lacus, ut vehicula est enim nec mi. Maecenas interdum tempus mollis. In hac habitasse platea dictumst. "
        )
        self.button_confirm1.configure(state="normal", text="Start")

    def button_select_folder01(self):
        dir = filedialog.askdirectory()
        self.label3_first_path.configure(text=dir)
        self.folder01 = dir

        if self.folder01 != "..." and self.folder02 != "...":
            self.change_frames_and_button()

    # ------------------------

    def button_select_folder02(self):
        dir = filedialog.askdirectory()
        self.label5_second_path.configure(text=dir)
        self.folder02 = dir

        if self.folder01 != "..." and self.folder02 != "...":
            self.change_frames_and_button()

    # ------------------------

    def confirm(self):
        confirm_msg = "Confirm"
        print(self.folder01)
        print(self.folder02)
        print(confirm_msg)
        return confirm_msg

    # ------------------------

    def listfolders(path):
        onlyfolders = [f for f in listdir(path)]
        if "Complete" in onlyfolders:
            onlyfolders.remove("Complete")
        return onlyfolders

    # ------------------------

    def listzipfiles(path):
        zipfiles = []
        for dirName, subdirList, fileList in os.walk(path):
            dir = dirName.replace(path, "")
            for fname in fileList:
                if fname.endswith(".zip"):
                    zipfiles.append([dir, os.path.join(dir, fname)])
        return zipfiles

    # ------------------------

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
        zipfiles = self.listzipfiles(self.folder01)
        for current_zipfile in zipfiles:
            where_is_the_zip_file = self.folder01 + current_zipfile[1]
            target_directory = self.folder02 + current_zipfile[0]
            os.makedirs(target_directory, exist_ok=True)
            self.extract_files(where_is_the_zip_file, target_directory)
            print(
                f"Files extracted and folders renamed successfully! ({current_zipfile[0]})"
            )
        print()

    # ------------------------

    def copy_folder_without_zip_file(self):
        diff = self.what_is_different()

        for folder_without_zip_file in diff["files_only_in_x"]:
            # Specify the paths
            source_folder_path = self.folder01 + "\\" + folder_without_zip_file
            target_directory_path = self.folder02 + "\\" + folder_without_zip_file

            # Copy the folder, overwriting existing files if necessary
            shutil.copytree(
                source_folder_path, target_directory_path, dirs_exist_ok=True
            )

            print(
                f"Folder without zip file copied successfully! ({folder_without_zip_file})"
            )
        print()

    # ------------------------

    def move_to_complete(self):
        diff = self.what_is_different()

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

                print(
                    f"Folder moved successfully to Complete! ({folder_moving_to_complete})"
                )

    # ------------------------


# ------------------------------------------------------------------------------------
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = App()
app.mainloop()
