from cmu_graphics import *
import random
import images, maze, powerups

class Character:
    allCharacters = [images.karmaLee, images.guyDanger, 
                     images.scarlettFox, images.franciscoMontoya]
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.updatePosition()
        self.isMoving = None
        self.width, self.height = maze.getCellSize(app)
    
    @staticmethod
    def validLocations():
        validLocations = []
        # don't go through 3x3 top left corner
        for row in range(2, app.grid.rows):
            for col in range(2, app.grid.cols):
                # create list of remainingvalid locations
                if app.grid.maze[row][col] == True:
                    validLocations.append((row, col))
        return validLocations
        
    def updatePosition(self):
        self.posX, self.posY = maze.getCellLeftTop(app, self.row, self.col)

    def updateRowCol(self):
        cellW, cellH = maze.getCellSize(app)

        self.col = (self.posX - app.grid.left) // cellW
        self.row = (self.posY - app.grid.top) //cellH

    def move(self, direction, speed):
        ogLocation = self.posX, self.posY
        cellW, cellH = maze.getCellSize(app)
        # move col & row based on direction
        if direction == 'left':
            self.posX -= 11.5*speed
        elif direction == 'right':
            self.posX += 11.5*speed
        elif direction == 'up':
            self.posY -= 13*speed
        elif direction == 'down':
            self.posY += 13*speed
        self.updateRowCol() 
        # undo move if not valid location
        indx = powerups.findPowerup(powerups.WallWalk)
        if (isinstance(self, MainChar) and
            (indx != -1) and (app.powerups[indx].activated)):
                # if WallWalk powerup active, MainChar can move anywhere on grid
                if ((not (0<=self.row<app.grid.rows) and (0<=self.col<app.grid.cols) or
                      (self.posX>app.grid.left + app.grid.width - cellW) 
                      or (self.posY>app.grid.top + app.grid.height - cellH))):
                    self.posX, self.posY = ogLocation
        else:
            # check if char position doesn't overlap any walls
            for (r, c) in maze.wallLocations():
                wallX, wallY = maze.getCellLeftTop(app, r, c)
                if maze.doOverlap(app, self.posX, self.posY, wallX, wallY):
                    self.posX, self.posY = ogLocation
                    break   
        self.updateRowCol()
        # check if new row & col are validLocation for character type
        if (((self.row, self.col) not in self.validLocations()) or
            (self.posX>app.grid.left + app.grid.width - cellW) or 
            (self.posY>app.grid.top + app.grid.height - cellH)):
            self.posX, self.posY = ogLocation
            self.updateRowCol()
    
    def draw(self):
        drawImage(self.image, self.posX, self.posY, align='top-left',
                  width=self.width, height=self.height)

class MainChar(Character):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = Character.allCharacters[app.currChar]

    def updateImage(self):
        self.image = Character.allCharacters[app.currChar]

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
                if app.droppedWeight >= 5:
                    app.droppedWeight -= 5
                    app.score += 1
            elif (app.gem and maze.doOverlap(app, self.posX, self.posY, 
                                             app.gem.posX, app.gem.posY)):
                    app.heldGems += 1
                    app.gem = None
            else:
                for artifact in app.placedArtifacts:
                    artifactWeight = Artifact.weights[artifact.image]
                    # if at artifact location, pick up if total weight not over 10
                    if maze.doOverlap(app, self.posX, self.posY, artifact.posX, 
                                        artifact.posY):
                        # control max weight
                        if app.heldWeight + artifactWeight <= 10:
                            app.heldArtifacts.append(artifact)
                            app.placedArtifacts.remove(artifact)
                            app.heldWeight += artifactWeight
                        else:
                            app.maxWeightMsg = True
                            app.weightMsgTimer = 0
                    # if Magnet powerup activated
                    indx = powerups.findPowerup(powerups.Magnet)
                    dX, dY = maze.getCellSize(app)
                    if ((indx != -1) and (app.powerups[indx].activated)):
                        if ((self.row-4 <= artifact.row <= self.row+4) and
                            (self.col-4 <= artifact.col <= self.col+4)):
                            app.heldArtifacts.append(artifact)
                            app.placedArtifacts.remove(artifact)
                            app.heldWeight += artifactWeight
                            
        # move mainChar & held artifacts with direction keys            
        self.move(key, 1)

    def onKeyHold(self, keys):
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

class Monster(Character):
    speed = 1
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = images.monster

    def moveOnStep(self, directions):
        direction = random.choice(directions)
        ogLocation = self.row, self.col
        self.move(direction, 3)
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
        # randomly choose a valid location
        r, c = random.choice(app.validLocations)
        # create new monster placed at that location
        if (r, c) not in maze.wallLocations():
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
        # randomly choose a valid location
        r, c = random.choice(app.validLocations)
        # create new artifact placed at that location
        if (r, c) not in maze.wallLocations():
            newArtifact = Artifact(r,c)
            artifacts.append(newArtifact)
        return generateArtifacts(count, artifacts)
    
class Gem(Character):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.image = images.gem

def generateGem():
        validLocations = Gem.validLocations()
        # randomly choose a valid location
        r, c = random.choice(validLocations)
        # create one gem placed at that location
        return Gem(r, c)