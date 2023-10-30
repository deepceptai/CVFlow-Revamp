import cv2 as cv,cv2
import os
import time

def rescaleFrame(frame, scale=0.75):
    # for All 
    width = int(1280)
    height = int(720)
    dim = (width,height)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

def changeRes(weidth, height):
    #will only work for live 
    vid.set(3,weidth)
    vid.set(4,height)
#   ===============================================================================================
#                               Image dispslaying and resize=ing
#   ===============================================================================================
# img = cv.imread("C:\\Users\\rjdis\\OneDrive\\Desktop\\wallpaper\\sci-fi\\chin-fong-sakura-2k.jpg")
# imgre = rescaleFrame(img)
# cv.imshow('scifi',img)
# cv.imshow('scifi rescale',imgre)
# cv.waitKey(5000)

#   ===============================================================================================
#                               Video Playing
#   ===============================================================================================
vid = cv2.VideoCapture(0)
i = 199
while(i):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i -= 1
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
v=0
# v=1
if v == 1:
    vid = cv.VideoCapture("C:\\Users\\rjdis\\Music\\Music\\neffex\\Badshah - Paagal ( 1080 X 1920 ).mp4")
    # vid = cv.VideoCapture(0)
    n=0
    start = time.localtime()
    
    while n<1000:
        isTrue, frame = vid.read()
        frame_resized = rescaleFrame(frame)

        cv.imshow('video', frame)
        cv.imshow('Video Resized',frame_resized)

        if cv.waitKey(24) & 0xff == ord('d'):
            break
        n+=1

    end = time.localtime()
    print(end.tm_sec-start.tm_sec)
    vid.release()
    cv.destroyAllWindows()
