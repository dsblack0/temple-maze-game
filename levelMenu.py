from cmu_graphics import *
import images, guides

def getCXCY(i):
    if i % 2 == 0: 
        cX = app.width/4 + 50
    else: 
        cX = app.width*3/4 - 50
    if i < 2: 
        cY = app.width/4
    else: 
        cY = app.width*3/4
    return cX, cY

def drawLevelMenu(app):
    guides.drawBackground(app, 1)
    app.close.draw()
    levels = [20, 100, 150, 250]
    levelImages = [images.level0, images.level1, images.level2, images.level3]

    for i in range(len(levels)):
        cX, cY = getCXCY(i)

        image = levelImages[i]

        if levels[i] == app.stepsPerSecond:
            drawRect(cX, cY, 215, 315, fill='tan', 
                     align='center')
        drawRect(cX, cY, 200, 300, fill='saddleBrown', align='center')
        drawRect(cX, cY, 195, 295, fill=None, border='tan', align='center')
        drawImage(image, cX, cY, width=195, height=295, align='center')

def selectLevel(mx, my):
    levels = [20, 100, 150, 250]
    
    for i in range(len(levels)):
        cX, cY = getCXCY(i)

        leftX, rightX = cX-100, cX+100
        topY, bottomY = cY-150, cY+150
        if ((leftX<=mx<=rightX) and (topY<=my<=bottomY)):
            app.stepsPerSecond = levels[i]