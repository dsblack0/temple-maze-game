from cmu_graphics import *
import images

class Button:
    pass

def drawBackground(app):
    pass

def drawGameStart(app):
    pass

def drawInstructions(app):
    pass

def pauseScreen(app):
    pass

def drawScoreBox(app):
    drawRect(app.width-50, 20, app.width/4, app.width/6, 
             fill='saddleBrown', align='top-right')
    drawLabel(f'Current Weight Held: {app.heldWeight}',
              app.width*3/4-40, 50, align='top-left',
              fill='tan', size=15)
    drawLabel(f'Current Dropped Weight: {app.droppedWeight}',
              app.width*3/4-40, 80, align='top-left',
              fill='tan', size=15)
    drawLabel(f'Current Score: {app.score}',
              app.width*3/4-40, 110, align='top-left',
              fill='tan', size=15)

def drawGameOver(app):
    drawRect(0, 0, app.width, app.height, fill='saddleBrown')
    drawLabel("Game Over", app.width/2, app.height/2, 
              fill='tan', size=100)