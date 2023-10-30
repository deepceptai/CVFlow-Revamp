import cv2 as cv
from basic import *
from translating import *

vid = cv.VideoCapture(0)
t = 0
while t < 200:
    isTrue, frame = vid.read()
    if (t<100):
        gre(frame)
        blu(frame)
    elif (101<t<200):
        erode(frame)
        gre(frame)
        flip(frame)

    elif (201<t<300):
        resize(frame)
        roatation(frame, 90)
        gre(frame)
        
    elif (301<t<400):
        blu(frame)
        translate(frame, 100,300)

    else:
        blu(frame)
        erode(frame)
        flip(frame)
        translate(frame)
    
    cv.imshow("vid",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()