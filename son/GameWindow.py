import pyglet
from GameObjects import PlayerObject
from MinionObjects import CowboyObject


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400, 100)
        self.frame_rate = 1/16

        # blob = pyglet.image.load("/tmp/guest-gizzpk/nson/son/res/sprites/Cowboy2.png")
        # blob_seq = pyglet.image.ImageGrid(blob, 4 ,8 ,item_width = 45, item_height = 45)
        # blob_seq.width = 100
        # blob_texture = pyglet.image.TextureGrid(blob_seq)
        # blob_animation = pyglet.image.Animation.from_image_sequence(blob_texture[10:20], 0.1, loop=True)
        #
        # self.blob_sprite = pyglet.sprite.Sprite(blob_animation, x=400, y=400)
        self.player = PlayerObject(800, 800, "Cowboy2_idle with gun_0.png")
        self.cowboy = CowboyObject(10, 30, "Cowboy2_idle with gun_0.png")
        self.cowboy2 = CowboyObject(10, 450, "Cowboy2_idle with gun_0.png")
        self.cowboy3 = CowboyObject(30, 650, "Cowboy2_idle with gun_0.png")
    def on_draw(self):
        self.clear()
        self.player.sprite.draw()

        self.cowboy.sprite.draw()
        self.cowboy2.sprite.draw()
        self.cowboy3.sprite.draw()
        # self.blob_sprite.Sprite(blob_animation, x=400, y=400).draw()

    def update(self, dt):
        self.player.update(dt)

        self.cowboy.update(dt)
        self.cowboy2.update(dt)
        self.cowboy3.update(dt)


if __name__ == "__main__":
    window = GameWindow(1200, 900, "Shooting", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()