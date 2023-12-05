from cmu_graphics import *
import images, guides, characters

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

def drawCharacterMenu(app):
    guides.drawBackground(app, 1)
    app.close.draw()
    allCharacters = characters.Character.allCharacters
    charNames = ['Karma Lee', 'Guy Danger', 'Scarlett Fox', 'Francisco Montoya']

    for i in range(len(allCharacters)):
        cX, cY = getCXCY(i)

        if allCharacters[i] in app.characters:
            image = allCharacters[i]
        else:
            image = images.lockedChar

        if i == app.currChar:
            drawRect(cX, cY, 215, 315, fill='tan', 
                     align='center')
        drawRect(cX, cY, 200, 300, fill='saddleBrown', align='center')
        drawRect(cX, cY, 195, 295, fill=None, border='tan', align='center')
        drawImage(image, cX, cY, width=195, height=295, align='center')
        drawLabel(charNames[i], cX, cY+170, fill='saddleBrown', 
                  font='monospace', size=25, bold=True)

def selectCharacter(mx, my):
    allCharacters = characters.Character.allCharacters
    for i in range(len(allCharacters)):
        cX, cY = getCXCY(i)

        leftX, rightX = cX-100, cX+100
        topY, bottomY = cY-150, cY+150
        if ((leftX<=mx<=rightX) and (topY<=my<=bottomY) and 
            (allCharacters[i] in app.characters)):
            app.currChar = i
            app.mainChar.updateImage()