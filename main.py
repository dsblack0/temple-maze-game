from cmu_graphics import *
import maze, characters, guides, images, buttons


def onAppStart(app):
    app.width = 800
    app.height = 800
    app.setMaxShapeCount(100000)
    app.highScore = 0
    restartGame(app)

def restartGame(app):
    app.grid = maze.Grid()
    app.mainChar = characters.MainChar(0, 0)
    app.monsters = characters.generateMonsters(2)
    app.placedArtifacts = characters.generateArtifacts(3)
    app.heldArtifacts = []
    buttons.initializeButtons(app)

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
    if not app.gameOver and not app.paused:
        if app.instructions.pressButton(mx, my):
            app.showInstructions = not app.showInstructions
    if not app.gameOver:
        if app.pause.pressButton(mx, my):
            app.paused = not app.paused
    else:
        if app.restart.pressButton(mx, my):
            restartGame(app)

def onKeyHold(app, keys):
    if not app.gameOver and not app.paused:
        app.mainChar.onKeyHold(keys)

def redrawAll(app):
    guides.drawBackground(app)
    guides.drawInGameButtons(app)
    guides.drawScoreBox(app)
    if app.paused:
        guides.drawPauseScreen(app)
    elif app.showInstructions:
        guides.drawInstructions(app)
    elif not app.gameOver and not app.paused:
        maze.drawGrid(app)
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