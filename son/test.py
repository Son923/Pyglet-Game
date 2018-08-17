import pyglet
from GameObjects import PlayerObject
from MinionObjects import CowboyObject


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400, 100)
        self.frame_rate = 1/16

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
        pos = self.player.update(dt)

        self.cowboy.update(dt, pos)
        self.cowboy2.update(dt, pos)
        self.cowboy3.update(dt, pos)


if __name__ == "__main__":
    window = GameWindow(1200, 900, "Shooting", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
