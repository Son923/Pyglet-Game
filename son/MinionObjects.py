import pyglet
from random import randint

class CowboyObject:
    def __init__(self, posx, posy, image=None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            image = pyglet.image.load('/tmp/guest-ze4hfy/nson/son/res/sprites/' + image)
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)


    def draw(self):
        self.sprite.draw()


    def update(self, dt, pos):
        print(pos)
        if self.sprite.x <= pos[0] and self.sprite.y < pos[1]:
            self.sprite.x += 50*dt
            self.sprite.y += 50*dt
        elif self.sprite.x <= pos[0] and self.sprite.y > pos[1]:
            self.sprite.x += 50*dt
            self.sprite.y -= 50*dt
        elif self.sprite.x >= pos[0] and self.sprite.y > pos[1]:
            self.sprite.x -= 50*dt
            self.sprite.y -= 50*dt
        else:
            self.sprite.x -= 50*dt
            self.sprite.y += 50*dt
