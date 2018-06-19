import cv2 
import numpy as np 
import imutils

capture = cv2.VideoCapture(1) # real_drone_feed.mp4

# cv2.namedWindow('main', cv2.WINDOW_NORMAL)
first_frame = None
frame_count = 0
while capture.isOpened(): 
    ret, frame_c = capture.read()
    frame_c = cv2.resize(frame_c, (300,300))
    frame = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (35,35),0)
   
    cv2.imshow('Feed (Gray)', frame)
    
    if frame_count % 100 == 0 or first_frame is None:
        first_frame = frame

    frame_delta = cv2.absdiff(first_frame, frame)
    cv2.imshow('Frame delta', frame_delta)
    
    threshold = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations=2) #dilate the image to fill holes
    cv2.imshow('Threshold', threshold)

    contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if imutils.is_cv2() else contours[1]

    for cnt in contours:
        if cv2.contourArea(cnt) < 500:
            continue 
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame_c, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow("Tracking",frame_c)

    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# out.release()
capture.release()
cv2.destroyAllWindows()
