#! /usr/bin/env/Python38
#Written by Odiase Pedro

import cv2
import numpy as np
import datetime
from time import sleep

def Vision():
    pass
    var = cv2.VideoCapture(0)
    ret, frame1 = var.read()
    ret, frame2 = var.read()
    sleep(1)

    while var.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        buju, thresh = cv2.threshold(blur, 20, 256, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, wizkid = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)

            if cv2.contourArea(contour) < 770:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0),2)
            cv2.putText(frame1, " {}".format("Moving"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2)
        cv2.putText(frame1, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        cv2.imshow("Info", frame1)
        frame1 = frame2
        ret, frame2 = var.read()

        if cv2.waitKey(40) == 27:
            break

if __name__ == "__main__":
    Vision()

cv2.destroyAllWindows()
var.release()


