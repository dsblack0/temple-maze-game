from cmu_graphics import *
import maze

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.grid = maze.Grid()
    app.setMaxShapeCount(100000)

def redrawAll(app):
    print(app.grid)
    maze.drawGrid(app)

def main():
    runApp()

main()