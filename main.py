from cmu_graphics import *
import maze
import characters

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.grid = maze.Grid()
    app.setMaxShapeCount(100000)
    restartGame(app)

def restartGame(app):
    app.mainChar = characters.MainChar(0, 0)
    app.monsters = characters.generateMonsters(2, [])
    app.stepsPerSecond = 5
    app.timer = 0

def onStep(app):
    app.timer += 1
    for monster in app.monsters:
        monster.moveOnStep()

def onKeyPress(app, key):
    app.mainChar.onKeyPress(key)

def onKeyHold(app, keys):
    app.mainChar.onKeyHold(keys)

def redrawAll(app):
    maze.drawGrid(app)
    app.mainChar.draw()
    for monster in app.monsters:
        monster.draw()

def main():
    runApp()

main()