#!/usr/bin/python
# -*- coding:UTF－8 -*-
import os
import random

def computer_first():
    chess= board_chess()
    ai = computerplayer( chess._chess_board)
    chess._chess_board[5][5]=1


    while(True):
        print( chess.t_ui_print())
        while(True):
            
            print("Enter The Position of Movement(x y) or\nEnter 0 For Quit The Game")
            
            uinput  = input()
            move = uinput.split(' ')
            
            
            if (uinput  == "0"):
                print ('You Choose Quit The Game')
                return 0
            else:
                if len(move) == 2 and len(move[0]) == 1 and len(move[1]) == 1 :
                    row = int(move[0])
                    col = int(move[1])
                    if row>=0 and row< g_rows and col>=0 and col<g_cols:
                        if(chess._chess_board[row][col] == 0):
                            chess._chess_board[row][col] = 2
                            break
                        else:
                            print ("Cann't Put Chess Here,Has One Already")
                            continue
                    else:
                        print( "Invalid Input")
                        continue
                else:
                    print( "Invalid Input, Try Again")
                    continue

        if(chess.judge_over(player_)): #user wins
            print (chess.t_ui_print())
            print ("Congratulation!")
            print("Do You Want to Play Again??")
            print('1.Yes\n2.No\n')
            inp=int(input())
            if(inp==int(1)):
                play=True
            else:
                play=False
            return play

        print ("Computer's Turn")
        #ai = computerplayer( chess._chess_board)
        score,step = ai._calc_good_postion()
        print (score,step)
        chess._chess_board[score][step] = 1

        if(chess.judge_over(computer_)): #PC wins
            print (chess.t_ui_print())
            print ("Computer Win!")
            print("Do You Want to Play Again??")
            print('1.Yes\n2.No\n')
            inp=int(input())
            if(inp==int(1)):
                play=True
            else:
                play=False
            return play

g_temp_a = 100000
g_temp_b = 10000
computer_ = 1
player_ = 2
g_temp_c = 1000
g_temp_d = 100
g_temp_e = 10
g_rows = 10
g_cols = 10
g_temp_f = 1000
g_temp_g = 100
g_temp_h = 10

