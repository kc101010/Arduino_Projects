# SAFESYS 0 - Camera Management Module
# Capturing video from webcam w/ opencv 
# Written by Kyle Christie xx/7/2020

#library imports
import numpy as np                 # needed for opencv to work
import cv2                         # opencv module for camera manipulation/usage
from datetime import datetime      # datetime used when naming files
import winsound                    # winsound to allow beeping
import os                          # os module used for file management

cap = cv2.VideoCapture(0)

# Capture frame-by-frame
ret, frame = cap.read()
font = cv2.FONT_HERSHEY_SIMPLEX
    
#write text and place a red circle on the camera GUI
gray = cv2.putText(frame ,'You have been caught!',(10,100), font, 1,(0,0,0),2,cv2.LINE_AA)
cv2.circle(frame,(575,75), 63, (0,0,255), -1)

# try to create folder - handle error (implemented to clean up working directory/have a dedicated area for safesys alerts)
try:    
    os.mkdir("Safesys Captures")
except:
    print("Folder already exists")
 
#use date/time to generate part of the filename
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
        
winsound.Beep(500,200)
    
#concat date/time into the below text to create the filename
file_name = "Safesys Captures/safesys_alert_" + current_time + ".png"
print("Saving... " + file_name)
    
winsound.Beep(300,200)
    
#save the image to current dir
cv2.imwrite(file_name, frame)
    
winsound.Beep(200,200)
   
#Show the UI & img to the user
cv2.imshow('frame', gray)   
     
# When everythings done, release the capture
cap.release()
cv2.destroyAllWindows()
