import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    h=int(cap.get(4))
    w=int(cap.get(3))
    img=cv2.rectangle(frame,(0,0),(w,h),(255,0,0),10)
    img1=cv2.line(img,(0,0),(w,h),(0,255,0),10)
    x=int(w/2)
    y=int(h/2)
    img2=cv2.circle(img1,(x,y),x,(0,0,255),-1)#to fill color
    font=cv2.FONT_HERSHEY_SIMPLEX
    img3=cv2.putText(img2,'Tharika',(10,h-10),font,1,(0,0,0),5,cv2.LINE_AA)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
