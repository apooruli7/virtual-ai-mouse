import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##########################
wCam, hCam = 640, 480
frameR = 100
smoothening = 7
#########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)

while True:

    # Step One is to find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    
    # Step Two find the tip of the indez finger and thumb
    # Step Three is to check if the fingers are up
    # Step Four if index finger moving just move the mouse
    # Step Five get and convert coordinates
    # Step Six value smoothing
    # Step Seven will be to move the mouse
    # Step Eight if idex and thumb finger are between a certian distance then click
    # Step Nine will be to find the distance
    # Step Ten click the mouse if within the value

    # Step Eleven is to Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
