import pgzrun
import random
TITLE="Hit the monster"
WIDTH=500
HEIGHT=500
mon=Actor("monster.png")
def draw():
    screen.fill("hot pink")
    mon.draw()
    screen.draw.text("Hit the monster", center=(250,250), fontsize= 25, color="yellow",fontname="Times New Bd")
pgzrun.go()