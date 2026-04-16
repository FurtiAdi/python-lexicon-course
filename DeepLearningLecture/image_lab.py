import cv2
import numpy as np

#Load image
image = cv2.imread("titanic1.png")

# Check if image loaded 
if image is None:
    print("Error: Image could not be loaded!")
    exit()

# Print shape
print("Image shape:", image.shape)

"""
QUESTIONS 1-2

Whhat do the three values in shape represent?
Ans -> (height, width, channels)

Which value corresponds to height? width? channels?
Ans: 
-> shape[0] = height 
-> shape[1] = width 
-> shape[2] = channels 
"""


print("Data type:", image.dtype) # Data type: uint8

"""
QUESTIONS 3

What is the data type of the image array?
Ans ->  uint8 (unsigned 8-bit integer)

"""

# Access pixel at row 100, column 100
pixel = image[100, 100]
print("Original pixel value:", pixel)

# Modify that pixel to pure red
image[100, 100] = [0, 0, 255] # BGR format, so Red is 255 and Blue, Green are 0


"""
QUESTIONS 4-6

In what order are color values stored in OpenCV?
Ans -> BGR (Blue, Green, Red)

What happens when you set all values to maximum?
Ans -> [255,255,255] becomes white

What happens when you set all values to zero?
Ans-> [0,0,0] becomes black

"""

# Select rectangular region
# Format: image[row_start:row_end, col_start:col_end]
image[50:200, 50:200] = [255, 0, 0] # Blue

# Display  result
cv2.imshow("Modified Region Image", image)
cv2.waitKey(0)

"""
QUESTIONS 7-8

How does slicing work in NumPy for images?
Ans -> image[row_start:row_end, col_start:col_end]
        selects a block using row and column ranges

# What do the row and column ranges represent?
Ans -> Rows = height
    -> Columns = width

"""
