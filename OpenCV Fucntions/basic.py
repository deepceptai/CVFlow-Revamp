import cv2 as cv
img = cv.imread("C:\\Users\\rjdis\\OneDrive\\Documents\\digital art\\katana.jpg")

ratio = (img.shape[1] *20 // 100, img.shape[0] *20 // 100)
img = cv.resize(img, ratio, interpolation=cv.INTER_AREA)

# grayScale
def gre(grey):
    grey = cv.cvtColor(grey, cv.COLOR_BGR2GRAY)
    return grey
# blur
def blu(blur):
    blur = cv.GaussianBlur(blur, (17,17),cv.BORDER_DEFAULT)
    return blur
# Edge cascade
def cany(canny):
    canny= cv.Canny(canny, 1250,1706)
    return canny
# Dilating image
def dil(dia):
    dia = cv.dilate(dia , (7,7), iterations=13)
    return dia

# Erording
def erode(erode):
    erode = cv.erode(erode, (7,7), iterations=13)
    return erode

# cv.imshow('katana', img)

# cv.waitKey(0)


# ======================================= Practice =============================================
vid = cv.VideoCapture(0)
t = 1
while t<200:
    t+=1
    isTrue, frame = vid.read()
    
    if t < 15:
        frame = gre(frame)
    elif 60 > t > 30:
        frame = blu(frame)
    elif 130 >t > 100:
        frame = gre(frame)
        frame = blu(frame)
        frame = dil(frame)
    elif 200 > t > 150:
        frame = gre(frame)
        frame = erode(frame)

    cv.imshow('vid',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# cv.waitKey(0)   
vid.release()
