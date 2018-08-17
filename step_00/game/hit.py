import pyglet

def hit(x, y, position_x, position_y):
    target_width = 200
    target_height = 200
    if range_x(position_x, target_width, x) is True and range_y(position_y, target_height, y) is True:
        return True
    else:
        return False

def range_x(position_x, width, x):
    if position_x - (width / 2) <= x <= position_x + (width / 2):
        return True
    else:
        return False


def range_y(position_y, height, y):
    if position_y - (height / 2) <= y <= position_y + (height / 2):
        return True
    else:
        return False
