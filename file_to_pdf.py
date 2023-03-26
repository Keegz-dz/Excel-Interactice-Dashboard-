from xls2xlsx import XLS2XLSX
import tkinter.filedialog
import tkinter as tk
import Directories
import docx2pdf
import doc2pdf
import ppt2pdf
import os


def move_pdf(file_path: str, destination_folder: None) -> None:
    """This functions moves pdfs into Stored PDFs folder"""

    destination = os.path.join(os.getcwd(), 'Stored PDFs', os.path.basename(file_path))
    try:
        os.rename(file_path, destination)
    except OSError as e:
        print(f"Error moving file {file_path} to {destination}: {e}")


def doc_conv_pdf(file_path: str, destination_folder: str) -> None:
    """This Function converts Doc file types into pdf format"""

    destination = os.path.join(os.getcwd(), 'Stored PDFs', os.path.basename(file_path))
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


# def move_image_file(file_path, destination_folder):
#     """
#     Move the image file to the destination folder.
#     """
#     destination = os.path.join(destination_folder, 'Images', os.path.basename(file_path))
#     move_file(file_path, destination_folder)


def convert(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    file_type = os.path.splitext(file_name)[1]
    file_name = os.path.splitext(file_name)[0]  # Removes the file extension from the file name
    destination_folder = os.path.join(os.getcwd(), 'Stored Files')
    # A Dictionary of functions for handling different file types
    conversion_functions = {
        '.docx': doc_conv_pdf,
        '.doc': doc_conv_pdf,
        # '.xlsx': convert_excel,
        # '.xls': convert_excel,
        # '.txt': move_text_file,
        # '.rtf': move_text_file,
        # '.jpeg': move_image_file,
        # '.jpg': move_image_file,
        # '.png': move_image_file,
        # '.tif': move_image_file,
        # '.tiff': move_image_file,
        '.pdf': move_pdf,
    }

    if file_type in conversion_functions:  # Checks whether uploaded file type's conversion to pdf is supported
        conversion_functions[file_type](file_path, destination_folder)  # Calls the corresponding function
        tkinter.messagebox.showinfo("Success!", f"File {file_name} has been uploaded.")
    else:
        tkinter.messagebox.showerror("Error", f"Unsupported file type: {file_type}")


def upload_file() -> None:
    """ This function is the main function for uploading a file to the system.
    It prompts the user to select a file, then converts the file to PDF if it is a .docx file
    and moves it to the destination folder. It displays a success message if the file is uploaded successfully.
    If the file is not supported, it displays an error message. """
    try:
        option_text = "option clicked: --From device"
        print(option_text)
        file_path = tk.filedialog.askopenfilename(title="Select a file")
        if file_path:
            Directories.create_root_folder_dir(['Stored Files'])
            for sub_folder in ['Pdf', 'Images', 'Text', 'Excel']:
                Directories.create_sub_folder_dir('Stored Files', sub_folder)
            convert(file_path)

    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    upload_file()
