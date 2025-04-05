import cv2
import numpy as np
import utlis
#cv2.resize(src, dsize, dst=None, fx=0, fy=0, interpolation=cv2.INTER_LINEAR)


webcam = True
path='5.jpg'
cap=cv2.VideoCapture(1)
#cap.set(3,1280)
#cap.set(4,720)
#wP=210
#hP=297
hP=300
wP=300
scale=3 

#cap.set(10,1000)
while True:
    if (webcam):success,img = cap.read()
    else: img = cv2.imread(path)
   # print(img.shape)
    img,conts = utlis.getContours(img,showCanny=True,draw=True,minArea=500,filter=4) 
    cv2.imshow("org0", img)
    
    if len(conts) != 0:
        biggest = conts[0][2]
        print(biggest)
        imgWarp = utlis.warpImg(img,biggest,wP,hP)
        cv2.imshow('A4',imgWarp)
        utlis.findcircles(imgWarp)
    img = cv2.resize(img, (0,0),None,0.5,0.5)
    

    cv2.imshow("org", img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.waitKey(200)
    #break




