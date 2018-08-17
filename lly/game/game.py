import pyglet
import random
import resources
monsters_group = []

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
    new_monster = group_monsters(100)
    for monster in new_monster:
        monsters_group.append(monster)
    # monsters_group = (group_monsters(2))
    print(monsters_group)
    for monster in monsters_group:
        monster.draw()
# def begin_value():


def group_monsters(num_monsters):
    # Make monsteres
    monsters = []
    # global monsters_group
    global monster_position
    monster_position = []
    for i in range(num_monsters):
        monster_x = random.randint(0, 1200)
        monster_y = random.randint(450, 900)
        monster_position.append([monster_x, monster_y])
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

def update(dt):
    on_draw()
# pyglet.app.run()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0)
    pyglet.app.run()
