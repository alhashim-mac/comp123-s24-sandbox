"""
Calculate the average and standard deviation of the low and high temperatures of 5 days read from the user
"""
import statistics


def multivariable_approach():
    print("Day 1")
    day1_lo = int(input("Enter low  temperature: "))
    day1_hi = int(input("Enter high temperature: "))

    print("Day 2")
    day2_lo = int(input("Enter low  temperature: "))
    day2_hi = int(input("Enter high temperature: "))

    print("Day 3")
    day3_lo = int(input("Enter low  temperature: "))
    day3_hi = int(input("Enter high temperature: "))

    print("Day 4")
    day4_lo = int(input("Enter low  temperature: "))
    day4_hi = int(input("Enter high temperature: "))

    print("Day 5")
    day5_lo = int(input("Enter low  temperature: "))
    day5_hi = int(input("Enter high temperature: "))

    lo_avg = statistics.mean([day1_lo, day2_lo, day3_lo, day4_lo, day5_lo])
    hi_avg = statistics.mean([day1_hi, day2_hi, day3_hi, day4_hi, day5_hi])

    lo_sd = statistics.stdev([day1_lo, day2_lo, day3_lo, day4_lo, day5_lo])
    hi_sd = statistics.stdev([day1_hi, day2_hi, day3_hi, day4_hi, day5_hi])

    print(f"Average low  temperature: {lo_avg:.2f}±{lo_sd:.2f}")
    print(f"Average low  temperature: {hi_avg:.2f}±{hi_sd:.2f}")


def list_approach():
    lo_temps: int = []
    hi_temps: int = []

    for i in range(1, 6):
        print("Day", i)
        lo = int(input("Enter low  temperature: "))
        hi = int(input("Enter high temperature: "))
        lo_temps.append(lo)
        hi_temps.append(hi)

    lo_avg = statistics.mean(lo_temps)
    hi_avg = statistics.mean(hi_temps)

    lo_sd = statistics.stdev(lo_temps)
    hi_sd = statistics.stdev(hi_temps)

    print(f"Average low  temperature: {lo_avg:.2f}±{lo_sd:.2f}")
    print(f"Average low  temperature: {hi_avg:.2f}±{hi_sd:.2f}")


class Temperature:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi


def class_approach():
    temps = []

    for i in range(1, 6):
        print("Day", i)
        lo = int(input("Enter low  temperature: "))
        hi = int(input("Enter high temperature: "))
        temp = Temperature(lo, hi)
        temps.append(temp)

    lo_temps = [temperature.lo for temperature in temps]  # List Comprehension
    hi_temps = [temperature.hi for temperature in temps]  # List Comprehension

    lo_avg = statistics.mean(lo_temps)
    hi_avg = statistics.mean(hi_temps)

    lo_sd = statistics.stdev(lo_temps)
    hi_sd = statistics.stdev(hi_temps)

    print(f"Average low  temperature: {lo_avg:.2f}±{lo_sd:.2f}")
    print(f"Average low  temperature: {hi_avg:.2f}±{hi_sd:.2f}")


def main():
    # multivariable_approach()
    # list_approach()
    # class_approach()
    pass


if __name__ == '__main__':
    main()
