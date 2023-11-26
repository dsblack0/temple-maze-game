from cmu_graphics import *
import images, buttons

def drawBackground(app):
    drawImage(images.background, 0, 0,
              width=app.width, height=app.height)

def drawInGameButtons(app):
    app.pause.draw()
    app.instructions.draw()

def drawGameStart(app):
    pass

def drawInstructions(app):
    drawRect(0, app.width/5, app.width, app.height, fill='saddleBrown')
    drawLabel("Instructions", app.width/2, app.height/2, 
              fill='tan', size=100)

def drawPauseScreen(app):
    drawRect(0, app.width/5, app.width, app.height, fill='saddleBrown')
    drawLabel("Paused", app.width/2, app.height/2, 
              fill='tan', size=100)

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
    drawRect(0, 0, app.width, app.height, fill='saddleBrown')
    drawLabel("Game Over", app.width/2, app.height/2, 
              fill='tan', size=100)