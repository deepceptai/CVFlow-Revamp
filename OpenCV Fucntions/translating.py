import cv2 as cv
import numpy as np
import random
def translate( img, x, y):
    trasnMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, trasnMat, dimensions)

def roatation(img, angle, rotPoint=None):
    (height,width) = img.shape
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle=angle,scale=1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

def resize(img):
    return cv.resize(img, (img.shape[1]//5,img.shape[0]//5), interpolation=cv.INTER_CUBIC)

def flip(img):
    i = random.randint(0,6)
    if i<2:
        return cv.flip(img, 1)
    elif 2<=i<=3:
        return cv.flip(img, 0)
    else:
        return cv.flip(img, -1)
    
# img = cv.imread("C:\\Users\\rjdis\\OneDrive\\Documents\\digital art\\katana.jpg")
# img = resize(img)
# img = flip(img)
# cv.imshow("flip", img)
# cv.waitKey(0)