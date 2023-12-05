from cmu_graphics import *

class Button:
    def __init__(self, cX, cY, size, label, type, width='short'):
        self.cX = cX
        self.cY = cY
        self.size = size
        self.label = label
        self.type = type
        self.width = width

    def draw(self):
        if self.type == 'rect':
            if self.width=='long': width=self.size*7
            else: width = self.size*3
            drawRect(self.cX, self.cY, width,
                     self.size, fill='saddleBrown', align='center')
            drawRect(self.cX, self.cY, width-5, self.size-5,
                     fill=None, border='tan', align='center')
        elif self.type == 'circle':
            drawCircle(self.cX, self.cY, self.size,
                       fill='saddleBrown')
            drawCircle(self.cX, self.cY, self.size-5,
                       fill=None, border='tan')
        drawLabel(self.label, self.cX, self.cY, size=self.size*2/3, 
                  fill='tan', bold=True, align='center', font='monospace')
            
        
    def pressButton(self, mx, my):
        if self.type == 'rect':
            leftX, rightX = self.cX-self.size, self.cX+self.size
            topY, bottomY = self.cY-self.size/2, self.cY+self.size/2
            return (leftX<=mx<=rightX) and (topY<=my<=bottomY)
        elif self.type == 'circle':
            return ((self.cX-mx)**2+(self.cY-my)**2)**0.5 <= self.size

def initializeButtons(app):
    app.pause = Button(app.width-100, 20+app.height/24, app.width/30, '||', 'circle')
    app.instructions = Button(app.width-100, 20+app.height/8, app.width/30, 'I', 'circle')
    app.restartEndGame = Button(app.width/2, app.height/2+200, 50, 'Restart', 'rect')
    app.restartInGame = Button(app.width/7+10, app.height/12+20, 50, 'Restart', 'rect')
    app.startGame = Button(app.width/2, app.height/2+200, 50, 'Start', 'rect')
    app.invisPowerup = Button(app.width/4+30, 50, 15, '', 'circle')
    app.wallPowerup = Button(app.width/4+30, 90, 15, '', 'circle')
    app.openSpinner = Button(app.width/4+30, 130, 15, '', 'circle')
    app.close = Button(app.width-100, 20+app.height/24, app.width/30, 'X', 'circle')
    app.spinSpinner = Button(app.width/2, app.height*3/4+100, 50, 'Spin!', 'rect')
    app.openCharacters = app.restartEndGame = Button(app.width/2, app.height-100, 50, 'Switch Character', 'rect', 'long')