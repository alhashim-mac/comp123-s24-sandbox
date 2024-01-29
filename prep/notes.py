"""
This is a _module comment_ used to explain what the module does.
"""

import turtle as t
# reference the turtle module and name it `t`
print(t)

t1 = t.Turtle
# from the module turtle, access the Python element called `Turtle`
print(t1)

t2 = t.Turtle()
print(t2)

t1().forward(100)
t2.back(100)

t2.screen.mainloop()


def example_fun():
    """
    This is a _function comment_ used to explain what the function does
    :return:
    """
