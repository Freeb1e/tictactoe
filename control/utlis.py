import cv2
import numpy as np


def getContours(img,cThr=[100,100],showCanny=False,minArea=1000,filter=-1,draw=False):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,cThr[0],cThr[1])
    kernel = np.ones((5,5))
    
    imgDial = cv2.dilate(imgCanny,kernel,iterations=3)
    imgThre = cv2.erode(imgDial,kernel,iterations=2)
    if showCanny:
        cv2.imshow('Canny',imgThre)
        #print('Canny_shape=',imgThre.shape)

    contours,hiearchy=cv2.findContours(imgThre,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    finalContours = []
    for i in contours:
        area = cv2.contourArea(i)
        if area>minArea:
            peri=cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            bbox = cv2.boundingRect(approx)
            if filter > 0:
                if len(approx) == filter:
                    finalContours.append([len(approx),area,approx,bbox,i])
            else:
                finalContours.append([len(approx),area,approx,bbox,i])
    finalContours = sorted(finalContours,key = lambda x:x[1],reverse=True)

    if draw: 
        for con in finalContours:
            cv2.drawContours(img,con[4],-1,(0,0,255),3)
    return img, finalContours


        

def recoder(mypoints):
        #print(mypoints.shape)
        mypointsNew = np.zeros_like(mypoints)
        mypoints=mypoints.reshape((4,2))
        add = mypoints.sum(1)
        mypointsNew[0] = mypoints[np.argmin(add)]
        mypointsNew[3] = mypoints[np.argmax(add)]
        diff = np.diff(mypoints,axis=1)
        mypointsNew[1]= mypoints[np.argmin(diff)]
        mypointsNew[2] = mypoints[np.argmax(diff)]
        return mypointsNew


def warpImg(img,points,w,h):
    #print(points)
    points = recoder(points)
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp


def findcircles(img,draw=True,cThr=[100,100]):
    pieces = []
    pieces_gray = []
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,cThr[0],cThr[1])
    kernel = np.ones((3,3))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=3)
    imgThre = cv2.erode(imgDial,kernel,iterations=2)
    if draw:
        cv2.imshow('precircle',imgThre)
    circles=cv2.HoughCircles(imgThre,cv2.HOUGH_GRADIENT,1,20,param1=100,param2=35,minRadius=0,maxRadius=0)
    
        # 确保至少检测到一个圆
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # 绘制圆的外圆
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # 绘制圆的中心
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
           # print(i)
            gray_light=0
            count=0
            for dx in range(-10,11):
                for dy in range(-10,11):
                    if 0 <= i[0] + dx < imgGray.shape[1] and 0 <= i[1] + dy < imgGray.shape[0]:
                        gray_light+=imgGray[i[0]+dx,i[1]+dy]
                        count+=1
            gray_light=int(gray_light/count)
            pieces.append((i[0]//100+1,i[1]//100+1,1 if gray_light>100 else -1))
            pieces_gray.append(gray_light)
            
    # 显示结果
    #for i in pieces:
        #print(i)
    boardx = np.zeros((3,3))
    for i in pieces:
        x,y,color=i
        boardx[x-1][y-1]=color

    
    cv2.imshow('detected circles', img)
    cv2.waitKey(1)
    return boardx