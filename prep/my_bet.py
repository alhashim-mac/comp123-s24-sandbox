def between(value, lo, hi):
    """Takes in three numbers: a value, a low number, and a high number
    and it returns True if value is between lo and hi, inclusively."""
    assert type(value) in [int, float]
    assert type(lo) in [int, float]
    assert type(hi) in [int, float]
    if (lo <= value) and (value <= hi):
        return True
    else:
        return False
