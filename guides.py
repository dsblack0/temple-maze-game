from cmu_graphics import *
import images, buttons

def drawBackground(app, num):
    if num == 1:
        image = images.background1
    else:
        image = images.background2
    drawImage(image, 0, 0,
              width=app.width, height=app.height)

def drawInGameButtons(app):
    app.pause.draw()
    app.instructions.draw()
    app.restartInGame.draw()

def drawGameStart(app):
    drawBackground(app, 2)
    drawLabel("Welcome to the", app.width/2, app.height/2-45, 
              fill='saddleBrown', size=90, bold=True, font='monospace')
    drawLabel("Temple Maze", app.width/2, app.height/2+45,
              fill='saddleBrown', size=90, bold=True, font='monospace')
    app.startGame.draw()
    app.instructions.draw()

def drawInGame(app):
    drawBackground(app, 1)
    drawInGameButtons(app)
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