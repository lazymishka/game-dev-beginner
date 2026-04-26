import random
import pgzrun

WIDTH=891
HEIGHT=500
#gaming variables
gameover=False
gamewin=False
currentlev=1
totallev=7
speedob=8
listtt=["notebook.png", "ruler.png","pencil sharp.png", "rubber.png", "pencil.png"]
list2=[]
targett=None

def draw():
    screen.blit("classroom.jpg", (0,0))
    if gameover:
        screen.fill("white")
        screen.draw.text("!!GAME OVER!!", (400, 200), fontsize=60)
    for i in list2:
        i.draw()
    screen.draw.text(f"level-{currentlev}",(400, 50), fontsize=30)
    if targett:
        screen.draw.text(f"click the {targett}", (400, 150), fontsize=30)
def update():
    pass
    global list2, currentlev
    if gameover or gamewin:
        return
    if len(list2)==0:
        list2=crefall(currentlev)
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
        animate(act, duration=max(1, speedob-currentlev),on_finished=lambda a=act: reached_bottom(a), y=HEIGHT)
    return list3
#function for the bottom
def reached_bottom(a):
    global gameover
    if not a.active:
        return
    if a.image==targett:
        gameover=True
#game over function
def gameoverr():
    global gameoverr
    gameoverr=True
#mouse click event
def on_mouse_down(pos):
    global currentlev, gameover, gamewin, list2
    if gameover or gamewin:
        return 
    #game still running
    for i in list2:
        if i.collidepoint(pos):
            if i.image==targett:
                if currentlev==totallev:
                     gamewin=True
                else:
                    currentlev=currentlev+1
                    for a in list2:
                        a.active=False
                    list2=[]
            else:
                gameoverr()
#restarting function
def restartt():
    global gameover, gamewin, currentlev, list2, targett
    for e in list2:
        e.active=False
    gameover=False
    gamewin=False
    currentlev=1
    list2=[]
    targett=None
pgzrun.go() 

