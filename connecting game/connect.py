import pgzrun
import random
import time

WIDTH=750
HEIGHT=449
listt= []
cupcakeline=[]
#gaming variables
totalcupcakes=8
countcupcake=0
starttime=0
totaltime=0
endtime=0
#loop for creating cupcakes
def loopcake():
    global starttime
    for i in range(totalcupcakes):
        cupact= Actor("cupcake.png")
        xrand=random.randint(30,700)
        yrand=random.randint(30,400)
        cupact.pos=xrand,yrand
        listt.append(cupact)
    starttime=time.time()
def draw():
    global totaltime
    screen.blit("baking.jpeg", (0,0))
    for i in listt:
        i.draw()
    if countcupcake < totalcupcakes:
        totaltime=time.time()-starttime
        screen.draw.text(str(round(totaltime,1)),(15,15))
def update():
    pass

loopcake()
pgzrun.go()
