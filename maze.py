from cmu_graphics import *
import images
import random

class Grid:
    def __init__(self):
        self.top = app.width/5
        self.margin = 50
        self.left = self.margin
        self.width = app.width - 2*self.margin
        self.height = app.height - self.top - self.margin
        self.rows = 15
        self.cols = 15
        self.maze = self.generateMaze()

    def generateMaze(self):
        maze = [[True]*self.cols for _ in range(self.rows)]

        for row in range(self.rows):
            if row % 2 == 1:
                maze[row] = [False] * self.cols
            if row % 4 == 1:
                maze[row][self.cols-1] = True
            elif row % 4 == 3:
                maze[row][0] = True
        
        return maze

# CITATION: general structure for drawing grid from: CS Academy 5.3.2 Drawing a 2d Board
def getCellSize(app):
    cellW = app.grid.width / app.grid.cols
    cellH = app.grid.height / app.grid.rows
    return cellW, cellH

def getCellLeftTop(app, r, c):
    cellW, cellH = getCellSize(app)

    cellX0 = app.grid.left + c*cellW
    cellY0 = app.grid.top + r*cellH

    return cellX0, cellY0

def drawCell(app, r, c):
    cellX0, cellY0 = getCellLeftTop(app, r, c)
    cellW, cellH = getCellSize(app)

    if app.grid.maze[r][c] == False:
        drawImage(images.walls, cellX0, cellY0, 
                  width=cellW, height=cellH, align='top-left')
    else:
        drawRect(cellX0, cellY0, cellW, cellH, 
                fill=None, border='saddleBrown')

def drawGridBorder(app):
    drawRect(app.grid.left, app.grid.top, app.grid.width, app.grid.height,
             fill=None, border='saddleBrown')
    
def drawCart(app):
    posX, posY = getCellLeftTop(app, 0, 0)
    width, height = getCellSize(app)
    drawImage(images.cart, posX, posY, align='top-left',
              width=width, height=height)
    
def drawGrid(app):
    for r in range(app.grid.rows):
        for c in range(app.grid.cols):
            drawCell(app, r, c)

    drawGridBorder(app)
    drawCart(app)