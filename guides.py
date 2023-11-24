from cmu_graphics import *

def drawGameOver(app):
    drawRect(0, 0, app.width, app.height, fill='brown')
    drawLabel("Game Over", app.width/2, app.height/2, 
              fill='white', size=100)