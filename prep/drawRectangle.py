import turtle

screen1 = turtle.Screen()     # instantiate a Screen object
screen1.bgcolor("PeachPuff")  # change the background color attribute of the
                              # Screen object by invoking/calling the bgcolor
                              # method

turtle1 = turtle.Turtle()   # instantiate a Turtle object
turtle1.pensize(10)         # change the pen size attribute of the Turtle object

turtle1.forward(100)        # moving the Turtle object forward by invoke/call
                            # the forward method
turtle1.left(90)            # turning the Turtle object to the left
                            # 90 degrees by invoke/call the left method

turtle1.forward(200)
turtle1.left(90)

turtle1.forward(100)
turtle1.left(90)

turtle1.forward(200)

screen1.exitonclick()
