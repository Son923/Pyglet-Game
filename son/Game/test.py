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


player = PlayerObject(800, 800, "Cowboy2_idle with gun_0.png")

monsters = []
# global monsters_group
global monster_position
monster_position = []
for i in range(1000):
    cowboy = Cowboy("Cowboy2.png")
    monsters.append(cowboy)

# cowboy = Cowboy("Cowboy2.png")
# cowboy2 = Cowboy("Cowboy2.png")
# cowboy3 = Cowboy("Cowboy2.png")
# witch1 = Witch(100, 20, "sorcerer villain.png")

@window.event
def on_draw():
    window.clear()
    background_sprite.draw()

    player.sprite.draw()

    for i in monsters:
        i.draw()

    # cowboy.draw()
    # cowboy2.draw()
    # cowboy3.draw()
    # self.witch1.draw()
    # self.blob_sprite.Sprite(blob_animation, x=400, y=400).draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        player.sprite.x += 30
    elif symbol == key.LEFT:
        player.sprite.x += -30
    elif symbol == key.UP:
        player.sprite.y += 30
    elif symbol == key.DOWN:
        player.sprite.y += -30


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
