from cmu_graphics import *
import os, pathlib

# CITATION: Code for loading sound from soundDemo Piazza Post 2147
def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)

# CITATION: https://www.youtube.com/watch?v=RQN1Pl1xUZM&ab_channel=ShadyInktail
emeraldCity = loadSound('music/emeraldCity.mp3')
# CITATION: https://www.youtube.com/watch?v=18qQrYMmrOg&list=PLx7hJyUUtt00zEzesvYlyyiJKJ3hqou-F&index=2&ab_channel=ShadyInktail
skySummit = loadSound('music/skySummit.mp3')