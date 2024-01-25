import customtkinter
from tkinter import filedialog


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("680x420")


def button_function():
    filedialog.askdirectory()


frame = customtkinter.CTkFrame(master=app)
frame.pack(expand=True)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
