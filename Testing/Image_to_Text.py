# ****************IMPORTING MODULES*******************##

import Pdf_to_Image as p2i
import pytesseract
import os
from PIL import Image


# ***********IGNORE THE FOLLOWING LINES****************##

# main_directory = os.getcwd()  # Main Directory
# if not os.path.exists(os.path.join(main_directory, "Converted OCR Text")):  # Checks Whether Directory exists or not
#     os.mkdir("Converted OCR Text")
# Ocr_directory = os.path.join(main_directory, "Converted OCR Text")  # Directory Of OCR Texts
# os.chdir(os.path.join(os.getcwd(), "Converted PDFs"))
# converted_pdfs = os.getcwd()
# convert_pdf_image()


##*********************FUNCTIONS***********************##

# This functions converts the pdf to images

def convert_pdf_image():
    """This function converts the PDF into Images"""

    p2i.convert_pdf()


# This Function converts a single file and store it in the directory

def convert_file(image, file_name, folder_name):
    """This Function is used to convert the Image stored in Converted PDFs directory and store them as texts
       in the Converted OCR Text directory.This returns A file"""

    result = pytesseract.image_to_string(image)
                            # subfolder_dir,                                filename
    file = open(os.path.join(os.path.join(Ocr_directory, folder_name), f"{os.path.splitext(file_name)[0]}" + ".txt"),
                'w')
    file.write(result)
    file.close()
    return file


# This Function convers from a given path and store in the directory

def convert_from_path():
    img_file = Image.open(files.path)
    convert_file(img_file, files.name, entry.name)


main_directory = os.getcwd()  # Main Directory
if not os.path.exists(os.path.join(main_directory, "Converted OCR Text")):  # Checks Whether Directory exists or not
    os.mkdir("Converted OCR Text")
Ocr_directory = os.path.join(main_directory, "Converted OCR Text")  # Directory Of OCR Texts
os.chdir(os.path.join(os.getcwd(), "Converted PDFs"))
converted_pdfs = os.getcwd()

if __name__ == '__main__':
    convert_from_path()
