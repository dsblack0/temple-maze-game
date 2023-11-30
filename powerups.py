from cmu_graphics import *
import images, guides

class Powerup:
    spinTimer = 0
    powerupTimer = 0
    def __init__(self):
        self.activated = False

    def engagePowerup(self):
        self.activated = True

    def powerup(self):
        return self.activated


class WallWalk(Powerup):
    count = 0
    name = 'WallWalking'
    image = images.walls
    def __init__(self):
        super().__init__()
        WallWalk.count += 1
    
class Invis(Powerup):
    count = 0
    name = 'Insivibility'
    image = images.invis
    def __init__(self):
        super().__init__()
        Invis.count += 1

def findPowerup(powerup):
    for i in range(len(app.powerups)):
        if isinstance(app.powerups[i], powerup):
            return i
    return -1

def labelLocation(i):
    if i == 0:
        return app.width/2+110, app.height/2-75
    elif i == 1:
        return app.width/2, app.height/2-150
    elif i == 2:
        return app.width/2-110, app.height/2-75
    elif i == 3:
        return app.width/2-100, app.height/2+50
    elif i == 4:
        return app.width/2, app.height/2+100
    elif i == 5:
        return app.width/2+100, app.height/2+50

def drawSpinner(app):
    guides.drawBackground(app, 2)
    app.closeSpinner.draw()
    degree = 360 / len(app.spinner)
    for i in range(len(app.spinner)):
        section = app.spinner[i]
        drawArc(app.width/2, app.height/2, app.width/2, app.height/2,
                i*degree, degree, fill='saddleBrown', border='tan')
        if section == 'Invis': image, label = Invis.image, Invis.name
        elif section == 'WallWalk': image, label = WallWalk.image, WallWalk.name
        elif section == 'Gem': image, label = images.gem, '+1 Gem'
        else: image, label = images.sadFace, 'Too Bad...'
        cx, cy = labelLocation(i)
        drawLabel(label, cx, cy, fill='tan', size=18)
        drawImage(image, cx, cy+30, width=30, height=30, align='center')
    drawArc(app.width/2, app.height/2-app.height/4+30, 100, 100,
            60, 60, fill='tan')
    app.spinSpinner.draw()

def spinSpinner(app):
    lastSection = app.spinner.pop()
    app.spinner = [lastSection] + app.spinner

def addPowerup(app):
    powerup = app.spinner[1]
    if powerup == 'WallWalk':
        app.powerups.append(WallWalk())
    elif powerup == 'Invis':
        app.powerups.append(Invis())
    elif powerup == 'Gem':
        app.heldGems += 1
