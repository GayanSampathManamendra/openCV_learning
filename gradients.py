import  cv2
import  numpy as np

capture=cv2.VideoCapture(0)

while True:

    ret , frame=capture.read()

    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    soblex=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobley=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(frame,100,200)

   # cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',soblex)
    cv2.imshow('sobely',sobley)
    cv2.imshow('sobely edges',edges)

    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break


cv2.destroyAllWindows()
capture.release()