"""Practice problem function writing."""
__author__ = "730400711"


def odd_and_even(input_list: list[int]) -> list[int]:
    """Function that returns new list containing elements of input list that are odd but have even index."""
    idx: int = 0
    list2: list[int] = []
    while idx < len(input_list):
        if input_list[idx] % 2 == 1 and idx % 2 == 0:
            list2.append(input_list[idx])
        idx += 1
    return list2