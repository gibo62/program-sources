import cv2     # for capturing videos
import math   # for mathematical operations
import matplotlib.pyplot as plt    # for plotting the images
#%matplotlib inline
import pandas as pd
#from keras.preprocessing import image   # for preprocessing the images
import numpy as np    # for mathematical operations
#from keras.utils import np_utils
#from skimage.transform import resize   # for resizing images
count = 0
videoFile = "D:\\10BITS_V210\\003\\V210\\ORIG\\003-2011-68\\data\\MEDIA\\3 Testigo.avi"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
#        filename ="test%d.jpg" % count;count+=1
#        cv2.imwrite(filename, frame)
        count+=1
cap.release()
print ("Done!", videoFile,count)
