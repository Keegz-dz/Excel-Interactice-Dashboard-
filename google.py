from file_to_pdf import convert
import tkinter as tk
import webbrowser

google_drive_url = "https://drive.google.com/drive/my-drive"


def getfilepath_drive() -> None:
    webbrowser.open_new_tab(google_drive_url)  # Opens Google Drive in a new browser tab
    option_text = "option clicked : --From Google Drive"
    print(option_text)
    # Prompt the user to select the file they just downloaded
    downloaded_file_path = tk.filedialog.askopenfilename(title="Select the Google Drive file you just downloaded")

    # if downloaded_file_path:
    #     convert(file_name, file_type, file_path)  # Convert accepted file type into PDF


if __name__ == "__main__":
    getfilepath_drive()

"""Pending : Increase the font size"""
