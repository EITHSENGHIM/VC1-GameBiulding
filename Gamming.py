#--------------------------------------------------IMPORTS---------------------------------------------#
import tkinter as tk
import random
import winsound
from tkinter import *
#--------------------------------------------------CONSTANTS---------------------------------------------#
ScoreText = 0
moveX = 725
moveY = 175
moveX1 = 60
moveY1 = 300
moveX2 = 370
moveY2 = 180
moveX3 = 430
moveY3 = 480
YouWin = returnBack = returnBack1 = returnBack2 = returnBack3 = TouchEmemy = True
SCREEN_WIDTH = 1015
SCREEN_HEIGHT = 700
SCREEN_TITLE = "You can use Keys Right, Left, Up, and Down."
#--------------------------------------------------VARIABLES---------------------------------------------#
TouchEmemy1 = 0
TouchEmemy2 = 0
grid = [
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,1,0,0,2,3,4,4,4,4,4,3,0,2,3],
[3,0,3,0,3,2,0,0,3,0,3,4,0,3,3],
[3,4,4,4,4,3,0,3,2,0,0,4,3,2,3],
[3,3,0,3,2,0,0,3,2,0,3,4,0,0,3],
[3,0,0,0,3,0,0,0,3,0,0,3,0,0,3],
[3,2,3,0,0,2,3,4,4,4,4,4,3,2,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]
x1 = 0
x2 = 0
y1 = 0
y2 = 0
#--------------------------------------------------draw grid as ractangle and follow by positions---------------------------------------------#
def arrayToDrawing():
    global x1, x2, y1, y2, TouchEmemy1, TouchEmemy2
    for rowGRid in range(len(grid)) :
        for colGrid in range(len(grid[rowGRid])):
            x1 = (colGrid * 60)
            x2 = 60 + x1
            y1 = (rowGRid * 60)
            y2 = 60 + y1
            if grid[rowGRid][colGrid]==1 :
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
                canvas.create_image(67+x1,60+y2, image=imageDoctor, anchor=NW)
            elif grid[rowGRid][colGrid]==4 :
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
            elif grid[rowGRid][colGrid]==2 :
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
                canMove3 = canvas.create_image(67+x1,60+y2, image=entiVirus, anchor=NW)
            elif grid[rowGRid][colGrid]==3 :
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="red", outline="blue")
                canvas.create_image(67+x1,60+y2, image=imageWall, anchor=NW) 
            else:
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
                
#--------------------------------------------------Move Ememy one---------------------------------------------# 
def ememyMove0() :
    global canMove0, moveX, moveY, returnBack, TouchEmemy1, TouchEmemy2, TouchEmemy, YouWin
    canvas.moveto(canMove0, moveX,moveY)
    if moveY<=420 and returnBack and YouWin:
        canvas.after(30, lambda:ememyMove0())
        moveY += 5
        if moveY==420 :
            returnBack = False
    elif moveY>180 and not returnBack and YouWin:
        canvas.after(30, lambda:ememyMove0())
        moveY -= 5
        if moveY==180 :
            returnBack = True
#--------------------------------------------------Move Ememy Two---------------------------------------------#
def ememyMove1() :
    global returnBack1, moveX1, moveY1, canMove1, TouchEmemy1, TouchEmemy2, TouchEmemy, YouWin
    canvas.moveto(canMove1, moveX1,moveY1)
    if moveX1<=320 and returnBack1 and YouWin:
        canvas.after(25, lambda:ememyMove1())
        moveX1 += 5
        if moveX1==320 :
            returnBack1 = False
    elif moveX1>105 and not returnBack1 and YouWin:
        canvas.after(30, lambda:ememyMove1())
        moveX1 -= 5
        if moveX1==105 :
            returnBack1 = True
