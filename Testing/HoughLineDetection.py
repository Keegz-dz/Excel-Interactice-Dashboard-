# Code is to be written

import os
import cv2
import numpy as np

os.chdir("../..")
path = os.getcwd()
outputs_directory = os.path.join(os.path.join(path, "OCR"), "Outputs")
print(outputs_directory)
images_directory = os.path.join(os.path.join(path, "OCR"), "Testing Images")
print("/Users/keegz_dsouza/Documents/Excel Dashboard Visualization/mini-project/OCR/Testing Images")

os.chdir(images_directory)

image = cv2.imread("tables.png")
base_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)[1]
threshAbs = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 1)
inv = cv2.bitwise_not(threshAbs)
# cv2.imshow("inverse", inv)
# cv2.waitKey(0)


def drawLineOld(lines):
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)

        x0 = a * rho
        y0 = b * rho

        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000 * (a))
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000 * (a))

        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)


def drawLines(lines):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)


# Horizontal Line Detection


horizontalStruture = cv2.getStructuringElement(cv2.MORPH_RECT, (15,
                                                                1))  # The smaller the better ksize(width,height) In the context of image processing, a kernel is a small matrix that is used to perform operations on an image
horizontal = cv2.erode(inv, horizontalStruture, iterations=2)
cv2.imwrite(os.path.join(outputs_directory, "eroded.png"), horizontal)
canny = cv2.Canny(horizontal, 175, 255)

cv2.imwrite(os.path.join(outputs_directory, "CannyH.png"), canny)
# cv2.waitKey(0)

linesH = cv2.HoughLinesP(canny, 1, np.pi / 180, 200)
drawLines(linesH)

# Vertical Line Detection


verticalStruture = cv2.getStructuringElement(cv2.MORPH_RECT, (1,
                                                              15))  # The smaller the better ksize(width,height) In the context of image processing, a kernel is a small matrix that is used to perform operations on an image
vertical = cv2.erode(inv, verticalStruture, iterations=2)
canny = cv2.Canny(vertical, 175, 255)

cv2.imwrite(os.path.join(outputs_directory, "CannyV.png"), canny)
# cv2.waitKey(0)

linesV = cv2.HoughLinesP(canny, 1, np.pi / 180, 200)

drawLines(linesV)

# Writing The Detected Lines Image


cv2.imwrite(os.path.join(outputs_directory, "LineDetection.png"), image)
# cv2.waitKey(0)
