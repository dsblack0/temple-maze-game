from cmu_graphics import *
from PIL import Image

# CITATION: https://www.istockphoto.com/photos/desert-ground
background1 = Image.open('images/background1.jpg')
background1 = CMUImage(background1)

# CITATION: https://en.wikipedia.org/wiki/Western_Wall_Tunnel
background2 = Image.open('images/background2.jpg')
background2 = CMUImage(background2)

# CITATION: https://www.123rf.com/photo_17362040_old-temple-brick-wall.html
walls = Image.open('images/walls.jpg')
walls = CMUImage(walls)

# CITATION: https://templerun.fandom.com/wiki/Invincibility
invis = Image.open('images/invis.png')
invis = CMUImage(invis)

# CITATION: https://stock.adobe.com/images/board-game-color-spinner-vector-illustration-icon-symbol-graphic/249920162
spin = Image.open('images/spin.png')
spin = CMUImage(spin)

# CITATION: https://templerun.fandom.com/wiki/Gems
gem = Image.open('images/gem.png')
gem = CMUImage(gem)

# CITATION: https://www.dictionary.com/e/emoji/crying-face-emoji/
sadFace = Image.open('images/sadFace.png')
sadFace = CMUImage(sadFace)

# CITATION: https://www.models-resource.com/resources/big_icons/21/20777.png?updated=1501277066
guyDanger = Image.open('images/guyDanger.png')
guyDanger = CMUImage(guyDanger)

# CITATION: http://vgame.vivas.vn/index.php?r=content%2Fdetail&contentid=6698
karmaLee = Image.open('images/karmaLee.png')
karmaLee = CMUImage(karmaLee)

# CITATION: https://venturebeat.com/games/temple-run-2-review/
scarlettFox = Image.open('images/scarlettFox.png')
scarlettFox = CMUImage(scarlettFox)

# CITATION: https://www.youtube.com/watch?app=desktop&v=occSvatkG1I&ab_channel=4PlayersOnly
franciscoMontoya = Image.open('images/franciscoMontoya.png')
franciscoMontoya = CMUImage(franciscoMontoya)

lockedChar = Image.open('images/lockedChar.png')
lockedChar = CMUImage(lockedChar)

# CITATION: https://dragoart.com/tut/how-to-draw-an-evil-demon-monkey-from-temple-run-17074
monster = Image.open('images/monster.png')
monster = CMUImage(monster)

# CITATION: https://www.eventprophire.com/product/wooden-mine-cart/
cart = Image.open('images/cart.png')
cart = CMUImage(cart)

# CITATION: https://solaralberta.ca/2021/06/25/religion-culture-and-the-sun/
artifact1 = Image.open('images/artifact1.png')
artifact1 = CMUImage(artifact1)

artifact2 = Image.open('images/artifact2.png')
artifact2 = CMUImage(artifact2)

artifact3 = Image.open('images/artifact3.png')
artifact3 = CMUImage(artifact3)

artifact4 = Image.open('images/artifact4.png')
artifact4 = CMUImage(artifact4)

# CITATION: https://www.facebook.com/TempleRun/posts/by-popular-demand-the-idol-image-from-yesterday-in-wallpaper-size-for-your-devic/1041864785863780/
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
