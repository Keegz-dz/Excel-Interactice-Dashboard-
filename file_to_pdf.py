""" 
It seems like the code is designed to allow a user to upload a file to a system, 
convert it to PDF if it is a .docx file, and move it to a specific folder. The code
 also handles several different file types, including .jpeg, .jpg, .png, .tif, .tiff, and .pdf.

The code imports several libraries, including XLS2XLSX, tkinter.filedialog, tkinter,
 Directories, doc2pdf, os, and PIL.Image.

The code defines several functions, including MovePdf, DocConvertPdf, ImgConvertPdf, conversion, and upload_file.

The MovePdf function moves pdfs into the Stored PDFs folder.

The DocConvertPdf function converts Doc file types into pdf format.

The ImgConvertPdf function converts image file types into pdf format.

The conversion function checks the file type of the uploaded file and calls the appropriate
 function for handling the file type. If the file type is not supported, the function displays an error message.

The upload_file function prompts the user to select a file and then converts it to PDF if it is a 
.docx file and moves it to the destination folder. If the file is not supported, the function displays an error message.
"""
from xls2xlsx import XLS2XLSX
import tkinter.filedialog
import tkinter as tk
import Directories
import doc2pdf
import os
from PIL import Image


def MovePdf(file_path: str) -> None:
    """This functions moves pdfs into Stored PDFs folder"""

    destination = os.path.join(os.getcwd(),'Stored Pdfs', os.path.basename(file_path))
    try:
        os.rename(file_path, destination)
    except OSError as e:
        print(f"Error moving file {file_path} to {destination}: {e}")


def DocConvertPdf(file_path: str) -> None:
    """This Function converts Doc file types into pdf format"""

    destination = os.path.join(os.getcwd(),'Stored Pdfs',os.path.basename(file_path))
    try:
        doc2pdf.convert(file_path,destination)
        print("Conversion successful!")
    except Exception as e:
             print(f"Conversion failed: {str(e)}")
def MoveExcel(file_path):
    destination = os.path.join(os.getcwd(),'Stored Pdfs', os.path.basename(file_path))
    if file_path.endswith('.xlsx'):
        os.rename(file_path, destination)
    elif file_path.endswith('.xls'):
        x2x = XLS2XLSX(file_path)
        file_name = os.path.basename(file_path)
       
        output_file_path= os.path.join(os.getcwd(),'Stored Pdfs', os.path.splitext(file_name)[0] + ".xlsx")
        try:
            x2x.to_xlsx(output_file_path)
        except OSError as e:
            print(f"Error converting file {file_path} to xlsx: {e}")
    else:
        print(f"File format not supported: {file_path}")    




def ImgConvertPdf(file_path: str) -> None:
    destination = os.path.join(os.getcwd(),'Stored Pdfs', os.path.basename(file_path))
    image = Image.open(file_path)
    pdf_path = os.path.splitext(file_path)[0] + '.pdf'
    image.save(pdf_path)
    MovePdf(pdf_path)

   
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
        '.jpeg':ImgConvertPdf ,
        '.jpg': ImgConvertPdf,
        '.png': ImgConvertPdf,
        '.tif': ImgConvertPdf,
        '.tiff': ImgConvertPdf,
        '.pdf': MovePdf
    }

    if file_type in conversion_functions:  # Checks whether uploaded file type's conversion to pdf is supported
        conversion_functions[file_type](file_path,)  # Calls the corresponding function
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
            Directories.create_root_folder_dir(['Stored Pdfs'])
            conversion(file_path)

    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e)) 


if __name__ == "__main__":
    upload_file()
