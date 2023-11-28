from cmu_graphics import *
import maze, characters, guides, buttons, powerups


def onAppStart(app):
    app.width = 800
    app.height = 800
    app.setMaxShapeCount(100000)
    app.highScore = 0

    app.gameStarted = False
    app.gameOver = False
    app.paused = True
    app.showInstructions = False
    buttons.initializeButtons(app)
    app.powerups = [powerups.WallWalk(), powerups.Invis(), powerups.WallWalk()]

def restartGame(app):
    app.gameStarted = True
    app.grid = maze.Grid()
    app.mainChar = characters.MainChar(0, 0)
    app.monsters = characters.generateMonsters(2)
    app.placedArtifacts = characters.generateArtifacts(3)
    app.heldArtifacts = []

    app.stepsPerSecond = 5
    app.timer = 0
    app.gameOver = False
    app.paused = False
    app.showInstructions = False

    app.score = 0
    app.droppedWeight = 0
    app.heldWeight = 0

def checkForCapture(app):
    for monster in app.monsters:
        if ((monster.row == app.mainChar.row) and
            (monster.col == app.mainChar.col)):
            app.gameOver = True
            if app.score > app.highScore:
                app.highScore = app.score

def onStep(app):
    if not app.gameOver and not app.paused and not app.showInstructions:
        app.timer += 1
        for monster in app.monsters:
            monster.moveOnStep(['left', 'right', 'up', 'down'])
        checkForCapture(app)
        if len(app.placedArtifacts) < 2:
            characters.generateArtifacts(2)

def onKeyPress(app, key):
    if not app.gameOver and not app.paused and not app.showInstructions:
        app.mainChar.onKeyPress(key)

def onMousePress(app, mx, my):
    if not app.gameStarted:
        if app.instructions.pressButton(mx, my):
            app.showInstructions = not app.showInstructions
        elif app.startGame.pressButton(mx, my):
            restartGame(app)
    if not app.gameOver and not app.paused:
        if app.instructions.pressButton(mx, my):
            app.showInstructions = not app.showInstructions
    if not app.gameOver:
        if app.pause.pressButton(mx, my):
            app.paused = not app.paused
        if app.restartInGame.pressButton(mx, my):
            app.gameStarted = False
    else:
        if app.restartEndGame.pressButton(mx, my):
            restartGame(app)

def onKeyHold(app, keys):
    if not app.gameOver and not app.paused:
        app.mainChar.onKeyHold(keys)

def redrawAll(app):
    if not app.gameStarted:
        guides.drawGameStart(app)
        if app.showInstructions:
            guides.drawInstructions(app)
    elif app.gameOver:
        guides.drawGameOver(app)
    else:
        guides.drawInGame(app)
        if app.paused:
            guides.drawPauseScreen(app)
        if app.showInstructions:
            guides.drawInstructions(app)
        else:
            maze.drawGrid(app)
            app.mainChar.draw()
            for monster in app.monsters:
                monster.draw()
            for artifact in app.placedArtifacts:
                artifact.draw()
            for artifact in app.heldArtifacts:
                artifact.draw()

def main():
    runApp()

main()