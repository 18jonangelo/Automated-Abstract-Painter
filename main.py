import turtle as t
import random

turt = t.Turtle()
t.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def turt_movement():
    turt.pensize(10)

    #colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
    movement = [0, 90, 180, 270]
    turt.seth(random.choice(movement))
    turt.speed(0)
    colors = random_colors()
    #turt.color(random.choice(colors))
    turt.color(colors)
    turt.forward(20)


# random.choice(movement_dir)

while True:
    turt_movement()


screen = Screen()
screen.exitonclick()
