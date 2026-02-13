import pgzrun
import random
WIDTH=736
HEIGHT=414
monkey = Actor('monkey.png')
banana = Actor('banana.png')
score = 0 
def draw():
    #bgimage
    screen.blit("house.jpg",(0,0))
    monkey.draw()
    banana.draw()
    #writing score
    screen.draw.text("Score : "+str(score), color="yellow",center=(35,15))
    #changescreen
    if over == True:
        screen.fill("white")
        screen.draw.text("Game over!", color="Black",center = (368, 207),fontsize=55)
#randomposbanana
def posbanana():
    banana.x=random.randint(0,736)
    banana.y=random.randint(0,414)
def update():
    global score
    if keyboard.W:
        monkey.y-=6
    if keyboard.S:
        monkey.y+=6
    if keyboard.A:
        monkey.x-=6
    if keyboard.D:
        monkey.x+=6
    #monkeytouchingbanana
    if monkey.colliderect(banana):
        score +=1
        posbanana()
#game over
over = False
def gover():
    global over
    over = True
#scheduling game ovrr function after 60s
clock.schedule(gover, 60.0)
posbanana()
pgzrun.go()
