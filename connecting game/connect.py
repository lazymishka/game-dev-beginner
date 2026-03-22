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
    count=1
    for i in listt:
        i.draw()
        screen.draw.text(str(count),(i.pos[0], i.pos[1]+20))
        count=count+1
    for g in cupcakeline:
        screen.draw.line(g[0],g[1],"black")
    if countcupcake < totalcupcakes:
        totaltime=time.time()-starttime
        screen.draw.text(str(round(totaltime,1)),(15,15))
    else:
       screen.draw.text(str(round(totaltime,1)),(15,15)) 

#function for mouseclick
def on_mouse_down(pos):
    global countcupcake, cupcakeline
    if countcupcake < totalcupcakes:
        if listt[countcupcake].collidepoint(pos):
            if countcupcake:
                cupcakeline.append((listt[countcupcake-1].pos, listt[countcupcake].pos))
            countcupcake=countcupcake+1
        else:
            cupcakeline=[]
            countcupcake=0
        

def update():
    pass

loopcake()
pgzrun.go()
