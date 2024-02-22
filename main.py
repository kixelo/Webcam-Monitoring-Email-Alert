import time

import cv2
import time

video = cv2.VideoCapture(1) # 0 - one camera, 1 - secondary usb camera, 2
time.sleep(1)     # to avoid camera blackframes we will wait one second to start the cam

first_frame = None

while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)  # amount of blurness
    #cv2.imshow("My video", gray_frame_gau)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    #cv2.imshow("My video", delta_frame)

    thresh_frame = cv2.threshold(delta_frame, 65, 255, cv2.THRESH_BINARY)[1] # 30 is threshold
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000: # 10000 pixels
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)  # color of rectangle (0, 255, 0) -->> green, 3 is width

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break


video.release()