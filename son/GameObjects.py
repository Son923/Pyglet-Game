import pyglet

class GameObject:
    def __init__(self, posx, posy, image=None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            image = pyglet.image.load('/tmp/guest-gizzpk/nson/son/res/sprites/' + image)
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)


    def draw(self):
        self.sprite.draw()


    def update(self, dt):
        self.sprite.x += 100*dt
        self.sprite.y += 90*dt
