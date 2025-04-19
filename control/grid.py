import cv2
import numpy as np
import utlis
import maxmin
#import pyuart
#cv2.resize(src, dsize, dst=None, fx=0, fy=0, interpolation=cv2.INTER_LINEAR)



webcam = True
path = 'control/5.jpg'
cap=cv2.VideoCapture(1)
#cap.set(3,1280)
#cap.set(4,720)
#wP=210
#hP=297
hP=300
wP=300
scale=3 

def print_boardob():
    for i in range(3):
        print(' ---'*3)
        print('| '+str(boardob[i][0])+' | '+str(boardob[i][1])+' | '+str(boardob[i][2])+' |')
    print(' ---'*3)

def print_board_avg():
    for i in range(3):
        print(' ---'*3)
        print('| '+str(board_avg[i][0])+' | '+str(board_avg[i][1])+' | '+str(board_avg[i][2])+' |')
    print(' ---'*3)

def gen_connect():
    result = ""
    for i in range (3):
        for j in range(3):
            result += 'X' if board_avg[i][j] > 0.5 else 'O' if board_avg[i][j] < -0.5 else ' '
    return result

board_avg = np.zeros((3,3))
#cap.set(10,1000)
while True:
    board_avg = np.zeros((3,3))
    for i in range(10):
            if (webcam):success,img = cap.read()
            else: img = cv2.imread(path)
        # print(img.shape)
            img,conts = utlis.getContours(img,showCanny=False,draw=True,minArea=500,filter=4) 
            #cv2.imshow("org0", img)
            boardob = np.zeros((3,3))
            if len(conts) != 0:
                biggest = conts[0][2]
                #print(biggest)
                imgWarp = utlis.warpImg(img,biggest,wP,hP)
                cv2.imshow('A4',imgWarp)
                boardob=utlis.findcircles(imgWarp)
                #print_boardob()
            img = cv2.resize(img, (0,0),None,0.5,0.5)
            cv2.imshow("org", img)
            cv2.waitKey(200)
            board_avg += boardob
    #break
    
    board_avg = board_avg / 10
    print_board_avg()
    connect_str=gen_connect()
    #pyuart.send_message_once(connect_str)
    print('observe',connect_str)
    maxmin.one_step(connect_str)




