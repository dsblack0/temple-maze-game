from cmu_graphics import *
import random
import maze, buttons, music, images
import characters, guides, powerups, charMenu, levelMenu


def onAppStart(app):
    app.width = 800
    app.height = 800
    app.stepsPerSecond = 20
    app.setMaxShapeCount(100000)
    app.spinner = ['WallWalk', 'Invis', None, 
                   'newChar', 'Magnet', 'Gem']
    
    # initialze score, gems & powerups to last whole game
    app.highScore = 0
    app.heldGems = 0
    app.powerups = []
    app.characters = [images.karmaLee]
    app.currChar = 0

    app.gameStarted = False
    app.gameOver = False
    app.paused = True
    app.showSpinner = False
    app.showInstructions = False
    app.characterMenu = False
    app.showLevelMenu = False
    buttons.initializeButtons(app)

def restartGame(app):
    app.timer = 0
    app.gameOver = False
    app.paused = False
    app.showInstructions = False
    app.maxWeightMsg = False
    app.characterMenu = False
    app.showLevelMenu = False
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
        # game over if char overlaps any monster
        if maze.doOverlap(app, monster.posX, monster.posY,
                           app.mainChar.posX, app.mainChar.posY):
            app.gameOver = True
            messages = ["You life ambition was to become lunch?",
                        "Imagine working so hard to get eaten...",
                        "IDK if I ever even had faith in you...",
                        "Lovely...you died..."]
            app.endMessage = random.choice(messages)
            if app.score > app.highScore:
                app.highScore = app.score
                app.endMessage = "Ah beat high scores...I'll pretend to be proud..."
            music.skySummit.pause()
            music.emeraldCity.play(loop = True)

def onStep(app):
    # when playing game
    if app.gameStarted and not app.gameOver and not app.paused:
        # move monsters
        for monster in app.monsters:
            monster.moveOnStep(['left', 'right', 'up', 'down'])
        # Unless invisibility powerup active, check for capture
        indx = powerups.findPowerup(powerups.Invis)
        if indx == -1 or not app.powerups[indx].activated:
            checkForCapture(app)
        # generate new artifacts each time pick up one
        if len(app.placedArtifacts) < 2:
            characters.generateArtifacts(2)
        # move held artifacts with main char
        for artifact in app.heldArtifacts:
            artifact.posX, artifact.posY = app.mainChar.posX, app.mainChar.posY
        if app.maxWeightMsg:
            app.weightMsgTimer += 1
            if app.weightMsgTimer > app.stepsPerSecond:
                app.maxWeightMsg = False
        for powerup in app.powerups:
            if isinstance(powerup, powerups.WallWalk) and powerup.activated:
                powerups.Powerup.powerupTimer += 1
                # disable powerup after 5 seconds
                if powerups.Powerup.powerupTimer > 2.5*app.stepsPerSecond:
                    app.powerups.remove(powerup)
                    powerup.activated = False
                    validLocations = characters.MainChar.validLocations()
                    iterations = 0
                    # if char in middle of wall, move to closest path above or below
                    while (app.mainChar.row, app.mainChar.col) not in validLocations:
                        iterations += 1
                        if iterations > 10: app.mainChar.row += 1
                        else: app.mainChar.row -= 1
                    app.mainChar.updatePosition()
            elif isinstance(powerup, powerups.Invis) and powerup.activated:
                powerups.Powerup.powerupTimer += 1
                # disable powerup after 5 seconds
                if powerups.Powerup.powerupTimer > 2.5*app.stepsPerSecond:
                    app.powerups.remove(powerup)
                    powerup.activated = False
            elif isinstance(powerup, powerups.Magnet) and powerup.activated:
                powerups.Powerup.powerupTimer += 1
                # disable powerup after 5 seconds
                if powerups.Powerup.powerupTimer > 2.5*app.stepsPerSecond:
                    app.powerups.remove(powerup)
                    powerup.activated = False
    # when game started but paused
    elif app.gameStarted and not app.gameOver:
        if app.spinning:
            # run spinner for 10 sec.
            powerups.spinSpinner(app)
            powerups.Powerup.spinTimer += 1
            if powerups.Powerup.spinTimer > 5*app.stepsPerSecond:
                app.spinning = False
                powerups.addPowerup(app)
    elif not app.gameStarted:
        music.emeraldCity.play(loop = True)

