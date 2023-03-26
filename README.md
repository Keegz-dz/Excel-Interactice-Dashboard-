# Work Flow : 
Pillow (Open an image) -> OpenCV (Change an image) -> PyTesseract (OCR an image)

## Library : 
Libraries to be downloaded are as follows :
1. Pillow Library - pip3 install pillow --macOS/Windows
2. OpenCV Library - pip3 install opencv-python --macOS/Windows
3. Tesseract Library - brew install tesseract --macOS
4. Pytesseract Library - pip3 install pytesseract --macOS

## Preprocess Imaging Techniques  :
1. Inverted images
2. Rescaling 
3. Binarization
4. Noise Removal
5. Dilation and Erosion
6. Rotation / De-skewing 
7. Removing Borders


## Functions used in Image_Preprocessing.py :
1. **thresh_val, threshold_img = cv2.threshold(gray_img, 200, 230, cv2.THRESH_BINARY) :** Pixels with a value greater than or equal to the threshold value are set to the maximum value, while pixels with a value less than the threshold value are set to 0. In this code, the threshold value is set to 200, the maximum value is set to 230
**Note :** *cv2.THRESH_BINARY* produces a binary image where pixel values are either 0 or 255, based on whether they are below or above the threshold value respectively.
The INV in *THRESH_BINARY_INV* stands for inverse, which means the thresholding operation is applied in reverse.
*THRESH_OTSU* is a thresholding method in OpenCV used to automatically determine an optimal threshold value for a given input image
2. **kernel = np.ones((1, 1), np.uint8) :** Creates a 1x1 square kernel with all values set to 1 using the NumPy ones function.
3. **image = cv2.dilate(image, kernel, iterations=1) :** Dilates the image using the kernel defined earlier to thicken the foreground regions and merge nearby regions together.
4. **image = cv2.erode(image, kernel, iterations=1) :** Erodes the image using the same kernel to shrink the foreground regions and remove small white noise pixels.
5. **image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel) :** Applies a morphological closing operation using the same kernel to fill in gaps in the foreground regions and smooth out the edges.
**Note :** cv2.MORPH_CLOSE can be used to remove small holes in the foreground and small protrusions on the foreground. It can also be used to close small gaps between the foreground.
6. **image = cv2.medianBlur(image, 3) :** Applies a median filter with kernel size 3x3 to remove remaining salt-and-pepper noise from the image.
7. **Image.copy()** is a method used in OpenCV to create a copy of an input image. It creates a new image with the same pixel values as the input image, allowing you to modify the new image without affecting the original one. 
8. **cv2.GaussianBlur() :** is a method in OpenCV used to apply Gaussian blur to an image. Gaussian blur is a type of image blur that is commonly used to reduce noise and smooth an image
9. **contour, hierarchy = cv2.findContours() :** is a method in the OpenCV library used for detecting and extracting contours from an image. Contours are the boundaries of an object in an image, represented as a sequence of points along the object's outline
**Note :** *cv2.RETR_LIST* It specifies that all the contours in the image will be retrieved and no hierarchical relationships between them will be created. This means that each contour will be treated as a separate, independent object.
The *cv2.CHAIN_APPROX_SIMPLE* method approximates a contour by removing all redundant points along a straight line segment and retaining only the end points of the segment.
*cv2.contourArea* is a function in OpenCV that calculates the area of a contour. It takes the contour as its argument and returns a floating-point value that represents the area enclosed by the contour.
10. **cv2.rectangle() :** is a function in OpenCV used to draw a rectangle on an image. It takes five arguments:
image: The input image on which the rectangle is to be drawn.
(x,y): The top-left corner of the rectangle.
(w, h): The bottom-right corner of the rectangle.
(b,g,r): The color of the rectangle, the values of blue, green, and red.
thickness: The thickness of the rectangle line in pixels.
11. **cv2.boundingRect(c) :** is a function in OpenCV that computes the minimum bounding rectangle (aligned with the x and y axes) that contains all the points of a contour c. The function takes a single argument, which is the contour c.
12. **The cv2.minAreaRect() :** function in OpenCV takes a contour as input and returns the minimum area rectangle that can fit around the contour.
The rectangle returned by cv2.minAreaRect() is represented as a tuple of three values:
The first value is the center coordinates of the rectangle, represented as a tuple of two floating-point values (x, y).
The second value is the dimensions of the rectangle, represented as a tuple of two floating-point values (width, height).
The third value is the angle of rotation of the rectangle, in degrees. The angle ranges from -90 degrees (lying flat on its long side) to 0 degrees (standing upright) to 90 degrees (lying flat on its short side).
13. **cv2.getRotationMatrix2D() :** is a function in OpenCV that returns the transformation matrix for rotating an image around a specified center point
14. **cv2.warpAffine() :** is a function in OpenCV used for image transformation. It applies an affine transformation to an image, which includes scaling, rotating, and translating the image. 
**Note :** *cv2.INTER_CUBIC* is a flag that specifies the interpolation method used during image transformations. 
When an image is transformed using cv2.warpAffine(), there may be areas of the output image that do not correspond to any pixel in the input image. The *cv2.BORDER_REPLICATE* method fills those areas with the values of the nearest edge pixels.

## Functions used in Pdf_to_Image.py :
1. **os.path.exists(pathname) :** is a Python function that returns True if a file or directory exists at the specified path, and False otherwise.
2. **os.path.join(directory, filename) :** is a Python function that concatenates one or more path components (directories or filenames) to form a complete path. It is used to construct file or directory paths in a platform-independent way.
3. **os.mkdir() :** is a Python function used to create a new directory (folder) with a specified name in the file system. It takes a single argument, which is the path of the directory to create.
4. **os.scandir() :** is a Python function that returns an iterator over the files and directories in a given directory.
5. **os.path.basename() :** is a Python function that returns the base name of a path. The base name is the final component of the path, after stripping all preceding directories. In other words, os.path.basename() returns the filename or directory name at the end of the path.
6. **os.path.splitext() :** is a Python function that splits a path into its base name and extension. It returns a tuple containing the base name and extension, with the extension including the dot ("."). If the path does not have an extension, the second element of the tuple will be an empty string.
7. **pdf2image.convert_from_path() :** is a Python function that converts a PDF file into a sequence of PIL (Python Imaging Library) images
8. **enumerate() :** is a built-in Python function that allows you to loop over an iterable while keeping track of the index of the current element. It returns an iterator of tuples, where each tuple contains the index and the corresponding element from the iterable.

## Drawback : 
Doesn't work for handwritten documents.

