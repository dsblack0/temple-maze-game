from cmu_graphics import *
import images, powerups, charMenu, levelMenu

def drawBackground(app, num):
    if num == 1:
        image = images.background1
    else:
        image = images.background2
    drawImage(image, 0, 0,
              width=app.width, height=app.height)

def drawInGameButtons(app):
    if not app.showSpinner:
        app.pause.draw()
    app.instructions.draw()
    app.restartInGame.draw()

def drawPowerupBox(app):
    drawRect(app.width/4+5, 20, app.width/3-25, app.height/6, 
             fill='tan', align='top-left')
    drawRect(app.width/4+10, 25, app.width/3-35, app.height/6-10, 
             fill=None, border='saddleBrown', align='top-left')
    app.invisPowerup.draw()
    drawLabel(f'{powerups.Invis.name} x{powerups.Invis.count}',
              app.width/4+47, 50, size=12, fill='saddleBrown', align='left')
    app.wallPowerup.draw()
    drawLabel(f'{powerups.WallWalk.name} x{powerups.WallWalk.count}',
              app.width/4+47, 90, size=12, fill='saddleBrown', align='left')
    app.openSpinner.draw()
    drawLabel('Get Powerups!',
              app.width/4+47, 130, size=12, fill='saddleBrown', align='left')
    app.magnetPowerup.draw()
    drawLabel(f'{powerups.Magnet.name} x{powerups.Magnet.count}',
              app.width/3+97, 50, size=12, fill='saddleBrown', align='left')
    drawImage(images.gem, app.width/3+80, 90, 
              width=15, height=15, align='center')
    drawLabel(f'x{app.heldGems}', 
              app.width/3+92, 90, size=15, fill='saddleBrown', align='left')
    for powerup in app.powerups:
        if powerup.activated:
            totalTime = 2.5*app.stepsPerSecond
            timer = (totalTime-powerups.Powerup.powerupTimer) // (app.stepsPerSecond/2) + 1
            drawLabel(f'Powerup: {int(timer)}s',
                      app.width/3+80, 130, size=15, fill='saddleBrown', align='left')

def drawGameStart(app):
    drawBackground(app, 2)
    drawLabel("Welcome to the", app.width/2, app.height/2-45, 
              fill='saddleBrown', size=90, bold=True, font='monospace')
    drawLabel("Temple Maze", app.width/2, app.height/2+45,
              fill='saddleBrown', size=90, bold=True, font='monospace')
    app.startGame.draw()
    app.instructions.draw()
    app.openLevelMenu.draw()

def drawInGame(app):
    drawInGameButtons(app)
    drawPowerupBox(app)
    drawScoreBox(app)

