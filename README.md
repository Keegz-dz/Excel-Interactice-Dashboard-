# Work Flow : 
* GUI to accept files from user 
* Selected files can be of various types 
* Converts all files into PDFs 
* Stores it in a Stored Directory
* (For each Stored PDF) : 
  * Pillow (Opens an Image) 
  * OpenCV (Transforms an Image) 
  * PyTesseract (Converts to Text) 
  * Stores Text in CSV format 
* Loads CSV files into Excel (Work in Progress)

## Library : 
Libraries to be downloaded are as follows :
1. Pillow Library - pip3 install pillow --macOS/Windows
2. OpenCV Library - pip3 install opencv-python --macOS/Windows
3. Tesseract Library - brew install tesseract --macOS
4. Pytesseract Library - pip3 install pytesseract --macOS
5. Tkinter Library - pip3 install tkinter --macOS/Windows
6. doc2pdf Library - pip3 install doc2pdf --macOS/Windows
7. customtkinter Library - pip3 install customtkinter --macOS/Windows
8. pdf2image Library - brew install pdf2image --macOS

## Preprocess Imaging Techniques  :
1. Inverted images
2. Rescaling 
3. Binarization
4. Noise Removal
5. Dilation and Erosion
6. Rotation / De-skewing 
7. Removing Borders

## Functions used in Google_drive.py :
1. **webbrowser.open_new_tab() :** is a method provided by the Python standard library's webbrowser module that opens a URL in a new tab in the user's default web browser.
2. **tk.filedialog.askopenfilename() :** is a method provided by the tkinter module in Python that opens a file dialog box and allows the user to select a file from their local system. When called, the askopenfilename() method displays a file dialog box that prompts the user to navigate their local file system and select a file. Once the user selects a file, the method returns the full path to the selected file as a string.

## Functions used in Directories.py :
1. **os.path.exists() :** is a Python built-in method that is used to check whether a file or directory exists at a specified path or not. It returns a boolean value indicating whether the file/directory exists or not.
2. **os.path.join() :** is a function from the Python os.path module that joins one or more path components (strings) intelligently. It takes one or more path components as arguments and returns a single path string. On Windows: dir1\dir2. On Unix-like systems: dir1/dir2
3. **os.getcwd() :** is a function in the Python os module that returns the current working directory as a string
4. **os.mkdir() :** This method in the os module creates a new directory at the specified path.

## Functions used in FilePdf_conv.py :
1. **os.path.basename() :** is a Python function that returns the base filename of a file path. In other words, it returns the last component of the path passed to it.
2. **os.rename() :** is used to rename a file or directory. The method takes two arguments: the current name of the file or directory and the new name that it should be renamed to
3. **doc2pdf.convert() :** is used to convert a Microsoft Word document to a PDF file using the doc2pdf library in Python.
4. **os.path.splitext() :** is a function provided by the os module in Python that splits a file path into two parts: the file's base name and its extension. The function returns a tuple containing the base name and extension of the file.
5. **tkinter.messagebox.showinfo() :** is a function in the Tkinter library in Python that displays an informational message box with a given title and message

## Functions used in ImageText_conv.py :
1. **pdf2image.convert_from_path() :** is a Python function that converts a PDF file into a sequence of PIL (Python Imaging Library) images
2. **enumerate() :** is a built-in Python function that allows you to loop over an iterable while keeping track of the index of the current element. It returns an iterator of tuples, where each tuple contains the index and the corresponding element from the iterable.

## Drawback : 
Doesn't work for handwritten documents.

