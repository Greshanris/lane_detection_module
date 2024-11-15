# importing the library
import cv2
import numpy as np
import utils  # importing supporting file that will be created

# Creating a Function for lane_detection
def get_lane_curve(img):
    # Step1: Thresholding based on canny edge detector/ color
    img_threshold = utils.thresholding(img)
    # Step2: Warping
    # Step3: Summation of Pixels
    cv2.imshow("Thres", img_threshold)
    return None


''' Because we are making it a module 
and we want to run it by itself,
we will write this condition.
- We will check if we are running by ourselves, if this is the main script we are running
Or, it is called by another function
'''

if __name__=='__main__':
    # so, if we are running our main module, we want to run a video for testing
    cap = cv2.VideoCapture("./video/test_video.mp4")
    while True:
        # Getting Frames from this video
        success, img = cap.read()
        # To ensure the video processing stops, when there is no more frames to read.
        if not success:
            break
        # resize our image
        img = cv2.resize(img,(480,240))

        # calling the getLaneCurve after resizing
        get_lane_curve(img)
        # To show
        cv2.imshow("vid",img)
        # Delaying by 1 milisecond
        cv2.waitKey(1)