#--------------------------------------------------Move Ememy three---------------------------------------------#
def ememyMove2() :
    global returnBack2, moveX2, moveY2, canMove2, TouchEmemy1, TouchEmemy2, TouchEmemy, YouWin
    canvas.moveto(canMove2, moveX2,moveY2)
    if moveX2<=680 and returnBack2 and YouWin:
        canvas.after(10, lambda:ememyMove2())
        moveX2 += 2
        if moveX2==680 :
            returnBack2 = False
    elif moveX2>=400 and not returnBack2 and YouWin :
        canvas.after(10, lambda:ememyMove2())
        moveX2 -= 2
        if moveX2==400 :
            returnBack2 = True
#--------------------------------------------------Move Ememy Four---------------------------------------------#    
def ememyMove3() :
    global returnBack3, moveX3, moveY3, canMove3, TouchEmemy1, TouchEmemy2, TouchEmemy, YouWin
    canvas.moveto(canMove3, moveX3,moveY3)
    if moveX3<=755 and returnBack3 and YouWin :
        canvas.after(30, lambda:ememyMove3())
        moveX3 += 5
        if moveX3==755 :
            returnBack3 = False
    elif moveX3>=460 and not returnBack3 and YouWin :
        canvas.after(30, lambda:ememyMove3())
        moveX3 -= 5
        if moveX3==460 :
            returnBack3 = True
#--------------------------------------------------Find the positions of grid---------------------------------------------#
def findPlayerPosition(grid) :
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            if grid[i][n]== 1 :
                position=[i,n]
    return position
#--------------------------------------------------Button go Right---------------------------------------------#
def moveRight(event):
    global position, grid, canMove0, canMove1, canMove2, canMove3, number_entiVirus, TouchEmemy, YouWin , TouchEmemy, ScoreText
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row][p_column+1] ==0 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row][p_column+1]=1
    elif grid[p_row][p_column+1]==2 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row][p_column+1]=1
        ScoreText += 10
    elif grid[p_row][p_column+1]==4 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row][p_column+1]=1
        
        TouchEmemy = False
    canvas.delete("all")
    backgound_windows=canvas.create_image(500,500,image=bg)
    canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
    canMove1 = canvas.create_image(60,300, image=imageVirus1, anchor=NW)
    canMove2 = canvas.create_image(370,180, image=imageVirus2, anchor=NW)
    canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
    if ScoreText==100 :
        canvas.create_text(500,60, text="YOU WON!!!",fill="white", font=("Purisa", 50,"bold"))
        sd_Win()
        YouWin = False
    else :
        canvas.create_text(500,50, text="Enjoy to play without lost.",fill="white", font=("Purisa", 20,"bold"))
    canvas.create_text(510,630, text="If you can pick up many AntiVirus on the grid equal 100/100, you win.",fill="blue", font=("Purisa", 18))
    canvas.create_text(510,660, text="I am sorry to player this game is easy player becuase you cannot lose.",fill="blue", font=("Purisa", 18))
    canvas.create_text(170,90, text="Scores : " + str(ScoreText) + "/100",fill="yellow", font=("Purisa", 18))
    canvas.create_image(900, 60, image=heart_image, anchor=NW)
    canvas.create_image(850, 60, image=heart_image, anchor=NW)
    canvas.create_image(800, 60, image=heart_image, anchor=NW)
    canvas.create_image(750, 60, image=heart_image, anchor=NW)
    canvas.create_image(700, 60, image=heart_image, anchor=NW)
    sd_RightLeftUpDown()
    arrayToDrawing()
