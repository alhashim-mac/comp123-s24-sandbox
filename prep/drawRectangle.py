import turtle

# instantiate a Screen object
screen1 = turtle.Screen()

# change the background color attribute of the Screen object by
# invoking/calling the bgcolor method
screen1.bgcolor("PeachPuff")

# instantiate a Turtle object
turtle1 = turtle.Turtle()

# change the pen size attribute of the Turtle object
turtle1.pensize(10)

# moving the Turtle object forward by invoke/call the forward method
turtle1.forward(100)

# turning the Turtle object to the left 90 degrees by invoke/call the
# left method
turtle1.left(90)

turtle1.forward(200)
turtle1.left(90)

turtle1.forward(100)
turtle1.left(90)

turtle1.forward(200)

screen1.exitonclick()
