from cmu_graphics import *
import random
import maze, characters, guides, buttons, powerups


def onAppStart(app):
    app.width = 800
    app.height = 800
    app.setMaxShapeCount(100000)
    app.spinner = ['WallWalk', 'Invis', None, 
                   'Invis', 'WallWalk', 'Gem']
    
    app.highScore = 0
    app.gameStarted = False
    app.gameOver = False
    app.paused = True
    app.showInstructions = False
    buttons.initializeButtons(app)
    app.heldGems = 0
    app.powerups = []

def restartGame(app):
    app.stepsPerSecond = 5
    app.timer = 0
    app.gameOver = False
    app.paused = False
    app.showInstructions = False
    app.showSpinner = False
    app.spinning = False

    app.gameStarted = True
    app.grid = maze.Grid()
    app.mainChar = characters.MainChar(0, 0)
    app.monsters = characters.generateMonsters(2)
    app.placedArtifacts = characters.generateArtifacts(3)
    app.heldArtifacts = []
    app.gem = characters.generateGem()

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
    if app.gameStarted and not app.gameOver and not app.paused:
        app.timer += 1
        for monster in app.monsters:
            monster.moveOnStep(['left', 'right', 'up', 'down'])
        checkForCapture(app)
        if len(app.placedArtifacts) < 2:
            characters.generateArtifacts(2)
    elif app.gameStarted and not app.gameOver:
        if app.spinning:
            powerups.spinSpinner(app)
            powerups.Powerup.spinTimer += 1
            if powerups.Powerup.spinTimer > 25:
                app.spinning = False
                powerups.addPowerup(app)

def onKeyPress(app, key):
    if not app.gameOver and not app.paused and not app.showInstructions:
        app.mainChar.onKeyPress(key)

def onMousePress(app, mx, my):
    if not app.gameStarted:
        if app.instructions.pressButton(mx, my):
            app.showInstructions = not app.showInstructions
        elif app.startGame.pressButton(mx, my):
            app.gameStarted = True
            restartGame(app)
    elif not app.gameOver:
        if app.instructions.pressButton(mx, my):
            app.showInstructions = not app.showInstructions
            app.paused = not app.paused
        elif app.openSpinner.pressButton(mx, my):
            random.shuffle(app.spinner)
            app.showSpinner = True
            app.paused = True
        elif app.restartInGame.pressButton(mx, my):
            app.gameStarted = False
        elif app.showSpinner == True:
            if app.closeSpinner.pressButton(mx, my):
                app.showSpinner = False
                app.paused = False
            elif app.spinSpinner.pressButton(mx, my) and app.heldGems > 0:
                app.heldGems -= 1
                powerups.Powerup.spinTimer = 0
                app.spinning = True
        elif app.pause.pressButton(mx, my):
            app.paused = not app.paused
    else:
        if app.restartEndGame.pressButton(mx, my):
            restartGame(app)
            app.gameStarted = False

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
        guides.drawBackground(app, 1)
        if app.showInstructions:
            guides.drawInstructions(app)
        elif app.showSpinner:
            powerups.drawSpinner(app)
        elif app.paused:
            guides.drawPauseScreen(app)
        else:
            maze.drawGrid(app)
            app.mainChar.draw()
            for monster in app.monsters:
                monster.draw()
            for artifact in app.placedArtifacts:
                artifact.draw()
            for artifact in app.heldArtifacts:
                artifact.draw()
            if app.gem:
                app.gem.draw()
        guides.drawInGame(app)

def main():
    runApp()

main()