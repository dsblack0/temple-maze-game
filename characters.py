from cmu_graphics import *
import random
import images
import maze

class Character:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.width, self.height = maze.getCellSize(app)
    
    @staticmethod
    def validLocation(char):
        if isinstance(char, Monster):
            return ((3<=char.row<app.grid.rows) and
                    (3<=char.col<app.grid.cols))
        else:
            return ((0<=char.row<app.grid.rows) and
                    (0<=char.col<app.grid.cols))
        
    def move(self, direction):
        if direction == 'left':
            self.col -= 1
        elif direction == 'right':
            self.col += 1
        elif direction == 'up':
            self.row -= 1
        elif direction == 'down':
            self.row += 1
    
    def draw(self):
        posX, posY = maze.getCellLeftTop(app, self.row, self.col)
        drawImage(self.image, posX, posY, align='top-left',
                  width=self.width, height=self.height)

class MainChar(Character):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = images.mainChar
    
    def onKeyPress(self, key):
        ogLocation = self.row, self.col
        self.move(key)
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

class Monster(Character):
    speed = 2
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = images.monster

    def moveOnStep(self):
        if app.timer % (app.stepsPerSecond/Monster.speed) == 0.0:
            direction = random.choice(['left', 'right', 'up', 'down'])
            ogLocation = self.row, self.col
            self.move(direction)
            if not Monster.validLocation(self):
                self.row, self.col = ogLocation
                self.moveOnStep()

def generateMonsters(count, monsters):
    if len(monsters) == count:
        return monsters
    else:
        r, c = random.randrange(app.grid.rows), random.randrange(app.grid.cols)
        newMonster = Monster(r,c)
        if Monster.validLocation(newMonster):
            monsters.append(newMonster)
        return generateMonsters(count, monsters)
    
class Artifact(Character):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = random.choice(images.artifacts)

def generateArtifacts(count, artifacts):
    if len(artifacts) == count:
        return artifacts
    else:
        r, c = random.randrange(app.grid.rows), random.randrange(app.grid.cols)
        newArtifact = Artifact(r,c)
        if Artifact.validLocation(newArtifact):
            artifacts.append(newArtifact)
        return generateArtifacts(count, artifacts)