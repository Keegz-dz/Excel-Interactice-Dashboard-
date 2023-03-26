import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image
import Directories
import os
from file_to_pdf import main as m1
from google_drive import main as m2


# import google_drive

class Main_Frame(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        # font of the project name
        self.my_font = customtkinter.CTkFont(family="Cascadia Mono", size=20)

        # adding labels
        self.label = customtkinter.CTkLabel(
            self, text="PDFMate", font=self.my_font, text_color='BLUE')
        self.appearance_mode_label = customtkinter.CTkLabel(
            self, text="Appearance Mode :", anchor="w", text_color='BLUE')

        # adding options
        self.file_options1 = customtkinter.CTkOptionMenu(
            self, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)

        self.label.grid(padx=20, pady=20)
        self.appearance_mode_label.grid(
            row=4, column=0, padx=(700, 00), pady=(65, 0), )
        self.file_options1.grid(padx=(700, 00), pady=(0, 20), )

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


class Main_software(customtkinter.CTk):
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    def handle_options(self, choice):

        if choice == "From device":
            m1()
            pass
        if choice == "From Google Drive":
            m2()
            pass

    def handle_button_1(self):
        self.button_1_text = "button 1  clicked"
        print(self.button_1_text)

    def handle_button_2(self):
        self.button_2_text = "button 2  clicked"
        print(self.button_2_text)

    def __init__(self):
        super().__init__()

        self.button_1_text = None
        self.button_2_text = None
        self.destination = None
        self.destination_folder = None
        self.option_text = None
        self.file_name = None
        self.title("Excel Dashboard Automation")
        self.geometry("900x600")
        self.resizable(False, False)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        # all the frames
        self.my_frame = Main_Frame(master=self, border_color='blue', )
        self.my_frame.grid(row=0, column=0, padx=20,
                           pady=(50, 20), sticky="nsew")

        self.frame1 = customtkinter.CTkFrame(
            self.my_frame, width=420, height=50, corner_radius=10, border_color='blue')
        self.frame1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.frame2 = customtkinter.CTkFrame(
            self.my_frame, width=420, height=200, corner_radius=10, border_color='blue', )
        self.frame2.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        self.my_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(os.getcwd(), '1.png')), size=(30, 30))

        self.file_options = customtkinter.CTkOptionMenu(self.frame2, values=[
            "From device", "From Google Drive"], command=self.handle_options, corner_radius=8)

        # buttons and labels for frame 2
        self.label1 = customtkinter.CTkLabel(
            self.frame2, text="\n", image=self.my_image, compound=tkinter.BOTTOM, corner_radius=8, text_color='BLUE')
        self.label2 = customtkinter.CTkLabel(
            self.frame2, text="drop your pdf files here \n", compound=tkinter.BOTTOM, corner_radius=8)
        self.label3 = customtkinter.CTkLabel(
            self.frame2, text="CHOOSE YOUR OPTION", compound=tkinter.BOTTOM, corner_radius=8, text_color='BLUE')

        # buttons and labels for frame 2
        self.button_1 = customtkinter.CTkButton(self.frame1, text="Upload document", command=self.handle_button_1(),
                                                corner_radius=8)
        self.button_2 = customtkinter.CTkButton(
            self.frame1, text="Choose data extracting rules", command=self.handle_button_2, corner_radius=8)

        # addding widgets
        self.button_1.pack(side=tk.LEFT)
        self.button_2.pack(side=tk.RIGHT)
        self.label1.pack(padx=(0, 00), pady=(20, 0), )
        self.label3.pack(padx=(0, 00), pady=(5, 5), )

        self.file_options.pack(padx=(0, 00), pady=(0, 0))
        self.label2.pack(padx=(0, 00), pady=(5, 50), )


if __name__ == "__main__":
    Main_software = Main_software()
    Main_software.mainloop()