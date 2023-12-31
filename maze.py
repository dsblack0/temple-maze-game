from cmu_graphics import *
import random, func_timeout
import images

class Grid:
    def __init__(self):
        self.top = app.height/5
        self.margin = 50
        self.left = self.margin
        self.width = app.width - 2*self.margin
        self.height = app.height - self.top - self.margin
        self.rows = 15
        self.cols = 15
        self.pathsCount = 150
        self.maze = Grid.limitFTime(self.generateMaze, 10, None)
        # retry if maze generation times out
        while not self.maze:
            self.pathsCount -= 10
            self.maze = Grid.limitFTime(self.generateMaze, 10, None)

    # CITATION: Code for limiting run time of function call from https://blog.finxter.com/how-to-limit-the-execution-time-of-a-function-call/
    @staticmethod
    def limitFTime(f, max_wait, default_value):
        try:
            return func_timeout.func_timeout(max_wait, f)
        except func_timeout.FunctionTimedOut:
            pass
        return default_value

    def generateMaze(self):
        print(f'Generating Maze: {self.pathsCount} paths')
        maze = [[False]*self.cols for _ in range(self.rows)]
        maze[0][0] = True
        return self.createMazePattern(maze, 0, 0, 0)

    # CITATION: Used code in Ruby as reference point from https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking
    def createMazePattern(self, maze, n, currRow, currCol):
        if n == self.pathsCount:
            return maze
        else:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            random.shuffle(directions)
            for drow, dcol in directions:
                nextRow, nextCol = currRow+drow, currCol+dcol
                if ((0<=nextRow<self.rows) and (0<=nextCol<self.cols) and
                    (maze[nextRow][nextCol] == False)):
                        maze[currRow][currCol] = True
                        maze[nextRow][nextCol] = True
                        solution = self.createMazePattern(maze, n+1, nextRow, nextCol)
                        if solution != None:
                            return solution
                        maze[nextRow][nextCol] = False
            return None

def doOverlap(app, x0, y0, x1, y1):
    cellW, cellH = getCellSize(app)
    return (abs(x0-x1)<cellW-10) and (abs(y0-y1)<cellH-10)

def wallLocations():
    wallLocations = []
    # go through whole board
    for row in range(app.grid.rows):
            for col in range(app.grid.cols):
                # create list of all wall's locations
                if app.grid.maze[row][col] == False:
                    wallLocations.append((row, col))
    return wallLocations

# CITATION: general structure for drawing grid from CS Academy 5.3.2 Drawing a 2d Board
def getCellSize(app):
    cellW = app.grid.width // app.grid.cols
    cellH = app.grid.height // app.grid.rows
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
                fill=None, border=None)

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