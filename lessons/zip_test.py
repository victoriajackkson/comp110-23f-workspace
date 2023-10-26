"""Testing my zip function."""
__author__ = "730400711"

from lessons.zip import zip


# Test for empty strings, if yes, return empty dictionary
def test_empty_list() -> None:
    """zip([], []) should return {}."""
    assert zip([], []) == {}


# Testing that parameters given create key pair with key being from first list and value being from second list.
def test_dict() -> None:
    """zip([],[]) should return {key from list 1, value from list 2} if lists are equal lengths."""
    test_list1: list[str] = ["Hello", "Victoria"]
    test_list2: list[int] = [1, 2]
    assert zip(test_list1, test_list2) == {"Hello": 1, "Victoria": 2}


# Testing lengths of lists given, if unequal, return empty dictionary.
def test_list_lengths() -> None:
    """zip([], []) should return {} if lists are unequal lengths."""
    test_list1: list[str] = ["Hello", "Victoria"]
    test_list2: list[int] = [1]
    assert zip(test_list1, test_list2) == {}
