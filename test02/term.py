"""
This is a program used in the practice test

@author: Amin G. Alhashim (aalhashi@macaleser.edu)
"""


def something(x, y):
    """
    Given a list of numbers, count how many are divisible by x

    :param x: first number
    :param y: second number
    :return: something
    :precondition: y is list
    :post condition: return number of numbers in y divisible by x
    """
    assert type(y) is list

    c = 0
    for a in y:
        if a % x == 0:
            c = c + 1

    return c


if __name__ == "__main__":
    a = 3
    b = [8, 9, 3, 1, 4, 2]
    c = something(a, b)
    print(c)
