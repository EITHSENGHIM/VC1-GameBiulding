# IMPORTS
import tkinter as tk
import random
from tkinter import *

# CONSTANTS
PLAYER  = 1
EMPTY = 0
moveX = 725
moveY = 175
moveX1 = 80
moveY1 = 300
moveX2 = 370
moveY2 = 180
moveX3 = 430
moveY3 = 480
returnBack = True
returnBack1 = True
returnBack2 = True
returnBack3 = True
SCREEN_WIDTH = 1015
SCREEN_HEIGHT = 700
SCREEN_TITLE = "You can Right, Left, Up, and Down."

# VARIABLES
number_entiVirus = 0

grid = [
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[3,1,0,0,2,3,0,0,0,0,0,3,0,2,3],
[3,0,3,0,3,2,0,0,3,0,3,0,0,3,3],
[3,0,0,0,0,3,0,3,2,0,0,0,3,2,3],
[3,3,0,3,0,0,0,3,2,0,3,0,0,0,3],
[3,0,0,0,3,0,0,0,3,0,0,3,0,0,3],
[3,2,3,0,0,0,3,0,0,0,0,0,3,2,3],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]
x1 = 0
x2 = 0
y1 = 0
y2 = 0


# draw grid as ractangle
def arrayToDrawing():
    global x1, x2, y1, y2
    for rowGRid in range(len(grid)) :
        for colGrid in range(len(grid[rowGRid])):
            x1 = (colGrid * 60)
            x2 = 60 + x1
            y1 = (rowGRid * 60)
            y2 = 60 + y1
            if grid[rowGRid][colGrid]==1 :
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
                canvas.create_image(67+x1,60+y2, image=imageDoctor, anchor=NW)
            elif colGrid==11 and rowGRid>1 and rowGRid<len(grid)-3 :
                    canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
            elif colGrid>0 and colGrid<5 and rowGRid==3 :
                    canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
            elif colGrid>5 and colGrid<11 and rowGRid==1 :
                    canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
            elif colGrid>6 and colGrid<12 and rowGRid==6 :
                    canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
            elif grid[rowGRid][colGrid]==2 :
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="", outline="blue")
                canMove3 = canvas.create_image(67+x1,60+y2, image=entiVirus, anchor=NW)
            elif grid[rowGRid][colGrid]==3 :
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="red", outline="blue")
                canvas.create_image(67+x1,60+y2, image=imageWall, anchor=NW) 
            else:
                canvas.create_rectangle(60+x1,115+y1,60+x2,115+y2,fill="#7851ae", outline="blue")
            
def ememyMove0() :
    global canMove0, moveX, moveY, returnBack
    canvas.moveto(canMove0, moveX,moveY)
    
    if moveY<=380 and returnBack :
        canvas.after(99, lambda:ememyMove0())
        moveY += 5
        if moveY==380 :
            returnBack = False
    elif moveY>220 and not returnBack :
        canvas.after(99, lambda:ememyMove0())
        moveY -= 5
        if moveY==220 :
            returnBack = True
def ememyMove1() :
    global returnBack1, moveX1, moveY1, canMove1
    canvas.moveto(canMove1, moveX1,moveY1)
    if moveX1<=320 and returnBack1 :
        canvas.after(80, lambda:ememyMove1())
        moveX1 += 5
        if moveX1==320 :
            returnBack1 = False
    elif moveX1>105 and not returnBack1 :
        canvas.after(80, lambda:ememyMove1())
        moveX1 -= 5
        if moveX1==105 :
            returnBack1 = True
def ememyMove2() :
    global returnBack2, moveX2, moveY2, canMove2
    canvas.moveto(canMove2, moveX2,moveY2)
    if moveX2<=680 and returnBack2 :
        canvas.after(60, lambda:ememyMove2())
        moveX2 += 5
        if moveX2==680 :
            returnBack2 = False
    elif moveX2>=400 and not returnBack2 :
        canvas.after(60, lambda:ememyMove2())
        moveX2 -= 5
        if moveX2==400 :
            returnBack2 = True
def ememyMove3() :
    global returnBack3, moveX3, moveY3, canMove3
    canvas.moveto(canMove3, moveX3,moveY3)
    if moveX3<=755 and returnBack3 :
        canvas.after(60, lambda:ememyMove3())
        moveX3 += 5
        if moveX3==755 :
            returnBack3 = False
    elif moveX3>=460 and not returnBack3 :
        canvas.after(60, lambda:ememyMove3())
        moveX3 -= 5
        if moveX3==460 :
            returnBack3 = True
def findPlayerPosition(grid) :
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            if grid[i][n]== 1:
                position=[i,n]
    return position
def moveRight(event):
    global position, grid, canMove0, canMove1, canMove2, canMove3, number_entiVirus
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row][p_column+1] ==0  :
        grid[p_row][p_column]=0
        grid[p_row][p_column+1]=1
    elif grid[p_row][p_column+1]==2 :
        grid[p_row][p_column]=0
        grid[p_row][p_column+1]=1
        number_entiVirus += 1

    canvas.delete("all")
    backgound_windows=canvas.create_image(500,500,image=bg)
    canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
    canMove1 = canvas.create_image(80,300, image=imageVirus1, anchor=NW)
    canMove2 = canvas.create_image(370,180, image=imageVirus2, anchor=NW)
    canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
    if number_entiVirus==8 :
        canvas.create_text(470,50, text="YOU WON.",fill="green", font=("Purisa", 35,"bold"))
    canvas.create_text(530,630, text="If you can kills many Virus on the time, you win else lost.",fill="blue", font=("Purisa", 18))
    canvas.create_text(500,660, text="It is follow level be level.",fill="blue", font=("Purisa", 18))
    arrayToDrawing()
    
