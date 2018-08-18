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

class Timer:
    def __init__(self):
        self.label = pyglet.text.Label('00:00', font_size=30, x=1070, y=850)
        self.reset()

    def reset(self):
        self.time = 0
        self.running = True
        self.label.text = '00:00'
        self.label.color = (255, 255, 255, 255)

    def update(self, dt):
        if self.running:
            self.time += dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            if m >= 5:
                self.label.color = (180, 0, 0, 255)
        else:
            self.label = pyglet.text.Label(self.label.text, font_size=300,
                                           x=window.width // 2,
                                           y=window.height // 2,
                                           anchor_x='center', anchor_y='center')



@window.event
def on_draw():
    window.clear()
    background_sprite.draw()


    new_monster = group_monsters(10)
    for monster in new_monster:
        monsters_group.append(monster)
    # monsters_group = (group_monsters(2))
    # print(monsters_group)
    for monster in monsters_group:
        monster.draw()
    # Draw the clock
    if len(monsters_group) == 100:
        timer.running = False
    timer.label.draw()

def group_monsters(num_monsters):
    # Make monsteres
    monsters = []
    # global monsters_group
    global monster_position
    monster_position = []
    for i in range(num_monsters):
        monster_x = random.randint(0, 1200)
        monster_y = random.randint(0, 900)
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
    timer = Timer()
    pyglet.clock.schedule_interval(update, 1.0)
    pyglet.clock.schedule_interval(timer.update, 1.0)
    pyglet.app.run()
