import resources
import pyglet
from GameObjects import PlayerObject
from MinionObjects import Cowboy, Witch
from pyglet.window import key


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


def spawn():
    monsters = []
    # global monsters_group
    for i in range(1):
        cowboy = Cowboy("Cowboy2.png")
        monsters.append(cowboy)
    return monsters

# cowboy = Cowboy("Cowboy2.png")
# cowboy2 = Cowboy("Cowboy2.png")
# cowboy3 = Cowboy("Cowboy2.png")
# witch1 = Witch(100, 20, "sorcerer villain.png")

monsters = []

@window.event
def on_draw():
    window.clear()
    background_sprite.draw()
    player.sprite.draw()
    new = spawn()
    for i in new:
        monsters.append(i)
    for i in monsters:
        i.draw()

    # cowboy.draw()
    # cowboy2.draw()
    # cowboy3.draw()
    # self.witch1.draw()
    # self.blob_sprite.Sprite(blob_animation, x=400, y=400).draw()


@window.event
def on_text_motion(motion):
    if motion == pyglet.window.key.MOTION_LEFT:
        player.sprite.x -= 10
    if motion == pyglet.window.key.MOTION_RIGHT:
        player.sprite.x += 10
    if motion == pyglet.window.key.MOTION_UP:
        player.sprite.y += 10
    if motion == pyglet.window.key.MOTION_DOWN:
        player.sprite.y -= 10


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
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()
