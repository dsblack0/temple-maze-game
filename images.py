from cmu_graphics import *
from PIL import Image

mainChar = Image.open('images/mainChar.png')
mainChar = CMUImage(mainChar)

monster = Image.open('images/monster.png')
monster = CMUImage(monster)

artifact1 = Image.open('images/artifact1.png')
artifact1 = CMUImage(artifact1)

artifact2 = Image.open('images/artifact2.png')
artifact2 = CMUImage(artifact2)

artifact3 = Image.open('images/artifact3.png')
artifact3 = CMUImage(artifact3)

artifact4 = Image.open('images/artifact4.png')
artifact4 = CMUImage(artifact4)

idol1 = Image.open('images/idol1.png')
idol1 = CMUImage(idol1)

idol2 = Image.open('images/idol2.png')
idol2 = CMUImage(idol2)

idol3 = Image.open('images/idol3.png')
idol3 = CMUImage(idol3)

idol4 = Image.open('images/idol4.png')
idol4 = CMUImage(idol4)

idol5 = Image.open('images/idol5.png')
idol5 = CMUImage(idol5)

artifacts = [artifact1, artifact2, artifact3, artifact4,
             idol1, idol2, idol3, idol4, idol5]
