from cmu_graphics import *
import maze
import characters
import guides

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
    app.gameOver = False
    app.paused = False

def checkForCapture(app):
    for monster in app.monsters:
        if ((monster.row == app.mainChar.row) and
            (monster.col == app.mainChar.col)):
            app.gameOver = True

def onStep(app):
    if not app.gameOver and not app.paused:
        for monster in app.monsters:
            monster.moveOnStep()
        checkForCapture(app)

def onKeyPress(app, key):
    if not app.gameOver and not app.paused:
        app.mainChar.onKeyPress(key)

def onKeyHold(app, keys):
    if not app.gameOver and not app.paused:
        app.mainChar.onKeyHold(keys)

def redrawAll(app):
    if not app.gameOver and not app.paused:
        maze.drawGrid(app)
        app.mainChar.draw()
        for monster in app.monsters:
            monster.draw()
    elif app.gameOver:
        guides.drawGameOver(app)

def main():
    runApp()

main()