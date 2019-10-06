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

def positioning(center):
    print(center)


def make_setup(objects, setup):  # p, pos, radius, v, n):
    for i, o in enumerate(objects):
        o.turt.color(o.color)
        if o.planet == 0:
            o.turt.penup()
            o.turt.goto(o.parent.turt.pos() + (o.r, 0))
            o.turt.speed(0)
            o.turt.pensize(2)
            o.parent_pos = o.parent.turt.pos()
            o.turt.pendown()
        else:
            o.turt.speed(0)
            o.turt.pensize(1)
        # p.forward(radius)
        # p.setx(pos[1])
        # p.sety(pos[0])
            o.turt.goto(center)
            o.turt.lt(setup[i])
            o.turt.fd(o.r)
            # o.turt.setpos((o.r, 0))
        # p.left(90)
        # o.turt.setheading(90)
        # o.turt.seth(90)
        o.turt.lt(90)
        o.turt.forward(2*pi*o.r/o.orbittime/2)


def make_move(p, radius, n):
    p.left(rad_grad(get_rad_step(n)))
    p.forward(2*pi*radius/n)


def display_percent(m, n):
    if m/n*100 % 5 == 0:
        print(int(m/n*100), '%')


def make_movement(planets, steps):
    # approx ist die Anzahl der Schritte zur Annäherung des Kreises
    # steps = 30_000  # _000
    for i in range(steps):
        display_percent(i, steps)

        for planet in planets:
            # print(i, planet.orbittime)
            if i % planet.orbittime == 0:
                # print('as', 1 % planet.orbittime)
                if planet.planet == 0:
                    # print('Moon movement', planet.parent.turt.pos())
                    # planet.turt.goto(planet.parent.turt.pos() + (planet.r, 0))
                    # print(planet.parent_pos, planet.parent.turt.pos())
                    if planet.parent_pos != planet.parent.turt.pos():
                        # print(planet.center())
                        print('here', planet.get_center(), planet.parent.turt.pos())
                        planet.turt.setpos((planet.turt.pos() +
                                            planet.parent.turt.pos() - planet.parent_pos))
                        planet.parent_pos = planet.parent.turt.pos()
                make_move(planet.turt, planet.r, planet.orbittime)
            # p.circle(r)
            # print(p.pos())
            # print(round(p.xcor(), 2))
        # if i == 4:
        #     p.home()


class Planet:  # - adjective center
    def __init__(self, turt, color, center, distance2center, orbittime):
        self.planet = True
        self.turt = turt
        self.color = color
        # self.pos = pos
        self.center = center
        self.r = distance2center
        self.orbittime = orbittime


class Moon(Planet):  # - adjectve adjective center
    def __init__(self, parent, turt, color, distance2center, ortbittime):
        self.parent = parent
        Planet.__init__(self, turt, color, center, distance2center, ortbittime)
        self.planet = False
        self.parent_pos = (0, 0)
        # self.center = self.get_center()

    def get_center(self):
        return self.parent.turt.pos()

        # self.orbittime = orbittime


# position = [(228, 0), (150, 0), (108, 100), (58, 100)]
radius = [228, 150, 108, 58]
orbittime = [687, 365, 225, 88]
color = ['black', 'black', 'black', 'black', ]

center = (30, 10)

planet1 = Planet(turtle.Turtle(), color[0], center, radius[0], orbittime[0])
earth = Planet(turtle.Turtle(), color[1], center, radius[1], orbittime[1])
planet3 = Planet(turtle.Turtle(), color[2], center, radius[2], orbittime[2])
planet4 = Planet(turtle.Turtle(), color[3], center, radius[3], orbittime[3])

# mond = Moon(parent=earth, turt=turtle.Turtle(), color='blue',
#             distance2center=0.385, orbittime=27)
mond = Moon(earth, turtle.Turtle(), 'blue', 0.385, 27)

planets = [planet1, earth,
           planet3, planet4, mond]

# speed = [0, 0.5, 1, 1.5]
speed = [0 for i in range(len(planets))]

approx = 10
steps = 300_000

# is a list of fix angles - should be a setup by TIME
set_up = [45, 90, 135, 186]

make_setup(planets, set_up)

make_movement(planets, steps)

positioning((0, 0))

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


time.sleep(0.5)
# n = 1000
# for i in range(n):
#     planet1.left(rad_grad(get_rad_step(n)))
#     planet1.forward(2*pi*radius/n)

# Solar - center etc
# Planet - adjective center
# Moon - adjectve adjective center
