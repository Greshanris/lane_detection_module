import cv2
import numpy as np



# Using Canny Edge Detection
def thresholding(img):
    # Grayscaling from RGB color images for faster computation
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Noise Reduction using Gaussian distribution
    ''' It calculate weights, and apply weighted average to each pixel,
        based on surrounding pixels.
        - reduces high-frequency elements and enhances image quality.
        - creates smoother images and mimizes false edges caused by noise
    '''
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Applying Canny Edge Detection
    edges = cv2.Canny(blur, 50, 150) 
    return edges

# Using colors
# def thresholding(img):
#     # convert it into HSV(Hue, Saturation, Value) space
#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     lowerWhite = np.array([0,0,0])
#     upperWhite = np.array([179,255,255])
#     # Masking or creating Mask
#     maskWhite = cv2.inRange(imgHSV,lowerWhite,upperWhite)
#     return maskWhite