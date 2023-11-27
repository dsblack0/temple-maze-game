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
    def validLocations():
        validLocations = []
        # don't go through 3x3 top left corner
        for row in range(4, app.grid.rows):
            for col in range(4, app.grid.cols):
                # create list of remainingvalid locations
                if app.grid.maze[row][col] == True:
                    validLocations.append((row, col))
        return validLocations
        
    def move(self, direction, speed):
        # move col & row based on direction
        if direction == 'left':
            self.col -= 1*speed
        elif direction == 'right':
            self.col += 1*speed
        elif direction == 'up':
            self.row -= 1*speed
        elif direction == 'down':
            self.row += 1*speed
    
    def draw(self):
        posX, posY = maze.getCellLeftTop(app, self.row, self.col)
        drawImage(self.image, posX, posY, align='top-left',
                  width=self.width, height=self.height)

class MainChar(Character):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = images.mainChar

    @staticmethod
    def validLocations():
        validLocations = []
        # go through whole board
        for row in range(app.grid.rows):
                for col in range(app.grid.cols):
                    # create list of all valid locations
                    if app.grid.maze[row][col] == True:
                        validLocations.append((row, col))
        return validLocations

    def onKeyPress(self, key):
        ogLocation = self.row, self.col
        # pick up artifact when press 'space'
        if key == 'space':
            # if at cart, drop of one held artifact
            if ((self.row == 0) and (self.col == 0) and
                app.heldArtifacts != []):
                droppedArtifact = app.heldArtifacts.pop()
                artifactWeight = Artifact.weights[droppedArtifact.image]
                app.droppedWeight += artifactWeight
                app.heldWeight -= artifactWeight
                # increment score for every 10 weights
                if app.droppedWeight >= 10:
                    app.droppedWeight -= 10
                    app.score += 1
            else:
                for artifact in app.placedArtifacts:
                    artifactWeight = Artifact.weights[artifact.image]
                    # if at artifact location, pick up if total weight not over 10
                    if ((self.row == artifact.row) and (self.col == artifact.col) and
                        (app.heldWeight + artifactWeight <= 10)):
                            app.heldArtifacts.append(artifact)
                            app.placedArtifacts.remove(artifact)
                            app.heldWeight += artifactWeight
                            
        # move mainChar & held artifacts with direction keys            
        self.move(key, 1)
        for artifact in app.heldArtifacts:
            artifact.row, artifact.col = self.row, self.col
        # undo move if not valid location
        if (self.row, self.col) not in MainChar.validLocations():
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
        # move character & held artifacts if direction key held
        if key:
            self.move(key, 1)
            for artifact in app.heldArtifacts:
                artifact.row, artifact.col = self.row, self.col
        # undo move if not valid
        if (self.row, self.col) not in MainChar.validLocations():
            self.row, self.col = ogLocation
            for artifact in app.heldArtifacts:
                artifact.row, artifact.col = ogLocation

class Monster(Character):
    speed = 1
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = images.monster

    def moveOnStep(self, directions):
        if app.timer % (app.stepsPerSecond/Monster.speed) == 0.0:
            direction = random.choice(directions)
            ogLocation = self.row, self.col
            self.move(direction, 2)
            if (self.row, self.col) not in Monster.validLocations():
                # revert move if not valid
                self.row, self.col = ogLocation
                # try moving again in another direction
                directions.remove(direction)
                self.moveOnStep(directions)

def generateMonsters(count, monsters = []):
    # create monsters until reach desired count
    if len(monsters) == count:
        return monsters
    else:
        validLocations = Monster.validLocations()
        # randomly choose a valid location
        r, c = random.choice(validLocations)
        # create new monster placed at that location
        newMonster = Monster(r,c)
        monsters.append(newMonster)
        return generateMonsters(count, monsters)
    
class Artifact(Character):
    # initialize weights of each artifact piece
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
                      posY+height/2, fill='saddleBrown', size=width/2, bold=True)

def generateArtifacts(count, artifacts=[]):
    if len(artifacts) == count:
        return artifacts
    else:
        validLocations = Artifact.validLocations()
        # randomly choose a valid location
        r, c = random.choice(validLocations)
        # create new artifact placed at that location
        newArtifact = Artifact(r,c)
        artifacts.append(newArtifact)
        return generateArtifacts(count, artifacts)