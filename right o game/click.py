import random
import pgzrun

WIDTH=891
HEIGHT=500
#gaming variables
gameover=False
gamewin=False
currentlev=1
totallev=10
speedob=4
listtt=["notebook.png", "ruler.png","pencil sharp.png", "rubber.png", "penci].webp"]
list2=[]
targett=None

def draw():
    screen.blit("classroom.jpg", (0,0))
def update():
    pass
#function to create falling items
def crefall(extra):
    global targett
    list3=[]
    targett=random.choice(listtt)
    wrongitem= random.choices([i for i in listtt if i != targett], k=extra)
    comblist=[targett]+wrongitem
    random.shuffle(comblist)
    sizee=WIDTH/(len(comblist)+1)
    for u, img in enumerate(comblist):
        act=Actor(img)
        act.active=True
        act.x = (u+1) * sizee
        act.y = random.randint(-100,0)
        list3.append(act)
        #animating
pgzrun.go() 

