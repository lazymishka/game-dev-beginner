import pgzrun
import random
TITLE="Hit the monster"
WIDTH=500
HEIGHT=500
mon=Actor("monster.png")
mes = "Hit the monster"
def draw():
    screen.fill("hot pink")
    mon.draw()
    screen.draw.text(mes, center=(250,250), fontsize= 25, color="yellow")
#functionforrandposofthemonster#
def monsterpos():
    mon.x=random.randint(0,500)
    mon.y=random.randint(0,500)
    clock.schedule_unique(misclick,2.0)
def misclick():
    global mes
    mes= "You've misclicked, try again!" 
    monsterpos()

monsterpos()
pgzrun.go()
