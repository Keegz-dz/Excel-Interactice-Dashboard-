import os
import tkinter as tk
import tkinter.filedialog
import docx2pdf
import Directories
from xls2xlsx import XLS2XLSX
import ppt2pdf
import doc2pdf


def move_file(file_path, destination_folder):
    """
    Move the file to the destination folder.

    Args:
    - file_path (str): Path of the file to move.
    - destination_folder (str): Path of the destination folder.

    Returns: None
    """
    destination = os.path.join(destination_folder, 'Pdf', os.path.basename(file_path))
    try:
        os.rename(file_path, destination)
    except OSError as e:
        print(f"Error moving file {file_path} to {destination}: {e}")


def convert_to_pdf(file_path, destination_folder):
    """
    Convert a docx file to pdf format and move it to the pdf folder.

    Args:
    - file_path (str): Path of the docx file to convert.
    - main_destination_folder (str): Path of the main destination folder.

    Returns: None
    """
    destination = os.path.join(destination_folder, 'Pdf', os.path.basename(file_path))
    if file_path.endswith('.docx'):
        try:
            docx2pdf.convert(file_path, destination)
        except OSError as e:
            print(f"Error converting file {file_path} to PDF: {e}")
    elif file_path.endswith('.doc'):
        # try converting to docx format first
        try:
            doc2pdf.convert(file_path, destination)
        except OSError as e:
            print(f"Error converting file {file_path} to PDF: {e}")

    else:
        print(f"File format not supported: {file_path}")


def convert_excel(file_path, destination_folder):
    """
    Convert an excel file to xlsx format or move it to the excel folder.

    Args:
    - file_path (str): Path of the excel file to convert.
    - main_destination_folder (str): Path of the main destination folder.

    Returns: None
    """

    if file_path.endswith('.xlsx'):
        move_file(file_path, destination)
    elif file_path.endswith('.xls'):
        x2x = XLS2XLSX(file_path)
        file_name = os.path.basename(file_path)
        output_file_path = os.path.join(destination_folder, 'Exel', os.path.splitext(file_name)[0] + ".xlsx")
        try:
            x2x.to_xlsx(output_file_path)
        except OSError as e:
            print(f"Error converting file {file_path} to xlsx: {e}")
    else:
        print(f"File format not supported: {file_path}")


def move_text_file(file_path, destination_folder):
    """
    Move a text file to the text folder.

    Args:
    - file_path (str): Path of the text file to move.
    - main_destination_folder (str): Path of the main destination folder.

      Returns: None
    """
    destination = os.path.join(destination_folder, 'Text', os.path.basename(file_path))
    move_file(file_path, destination_folder)


def move_image_file(file_path, destination_folder):
    """
    Move the image file to the destination folder.
    """
    destination = os.path.join(destination_folder, 'Images', os.path.basename(file_path))
    move_file(file_path, destination_folder)


def create_destination_folders():
    """
    This function creates destination folders for the provided folder names if they do not exist.

    Parameters:
    folder_names (list): A list of folder names to create.

    """
    folder_names = ['Stored Files', 'Stored Files/Pdf', 'Stored Files/Images', 'Stored Files/Text', 'Stored Files/Exel']
    for folder_name in folder_names:
        folder_path = os.path.join(os.getcwd(), folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


def convert(file_name, file_type, file_path):
    destination_folder = os.path.join(os.getcwd(), 'Stored Files')
    # A Dictionary of functions for handling different file types
    conversion_functions = {
        '.docx': convert_to_pdf,
        '.doc': convert_to_pdf,
        '.xlsx': convert_excel,
        '.xls': convert_excel,
        '.txt': move_text_file,
        '.rtf': move_text_file,
        '.jpeg': move_image_file,
        '.jpg': move_image_file,
        '.png': move_image_file,
        '.tif': move_image_file,
        '.tiff': move_image_file,
        '.pdf': move_file
    }
    if file_type in conversion_functions:  # if the file type is supported
        conversion_functions[file_type](file_path, destination_folder)  # call the corresponding function
        tkinter.messagebox.showinfo("Success!", f"File {file_name} has been uploaded.")
    else:
        tkinter.messagebox.showerror("Error",
                                     f"Unsupported file type: {file_type}")  # display an error message for unsupported file types


def main():
    """
    This function is the main function for uploading a file to the system.
    It prompts the user to select a file, then converts the file to PDF if it is a .docx file
    and moves it to the destination folder. It displays a success message if the file is uploaded successfully.
    If the file is not supported, it displays an error message.

    """
    try:
        option_text = "option clicked: --From device"
        print(option_text)
        file_path = tk.filedialog.askopenfilename(title="Select a file")
        if file_path:
            file_name = os.path.basename(file_path)  # get the file name
            file_type = os.path.splitext(file_name)[1]  # get the file type
            file_name = os.path.splitext(file_name)[0]  # remove the file extension from the file name
            print("File Name:", file_name)
            print("File Type:", file_type)
            create_destination_folders()

            convert(file_name, file_type, file_path)
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))  # display an error message for any other errors


if __name__ == "__main__":
    main()