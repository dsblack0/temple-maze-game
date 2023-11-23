from cmu_graphics import *
import images
import maze

class Character:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.width, self.height = maze.getCellSize(app)
    
    @staticmethod
    def validLocation(self):
        return ((0<=self.row<app.grid.rows) and
                (0<=self.col<app.grid.cols))

class Monster(Character):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.speed = 1

class MainChar(Character):
    def __init__(self, r, c):
        super().__init__(r, c)
    
    def onKeyPress(self, key):
        ogLocation = self.row, self.col
        if key == 'left':
            self.col -= 1
        elif key == 'right':
            self.col += 1
        elif key == 'up':
            self.row -= 1
        elif key == 'down':
            self.row += 1
        if not MainChar.validLocation(self):
            self.row, self.col = ogLocation

    def onKeyHold(self, keys):
        ogLocation = self.row, self.col
        if 'left' in keys:
            self.col -= 1
        elif 'right' in keys:
            self.col += 1
        elif 'up' in keys:
            self.row -= 1
        elif 'down' in keys:
            self.row += 1
        if not MainChar.validLocation(self):
            self.row, self.col = ogLocation
    
    def draw(self):
        posX, posY = maze.getCellLeftTop(app, self.row, self.col)
        drawImage(images.mainChar, posX, posY, align='top-left',
                  width=self.width, height=self.height)