"""."""
# trutle breath
import turtle
import time
import random
from math import pi, cos, sin

# for i in self.get_rad_list(approx):
#     orbit_points.append(Point2D(cos(i)*self.r[0]+self.x,
#                                 sin(i)*self.r[0]+self.y))


def draw_orbit(orbit_pos):
    """Draw the points."""
    # orbit_points = []
    turtle.tracer(0, 0)
    for x, y in orbit_pos:
        orbit = turtle.Turtle()
        orbit.ht()
        orbit.penup()
        # dot = Dot(r, r*i, 'red')
        # dot.goto(orbit)
        orbit.goto(x,y)
        orbit.dot(4, 'red')  # Radius and 'color'
        # orbit_points.append(orbit)

    for i in range(len(orbit_pos)):
        turtle.stamp()

    turtle.update()


def draw_lines(orbit_pos, factor):
    """Draw the lines between the points with a factor of neighbours."""
    turtle.tracer(0, 0)
    for i, (x, y) in enumerate(orbit_pos):
        orbit = turtle.Turtle()
        orbit.ht()
        next = i*factor
        while next >= len(orbit_pos):
            print('i', i)
            print('1', next)
            next -= (int(len(orbit_pos)))
            print('2', next)
        orbit.penup()
        orbit.goto(x,y)
        orbit.pendown()
        # if (i) < len(orbit_pos)-1:
        orbit.goto(orbit_pos[next])

    for i in range(len(orbit_pos)):
        turtle.stamp()

    turtle.update()


def get_orbit_points(n=10, r=400):
    """Get the aproximated orbit points for n points on a radius r."""
    orbit_pos = []
    for index, j in enumerate([(2*pi*i-2*pi)/n for i in range(1, n+1)]):
        orbit_pos.append((cos(j)*r, sin(j)*r))
    return orbit_pos

def main_loop(n):
    for i in range(1,6):
        main(i,n)

def main(factor,n):
    """Run main."""
    win = turtle.Screen()
    t = turtle.Turtle()
    pos = get_orbit_points(n)
    draw_orbit(pos)
    draw_lines(pos, factor)
    time.sleep(3)
    win.clear()

if __name__ == "__main__":
    """Run if called as main."""
    main(76,550)
