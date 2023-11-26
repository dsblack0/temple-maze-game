from cmu_graphics import *
import images

class Grid:
    def __init__(self):
        self.top = app.width/5
        self.margin = 50
        self.left = self.margin
        self.width = app.width - 2*self.margin
        self.height = app.height - self.top - self.margin
        self.rows = 15
        self.cols = 15

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

    color = None
    drawRect(cellX0, cellY0, cellW, cellH, 
             fill=color, border='saddleBrown')

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