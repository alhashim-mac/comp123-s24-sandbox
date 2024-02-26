# a = [10, 20, [30, 40], 50]
a = (10, 20, (30, 40), 50)
x = a

x[2][0] = 599
print(a)

# print(a)
# print(x[2][0])
# print(a[1])
#
# a[1] = 200
# print(a)
