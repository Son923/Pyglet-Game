import pyglet
import resources
import random
from shoot import hit
from pyglet.window import mouse

batch = pyglet.graphics.Batch()
window = pyglet.window.Window(800, 600)
# window.push_handlers(pyglet.window.event.WindowEventLogger())
label = pyglet.text.Label("0", x=0, y=0)
gun = pyglet.resource.image("battleback4.png")
bird0 = pyglet.resource.image("plant1.png")
gun.height = 400
gun.width = 400
bird0.height = 200
bird0.width = 200
gun = pyglet.sprite.Sprite(gun, x=400, y=0)
bird3 = pyglet.sprite.Sprite(img = bird0, x=700, y=300, batch=batch)
bird1 = pyglet.sprite.Sprite(img = bird0, x=100, y=300, batch=batch)
bird2 = pyglet.sprite.Sprite(img = bird0, x=400, y=300, batch=batch)
gun.image.anchor_x = gun.width / 2
gun.image.anchor_y = gun.height / 2
bird1.image.anchor_x = bird1.width / 2
bird1.image.anchor_y = bird1.height / 2
bird2.image.anchor_x = bird2.width / 2
bird2.image.anchor_y = bird2.height / 2
bird3.image.anchor_x = bird3.width / 2
bird3.image.anchor_y = bird3.height / 2
gun.rotation = 0
bird3.rotation = 0
bird1.rotation = 0
bird2.rotation = 0


sprites = []
sprites.append(bird1)
sprites.append(bird2)
sprites.append(bird3)
# Event callbacks
@window.event
def on_draw():
    window.clear()
    # label.draw()
    gun.draw()
    for a in sprites:
        a.draw()


@window.event
def on_mouse_press(x, y, button, modifier):
    for cay in sprites:
        if button == mouse.LEFT:
            if hit(x, y, cay.x, cay.y) is True:
                sprites.remove(cay)
                break


def game_loop(_):
    label.text = str(int(label.text) - 1)


# asteroids = load.asteroids(5)
pyglet.clock.schedule(game_loop)
pyglet.app.run()
