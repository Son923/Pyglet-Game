import pyglet
import random
import resources


window = pyglet.window.Window(1200, 900)
label = pyglet.text.Label("0", font_size=36, y=300, x=400)

def make_background():
    # Make background
    global background_sprite
    background = pyglet.resource.image('battleback4.png')
    background.width = 1200
    background.height = 900
    background_sprite = pyglet.sprite.Sprite(img=background, x=0, y=0)

make_background()

@window.event
def on_draw():
    window.clear()
    background_sprite.draw()
    monsters = group_monsters(50)
    for monster in monsters:
        monster.draw()

def group_monsters(num_monsters):
    # Make monsteres
    monsters = []
    for i in range(num_monsters):
        monster_x = random.randint(0, 1200)
        monster_y = random.randint(450, 900)
        # Make one monster
        monster = pyglet.resource.image('pipo-enemy007.png')
        monster.width = 200
        monster.height = 200
        new_monster = pyglet.sprite.Sprite(img=monster,
                                            x=monster_x, y=monster_y)
        # Reset the coordinates of a monster is the center of it
        new_monster.image.anchor_x = monster.width / 2
        new_monster.image.anchor_y = monster.height / 2
        new_monster.rotation = 0
        monsters.append(new_monster)
    return monsters


# pyglet.clock.schedule(game_loop)
pyglet.app.run()