def moveLeft(event):
    global position, grid, canMove0, canMove1, canMove2, canMove3, number_entiVirus
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row][p_column-1]==0:
        grid[p_row][p_column]=0
        grid[p_row][p_column-1]=1
    if grid[p_row][p_column-1]==2:
        grid[p_row][p_column]=0
        grid[p_row][p_column-1]=1
        number_entiVirus += 1
    canvas.delete("all")
    backgound_windows=canvas.create_image(500,500,image=bg)
    canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
    canMove1 = canvas.create_image(80,300, image=imageVirus1, anchor=NW)
    canMove2 = canvas.create_image(370,180, image=imageVirus2, anchor=NW)
    canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
    if number_entiVirus==8 :
        canvas.create_text(470,50, text="YOU WON.",fill="green", font=("Purisa", 35,"bold"))
    canvas.create_text(530,630, text="If you can kills many Virus on the time, you win else lost.",fill="blue", font=("Purisa", 18))
    canvas.create_text(500,660, text="It is follow level be level.",fill="blue", font=("Purisa", 18))
    arrayToDrawing()
    

def moveUp(event):
    global position, grid, canMove0, canMove1, canMove2, canMove3, number_entiVirus
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row-1][p_column]==0:
        grid[p_row][p_column]=0
        grid[p_row-1][p_column]=1
    if grid[p_row-1][p_column]==2:
        grid[p_row][p_column]=0
        grid[p_row-1][p_column]=1
        number_entiVirus += 1
    canvas.delete("all")
    backgound_windows=canvas.create_image(500,500,image=bg)
    canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
    canMove1 = canvas.create_image(80,300, image=imageVirus1, anchor=NW)
    canMove2 = canvas.create_image(370,180, image=imageVirus2, anchor=NW)
    canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
    if number_entiVirus==8 :
        canvas.create_text(470,50, text="YOU WON.",fill="green", font=("Purisa", 35,"bold"))
    canvas.create_text(530,630, text="If you can kills many Virus on the time, you win else lost.",fill="blue", font=("Purisa", 18))
    canvas.create_text(500,660, text="It is follow level be level.",fill="blue", font=("Purisa", 18))
    arrayToDrawing()

def moveDown(event):
    global position, grid, canMove0, canMove1, canMove2, canMove3, number_entiVirus
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row+1][p_column]==0:
        grid[p_row][p_column]=0
        grid[p_row+1][p_column]=1
    if grid[p_row+1][p_column]==2:
        grid[p_row][p_column]=0
        grid[p_row+1][p_column]=1
        number_entiVirus += 1
    canvas.delete("all")
    canvas.delete("all")
    backgound_windows=canvas.create_image(500,500,image=bg)
    canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
    canMove1 = canvas.create_image(80,300, image=imageVirus1, anchor=NW)
    canMove2 = canvas.create_image(370,180, image=imageVirus2, anchor=NW)
    canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)
    if number_entiVirus==8 :
        canvas.create_text(470,50, text="YOU WON.",fill="green", font=("Purisa", 35,"bold"))
    canvas.create_text(530,630, text="If you can kills many Virus on the time, you win else lost.",fill="blue", font=("Purisa", 18))
    canvas.create_text(500,660, text="It is follow level be level.",fill="blue", font=("Purisa", 18))
    arrayToDrawing()


    

# draw a line with white and black squares using the global array
root = tk.Tk()
root.title(SCREEN_TITLE)
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))

canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")

root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)




imageDoctor = PhotoImage(file="doctor.png")
imageWall = PhotoImage(file="wall.png")
bg=tk.PhotoImage(file="sky1.png")
backgound_windows=canvas.create_image(500,500,image=bg)
imageVirus0 = PhotoImage(file="virus.png")
imageVirus1 = PhotoImage(file="50ofVirus.png")
imageVirus2 = PhotoImage(file="virus.png")
imageVirus3 = PhotoImage(file="50ofVirus.png")
entiVirus = PhotoImage(file="entiVirus.png")


canMove0 = canvas.create_image(725,175, image=imageVirus0, anchor=NW)
canMove1 = canvas.create_image(80,300, image=imageVirus1, anchor=NW)
canMove2 = canvas.create_image(375,180, image=imageVirus2, anchor=NW)
canMove3 = canvas.create_image(430,480, image=imageVirus3, anchor=NW)

ememyMove0()
ememyMove1()
ememyMove2()
ememyMove3()

arrayToDrawing()


root.resizable(False,False)
canvas.create_text(530,630, text="If you can kills many Virus on the time, you win else lost.",fill="blue", font=("Purisa", 18))
canvas.create_text(500,660, text="It is follow level be level.",fill="blue", font=("Purisa", 18))


root.mainloop()
