sec = int(input("Enter time in seconds: "))

# calculate number of hours, if any
hours = sec // 3600
print("hours:", hours)

# find the remaining seconds
sec = sec - hours * 3600

# calculate number of minutes, if any
minutes = sec // 60
print("minutes:", minutes)

# find the remaining seconds
sec = sec - minutes * 60
print("seconds:", sec)
