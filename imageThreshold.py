import cv2
import  numpy as py

img=cv2.imread('test.jpg')
retval, thereshold=cv2.threshold(img,200,255,cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval1, thereshold1=cv2.threshold(grayscaled,120,255,cv2.THRESH_BINARY)

gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)


cv2.imshow('thereshold',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()