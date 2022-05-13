"""Simon Says

Exercises

1. Speed up tile flash rate.
2. Add more tiles.
"""

from random import choice
from time import sleep
from turtle import *
from random import randrange

from freegames import floor, square, vector

#Colores diferentes en cada juego - Santiago Ramírez
colorarray = ['red','blue','yellow','green','orange','blue violet','white','grey'] #Arrays con los colores claros y oscuros
darkcolorarray = ['dark red', 'dark blue', 'khaki', 'dark green','dark orange', 'dark violet', 'light gray' , 'dim grey']

panel1color = randrange(0,8) #Selecciona el indice del color al azar para cada panel
panel2color = randrange(0,8)
panel3color = randrange(0,8) #Luego se usan estos indices para seleccionar los colores del
panel4color = randrange(0,8) #array en tiles y grid()
#--------------------------------------------------------------------------------------------------------
pattern = []
guesses = []
tiles = {
    vector(0, 0): (colorarray[panel1color], darkcolorarray[panel1color]),
    vector(0, -200): (colorarray[panel2color], darkcolorarray[panel2color]),
    vector(-200, 0): (colorarray[panel3color], darkcolorarray[panel3color]),
    vector(-200, -200): (colorarray[panel4color], darkcolorarray[panel4color]),
}


def grid():
    """Draw grid of tiles."""
    square(0, 0, 200, darkcolorarray[panel1color])
    square(0, -200, 200, darkcolorarray[panel2color])
    square(-200, 0, 200, darkcolorarray[panel3color])
    square(-200, -200, 200, darkcolorarray[panel4color])
    update()


def flash(tile):
    """Flash tile in grid."""
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.3)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.3)


def grow():
    """Grow pattern and flash tiles."""
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()


def tap(x, y):
    """Respond to screen tap."""
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        exit()

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

    onscreenclick(tap)


def start(x, y):
    """Start game."""
    grow()
    onscreenclick(tap)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()