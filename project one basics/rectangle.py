import pgzrun
import random
WIDTH = 300
HEIGHT = 300
def draw():
    col = 255
    col2 = random.randint(0, 255)
    col3 = 120
    w = 300
    h = 100
    screen.fill("black")
    for i in range(30):        
      r = Rect((0, 0), (w, h))
      r.center = 150, 150
      screen.draw.rect(r, (col, col2, col3))
      col-=5
      #col3-=5
      w-=5
      h+=5

pgzrun.go()