class computerplayer:
    def __init__(self,_chess_board):    
        self.depth = 1
        self.color = 1            
        self._chess_board = _chess_board
        self._move_well = (-10,-10)
        self.step = ( (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1) )

    def next_postions(self):
        steps = []
        for i in range(g_rows):
            for j in range(g_cols):
                if(self._chess_board[i][j] != 0):
                    continue
                flag = False 
                for k in self.step:
                    if((i+k[0])>=0 and (i+k[0])<10 and(j+k[1]>=0) and (j+k[1]<10) and self._chess_board[i+k[0]][j+k[1]] != 0):
                        flag = True
                        break
                if(flag == False):
                    continue
                steps.append([i,j])
        return steps

    def computer_calc(self,color,next_color):
        str_board = self.board_to_str()
        temp_a = 0
        temp_b = 0
        for i in str_board:
            if(str(next_color)*5 in i):
                return -g_temp_a;
            if(str(color)*5 in i):
                return g_temp_a

            temp_b += 3 * g_temp_b*0.5 * i.count(str(color)*2 + '0' + str(color)*2)
            temp_b += 3 * g_temp_b*0.5 * i.count(str(color) + '0' + str(color) * 3)
            temp_a += g_temp_b * i.count('0' + str(next_color) * 4 + '0')
            temp_b += 3 * g_temp_b*0.5 * i.count(str(color)*3 + '0' + str(color))#11101
            temp_b += 3 * g_temp_c*0.5 * i.count('0' + str(color) +'0'+str(color)*2+'0')
            temp_b += 3 * g_temp_c*0.5 * i.count('0' + str(color)*2+'0'+str(color)+'0')
            temp_b += 3 * g_temp_b * i.count('0' + str(color) * 4 + '0')  
            temp_b += 3 * g_temp_c * i.count('0' + str(color) * 3 + '0') 
            temp_a += g_temp_c * i.count('0' + str(next_color) * 3 + '0') 
            temp_b += 3 * g_temp_d * i.count('0' + str(color) * 2 + '0')  
            temp_b += 3 * g_temp_e * i.count('0' + str(color) * 1 + '0')  
            temp_a += g_temp_d * i.count('0' + str(next_color) * 2 + '0')  
            temp_a += g_temp_e * i.count('0' + str(next_color) * 1 + '0')  
            temp_b += 13 * g_temp_f * (i.count(str(next_color) + str(color) * 4 + '0') + i.count('0' + str(color) * 4 + str(next_color)))
            temp_a += g_temp_f * (i.count(str(color) + str(next_color) * 4 + '0') + i.count('0' + str(next_color) * 4 + str(color)))
            temp_a += g_temp_g * (i.count(str(color) + str(next_color) * 3 + '0') + i.count('0' + str(next_color) * 3 + str(color)))
            temp_b += 3 * g_temp_g * (i.count(str(next_color) + str(color) * 3 + '0') + i.count('0' + str(color) * 3 + str(next_color)))
            temp_b += 3 * g_temp_h * (i.count(str(next_color) + str(color) * 2 + '0') + i.count('0' + str(color) * 2 + str(next_color)))    
            temp_a += g_temp_h * (i.count(str(color) + str(next_color) * 2 + '0') + i.count('0' + str(next_color) * 2 + str(color)))
  
        return temp_b - temp_a


    def computer_search_deep(self,color,next_color,depth):
        if(depth<=0):
            score = self.computer_calc(color,next_color)
            return score
        score = self.computer_calc(color,next_color)
        if(abs(score) >= g_temp_a):
            return score
        temp_s_c = -10000
        steps = self.next_postions()
        if(len(steps)<=0):
            self._move_well = [7,7]
            return
        _move_well = steps[0]
        for row,column in steps:
            self._chess_board[row][column] = color
            score = -self.computer_search_deep(next_color,color,depth-1)
            self._chess_board[row][column] = 0
            if(score > temp_s_c):
                temp_s_c = score
                _move_well = (row,column)

        if(depth == self.depth):
            self._move_well = _move_well

        return temp_s_c


    def _calc_good_postion(self):
        temp_s_c = self.computer_search_deep(1,2,self.depth)
        return self._move_well
    def board_to_str(self):
        b_s = ''
        for row in self._chess_board:
            for column in row:
                b_s += str(column)
        str_board = []
        lg = len(b_s)
        i = 0
        while(i<g_cols*g_rows):
            str_board.append(b_s[i:i+g_cols])
            i = i+g_cols
        i = 1
        while(i<g_cols):
            str_board.append(b_s[i:lg:g_cols])
            i += 1
        i = 4
        while(i<g_cols):
            str_board.append(b_s[i:i*g_cols+1:g_cols-1])
            i += 1
        i = 1
        while(i<g_rows-4):
            str_board.append(b_s[(i+1)*g_cols-1:lg:g_cols-1])
            i += 1
        i = 0
        while(i<g_cols-4):
            str_board.append(b_s[i:(g_rows-i)*g_cols:g_cols+1])
            i += 1
        i = 1
        while(i<g_rows-4):
            str_board.append(b_s[i*g_cols:lg:g_cols+1])
            i += 1

        return str_board


    
class board_chess:
    def __init__(self):
        
        self._chess_board = [[0 for i in range(g_rows)] for j in range(g_cols)]

    def t_ui_print(self):
        b = 0
        tag = ['.', '1', '0']
        a = '  0 1 2 3 4 5 6 7 8 9\n'
        row = []
        indx = 0
        while indx < len(self._chess_board):
            row = self._chess_board[indx]
            line = ' '.join([tag[n] for n in row])
            a += chr(ord('0')+b)+' '+line+'\n'
            indx += 1
            b += 1
        return a

    def judge_over(self,color):
        dirs = ((0,1),(1,-1),(1,0),(1,1))
        i = 0
        while i < g_cols:
            j = 0
            while j < g_cols:
                if(self._chess_board[i][j] != color):
                    j += 1
                    continue
                indxdir = 0
                while indxdir < len(dirs):
                    dir = dirs[indxdir]
                    flag = True
                    xrow = i
                    xcol = j
                    count = 0
                    while count < 4:
                        xrow += dir[0]
                        xcol += dir[1]
                        if(not (xrow>=0 and xrow< 10 and xcol>=0 and xcol<10)):#
                            flag = False
                            break
                        if(self._chess_board[xrow][xcol] != color):
                            flag = False
                            break
                        count += 1
                    if(flag == True):
                        return True
                    indxdir += 1
                j += 1
            i += 1
        return False

