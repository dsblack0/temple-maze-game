from cmu_graphics import *

class Button:
    def __init__(self, cX, cY, size, label, type):
        self.cX = cX
        self.cY = cY
        self.size = size
        self.label = label
        self.type = type

    def draw(self):
        if self.type == 'rect':
            drawRect(self.cX, self.cY, self.size*2,
                     self.size, fill='saddleBrown')
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