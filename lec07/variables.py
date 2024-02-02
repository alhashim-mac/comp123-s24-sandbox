"""
The script demonstrates
- local vs global variables
- how local variable can shadow global variables

@auther: Amin Alhashim (aalhashi@macalester.edu)
"""


# fruitful function with 1 (formal) parameters
def double(x):      # x is a local variable shadow global variable x
    d = 2*x         # d is a local variable shadow global variable d
    return d


x = 4           # x is a global variable
d = double(x)   # d is a global variable
print(d)
