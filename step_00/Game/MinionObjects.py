import resources
import pyglet
from random import randint

class Cowboy:
    def __init__(self, image=None):
        self.posx = randint(0, 1200)
        self.posy = randint(450, 950)
        self.velx = 0
        self.vely = 0
        if image is not None:
            cowboy = pyglet.resource.image(image)
            cowboy_seq = pyglet.image.ImageGrid(cowboy, 4 ,8 ,item_width = 45, item_height = 45)
            cowboy_animation = pyglet.image.Animation.from_image_sequence(cowboy_seq[10:20], 0.1, loop=True)
            self.cowboy_sprite = pyglet.sprite.Sprite(cowboy_animation, x=self.posx, y=self.posy)


    def draw(self):
        self.cowboy_sprite.draw()


    def update(self, dt, pos):
        print(pos)
        if self.cowboy_sprite.x <= pos[0] and self.cowboy_sprite.y < pos[1]:
            self.cowboy_sprite.x += 50*dt
            self.cowboy_sprite.y += 50*dt
        elif self.cowboy_sprite.x <= pos[0] and self.cowboy_sprite.y > pos[1]:
            self.cowboy_sprite.x += 50*dt
            self.cowboy_sprite.y -= 50*dt
        elif self.cowboy_sprite.x >= pos[0] and self.cowboy_sprite.y > pos[1]:
            self.cowboy_sprite.x -= 50*dt
            self.cowboy_sprite.y -= 50*dt
        else:
            self.cowboy_sprite.x -= 50*dt
            self.cowboy_sprite.y += 50*dt


class Witch(object):
    def __init__(self, posx, posy, image=None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            witch = pyglet.resource.image(image)
            witch_seq = pyglet.image.ImageGrid(witch, 1 ,10 ,item_width = 200, item_height = 200)
            witch_animation = pyglet.image.Animation.from_image_sequence(witch_seq[0:3], 0.1, loop=True)
            self.witch_sprite = pyglet.sprite.Sprite(witch_animation, x=self.posx, y=self.posy)


    def draw(self):
        self.witch_sprite.draw()

    def update(self, dt, pos):
        print(pos)
        if self.witch_sprite.x <= pos[0] and self.witch_sprite.y < pos[1]:
            self.witch_sprite.x += 100*dt
            self.witch_sprite.y += 100*dt
        elif self.witch_sprite.x <= pos[0] and self.witch_sprite.y > pos[1]:
            self.witch_sprite.x += 100*dt
            self.witch_sprite.y -= 100*dt
        elif self.witch_sprite.x >= pos[0] and self.witch_sprite.y > pos[1]:
            self.witch_sprite.x -= 100*dt
            self.witch_sprite.y -= 100*dt
        else:
            self.witch_sprite.x -= 100*dt
            self.witch_sprite.y += 100*dt


class Plant(object):
    def __init__(self, posx, posy, image=None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            plant = pyglet.image.load("/tmp/guest-mo1w68/nson/son/res/sprites/" + image)
            plant_seq = pyglet.image.ImageGrid(plant, 1 ,10 ,item_width = 200, item_height = 200)
            plant_animation = pyglet.image.Animation.from_image_sequence(plant_seq[0:3], 0.1, loop=True)
            self.plant_sprite = pyglet.sprite.Sprite(plant_animation, x=self.posx, y=self.posy)


    def draw(self):
        self.plant_sprite.draw()

    def update(self, dt, pos):
        print(pos)
        if self.plant_sprite.x <= pos[0] and self.plant_sprite.y < pos[1]:
            self.plant_sprite.x += 100*dt
            self.plant_sprite.y += 100*dt
        elif self.plant_sprite.x <= pos[0] and self.plant_sprite.y > pos[1]:
            self.plant_sprite.x += 100*dt
            self.plant_sprite.y -= 100*dt
        elif self.plant_sprite.x >= pos[0] and self.plant_sprite.y > pos[1]:
            self.plant_sprite.x -= 100*dt
            self.plant_sprite.y -= 100*dt
        else:
            self.plant_sprite.x -= 100*dt
            self.plant_sprite.y += 100*dt
