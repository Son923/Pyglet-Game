import resources
import pyglet
from GameObjects import PlayerObject
from MinionObjects import Cowboy, Witch
from pyglet.window import key
from Time import Timer
from shoot import hit
from pyglet.window import mouse


window = pyglet.window.Window(width=1200, height=900, caption="Space Invaders", resizable=False)
window.set_location(400, 100)
frame_rate = 1/16

cursor = pyglet.resource.image("oie_transparent.png")
cursor_sprite = pyglet.sprite.Sprite(img=cursor)
@window.event
def on_mouse_motion(x, y, dx, dy):
    window.set_mouse_visible(False)
    window.clear()
    cursor_sprite.x = x
    cursor_sprite.y = y


# Make background
global background_sprite
background = pyglet.resource.image('battleback1.png')
background.width = 1200
background.height = 900
background_sprite = pyglet.sprite.Sprite(img=background, x=0, y=0)

# Create player
player = PlayerObject(600, 0, "Cowboy2_idle with gun_0.png")

# Game settings
character_speed = 5.0
spawn_speed = 4  # seconds

global monster_position
monster_position = []
cowboys = []
number = 2
monsterBatch = pyglet.graphics.Batch()
pressing_keys=[]

def spawn(dt):
    # global monsters_group
    global number
    for i in range(number):
        cowboy = Cowboy(monsterBatch, "Cowboy2.png")
        cowboys.append(cowboy)
    number += 1

def moveCharacter(dt):
    if pyglet.window.key.LEFT in pressing_keys:
        player.move(-character_speed, 0)
    if pyglet.window.key.RIGHT in pressing_keys:
        player.move(character_speed, 0)
    if pyglet.window.key.UP in pressing_keys:
        player.move(0, character_speed)
    if pyglet.window.key.DOWN in pressing_keys:
        player.move(0, -character_speed)


@window.event
def on_draw():
    window.clear()
    background_sprite.draw()
    player.sprite.draw()
    for cowboy in cowboys:
        cowboy.draw()
    timer.label.draw()
    cursor_sprite.draw()


@window.event
def on_mouse_press(x, y, button, modifier):
    for cowboy in cowboys:
        if button == mouse.LEFT:
            if hit(x, y, cowboy.cowboy_sprite.x, cowboy.cowboy_sprite.y) is True:
                cowboys.remove(cowboy)
                break


@window.event
def on_key_press(symbol, modifiers):
    pressing_keys.append(symbol)

@window.event
def on_key_release(symbol, modifiers):
    pressing_keys.remove(symbol)

nhac_nen = pyglet.media.load("/tmp/guest-t3sj3t/nson/step_00/resources/nhacnen.wav")
nhac_nen.play()

def update(dt):
    player.update(dt)
    pos = player.update(dt)
    for cowboy in cowboys:
        # if cowboy.cowboy_sprite.x == player.sprite.x and cowboy.cowboy_sprite.y == player.sprite.y:
        cowboy.update(dt, pos)

    on_draw()

if __name__ == "__main__":
    timer = Timer()
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.clock.schedule_interval(spawn, spawn_speed)
    pyglet.clock.schedule_interval(moveCharacter, 1.0/60)
    pyglet.clock.schedule_interval(timer.update, 1.0)
    pyglet.app.run()
