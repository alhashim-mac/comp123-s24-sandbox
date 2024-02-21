# string format
# string comparison
"""
everything in computers are represented using number, strings are no
different, each character was assigned a numeric value and based and strings
are compared based on these values, see https://www.ascii-code.com/ for the
values assigned to each character when using the ascii encoding.
"""
# find out the characters for the first values from 0-200
for val in range(0, 200):
    print('{} -> {}'.format(val, chr(val)))

# the reverse can also be done
for ch in 'ABab123!#':
    print('{} -> {}'.format(ch, ord(ch)))


# slice operator
s = "This is a test for the slice operator"
print(s[0: 6])  # get the slice that starts at 0 (inclusive) and ends at 6 (exclusive)
