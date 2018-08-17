import pyglet
import resources
import random
from shoot import hit
from pyglet.window import mouse


window = pyglet.window.Window(800, 600)
# window.push_handlers(pyglet.window.event.WindowEventLogger())
label = pyglet.text.Label("0", x=0, y=0)
gun = pyglet.resource.image("Limra-Morning-Walking-Stick-SDL023968542-1-b9b19.jpg")
bird0 = pyglet.resource.image("Flappybirdlogo.jpg")
# bird1 = pyglet.resource.image("Flappybirdlogo.jpg")
bird2 = pyglet.resource.image("Flappybirdlogo.jpg")
gun.height = 400
gun.width = 400
bird0.height = 200
bird0.width = 200
img = bird0
gun = pyglet.sprite.Sprite(gun, x=400, y=0)
bird0_sprite = pyglet.sprite.Sprite(img, x=100, y=300)
bird1 = pyglet.sprite.Sprite(img, x=400, y=300)
bird2 = pyglet.sprite.Sprite(img, x=700, y=300)
gun.image.anchor_x = gun.width / 2
gun.image.anchor_y = gun.height / 2
bird0_sprite.image.anchor_x = bird0.width / 2
bird0_sprite.image.anchor_y = bird0.height / 2
bird1.image.anchor_x = bird1.width / 2
bird1.image.anchor_y = bird1.height / 2
bird2.image.anchor_x = bird2.width / 2
bird2.image.anchor_y = bird2.height / 2
gun.rotation = 0
bird0_sprite.rotation = 0
bird1.rotation = 0
bird2.rotation = 0


# Event callbacks
@window.event
def on_draw():
    window.clear()
    # label.draw()
    gun.draw()
    bird0_sprite.draw()
    bird0_sprite.delete()
    bird1.draw()
    bird2.draw()


@window.event
def on_mouse_motion(x, y, dx, dy):
    mouse_pos = x, y


@window.event
def on_mouse_press(x, y, button, modifier):
    hit_bird = []
    if button == mouse.LEFT:
        bird_flock = [[100, 300], [400, 300], [700, 300]]
        for chim in range(len(bird_flock)):
            if hit(x, y, 100, 300) is True:
                bird0_sprite.delete()
            else:
                return False


def game_loop(_):
    label.text = str(int(label.text) - 1)


# asteroids = load.asteroids(5)
pyglet.clock.schedule(game_loop)
pyglet.app.run()
