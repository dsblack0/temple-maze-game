from cmu_graphics import *
import images, powerups

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
    drawImage(powerups.Invis.image, app.width/4+30, 50, 
              width=10, height=10, align='center')
    app.wallPowerup.draw()
    drawLabel(f'{powerups.WallWalk.name} x{powerups.WallWalk.count}',
              app.width/4+47, 90, size=12, fill='saddleBrown', align='left')
    drawImage(powerups.WallWalk.image, app.width/4+30, 90, 
              width=10, height=10, align='center')
    app.openSpinner.draw()
    drawLabel('Get Powerups!',
              app.width/4+47, 130, size=12, fill='saddleBrown', align='left')
    drawImage(images.spin, app.width/4+30, 130, width=10, height=10, align='center')
    drawImage(images.gem, app.width/3+80, 50, 
              width=15, height=15, align='center')
    drawLabel(f'x{app.heldGems}', 
              app.width/3+92, 50, size=15, fill='saddleBrown', align='left')
    for powerup in app.powerups:
        if powerup.activated:
            timer = (50-powerups.Powerup.powerupTimer) // 10 + 1
            drawLabel(f'Powerup: {timer}s',
                      app.width/3+80, 130, size=15, fill='saddleBrown', align='left')

def drawGameStart(app):
    drawBackground(app, 2)
    drawLabel("Welcome to the", app.width/2, app.height/2-45, 
              fill='saddleBrown', size=90, bold=True, font='monospace')
    drawLabel("Temple Maze", app.width/2, app.height/2+45,
              fill='saddleBrown', size=90, bold=True, font='monospace')
    app.startGame.draw()
    app.instructions.draw()

def drawInGame(app):
    drawInGameButtons(app)
    drawPowerupBox(app)
    drawScoreBox(app)

def drawInstructions(app):
    drawRect(0, app.height/5, app.width, app.height, fill='saddleBrown')
    drawLabel('Instructions', app.width/2, app.height/4, 
              fill='tan', size=50)
    drawLabel('You have joined a group of temple robbers in their mission to steel artifacts from ancient temples.',
              app.width/2, app.height/4+50, fill='tan', size=18)

def drawPauseScreen(app):
    drawRect(0, app.height/5, app.width, app.height, fill='saddleBrown')
    drawLabel('Paused', app.width/2, app.height/2, 
              fill='tan', size=100, font='monospace')

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
    app.restartEndGame.draw()