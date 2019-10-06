# from objects.positions import Point1D
#
#
# class motion1D(Point1D):
#     """Moving object in 1D."""
#
#     def __init__(self, ):

import time
from math import pi  # , tan, sin
import turtle


def get_rad_list(n):
    return [(2*pi*i-2*pi)/n for i in range(1, n+1)]


def get_rad_step(n):
    return (2*pi)/n


def rad_grad(rad):
    return rad/(2*pi)*360


def grad_rad(grad):
    return grad/360*2*pi


# def motion():
#     radius = 100
#     planet1 = turtle.Turtle()
#     planet1.forward(radius)
#     planet1.left(90)
#     n = 1000
#     for i in range(n):
#         planet1.left(rad_grad(get_rad_step(n)))
#         planet1.forward(2*pi*radius/n)


# def calcer(radius, n):
#     print('r: ', radius)
#     step = 2*pi*radius/n
#     print('step: ', step)


# turtle.done()

# calcer(2, 8)

# motion()
# time.sleep(2)


"""functional programming by example"""


def calc(f, x, y):
    return f(x, y)


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


"""The first movement is in 2D and an approx circle."""


class Motion:
    """A clas that gives objects the fourth dimension."""

    def __init__(self, radius, approx):
        """Initiale the movement."""
        self.object = "PlanetA"
        self.approx = approx
        self.radius = radius
        self.step = 2*pi*self.radius/self.approx

    def make_move(self):
        pass


# first_try = Motion(80, 80)


def make_setup(p, pos, radius, v, n):
    p.speed(v)
    p.pensize(2)
    # p.forward(radius)
    # p.setx(pos[1])
    # p.sety(pos[0])
    p.setpos(pos)
    # p.left(90)
    p.setheading(90)
    p.forward(2*pi*radius/n/2)


def make_move(p, radius, n):
    p.left(rad_grad(get_rad_step(n)))
    p.forward(2*pi*radius/n)


def display_percent(m, n):
    if m/n*100 % 5 == 0:
        print(int(m/n*100), '%')


def make_movement(planets):
    # approx ist die Anzahl der Schritte zur Annäherung des Kreises
    steps = 100_000  # _000
    for i in range(steps):
        display_percent(i, steps)

        for planet in planets:
            # print(i, planet.orbittime)
            if i % planet.orbittime == 0:
                # print('as', 1 % planet.orbittime)
                if planet.planet == 0:
                    print('Moon movement', planet.parent.turt.pos())
                make_move(planet.turt, planet.r, planet.orbittime)
            # p.circle(r)
            # print(p.pos())
            # print(round(p.xcor(), 2))
        # if i == 4:
        #     p.home()


class Planet:  # - adjective center
    def __init__(self, turt, distance2center, orbittime):
        self.planet = 1
        self.turt = turt
        self.r = distance2center
        self.orbittime = orbittime


class Moon(Planet):  # - adjectve adjective center
    def __init__(self, parent, turt, distance2center, ortbittime):  # parent_planet
        self.parent = parent
        Planet.__init__(self, turt, distance2center, ortbittime)
        self.planet = 0


planet1 = Planet(turtle.Turtle(), 228, 687)
earth = Planet(turtle.Turtle(), 150, 365)
planet3 = Planet(turtle.Turtle(), 108, 225)
planet4 = Planet(turtle.Turtle(), 58, 88)

mond = Moon(earth, turtle.Turtle(), 01.385, 27)

planets = [planet1, earth,
           planet3, planet4, mond]

# platur1 = turtle.Turtle()
# platur2 = turtle.Turtle()
# platur3 = turtle.Turtle()
# platur4 = turtle.Turtle()
# platur5 = turtle.Turtle()

# platurs = [platur1, platur2,
#            platur3, platur4, platur5]
position = [(228, 0), (150, 0), (108, 0), (58, 0)]
radius = [228, 150, 108, 58]
# speed = [0, 0.5, 1, 1.5]
speed = [0 for i in range(len(planets))]

approx = 100

make_setup(planet1.turt, position[0], radius[0], speed[0], approx)
make_setup(earth.turt, position[1], radius[1], speed[1], approx)
make_setup(planet3.turt, position[2], radius[2], speed[2], approx)
make_setup(planet4.turt, position[3], radius[3], speed[3], approx)
make_setup(planet4.turt, position[3], mond.r, speed[3], approx)

make_movement(planets)


# tu = turtle.Screen()
# tt = turtle.Turtle()
# tt.color("Navy")
# tu.bgcolor("black")

# ninja = turtle.Turtle()
#
# ninja.speed(10)
#
# for i in range(180):
#     ninja.forward(100)
#     ninja.right(30)
#     ninja.forward(20)
#     ninja.left(60)
#     ninja.forward(50)
#     ninja.right(30)
#
#     # ninja.penup()
#     ninja.setposition(0, 0)
#     ninja.pendown()
#
#     ninja.right(2)
#
# turtle.done()

# make_movement()

time.sleep(0.5)
# n = 1000
# for i in range(n):
#     planet1.left(rad_grad(get_rad_step(n)))
#     planet1.forward(2*pi*radius/n)

# Solar - center etc
# Planet - adjective center
# Moon - adjectve adjective center
