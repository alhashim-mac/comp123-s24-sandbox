def something(n):
    if n < 10:
        return "okay"
    elif n < 100:
        return "I don't know"
    else:
        return "something wrong"


if __name__ == "__main__":
    assert something(9) == "okay"
    assert something(90) == "I don't know"
    assert something(110) == "something wrong"

