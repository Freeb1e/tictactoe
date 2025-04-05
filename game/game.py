import numpy as np
import random
board=[
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
global step
tree=[]
step=0
x,y=0,0
empty=[]


def print_board():
    for i in range(3):
        print(' ---'*3)
        print('| '+board[i][0]+' | '+board[i][1]+' | '+board[i][2]+' |')
    print(' ---'*3)

def offensive(step,prex=-1,prey=-1):
    global tree
    if step==0:
        #x0,y0=random.choice([(0,0),(0,2),(2,0),(2,2)])
        x0,y0=2,0
        put_piece('X',x0,y0)
        return
    elif step==1:
        if prex==1 and prey==1:
            x,y=0,0 
            x,y=random.choice([(0,0),(2,2)])
            tree=1              #tree=1 人下在中心，tree=2 人下在下半区，tree=3 人下在上半区
        elif (prex,prey)==(2,2) or (prex,prey)==(2,1) or (prex,prey)==(1,2):
            print('xiabanqu')
            x,y=0,0
            tree=2
            print('prex+prey=',prex+prey)
        else:
            x,y=2,2
            tree=3
            print('prex+prey=',prex+prey)
        put_piece('X',x,y)
    elif step==2:
        if tree==2:
            if (prex,prey)!=(1,0):
                put_piece('X',1,0) 
            else:
                put_piece('X',0,2)
        if tree==3:
            if (prex,prey)!=(2,1):
                put_piece('X',2,1)
            else:
                put_piece('X',0,2)
        else:#tree=1
            universal_step()
    elif step==3:
        if tree==1:
            universal_step()
        else :
            winplace=check_canwin('X')[1]
            put_piece('X',winplace[0],winplace[1])
    else:
        universal_step()

def defensive(step,prex=-1,prey=-1):
    if step==0:
        x,y=1,1
        put_piece('X',x,y)

def universal_step():
    
    if  check_canwin('X')[0]==True:
            x,y=check_canwin('X')[1]
    elif    check_canwin('O')[0]==True:
            x,y=check_canwin('O')[1]
    elif    finddoublethreats('X')[0]==True:
            x,y=finddoublethreats('X')[1],finddoublethreats('X')[2]     
    else:
    
            findempty()
            x,y=random.choice(empty)
    put_piece('X',x,y)


def check_winner():
    # 检查行
    for row in board:
        if row[0] == row[1] == row[2] == 'X' or row[0] == row[1] == row[2] == 'O':
            return row[0]
    # 检查列
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 'X' or board[0][col] == board[1][col] == board[2][col] == 'O':
            return board[0][col]
    # 检查对角线
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][0] == board[1][1] == board[2][2] == 'O':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return board[0][2]
    return None

def check_canwin(player):
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]=player
                if check_winner()==player:
                    board[i][j]=' '
                    return True,(i,j)
                else:
                    board[i][j]=' '
    return False,None

def put_piece(player,x,y):
    if board[x][y]==' ':
        board[x][y]=player
        return True
    else:
        print('Invalid move to',x,y,'by',player,'step=',step)
        return False

def restart():
    global step
    for i in range(3):
        for j in range(3):
            board[i][j]=' '
    step=0
    return

def findempty():
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                empty.append((i,j))
    return

def countthreats(player):
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]=player
                if check_winner()==player:
                    count+=1
                board[i][j]=' '
    return count

def finddoublethreats(player):
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]=player
                if countthreats(player)>=2:
                    board[i][j]=' '
                    return True,i,j
                board[i][j]=' '
    return False,None

'''
while True:
    offensive(step,prex=x-1,prey=y-1)
    print_board()
    if check_winner()=='O':
        print('Player win!')
        restart()
        continue
    elif check_winner()=='X':
        print('Computer win!')
        restart()
        continue
    elif step==4:
        print('Tie!')
        restart()
        continue
    x=int(input('Enter x: '))
    y=int(input('Enter y: '))
    put_piece('O',x-1,y-1)
    if x==5 or y==5:
        break
    else:
        step+=1
'''

while True:
    x=int(input('Enter x: '))
    y=int(input('Enter y: '))
    put_piece('O',x-1,y-1)
    if check_winner()=='O':
        print('Player win!')
        restart()
        continue
    elif step==4:
        print('Tie!')
        restart()
        continue
    defensive(step,prex=x-1,prey=y-1)
    