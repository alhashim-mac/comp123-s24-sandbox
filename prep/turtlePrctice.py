"""
Demo for the use of the turtle module

Source
- https://docs.python.org/3/library/turtle.html
"""

import turtle
from random import random

s = turtle.Screen()
s.title("Random Moves")

t = turtle.Turtle()
t.speed("fastest")
# see other speeds https://docs.python.org/3/library/turtle.html#turtle.speed

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

# keep screen till it get closed
s.mainloop()

# keep screen till it is clicked
# s.exitonclick()
