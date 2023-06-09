from xls2xlsx import XLS2XLSX
import tkinter.filedialog
import tkinter as tk
import Directories
import doc2pdf
import os
from PIL import Image


def MovePdf(file_path: str) -> None:
    """This function moves pdfs into Stored PDFs folder"""

    destination = os.path.join(os.getcwd(), 'Stored Pdfs', os.path.basename(file_path))
    try:
        os.rename(file_path, destination)
    except OSError as e:
        print(f"Error moving file {file_path} to {destination}: {e}")


def DocConvertPdf(file_path: str) -> None:
    """This function converts Doc file types into pdf format and stores it into Stored PDFs folder"""

    destination = os.path.join(os.getcwd(), 'Stored Pdfs', os.path.basename(file_path))
    try:
        doc2pdf.convert(file_path, destination)
        print("Conversion successful!")
    except Exception as e:
        print(f"Conversion failed: {str(e)}")


def MoveExcel(file_path):
    """Work in Progress, call it only once we have css file formats ready"""

    destination = os.path.join(os.getcwd(), 'Stored Pdfs', os.path.basename(file_path))
    if file_path.endswith('.xlsx'):
        os.rename(file_path, destination)
    elif file_path.endswith('.xls'):
        x2x = XLS2XLSX(file_path)
        file_name = os.path.basename(file_path)

        output_file_path = os.path.join(os.getcwd(), 'Stored Pdfs', os.path.splitext(file_name)[0] + ".xlsx")
        try:
            x2x.to_xlsx(output_file_path)
        except OSError as e:
            print(f"Error converting file {file_path} to xlsx: {e}")
    else:
        print(f"File format not supported: {file_path}")


def ImgConvertPdf(file_path: str) -> None:
    """This function converts images into pdf and stores it into Stored PDFs folder """
    destination = os.path.join(os.getcwd(), 'Stored Pdfs', os.path.basename(file_path))
    image = Image.open(file_path)
    pdf_path = os.path.splitext(file_path)[0] + '.pdf'
    image.save(pdf_path)
    MovePdf(pdf_path)


def conversion(file_path: str) -> None:
    """This function checks the uploaded file type and then calls the appropriate function required to convert the
    file into pdf """
    file_name = os.path.basename(file_path)
    file_type = os.path.splitext(file_name)[1]
    file_name = os.path.splitext(file_name)[0]  # Removes the file extension from the file name

    # A Dictionary of functions for handling different file types
    conversion_functions = {
        '.docx': DocConvertPdf,
        '.doc': DocConvertPdf,
        '.xlsx': MoveExcel,
        '.xls': MoveExcel,
        '.jpeg': ImgConvertPdf,
        '.jpg': ImgConvertPdf,
        '.png': ImgConvertPdf,
        '.tif': ImgConvertPdf,
        '.tiff': ImgConvertPdf,
        '.pdf': MovePdf
    }

    if file_type in conversion_functions:  # Checks whether uploaded file type's conversion to pdf is supported
        conversion_functions[file_type](file_path, )  # Calls the corresponding function
        tkinter.messagebox.showinfo("Success!", f"File {file_name} has been uploaded.")
    else:
        tkinter.messagebox.showerror("Error", f"Unsupported file type: {file_type}")


def upload_file() -> None:
    """ This function is the main function for uploading a file to the system.
    It prompts the user to select a file, then converts the file to PDF
    and moves it to the destination folder. It displays a success message if the file is uploaded successfully.
    If the file is not supported, it displays an error message. """
    try:
        option_text = "option clicked: --From device"
        print(option_text)
        file_path = tk.filedialog.askopenfilename(title="Select a file",
                                                  filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        if file_path:
            Directories.create_root_folder_dir(['Stored Pdfs'])
            conversion(file_path)

    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    upload_file()