def onKeyPress(app, key):
    if not app.gameStarted and key == 't':
        app.heldGems = 3
        app.powerups = [powerups.WallWalk(), powerups.Invis(), powerups.Magnet()]
        app.characters.append(images.guyDanger)
    # call onKeyPress of MainChar class
    if not app.gameOver and not app.paused and not app.showInstructions:
        app.mainChar.onKeyPress(key)

def onMousePress(app, mx, my):
    # when game not yet started
    if not app.gameStarted and not app.gameOver:
        if app.instructions.pressButton(mx, my):
            app.showInstructions = not app.showInstructions
        elif app.startGame.pressButton(mx, my):
            app.gameStarted = True
            restartGame(app)
            music.emeraldCity.pause()
            music.skySummit.play(loop = True)
        elif app.openLevelMenu.pressButton(mx, my):
            app.showLevelMenu = True
        if app.showLevelMenu:
            levelMenu.selectLevel(mx, my)
            if app.close.pressButton(mx, my):
                app.showLevelMenu = False
    # when game started
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
            music.skySummit.pause()
            music.emeraldCity.play(loop = True)
        elif app.showSpinner == True:
            if app.close.pressButton(mx, my):
                app.showSpinner = False
                app.paused = False
            elif app.spinSpinner.pressButton(mx, my) and app.heldGems > 0:
                app.heldGems -= 1
                powerups.Powerup.spinTimer = 0
                app.spinning = True
        # only when playing game & not paused
        if not app.paused:
            if app.wallPowerup.pressButton(mx, my) and powerups.WallWalk.count > 0:
                powerups.WallWalk.count -= 1
                indx = powerups.findPowerup(powerups.WallWalk)
                app.powerups[indx].engagePowerup()
                powerups.Powerup.powerupTimer = 0
            if app.invisPowerup.pressButton(mx, my) and powerups.Invis.count > 0:
                powerups.Invis.count -= 1
                indx = powerups.findPowerup(powerups.Invis)
                app.powerups[indx].engagePowerup()
                powerups.Powerup.powerupTimer = 0
            if app.magnetPowerup.pressButton(mx, my) and powerups.Magnet.count > 0:
                powerups.Magnet.count -= 1
                indx = powerups.findPowerup(powerups.Magnet)
                app.powerups[indx].engagePowerup()
                powerups.Powerup.powerupTimer = 0 
        if app.pause.pressButton(mx, my):
            app.paused = not app.paused
            messages = ["Wow...already taking a break...", "You're lazier than I thought...",
                "Don't tell me you're still here...", "Ummmm don't you want money..."]
            app.pauseMessage = random.choice(messages)
    # when game over
    else:
        if app.restartEndGame.pressButton(mx, my):
            app.gameStarted = False
            app.gameOver = False
            music.emeraldCity.pause()
            music.skySummit.play(loop = True)

    if ((app.showInstructions or (app.gameStarted and app.paused)) and
        not app.showSpinner):
        if app.openCharMenu.pressButton(mx, my):
            app.characterMenu = True
        if app.characterMenu:
            charMenu.selectCharacter(mx, my)
            if app.close.pressButton(mx, my):
                app.characterMenu = False

def onKeyHold(app, keys):
    # call onKeyHold from MainChar class
    if not app.gameOver and not app.paused:
        app.mainChar.onKeyHold(keys)

def redrawAll(app):
    if not app.gameStarted:
        guides.drawGameStart(app)
        if app.characterMenu:
            guides.drawCharacterMenu(app)
        elif app.showInstructions:
            guides.drawInstructions(app)
        elif app.showLevelMenu:
            guides.drawLevelMenu(app)
    elif app.gameOver:
        guides.drawGameOver(app)
    else:
        guides.drawBackground(app, 1)
        if app.characterMenu:
            guides.drawCharacterMenu(app)
        elif app.showInstructions:
            guides.drawInstructions(app)
        elif app.showSpinner:
            powerups.drawSpinner(app)
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
        if not app.characterMenu:
            guides.drawInGame(app)
        if app.maxWeightMsg:
            guides.drawMaxWeightMsg(app)

def main():
    runApp()

main()