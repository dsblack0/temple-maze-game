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
        if isinstance(char, MainChar):
            return ((0<=char.row<app.grid.rows) and
                    (0<=char.col<app.grid.cols))
        else:
            return ((3<=char.row<app.grid.rows) and
                    (3<=char.col<app.grid.cols))
        
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
        # pick up artifact when press 'space'
        if key == 'space':
            if self.row == 0 and self.col == 0:
                droppedArtifact = app.heldArtifacts.pop()
                artifactWeight = Artifact.weights[droppedArtifact.image]
                app.droppedWeight += artifactWeight
                app.heldWeight -= artifactWeight
                if app.droppedWeight >= 10:
                    app.droppedWeight -= 10
                    app.score += 1
            else:
                for artifact in app.placedArtifacts:
                    artifactWeight = Artifact.weights[artifact.image]
                    if ((self.row == artifact.row) and (self.col == artifact.col) and
                        (app.heldWeight + artifactWeight <= 10)):
                            app.heldArtifacts.append(artifact)
                            app.placedArtifacts.remove(artifact)
                            app.heldWeight += artifactWeight
                            
        # move mainChar & held artifacts with direction keys            
        self.move(key)
        for artifact in app.heldArtifacts:
            artifact.row, artifact.col = self.row, self.col
        # undo move if not valid location
        if not MainChar.validLocation(self):
            self.row, self.col = ogLocation
            for artifact in app.heldArtifacts:
                artifact.row, artifact.col = ogLocation

    def onKeyHold(self, keys):
        ogLocation = self.row, self.col
        key = None
        if 'left' in keys:
            key = 'left'
        elif 'right' in keys:
            key = 'right'
        elif 'up' in keys:
            key = 'up'
        elif 'down' in keys:
            key = 'down'
        if key:
            self.move(key)
            for artifact in app.heldArtifacts:
                artifact.row, artifact.col = self.row, self.col
        if not MainChar.validLocation(self):
            self.row, self.col = ogLocation
            for artifact in app.heldArtifacts:
                artifact.row, artifact.col = ogLocation

class Monster(Character):
    speed = 1
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

def generateMonsters(count, monsters = []):
    if len(monsters) == count:
        return monsters
    else:
        r, c = random.randrange(app.grid.rows), random.randrange(app.grid.cols)
        newMonster = Monster(r,c)
        if Monster.validLocation(newMonster):
            monsters.append(newMonster)
        return generateMonsters(count, monsters)
    
class Artifact(Character):
    weights = {images.artifact1:6, images.artifact2:3, images.artifact3:4, 
               images.artifact4:7, images.idol1:2, images.idol2:1, 
               images.idol3:5, images.idol4:3, images.idol5:2}
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = random.choice(images.artifacts)
    
    def draw(self):
        super().draw()
        if self not in app.heldArtifacts:
            posX, posY = maze.getCellLeftTop(app, self.row, self.col)
            width, height = maze.getCellSize(app)
            drawLabel(Artifact.weights[self.image], posX+width/2, 
                      posY+height/2, fill='tan', size=width/2, bold=True)

def generateArtifacts(count, artifacts=[]):
    if len(artifacts) == count:
        return artifacts
    else:
        r, c = random.randrange(app.grid.rows), random.randrange(app.grid.cols)
        newArtifact = Artifact(r,c)
        if Artifact.validLocation(newArtifact):
            artifacts.append(newArtifact)
        return generateArtifacts(count, artifacts)