"""."""
# trutle breath
import turtle
import time
# import random
from math import pi, cos, sin

# for i in self.get_rad_list(approx):
#     orbit_points.append(Point2D(cos(i)*self.r[0]+self.x,
#                                 sin(i)*self.r[0]+self.y))


def draw_orbit(orbit_pos, fast=True):
    """Draw the points."""
    # orbit_points = []
    if fast:
        turtle.tracer(0, 0)
    for x, y in orbit_pos:
        orbit = turtle.Turtle()
        orbit.ht()
        orbit.penup()
        # dot = Dot(r, r*i, 'red')
        # dot.goto(orbit)
        orbit.goto(x, y)
        orbit.dot(4, 'red')  # Radius and 'color'
        # orbit_points.append(orbit)

    for i in range(len(orbit_pos)):
        turtle.stamp()

    turtle.update()


def draw_lines(orbit_pos, x, y, factor, i):
    """Draw the lines between the points with a factor of neighbours."""
    # turtle.tracer(0, 0)
    # for i, (x, y) in enumerate(orbit_pos):
    orbit = turtle.Turtle()
    orbit.ht()
    next = i*factor
    while next >= len(orbit_pos):
        print('i', i)
        print('1', next)
        next -= (int(len(orbit_pos)))
        print('2', next)
    orbit.penup()
    orbit.goto(x, y)
    orbit.pendown()
    orbit.fd(0)
    # if (i) < len(orbit_pos)-1:
    # print(orbit.pos())
    orbit.goto(orbit_pos[next])

    # for i in range(len(orbit_pos)):
    #     turtle.stamp()

    # turtle.update()
    # turtle.update()


def draw_lines_insta(orbit_pos, factor):
    """Draw the line instant to see the result."""
    for i, (x, y) in enumerate(orbit_pos):
        draw_lines(orbit_pos, x, y, factor, i)
    turtle.update()


def draw_lines_fast(orbit_pos, factor):
    """Draw the lines instant line by line."""
    for i, (x, y) in enumerate(orbit_pos):
        draw_lines(orbit_pos, x, y, factor, i)
        turtle.update()


def draw_lines_slow(orbit_pos, factor):
    """Draw the lines so ypu can watch it."""


def get_orbit_points(n=10, r=400):
    """Get the aproximated orbit points for n points on a radius r."""
    orbit_pos = []
    for index, j in enumerate([(2*pi*i-2*pi)/n for i in range(1, n+1)]):
        orbit_pos.append((cos(j)*r, sin(j)*r))
    return orbit_pos


def main_loop(n):
    for i in range(1, 6):
        main(i, n)


def main(factor, n):
    """Run main."""
    win = turtle.Screen()
    pos = get_orbit_points(n)
    draw_orbit(pos)
    draw_lines_fast(pos, factor)
    time.sleep(3)
    win.clear()


def main2(factor, n):
    """Test the slow draw lines."""
    pos = get_orbit_points(n)
    draw_orbit(pos, fast=True)
    draw_lines_insta(pos, factor)


def draw_lines_slow(orbit_pos, factor):
    """Draw the lines so ypu can watch it."""

    for i, (x, y) in enumerate(orbit_pos):
        t = turtle.Turtle()
        # t.ht()
        next = i*factor
        while next >= len(orbit_pos):
            next -= (int(len(orbit_pos)))

        print(next)
        t.pd()
        t.goto(0, 0)
        t.left(90)
        t.fd(200)
        t.fd(200)

    # t.penup()
    # t.goto(x, y)
    # t.pendown()
    # t.fd(0)
    # # if (i) < len(orbit_pos)-1:
    # # print(t.pos())
    # t.goto(orbit_pos[next])


if __name__ == "__main__":
    """Run if called as main."""
    print('factor < n')
    main2(91, 800)
    time.sleep(3)


# senior data -