#--------------------------------------------------Button go Left---------------------------------------------#   
def moveLeft(event):
    global position, grid, canMove0, canMove1, canMove2, canMove3, number_entiVirus, TouchEmemy, YouWin, TouchEmemy, ScoreText
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row][p_column-1]==0 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row][p_column-1]=1
    elif grid[p_row][p_column-1]==2 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row][p_column-1]=1
        ScoreText += 10
    elif grid[p_row][p_column-1]==4 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row][p_column-1]=1
        TouchEmemy = False
    canvas.delete("all")
    backgound_windows=canvas.create_image(500,500,image=bg)
    canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
    canMove1 = canvas.create_image(60,300, image=imageVirus1, anchor=NW)
    canMove2 = canvas.create_image(370,180, image=imageVirus2, anchor=NW)
    canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
    if ScoreText==100 :
        canvas.create_text(500,60, text="YOU WON!!!",fill="white", font=("Purisa", 50,"bold"))
        sd_Win()
        YouWin = False
    else :
        canvas.create_text(500,50, text="Enjoy to play without lost.",fill="white", font=("Purisa", 20,"bold"))
    canvas.create_text(510,630, text="If you can pick up many AntiVirus on the grid equal 100/100, you win.",fill="blue", font=("Purisa", 18))
    canvas.create_text(510,660, text="I am sorry to player this game is easy player becuase you cannot lose.",fill="blue", font=("Purisa", 18))
    canvas.create_text(170,90, text="Scores : " + str(ScoreText) + "/100",fill="yellow", font=("Purisa", 18))
    canvas.create_image(900, 60, image=heart_image, anchor=NW)
    canvas.create_image(850, 60, image=heart_image, anchor=NW)
    canvas.create_image(800, 60, image=heart_image, anchor=NW)
    canvas.create_image(750, 60, image=heart_image, anchor=NW)
    canvas.create_image(700, 60, image=heart_image, anchor=NW)
    sd_RightLeftUpDown()
    arrayToDrawing()
#--------------------------------------------------Button go Up---------------------------------------------#
def moveUp(event):
    global position, grid, canMove0, canMove1, canMove2, canMove3, number_entiVirus, TouchEmemy, YouWin, TouchEmemy, ScoreText
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row-1][p_column]==0 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row-1][p_column]=1
    elif grid[p_row-1][p_column]==2 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row-1][p_column]=1
        ScoreText += 10
    elif grid[p_row-1][p_column]==4 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row-1][p_column]=1
        TouchEmemy = False
    canvas.delete("all")
    backgound_windows=canvas.create_image(500,500,image=bg)
    canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
    canMove1 = canvas.create_image(60,300, image=imageVirus1, anchor=NW)
    canMove2 = canvas.create_image(370,180, image=imageVirus2, anchor=NW)
    canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
    if ScoreText==100 :
        canvas.create_text(500,60, text="YOU WON!!!",fill="white", font=("Purisa", 50,"bold"))
        sd_Win()
        YouWin = False
    else :
        canvas.create_text(500,50, text="Enjoy to play without lost.",fill="white", font=("Purisa", 20,"bold"))
    canvas.create_text(510,630, text="If you can pick up many AntiVirus on the grid equal 100/100, you win.",fill="blue", font=("Purisa", 18))
    canvas.create_text(510,660, text="I am sorry to player this game is easy player becuase you cannot lose.",fill="blue", font=("Purisa", 18))
    canvas.create_text(170,90, text="Scores : " + str(ScoreText) + "/100",fill="yellow", font=("Purisa", 18))
    canvas.create_image(900, 60, image=heart_image, anchor=NW)
    canvas.create_image(850, 60, image=heart_image, anchor=NW)
    canvas.create_image(800, 60, image=heart_image, anchor=NW)
    canvas.create_image(750, 60, image=heart_image, anchor=NW)
    canvas.create_image(700, 60, image=heart_image, anchor=NW)
    sd_RightLeftUpDown()
    arrayToDrawing()
