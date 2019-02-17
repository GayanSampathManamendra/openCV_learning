import cv2
import  numpy as np

img1=cv2.imread('test.jpg')
img2=cv2.imread('test2.jpg')

#add= (img1 + img2)

add=cv2.add(img1,img2)
weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)

rows,cols,channels=img1.shape 
roi=img1[:rows,0:cols]

img12gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img12gray,130,200,cv2.THRESH_BINARY_INV)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()