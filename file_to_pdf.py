from xls2xlsx import XLS2XLSX
import tkinter.filedialog
import tkinter as tk
import Directories

import doc2pdf
import os


def MovePdf(file_path: str) -> None:
    """This functions moves pdfs into Stored PDFs folder"""

    destination = os.path.join(os.getcwd(), 'Stored Files\\Pdf', os.path.basename(file_path))
    try:
        os.rename(file_path, destination)
    except OSError as e:
        print(f"Error moving file {file_path} to {destination}: {e}")


def DocConvertPdf(file_path: str) -> None:
    """This Function converts Doc file types into pdf format"""

    destination = os.path.join(os.getcwd(), 'Stored Files\\Pdf', os.path.basename(file_path))
    try:
        doc2pdf.convert(file_path, destination)
        print("Conversion successful!")
    except Exception as e:
        print(f"Conversion failed: {str(e)}")


def MoveExcel(file_path):
    destination = os.path.join(os.getcwd(), 'Stored Files\\Excel', os.path.basename(file_path))
    if file_path.endswith('.xlsx'):
        os.rename(file_path, destination)
    elif file_path.endswith('.xls'):
        x2x = XLS2XLSX(file_path)
        file_name = os.path.basename(file_path)

        output_file_path = os.path.join(os.getcwd(), 'Stored Files\\Excel', os.path.splitext(file_name)[0] + ".xlsx")
        try:
            x2x.to_xlsx(output_file_path)
        except OSError as e:
            print(f"Error converting file {file_path} to xlsx: {e}")
    else:
        print(f"File format not supported: {file_path}")


def conversion(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    file_type = os.path.splitext(file_name)[1]
    file_name = os.path.splitext(file_name)[0]  # Removes the file extension from the file name

    # A Dictionary of functions for handling different file types
    conversion_functions = {
        '.docx': DocConvertPdf,
        '.doc': DocConvertPdf,
        '.xlsx': MoveExcel,
        '.xls': MoveExcel,
        # '.txt': ,
        # '.rtf': ,
        # '.jpeg': ,
        # '.jpg': ,
        # '.png': ,
        # '.tif': ,
        # '.tiff': m,
        '.pdf': MovePdf
    }

    if file_type in conversion_functions:  # Checks whether uploaded file type's conversion to pdf is supported
        conversion_functions[file_type](file_path, )  # Calls the corresponding function
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
            for sub_folder in ['Pdf', 'Excel']:
                Directories.create_sub_folder_dir('Stored Files', sub_folder)
            conversion(file_path)

    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    upload_file()
