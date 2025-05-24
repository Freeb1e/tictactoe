import numpy as np
import random
import pyuart
board=[
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
tree=[]
step=0
x,y=0,0
empty=[]
movex=''
# find_empty：检查棋盘上的空位
def find_empty(board):
    empty=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                empty.append((i,j))
    return empty

# minimax：进行回溯搜索，推测后面所有的可能性
# 使用'X'表示电脑，用'O'表示玩家行为
# 返回1表示电脑获胜，返回-1表示玩家获胜，返回0表示平局
# mode表示当前行动的一方，'X'表示电脑，'O'表示玩家
def minimax(mode,top):
    if is_win(board,'X'):
        return 1
    elif is_win(board,'O'):
        return -1
    elif len(find_empty(board))==0:
        return 0
    scores=[]
    moves=[]

    for i,j in find_empty(board):
        if mode=='X':
            board[i][j]='X'
            score=minimax('O',False)
            board[i][j]=' '
            scores.append(score)
            moves.append((i,j))
        else:
            board[i][j]='O'
            score=minimax('X',False)
            board[i][j]=' '
            scores.append(score)
            moves.append((i,j))
    if mode=='X':#电脑行动，选择有利的走法
        max_score=max(scores)
        best_moves = [moves[i] for i in range(len(scores)) if scores[i] == max_score]
        x,y = random.choice(best_moves)
        if top:
            board[x][y]='X' 
            #move=f"{x}{y}"
            move = 3*x+y+1
           # pyuart.send_message_once(str(move))
            print('send:',move)
            return move
            #print('choose:',i+1,j+1)
            #for i in range(len(scores)):
               # print(scores[i],'zuobiao:',moves[i][0]+1,moves[i][1]+1)          
        else:
            return max_score
    else :
        min_score=min(scores)
        #min_index=scores.index(min_score)
        #x,y=moves[min_index]
        return min_score
        

# is_win：判断是否有一方获胜
def is_win(board,player):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return True
        if board[0][i]==board[1][i]==board[2][i]==player:
            return True
    if board[0][0]==board[1][1]==board[2][2]==player:
        return True
    if board[0][2]==board[1][1]==board[2][0]==player:
        return True
    return False

# print_board：打印棋盘
def print_board():
    for i in range(3):
        print(' ---'*3)
        print('| '+board[i][0]+' | '+board[i][1]+' | '+board[i][2]+' |')
    print(' ---'*3)
    for i in range (3):
        for j in range(3):
            print('N' if board[i][j] == ' ' else board[i][j],end='')
    print()

def put_chess(x,y,player):
    board[x][y]=player


def input_board(board_ob):
    SOURCE = False
   
    while True:
        if SOURCE: 
            print("请输入棋盘的状态，顺次输入9个字符（'X', 'O', 或'N' 表示空格），例如：'XOXONXNNN'")
            board_input = input("输入棋盘状态: ").strip().replace('N', ' ')
        else :
            board_input = board_ob
        if len(board_input) == 9 and all(cell in ['X', 'O', ' '] for cell in board_input):
            new_board = [
                [board_input[0], board_input[1], board_input[2]],
                [board_input[3], board_input[4], board_input[5]],
                [board_input[6], board_input[7], board_input[8]],
            ]
            return new_board
        else:
            print("输入无效，请确保输入9个字符，只能是 'X', 'O' 或 'N'。")




#主函数


def one_step(board_ob):
    global board
    board=input_board(board_ob)
    if is_win(board,'O'):
        print('O win')
        print_board()
        return
    # 9个空位,先手下棋
    if len(find_empty(board))==9:
        x,y=random.choice([(0,0),(0,2),(2,0),(2,2)])
        board[x][y]='X'
        move = 3*x+y+1
       # pyuart.send_message_once(str(move))
    else :
       move= minimax('X',True)
    if is_win(board,'X'):
        print('X win')
        print_board()
        return str(move)
    print_board()
    return str(move)


#while True:
   # one_step('NNNNNNNNN')
'''
while True:
    input_valid=False
    Firststep=True
    offensive=input('Do you want to go first? (y/n)')
    if offensive=='y':
    attack=False
else:
    attack=True
    if attack:
        if len(find_empty(board))==0:
            print('Tie')
            break
        if Firststep:
            x,y=random.choice([(0,0),(0,2),(2,0),(2,2)])
            board[x][y]='X'
            Firststep=False
        else:
            minimax('X',True)
        input_valid=False
        print_board()
        if is_win(board,'X'):
            print('X win')
            break
        #board=input_board()
            
        while not input_valid:
            x=int(input('input x:'))-1
            y=int(input('input y:'))-1
            if board[x][y]==' ':
                board[x][y]='O'
                input_valid=True
            else:
                print('invalid input')
                continue
            
        if is_win(board,'O'):
            print('O win')
            break

    else:
        if Firststep:
            print_board()
            Firststep=False
        input_valid=False
        while not input_valid:
            x=int(input('input x:'))-1
            y=int(input('input y:'))-1
            if board[x][y]==' ':
                board[x][y]='O'
                input_valid=True
            else:
                print('invalid input')
                continue
        if len(find_empty(board))==0:
            print('Tie')
            break
        if is_win(board,'O'):
            print('O win')
            break
        minimax('X',True)
        print_board()
        if is_win(board,'X'):
            print('X win')
            break
'''

    


    