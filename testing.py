
# IMPORTS
import tkinter as tk


# CONSTANTS
SCREEN_WIDTH = 510
SCREEN_HEIGHT = 510
PLAYER = 2
EMPTY = 0
WALL = 1

# VARIABLES
grid =[
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 2, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
[0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
[0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 3, 1, 0, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
[0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 0, 3, 0, 0, 0, 1, 1, 0, 1, 1, 0],
[0, 3, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
[0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
[0, 1, 0, 3, 1, 0, 1, 1, 0, 3, 1, 0, 1, 0, 3, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]
# squareSize = #choose the appropriate size of the squares

# FUNCTION
def arrayToDrawing():
    for Y in range (len(grid)):
        for X in range (len(grid[0])):
            x1 = (X * 30)
            x2 = 30 + x1
            y1 = (Y * 30)
            y2 = 30 + y1

            value = grid[Y][X]
            if value == WALL:
                color = "black"
            if value == PLAYER:
                color = "blue"
            if value == EMPTY:
                color = ""
                canvas.create_image(x1+15,y1+15, image=walls)
            if value==3:
                canvas.create_image(x1+15,y1+15,image=Images,)

            canvas.create_rectangle(x1,y1,x2,y2,fill = color)
    return None

def findPlayerPosition(grid) :
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            if grid[i][n]== 2:
                position=[i,n]
    return position

def canGoRight(event):
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row][p_column+1]!=0:
        grid[p_row][p_column]=1
        grid[p_row][p_column+1]=2
    canvas.delete("all")
    arrayToDrawing()


def canGoLeft(event):
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row][p_column-1]!=0:
        grid[p_row][p_column]=1
        grid[p_row][p_column-1]=2
    canvas.delete("all")
    arrayToDrawing()

def canGoUp(event):
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row-1][p_column]!=0:
        grid[p_row][p_column]=1
        grid[p_row-1][p_column]=2
    canvas.delete("all")
    arrayToDrawing()


def canGoDown(event):
    position = findPlayerPosition(grid)
    p_column = position[1]
    p_row = position[0]
    if grid[p_row+1][p_column]!=0:
        grid[p_row][p_column]=1
        grid[p_row+1][p_column]=2
    canvas.delete("all")
    arrayToDrawing()



root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root)
walls=tk.PhotoImage(file="iconfinder_15-Wall_2672702.png")
Images=tk.PhotoImage(file="virus3.png")
root.bind("<Left>", canGoLeft) #LEFT CLICK
root.bind("<Right>", canGoRight) #RIGHT CLICK
root.bind("<Up>", canGoUp) #Up CLICK
root.bind("<Down>", canGoDown) #Down CLICK

canvas.pack(expand=True, fill="both")

arrayToDrawing()

root.mainloop()