import pyglet
import resources
import random
import load
from pyglet.window import mouse


mouse_pos = 0, 0
window = pyglet.window.Window(800, 600)
# window.push_handlers(pyglet.window.event.WindowEventLogger())
label = pyglet.text.Label("0", font_size=200, y=300, x=40)
gun = pyglet.resource.image("Limra-Morning-Walking-Stick-SDL023968542-1-b9b19.jpg")
bird0 = pyglet.resource.image("Flappybirdlogo.jpg")
gun.height = 400
gun.width = 400
bird0.height = 200
bird0.width = 200
gun = pyglet.sprite.Sprite(img=gun, x=200, y=0)
bird0 = pyglet.sprite.Sprite(img=bird0, x=350, y=300)
gun.anchor_x =
gun.anchor_y =
# bird0.image.anchor_x = bird0.width / 2
# bird0.image.anchor_y = bird0.height / 2


# Event callbacks
@window.event
def on_draw():
    window.clear()
    # label.draw()
    gun.draw()
    # bird0.draw()

@window.event
def on_mouse_press(x, y, button, modifier):
    if button == mouse.LEFT:
        if range_x()

def calculate_x(position_x, width):
    range_x = position_x - width / 2
    return range_x

def range_x(position_x, width, x):
    range_x = calculate_x(position_x, width)
    if x in range(range_x, range_x + width):
        return True
    else:
        return False




def game_loop(_):
    label.text = str(int(label.text) - 1)



# asteroids = load.asteroids(5)
pyglet.clock.schedule(game_loop)
pyglet.app.run()
