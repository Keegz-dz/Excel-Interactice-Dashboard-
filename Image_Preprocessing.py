import cv2
import numpy as np
from PIL import Image


# Loading image
def load(path: str, filename: str) -> np.ndarray:
    try:
        image = cv2.imread('/'.join([path, filename]))
        if image is None:
            raise ValueError("Failed to load image at {}".format(path))
        return image
    except cv2.error as e:
        raise RuntimeError("Error in cv2 read module: {}".format(e))


# Writing image
def write(image: np.ndarray, path: str, filename: str) -> None:
    try:
        cv2.imwrite('/'.join([path, filename]), image)
    except cv2.error as e:
        raise RuntimeError("Error in cv2 write module: {}".format(e))


# Show image
def show(path: str, filename: str) -> None:
    try:
        image = Image.open('/'.join([path, filename]))  # path specified should be with filename included
        image.show()
    except Exception as e:
        raise RuntimeError("Error in cv2 ")


# Inverted Images
def invert_img(image: np.ndarray, path: str) -> np.ndarray:
    try:
        inverted_img = cv2.bitwise_not(image)  # function to invert the colors of the original image
        # write(inverted_img, path, "inverted.jpg")
        return inverted_img
    except cv2.error as e:
        raise RuntimeError("\nError in inverting image: {}".format(e))


# Binarization
def binarization(image: np.ndarray, path: str) -> np.ndarray:
    try:
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converts the image from BGR (blue-green-red) to grayscale
        _, im_bw = cv2.threshold(gray_img, 200, 230, cv2.THRESH_BINARY)  # resulting binary image is stored in 'im_bw'
        # write(im_bw, path, "bw_image.jpg")
        return im_bw
    except cv2.error as e:
        raise RuntimeError("\nError in binarizing image : {}".format(e))


# Noise Removal
def noise_removal(image: np.ndarray, path: str) -> np.ndarray:  # Binarisation needs to be performed prior
    try:
        kernel = np.ones((1, 1), np.uint8)
        # creates a 1x1 square kernel with all values set to 1 using the NumPy ones function
        # The kernel defines the size and shape of the neighborhood of pixels around a given pixel, which is used to
        # calculate the new value of that pixel after the operation is performed
        image = binarization(image, path)
        no_noise = cv2.medianBlur(
            cv2.morphologyEx(cv2.erode(cv2.dilate(image, kernel, iterations=1), kernel, iterations=1), cv2.MORPH_CLOSE,
                             kernel), 3)
        # write(no_noise, path, "no_noise.jpg")
        return no_noise
    except cv2.error as e:
        raise RuntimeError("\nError in noise removal : {}".format(e))


# Dilation and Erosion
def thin_font(image: np.ndarray, path: str) -> np.ndarray:
    try:
        kernel = np.ones((2, 2), np.uint8)
        eroded_img = cv2.bitwise_not(cv2.erode(255 - image, kernel, iterations=1))
        # before applying cv2.erode, the input image is inverted using 255 - image
        # write(eroded_img, path, "eroded_img.jpg")
        return eroded_img
    except cv2.error as e:
        raise RuntimeError("\nError in erosion : {}".format(e))
