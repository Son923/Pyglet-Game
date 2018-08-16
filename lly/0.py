import pyglet
# import config
# from system.component import Component
# from entities.ball import Ball
# from random import randint


# Global variables
# window = pyglet.window.Window(height=config.window_height, width=config.window_width)
window = pyglet.window.Window(1104, 621)
label = pyglet.text.Label("0", font_size=36, y=300, x=400)
image = pyglet.image.load('battleback4.png')
background = pyglet.sprite.Sprite(img=image, y=0, x=0)
# image = pyglet.image.load('Turnon_button.png')
# button = pyglet.sprite.Sprite(img=image, y=300, x=400)

# Event callbacks
@window.event
def on_draw():
    window.clear()

    background.draw()
    label.draw()
    # button.draw()

# Game loop (loop? Why loop?)
def game_loop(_):
    label.text = str(int(label.text) + 1)

# this function runs only once, it loads two background images at the start
# def preload():
#     global preloaded
#     for i in range(2):
#         bg_list.append(pyglet.sprite.Sprite(space, x=0, y=i*1200))
#     preloaded = True
#
# def bg_move(dt):
#     for bg in bg_list:
#         bg.y -= 50*dt
#         if bg.y <= -1300:
#             bg_list.remove(bg)
#             bg_list.append(pyglet.sprite.Sprite(space, x=0, y=1100))

###############3

pyglet.clock.schedule(game_loop)
pyglet.app.run()
