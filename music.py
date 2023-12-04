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

emeraldCity = loadSound('music/emeraldCity.mp3')
skySummit = loadSound('music/skySummit.mp3')