"""Summing the elements of a list using different loops."""
__author__ = "730400711"


def w_sum(vals: list[float]) -> float:
    """Returns sum of input of values using while loop."""
    index: int = 0
    sum: float = 0.0
    while index < len(vals): 
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns sum of input of values using for loop."""
    sum: float = 0.0
    for item in vals:
        sum += item
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of input of values using for loop and range."""
    sum: float = 0.0
    for item in range(0, len(vals)):
        sum += vals[item]
    return sum