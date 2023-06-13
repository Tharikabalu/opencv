import numpy as np
import cv2
img=cv2.imread('apple.jpg')
temp=cv2.imread('template.png')
h=temp.shape[0]
w=temp.shape[1]

methods=[cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for method in methods:
    img1=img.copy()
    result=cv2.matchTemplate(img1,temp,method)
    minv,maxv,minl,maxl=cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location=minl
    else:
        location=maxl
    bottom_right=(location[0]+w,location[1]+h)
    cv2.rectangle(img1,location,bottom_right,255,5)    
    cv2.imshow('Match',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
