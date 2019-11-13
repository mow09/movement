"""."""
# trutle breath
import turtle
import time
import random
from math import pi, cos, sin

# for i in self.get_rad_list(approx):
#     orbit_points.append(Point2D(cos(i)*self.r[0]+self.x,
#                                 sin(i)*self.r[0]+self.y))


def draw_orbit(n=10, r=200):
    orbit_points = []
    turtle.tracer(0, 0)
    for j in [(2*pi*i-2*pi)/n for i in range(1, n+1)]:
        print(j)
        orbit = turtle.Turtle()
        orbit.penup()
        # dot = Dot(r, r*i, 'red')
        # dot.goto(orbit)
        orbit.goto(cos(j)*r, sin(j)*r)
        orbit.dot(10, 'red')  # Radius and 'color'
        orbit_points.append(orbit)

    for i in range(n):
        turtle.stamp()

    turtle.update()


def main():
    """Run main."""
    t = turtle.Turtle()
    draw_orbit()


if __name__ == "__main__":
    """Run if called as main."""
    main()
    time.sleep(3)
