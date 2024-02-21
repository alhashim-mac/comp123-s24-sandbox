"""
Practicing with string

@link: https://docs.python.org/3/library/stdtypes.html#str
"""
import string
import sys
import turtle

# since strings are immutable, only one string object is created per unique literal
a = 'one'
print(hex(id(a)))
b = 'one'
print(hex(id(b)))


# the r (raw) prefix: disable most escape sequence processing
with_r = r"s\niff"
without_r = "s\niff"
print(with_r)
print(without_r)


# building strings using str.join() or io.StringIO is more efficient
j = " ".join(['a', 'b'])
print(j)


# using different encoding
a = str(object='يا')    # Arabic
print(a)


# using format strings (fill-in-the-braces strings)
fs1 = 'This is COMP{}'.format(123)  # no specification
print(fs1)

fs2 = 'This is COMP{:.2f}'.format(123)  # 2 decimals specification
print(fs2)

fs3 = 'This is {{ COMP{} }}'.format(123)    # using { and }
print(fs3)

fs4 = 'This is COMP{1} not COMP{0}'.format(127, 123)    # reference arg 1
print(fs4)


# the slice operator
so = 'slicer'
print(so[0:2], so[-3:-1])
print(so[3:], so[-4:])  # omit 2nd index
print(so[:3], so[:-2])  # omit 1st index
print(so[3:999], so[-44:-4])    # slice operator is forgiving, no out-of-range exception


# comparison
a = 'hi'
b = 'Hi'
if a == b:
    print('{} == {}'.format(a, b))
elif a < b:
    print('{} <> {}'.format(a, b))
else:
    print('{} > {}'.format(a, b))


# ordinal value of characters
char = 'a'
print('Ordinal value of {} is {}'.format(char, ord(char)))

char = 'A'
print('Ordinal value of {} is {}'.format(char, ord(char)))


# get characters from their ordinal values
for c in range(10, 15):
    print('{} represents {}'.format(c, chr(c)))


# since strings are immutable, they can not be modified
im = 'hi'
print(im)
# im[0] = 'H'     # ERROR
# print(im)


# traversal: visiting elements of a collection one at a time ...
tra = 'This is a message to traverse'
# ... using foreach
for c in tra:
    print(c)
# ... using index & for loop
for i in range(len(tra)):
    print(tra[i])
# ... using index & while loop
i = -1
while i >= -len(tra):
    print(tra[i])
    i -= 1


# check if a string include another
str1 = "hello"
str2 = "h"
if str2 in str1:
    print('{} is in {}'.format(str2, str1))
else:
    print('{} is NOT in {}'.format(str2, str1))

str1 = "hello"
str2 = "max"
if str2 in str1:
    print('{} is in {}'.format(str2, str1))
else:
    print('{} is NOT in {}'.format(str2, str1))


# remove vowels
vo = "aeiuo"
sen = "This is a test sentence with some vowels"
print(sen)
for c in vo:
    sen = sen.replace(c, "")
print(sen)


# L-System
# Axiom: A
# Rule 1: A -> B
# Rule 2: B -> AB
def apply_lsystem1_rule(char):
    # if char == 'A':
    #     return 'B'
    # elif char == 'B':
    #     return 'AB'
    # else:
    #     return char

    if char == 'F':
        return 'F-F++F-F'
    else:
        return char


def apply_lsystem2_rule(char):
    if char == 'F':
        return 'F-F++F-F'
    else:
        return char

def generate_lsystem_once(str):
        new_str = ''
        for c in str:
            new_str += apply_lsystem1_rule(c)
        return new_str

def generate_lsystem1(axiom, n):
    str = axiom
    for i in range(n):
        str = generate_lsystem_once(str)
    return str


for i in range(3):
    # print(i, generate_lsystem1('A', i))
    print(i, generate_lsystem1('F', i))


# com = generate_lsystem1('F', 7)
# scr = turtle.Screen()
# trt = turtle.Turtle()
# trt.speed(0)
# for c in com:
#     if c == 'F':
#         trt.forward(30)
#     elif c == 'B':
#         trt.back(60)
#     elif c == '+':
#         trt.left(30)
#     elif c == '-':
#         trt.right(60)
# scr.mainloop()


# optional parameter
def mult(str, n=2):
    return str*n


print(mult('hello'))    # use default value for 2nd parameter
print(mult('hello', 4))


# string constants
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.printable)
print(string.punctuation)
