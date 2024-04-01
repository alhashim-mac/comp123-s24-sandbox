"""
Calculate the average and standard deviation of the low and high temperatures of 5 days read from the user
"""
import statistics


def approach1():
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
    hi_avg = statistics.mean([day1_hi, day2_hi, day3_hi, day5_hi, day5_hi])

    lo_sd = statistics.stdev([day1_lo, day2_lo, day3_lo, day4_lo, day5_lo])
    hi_sd = statistics.stdev([day1_hi, day2_hi, day3_hi, day5_hi, day5_hi])

    print(f"Average low  temperature: {lo_avg:.2f}±{lo_sd:.2f}")
    print(f"Average low  temperature: {hi_avg:.2f}±{hi_sd:.2f}")


def main():
    approach1()


if __name__ == '__main__':
    main()
