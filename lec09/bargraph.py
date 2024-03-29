"""
Source
How to Think Like a Computer Scientist: Interactive Edition,
https://runestone.academy/ns/books/published/MAC-COMP123-S24-AA/Functions/ATurtleBarChart.html
"""

import turtle


def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


def main():
    xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
    maxheight = max(xs)
    numbars = len(xs)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(-border, -border, 40*numbars+border, maxheight+border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)


    for a in xs:
        drawBar(tess, a)

    wn.mainloop()

if __name__ == "__main__":
    main()
