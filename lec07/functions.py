"""
The script demonstrates
- the different types of functions: fruitful vs non-fruitful and
  those with formal parameters vs those without
- the difference between formal parameter and actual parameters (arguments)
- how to call functions

@auther: Amin Alhashim (aalhashi@macalester.edu)
"""
import random


# non-fruitful function with no (formal) parameters
def print_hello_5():
    for i in range(5):
        print("Hello!")


# non-fruitful function with 1 (formal) parameters
def print_hello(n):
    for i in range(n):
        print("Hello!")
# fruitful function with no (formal) parameters


def give_rand():
    r = random.random()     # temporary local variable
    return r


# fruitful function with 1 (formal) parameters
def double(x):
    d = 2*x                 # temporary local variable
    return d


# print_hello_5()
# print_hello(3)            # 3 is the argument (actual parameter)
print(give_rand())
print(double(5))            # 5 is the argument (actual parameter)
