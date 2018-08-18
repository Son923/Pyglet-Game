import resources
import pyglet
from GameObjects import PlayerObject
from MinionObjects import Cowboy, Witch
from pyglet.window import key
import Time


window = pyglet.window.Window(width=1200, height=900, caption="Space Invaders", resizable=False)
window.set_location(400, 100)
frame_rate = 1/16

# Make background
global background_sprite
background = pyglet.resource.image('battleback4.png')
background.width = 1200
background.height = 900
background_sprite = pyglet.sprite.Sprite(img=background, x=0, y=0)


player = PlayerObject(600, 0, "Cowboy2_idle with gun_0.png")

global monster_position
monster_position = []
monsters = []
number = 2

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        if timer.running:
            timer.running = False
        else:
            if timer.time > 0:
                timer.reset()
            else:
                timer.running = True
    elif symbol == pyglet.window.key.ESCAPE:
        window.close()

def spawn(dt):
    # global monsters_group
    global number
    for i in range(number):
        cowboy = Cowboy("Cowboy2.png")
        monsters.append(cowboy)
    number += 1

# cowboy = Cowboy("Cowboy2.png")
# cowboy2 = Cowboy("Cowboy2.png")global time
# cowboy3 = Cowboy("Cowboy2.png")
# witch1 = Witch(100, 20, "sorcerer villain.png")


@window.event
def on_draw():
    window.clear()
    background_sprite.draw()
    player.sprite.draw()
    for enemy in monsters:
        enemy.draw()
    timer.label.draw()
    # cowboy.draw()
    # cowboy2.draw()
    # cowboy3.draw()
    # self.witch1.draw()
    # self.blob_sprite.Sprite(blob_animation, x=400, y=400).draw()



@window.event
def on_text_motion(motion):
    if motion == pyglet.window.key.MOTION_LEFT:
        player.sprite.x -= 20
    if motion == pyglet.window.key.MOTION_RIGHT:
        player.sprite.x += 20
    if motion == pyglet.window.key.MOTION_UP:
        player.sprite.y += 20
    if motion == pyglet.window.key.MOTION_DOWN:
        player.sprite.y -= 20


def update(dt):
    player.update(dt)
    pos = player.update(dt)
    for cowboy in monsters:
        cowboy.update(dt, pos)
    # cowboy2.update(dt, pos)
    # cowboy3.update(dt, pos)
    # witch1.update(dt, pos)
    on_draw()

if __name__ == "__main__":
    timer = Timer()
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.clock.schedule_interval(spawn, 5)
    pyglet.clock.schedule_interval(timer.update, 1.0)
    pyglet.app.run()
