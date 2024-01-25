import customtkinter
from tkinter import filedialog


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window
        self.geometry("400x600")
        self.title("For the record")

        # Labels
        self.label1_title = customtkinter.CTkLabel(
            self, text="For the record", fg_color="transparent"
        )
        self.label2_first_folder_name = customtkinter.CTkLabel(
            self, text="01. Master Fabrication Orders", fg_color="transparent"
        )
        self.label3_first_path = customtkinter.CTkLabel(
            self, text="Please select the first folder", fg_color="transparent"
        )
        self.label4_second_folder_name = customtkinter.CTkLabel(
            self, text="02. Master Document Control PDF", fg_color="transparent"
        )
        self.label5_second_path = customtkinter.CTkLabel(
            self, text="Please select the second folder", fg_color="transparent"
        )
        self.label6_to_do_first_dir = customtkinter.CTkLabel(
            self, text="01. Master Fabrication Orders", fg_color="transparent"
        )
        self.label7_to_do_second_dir = customtkinter.CTkLabel(
            self, text="02. Master Document Control PDF", fg_color="transparent"
        )

        # Buttons
        self.button_select_folder1 = customtkinter.CTkButton(
            self, text="Select folder 01", command=self.button_select_folder
        )
        self.button_select_folder2 = customtkinter.CTkButton(
            self, text="Select folder 02", command=self.button_select_folder
        )
        self.button_confirm1 = customtkinter.CTkButton(
            self, text="Confirm", command=self.confirm
        )

        # Grid
        self.label1_title.grid(row=0, column=0, padx=20, pady=10)

        self.label2_first_folder_name.grid(row=1, column=0, padx=20, pady=10)
        self.button_select_folder1.grid(row=2, column=0, padx=20, pady=10)
        self.label3_first_path.grid(row=3, column=0, padx=20, pady=10)

        self.label4_second_folder_name.grid(row=4, column=0, padx=20, pady=10)
        self.button_select_folder2.grid(row=5, column=0, padx=20, pady=10)
        self.label5_second_path.grid(row=6, column=0, padx=20, pady=10)

        self.label6_to_do_first_dir.grid(row=7, column=0, padx=20, pady=10)
        self.label7_to_do_second_dir.grid(row=8, column=0, padx=20, pady=10)

        self.button_confirm1.grid(row=9, column=0, padx=20, pady=10)

    # Methods
    def button_select_folder(self):
        dir = filedialog.askdirectory()
        print(dir)
        return dir

    def confirm(self):
        confirm_msg = "Confirm"
        print(confirm_msg)
        return confirm_msg


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = App()
app.mainloop()
