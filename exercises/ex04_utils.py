"""EX04- Work Utils."""
__author__ = "730400711"


def all(list: list[int], number: int) -> bool:
    """Returns T/F if integer inputted matches any in list given."""
    index: int = 0
    if list == []:
        return False
    while index < len(list):
        if number != list[index]:
            return False
        index += 1
    else:
        return True


def max(input: list[int]) -> int:
    """Given a list, the largest number is returned."""
    index: int = 0
    index2: int = 1
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        value: int = input[index]
        while index2 < len(input):
            if value < input[index2]:
                value = input[index2]
            index2 += 1
        return value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns T/F if elements are true to one another at each index in lists."""
    index: int = 0
    if len(list1) != len(list2):
        return False
    while index < len(list1) and len(list2):
        if list1[index] != list2[index]:
            return False
        index += 1
    else:
        return True