import pyglet
import resources

# import config
# from system.component import Component
# from entities.ball import Ball
# from random import randint


# Global variables
# window = pyglet.window.Window(height=config.window_height, width=config.window_width)
window = pyglet.window.Window(1200, 900)
label = pyglet.text.Label("0", font_size=36, y=300, x=400)
background = pyglet.resource.image('battleback4.png')
background.width = 1200
background.height = 900
background_sprite = pyglet.sprite.Sprite(img=background, x=0, y=0)

# image = pyglet.image.load('Turnon_button.png')
# button = pyglet.sprite.Sprite(img=image, y=300, x=400)

# Event callbacks
@window.event
def on_draw():
    window.clear()

    background_sprite.draw()
    label.draw()
    # button.draw()

# Game loop (loop? Why loop?)
def game_loop(_):
    label.text = str(int(label.text) + 1)


pyglet.clock.schedule(game_loop)
pyglet.app.run()
