import pgzrun
import random
WIDTH=736
HEIGHT=414
monkey = Actor('monkey.png')
banana = Actor('banana.png')
def draw():
    #bgimage
    screen.blit("house.jpg",(0,0))
    monkey.draw()
    banana.draw()
#randomposbanana
def posbanana():
    banana.x=random.randint(0,736)
    banana.y=random.randint(0,414)
def update():
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
        posbanana()
posbanana()
pgzrun.go()