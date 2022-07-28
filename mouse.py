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

    # Step Two find the tip of the index finger and thumb
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    # Step Three is to check if the fingers are up
    fingers = detector.fingersUp()
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
    (255, 0, 255), 2)

    # Step Four if index finger moving just move the mouse
    if fingers[1] == 1 and fingers[2] == 0:

    # Step Five get and convert coordinates
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

    # Step Six value smoothing
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

    # Step Seven will be to move the mouse
        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    # Step Eight if index and thumb finger are between a certain distance then click
    if fingers[1] == 1 and fingers[2] == 1:

    # Step Nine will be to find the distance
        length, img, lineInfo = detector.findDistance(8, 12, img)
        # print(length)

    # Step Ten click the mouse if within the value
    if length < 40:
        cv2.circle(img, (lineInfo[4], lineInfo[5]),
        15, (0, 255, 0), cv2.FILLED)
        autopy.mouse.click()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Step Eleven is to Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)


