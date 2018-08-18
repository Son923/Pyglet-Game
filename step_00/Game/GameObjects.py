import resources
import pyglet
from random import randint

class PlayerObject:
    pos = []
    def __init__(self, posx, posy, image=None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            image = pyglet.resource.image(image)
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)


    def draw(self):
        self.sprite.draw()


    def update(self, dt):
        pos=[0,0]
        pos[0] = self.sprite.x
        pos[1] = self.sprite.y
        return pos
