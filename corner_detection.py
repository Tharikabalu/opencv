import cv2
import numpy as np
img=cv2.imread('download.png')
img2=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(gray,50,0.5,50)
corners1=np.int8(corners)
for corner in corners1:
    x,y=corner.ravel()
    img1=cv2.circle(img2,(x,y),5,(0,0,255),-1)
cv2.imshow('Image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()