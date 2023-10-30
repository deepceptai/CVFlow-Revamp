import cv2 as cv

img = cv.imread("C:\\Users\\rjdis\\OneDrive\\Desktop\\wallpaper\\models\\blonde.jpg")
img = cv.resize(img, (img.shape[1]//2,img.shape[0]//2), interpolation=cv.INTER_AREA)

cv.imshow("My gf", img)
# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray",img)
img = cv.Canny(img, 125,175)
cv.imshow("canny",img)

contours, heirarchy = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} found")

cv.waitKey(0)