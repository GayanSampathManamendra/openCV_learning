import cv2
import numpy as np

capture=cv2.VideoCapture(0)


while True :

    _ , frame=capture.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,0,0])
    upper_red=np.array([255,255,255])


    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((15,15),np.float32)/225
    smoothed=cv2.filter2D(res,-1,kernel)

    blur=cv2.GaussianBlur(res,(15,15),0)
    median=cv2.medianBlur(res,15)
    bilateral=cv2.bilateralFilter(res,15,75,75)

    cv2.imshow('frame',frame)
    cv2.imshow('hsv Color frmae',hsv)
    cv2.imshow('mask frame',mask)
    cv2.imshow('res frame ',res)
   # cv2.imshow('kernel',kernel)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilatreral',bilateral)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()