from cmu_graphics import *
import images

class Powerup:
    def __init__(self):
        self.activated = False

    def engagePowerup(self):
        self.activated = True

    def powerup(self):
        return self.activated


class WallWalk(Powerup):
    count = 0
    name = 'WallWalking'
    def __init__(self):
        super().__init__()
        WallWalk.count += 1
    
class Invis(Powerup):
    count = 0
    name = 'Insivibility'
    def __init__(self):
        super().__init__()
        Invis.count += 1
