"""Combining two lists into a dictionary."""
__author__ = "730400711"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Producing dictonary of keys for first list and values from second list."""
    zip_dict: dict[str, int] = {}
    if len(list1) != len(list2):
        return {}
    
    index: int = 0
    while index < len(list1):
        zip_dict[list1[index]] = list2[index]
        index += 1
    return zip_dict