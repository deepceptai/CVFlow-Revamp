import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\rjdis\\OneDrive\\Desktop\\wallpaper\\sci-fi\\wallpaperflare.com_wallpaper (3).jpg")

width = int(1280)
height = int(720)
dim = (width,height)

img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

# blank = np.zeros((500,500,3), dtype='uint8')
# blank[200:400,200:400] = 30,25,10

cv.rectangle(img,(0,0), (255,255), (0,0,255), thickness=2)
# cv.imshow('blank',img)
cv.circle(img, (250,250), 40, (0,220,0), thickness=1)
cv.line(img, (0,0), (250,250), (45,0,54), thickness=2)

cv.putText(img, "This is the beginning", (225,255),cv.FONT_HERSHEY_COMPLEX ,1.0,(225,225,255),5)
cv.imshow('blank',img)
cv.waitKey(0)