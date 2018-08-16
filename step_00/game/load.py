import pyglet
import resources
import random


def asteroids(num_asteroids):
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x = random.randint(0, 800)
        asteroid_y = random.randint(0, 600)
        image = pyglet.resource.image("Flappybirdlogo.jpg")
        sprite = pyglet.sprite.Sprite(img=image, x=asteroid_x, y=asteroid_y)
        image.rotation = random.randint(0, 360)
        asteroids.append(image)
    return asteroids
