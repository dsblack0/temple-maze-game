from cmu_graphics import *
import maze
import characters

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.grid = maze.Grid()
    app.mainChar = characters.MainChar(0, 0)
    app.setMaxShapeCount(100000)
    app.stepsPerSecond = 5

def onKeyPress(app, key):
    app.mainChar.onKeyPress(key)

def onKeyHold(app, keys):
    app.mainChar.onKeyHold(keys)

def redrawAll(app):
    maze.drawGrid(app)
    app.mainChar.draw()

def main():
    runApp()

main()