if __name__ == "__main__":
    play=True
    while(play):
        print("------------start-------------")
        print('Do you want to play first??')
        print('1.Yes\n2.No\n')
        move1=int(1)
        cnt=int(0)
        game = True
        start=int(input())
        if(start==1):
            while(move1):
                
                if(move1==1):
                    chess=board_chess()
                    
                    print( chess.t_ui_print())
                    
                    print("Enter The Position of Movement(x y) or\nEnter 0 For Quit The Game")
                    
                    uinput  = input()
                    move = uinput.split(' ')
                    
                    
                    if (uinput  == "0"):
                        print ('You Choose Quit The Game')
                        break
                    else:
                        if len(move) == 2 and len(move[0]) == 1 and len(move[1]) == 1 :
                            row = int(move[0])
                            col = int(move[1])
                            if(row==int(5)):
                                cnt=int(cnt)+int(1)
                            if(col==int(5)):
                                cnt=int(cnt)+int(1)
                                
                            if row>=0 and row< g_rows and col>=0 and col<g_cols:
                                if(chess._chess_board[row][col] == 0):
                                    chess._chess_board[row][col] = 2
                                    move1=int(move1)+int(1)
                                    #break
                                else:
                                    print ("Cann't Put Chess Here,Has One Already")
                                    move1=int(1)
                                    #continue
                            else:
                                print( "Invalid Input")
                                move1 =int(1)
                                #continue
                        else:
                            print( "Invalid Input, Try Again")
                            move1 = int(1)
                    #chess1= board_chess1
                    #chess=board_chess()
                    print('Here')
                    print( chess.t_ui_print())
                    ai = computerplayer( chess._chess_board) 
                    if(cnt==int(2)):
                        score,step = ai._calc_good_postion()
                        print (score,step)
                        chess._chess_board[score][step] = 1
                        print( chess.t_ui_print())
                    else:
                        chess._chess_board[5][5]=1
                        print('ai')
                        print( chess.t_ui_print())
                        
                        
                    
                     
                    
                    #print( chess.t_ui_print())                     # continue
                else: 
                    
            
                    while(game):
                        
                        #chess = board_chess()
                        #print( chess.t_ui_print1())
                        #ai = computerplayer( chess._chess_board) 
                        while(True):
                            
                            print("Enter The Position of Movement(x y) or\nEnter 0 For Quit The Game")
                            
                            uinput  = input()
                            move = uinput.split(' ')
                            
                            
                            if (uinput  == "0"):
                                print ('you choose quit the game')
                                game=False
                                break
                            else:
                                if len(move) == 2 and len(move[0]) == 1 and len(move[1]) == 1 :
                                    row = int(move[0])
                                    col = int(move[1])
                                    if row>=0 and row< g_rows and col>=0 and col<g_cols:
                                        if(chess._chess_board[row][col] == 0):
                                            chess._chess_board[row][col] = 2
                                            print( chess.t_ui_print())
                    #ai = computerplayer( chess._chess_board) 
                                            break
                                        else:
                                            print ("cann't put chess here,has one already")
                                            continue
                                    else:
                                        print( "invalid input")
                                        continue
                                else:
                                    print( "invalid input, try again")
                                    continue
                        
                        if(game==False):
                            break
                    
                        if(chess.judge_over(player_)): #user wins
                            print (chess.t_ui_print())
                            print ("Congratulation!")
                            print("Do You Want to Play Again??")
                            print('1.Yes\n2.No\n')
                            inp=int(input())
                            if(inp==int(1)):
                                play=True
                            else:
                                play=False
                            game=False
                        print ("Computer's Turn")
    
                        #ai = computerplayer( chess._chess_board)
                        score,step = ai._calc_good_postion()
                        print (score,step)
                        chess._chess_board[score][step] = 1
                        print( chess.t_ui_print())
                        
                        if(chess.judge_over(computer_)): #PC wins
                            print (chess.t_ui_print())
                            print ("Computer Win!")
                            print("Do You Want to Play Again??")
                            print('1.Yes\n2.No\n')
                            inp=int(input())
                            if(inp==int(1)):
                                play=True
                            else:
                                play=False
                            game=False
                    if(game==False):
                        break
                    
    
                    
    
            
        elif(start==2):
            f= computer_first()
            if(f==True):
                play=True
            else:
                play=False
            
        
        
    #computer_first()

