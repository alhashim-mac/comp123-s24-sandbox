"""
The script demonstrates unit testing

@auther: Amin Alhashim (aalhashi@macalester.edu)
"""

def double(x):
    """
    Doubles the value passed to it
    """
    d = 2*x
    return d


assert 4 == double(2)
assert 9 == double(3)
