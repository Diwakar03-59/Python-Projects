# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 08:56:08 2020

@author: DEEPAKKUMAR
"""

from PIL import Image
import random

end = 100

def show_board():
    img = Image.open('board.jpg')
    img.show()
    
    
def reached_end(points):
    if points==end:
        return True
    else:
        return False
    
    
def check_ladder(points):
    if points==3:
        print("Ladder")
        return 20
    elif points==6:
        print("Ladder")
        return 14
    elif points==11:
        print("Ladder")
        return 28
    elif points==15:
        print("Ladder")
        return 34
    elif points==17:
        print("Ladder")
        return 74
    elif points==22:
        print("Ladder")
        return 37
    elif points==38:
        print("Ladder")
        return 59
    elif points==49:
        print("Ladder")
        return 67
    elif points==57:
        print("Ladder")
        return 76
    elif points==61:
        print("Ladder")
        return 78
    elif points==73:
        print("Ladder")
        return 86
    elif points==81:
        print("Ladder")
        return 98
    elif points==88:
        print("Ladder")
        return 91
    else:
        return points
    
def check_snake(points):
    if points==8:
        print("Snake")
        return 4
    elif points==18:
        print("Snake")
        return 1
    elif points==26:
        print("Snake")
        return 10
    elif points==39:
        print("Snake")
        return 5
    elif points==51:
        print("Snake")
        return 6
    elif points==54:
        print("Snake")
        return 36
    elif points==56:
        print("Snake")
        return 1
    elif points==60:
        print("Snake")
        return 23
    elif points==75:
        print("Snake")
        return 28
    elif points==83:
        print("Snake")
        return 45
    elif points==85:
        print("Snake")
        return 59
    elif points==90:
        print("Snake")
        return 48
    elif points==92:
        print("Snake")
        return 25
    elif points==97:
        print("Snake")
        return 87
    elif points==99:
        return 63
    else:
        return points
    
    
    
    
def play():
    p1_name=input("Player 1, Enter your Name: ")
    p2_name=input("Player 2, Enter your Name: ")
    print()
    pp1=0
    pp2=0
    
    
    turn=0
    while(1):
        show_board()
        if turn%2==0:
            print(p1_name, "Your turn: ", end='')
            c=int(input("Press 1 to roll the dice, 0 to quit: "))
            if c==0:
                print(p1_name, 'scored', pp1)
                print(p2_name, 'scored', pp2)
                print("Quitting the game, Thanks for playing.")
                break
            else:
                dice = random.randint(1,6)
                print("Dice showed ", dice)
                pp1 = pp1+dice
                pp1 = check_ladder(pp1)
                pp1 = check_snake(pp1)
                if pp1>end:
                    continue
                print(p1_name, 'Your score is: ', pp1)
                print()
                
                if reached_end(pp1):
                    print(p1_name, 'won.')
                    break
                
        else:
            print(p2_name, "Your turn: ", end='')
            c=int(input("Press 1 to roll the dice, 0 to quit: "))
            if c==0:
                print(p1_name, 'scored', pp1)
                print(p2_name, 'scored', pp2)
                print("Quitting the game, Thanks for playing.")
                break
            else:
                dice = random.randint(1,6)
                print("Dice showed ", dice)
                pp2 = pp2+dice
                pp2 = check_ladder(pp2)
                pp2 = check_snake(pp2)
                if pp2>end:
                    continue
                print(p2_name, 'Your score is: ', pp2)
                print()
                
                if reached_end(pp2):
                    print(p2_name, 'won.')
                    break
        turn = turn+1
        

play()
         
            
                    
               
                
                    
                
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
show_board()
  