def drawInstructions(app):
    drawRect(0, app.height/5, app.width, app.height, fill='saddleBrown')
    drawLabel('Instructions', app.width/2, app.height/4, 
              fill='tan', size=50, bold=True, font='monospace')
    drawLabel('You have joined a group of temple robbers in their mission to steel artifacts from ancient temples.',
              app.width/2, app.height/4+50, fill='tan', size=18)
    drawLabel('Go forth on your solo adventure through the temple maze, in search of these priceless artifacts.',
              app.width/2, app.height/4+70, fill='tan', size=18)
    drawLabel("As you run, BEWARE the monster! You're a crunchy human...",
              app.width/2, app.height/4+90, fill='tan', size=18)
    drawLabel('They will be looking for every chance to eat you when you least expect it.',
              app.width/2, app.height/4+110, fill='tan', size=18)
    drawLabel('Rules',app.width/2, app.height/4+140,
              fill='tan', size=25, bold=True, font='monospace')
    drawLabel('1. You often forget to go to the gym, so you can only carry 10 kg worth of artifacts at a time.',
              25, app.height/4+170, fill='tan', size=18, align='left')
    drawLabel('2. You must bring the artifacts back to your cart, located at the start of the maze',
              25, app.height/4+190, fill='tan', size=18, align='left')
    drawLabel('3. The artifacts have broken over time. For every 10kg you drop off, you will obtain 1 full artifact.',
              25, app.height/4+210, fill='tan', size=18, align='left')
    drawLabel("4. There are gems scattered through the temple's maze. Use them to spin the wheel of secrets!",
              25, app.height/4+230, fill='tan', size=18, align='left')
    drawLabel('Guides', app.width/2, app.height/4+260,
              fill='tan', size=25, bold=True, font='monospace')
    drawLabel('1. Use the arrow keys to navigate around the maze.',
              25, app.height/4+290, fill='tan', size=18, align='left')
    drawLabel('2. Use the space bar to pick up & drop off gems/artifact pieces.',
              25, app.height/4+310, fill='tan', size=18, align='left')
    drawLabel('Note: You will drop off one artifact piece each time you press the space bar',
              50, app.height/4+330, fill='tan', size=18, align='left', italic=True)
    drawLabel('3. Use the power ups box to activate powers & access the wheel of secrets.',
              25, app.height/4+350, fill='tan', size=18, align='left')
    drawLabel("4. TO LOAD TEST DEFAULTS: Press 't' before starting the game",
              25, app.height/4+370, fill='tan', size=18, align='left')
    drawLabel("Note: Not to be used for regular game play",
              50, app.height/4+390, fill='tan', size=18, align='left', italic=True)
    drawLabel('Powerups', app.width/2, app.height/4+420,
              fill='tan', size=25, bold=True, font='monospace')
    drawLabel('Invisibility: Keeps you hidden from the hungry monsters for 5 seconds',
              25, app.height/4+450, fill='tan', size=18, align='left')
    drawLabel('Wall Walking: You can walk through and hide in any wall for 5 seconds',
              25, app.height/4+470, fill='tan', size=18, align='left')
    drawLabel('Magnets: You can automatically pick up nearby artifacts without weight restrictions for 5 seconds',
              25, app.height/4+490, fill='tan', size=18, align='left')
    app.openCharMenu.draw()

def drawPauseScreen(app):
    
    drawRect(0, app.height/5, app.width, app.height, fill='saddleBrown')
    drawLabel('Paused', app.width/2, app.height/2, 
              fill='tan', size=100, font='monospace')
    drawLabel(app.pauseMessage, app.width/2, app.height/2+150, 
              fill='tan', size=38, font='monospace', bold=True, italic=True)
    app.openCharMenu.draw()

def drawCharacterMenu(app):
    charMenu.drawCharacterMenu(app)

def drawLevelMenu(app):
    levelMenu.drawLevelMenu(app)

def drawMaxWeightMsg(app):
    drawRect(app.width/2, 100, app.width/2, app.height/8, 
             fill='saddleBrown', align='center')
    drawRect(app.width/2, 100, app.width/2-10, app.height/8-10, 
             fill=None, border='tan', align='center')
    drawLabel("Applied to be a temple robber...", app.width/2, 85, 
              size=20, fill='tan', font='monospace', bold=True)
    drawLabel("but can only pick up 10kg...", app.width/2, 115, 
              size=20, fill='tan', font='monospace', bold=True)

def drawScoreBox(app):
    drawRect(app.width-150, 20, app.width/4, app.height/6, 
             fill='saddleBrown', align='top-right')
    drawRect(app.width-155, 25, app.width/4-10, app.height/6-10, 
             fill=None, border='tan', align='top-right')
    drawLabel(f'Current Weight Held: {app.heldWeight}',
              app.width*3/4-140, 35, align='top-left',
              fill='tan', size=15)
    drawLabel(f'Current Dropped Weight: {app.droppedWeight}',
              app.width*3/4-140, 65, align='top-left',
              fill='tan', size=15)
    drawLabel(f'Current Score: {app.score}',
              app.width*3/4-140, 95, align='top-left',
              fill='tan', size=15)
    drawLabel(f'High Score: {app.highScore}',
              app.width*3/4-140, 125, align='top-left',
              fill='tan', size=15)


def drawGameOver(app):
    drawBackground(app, 1)
    drawLabel('Game Over', app.width/2, app.height/2, 
              fill='saddleBrown', bold=True, size=100, font='monospace')
    drawRect(app.width/2, app.height/2+150, app.width, 50, fill='tan', align='center')
    drawLabel(app.endMessage, app.width/2, app.height/2+150, 
              fill='saddleBrown', size=25, font='monospace', bold=True, italic=True)
    app.restartEndGame.draw()