from cmu_graphics import *
import maze
import characters
import guides
import images

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.grid = maze.Grid()
    app.setMaxShapeCount(100000)
    restartGame(app)

def restartGame(app):
    app.mainChar = characters.MainChar(0, 0)
    app.monsters = characters.generateMonsters(2)
    app.placedArtifacts = characters.generateArtifacts(3)
    app.heldArtifacts = []

    app.stepsPerSecond = 5
    app.timer = 0
    app.gameOver = False
    app.paused = False

    app.score = 0
    app.droppedWeight = 0
    app.heldWeight = 0

def checkForCapture(app):
    for monster in app.monsters:
        if ((monster.row == app.mainChar.row) and
            (monster.col == app.mainChar.col)):
            app.gameOver = True

def onStep(app):
    if not app.gameOver and not app.paused:
        app.timer += 1
        for monster in app.monsters:
            monster.moveOnStep()
        checkForCapture(app)
        if len(app.placedArtifacts) < 2:
            characters.generateArtifacts(2)

def onKeyPress(app, key):
    if not app.gameOver and not app.paused:
        app.mainChar.onKeyPress(key)

def onKeyHold(app, keys):
    if not app.gameOver and not app.paused:
        app.mainChar.onKeyHold(keys)

def redrawAll(app):
    if not app.gameOver and not app.paused:
        maze.drawGrid(app)
        guides.drawScoreBox(app)
        app.mainChar.draw()
        for monster in app.monsters:
            monster.draw()
        for artifact in app.placedArtifacts:
            artifact.draw()
        for artifact in app.heldArtifacts:
            artifact.draw()
    elif app.gameOver:
        guides.drawGameOver(app)

def main():
    runApp()

main()