#--------------------------------------------------Button go Down---------------------------------------------#
def moveDown(event):
    global position, grid, canMove0, canMove1, canMove2, canMove3, number_entiVirus, TouchEmemy, YouWin, TouchEmemy, ScoreText
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row+1][p_column]==0 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row+1][p_column]=1
    elif grid[p_row+1][p_column]==2 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row+1][p_column]=1
        ScoreText += 10
    elif grid[p_row+1][p_column]==4 and YouWin :
        grid[p_row][p_column]=0
        grid[p_row+1][p_column]=1
        TouchEmemy = False
    canvas.delete("all")
    backgound_windows=canvas.create_image(500,500,image=bg)
    canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
    canMove1 = canvas.create_image(60,300, image=imageVirus1, anchor=NW)
    canMove2 = canvas.create_image(370,180, image=imageVirus2, anchor=NW)
    canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
    if ScoreText==100 :
        canvas.create_text(500,60, text="YOU WON!!!",fill="white", font=("Purisa", 50,"bold"))
        sd_Win()
        YouWin = False
    else :
        canvas.create_text(500,50, text="Enjoy to play without lost.",fill="white", font=("Purisa", 20,"bold"))
    canvas.create_text(510,630, text="If you can pick up many AntiVirus on the grid equal 100/100, you win.",fill="blue", font=("Purisa", 18))
    canvas.create_text(510,660, text="I am sorry to player this game is easy player becuase you cannot lose.",fill="blue", font=("Purisa", 18))
    canvas.create_text(170,90, text="Scores : " + str(ScoreText) + "/100",fill="yellow", font=("Purisa", 18))
    canvas.create_image(900, 60, image=heart_image, anchor=NW)
    canvas.create_image(850, 60, image=heart_image, anchor=NW)
    canvas.create_image(800, 60, image=heart_image, anchor=NW)
    canvas.create_image(750, 60, image=heart_image, anchor=NW)
    canvas.create_image(700, 60, image=heart_image, anchor=NW)
    sd_RightLeftUpDown()
    arrayToDrawing()
#--------------------------------------------------Main available of tkinter---------------------------------------------#
root = tk.Tk()
root.title(SCREEN_TITLE)
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)
#--------------------------------------------------Create image of grid---------------------------------------------#
imageDoctor = PhotoImage(file="doctor.png")
imageWall = PhotoImage(file="wall.png")
bg=tk.PhotoImage(file="sky1.png")
backgound_windows=canvas.create_image(500,500,image=bg)
imageVirus0 = PhotoImage(file="virus.png")
imageVirus1 = PhotoImage(file="virus.png")
imageVirus2 = PhotoImage(file="virus.png")
imageVirus3 = PhotoImage(file="virus.png")
entiVirus = PhotoImage(file="entiVirus.png")
#--------------------------------------------------Available move of image---------------------------------------------#
canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
canMove1 = canvas.create_image(60,300, image=imageVirus1, anchor=NW)
canMove2 = canvas.create_image(375,180, image=imageVirus2, anchor=NW)
canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
#--------------------------------------------------Call function and create function of sound---------------------------------------------#
ememyMove0()
ememyMove1()
ememyMove2()
ememyMove3()
def sd_RightLeftUpDown() :
    if YouWin :
        winsound.PlaySound("jump3.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def sd_Win() :
    winsound.PlaySound("upgrade5.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
#--------------------------------------------------Create image heart 5---------------------------------------------#

heart_image= tk.PhotoImage(file="heart.png")
canvas.create_image(900, 60, image=heart_image, anchor=NW)
canvas.create_image(850, 60, image=heart_image, anchor=NW)
canvas.create_image(800, 60, image=heart_image, anchor=NW)
canvas.create_image(750, 60, image=heart_image, anchor=NW)
canvas.create_image(700, 60, image=heart_image, anchor=NW)
#--------------------------------------------------Create Text for Instructions---------------------------------------------#
root.resizable(False,False)
canvas.create_text(510,630, text="If you can pick up many AntiVirus on the grid equal 100/100, you win.",fill="blue", font=("Purisa", 18))
canvas.create_text(510,660, text="I am sorry to player this game is easy player becuase you cannot lose.",fill="blue", font=("Purisa", 18))
canvas.create_text(170,90, text="Scores : " + str(ScoreText) + "/100",fill="yellow", font=("Purisa", 18))
canvas.create_text(500,50, text="Enjoy to play without lost.",fill="white", font=("Purisa", 20,"bold"))
arrayToDrawing()


root.mainloop()


#--------------------------------------------------The end of programming of Game building---------------------------------------------#
#--------------------------------------------------THANks---------------------------------------------#