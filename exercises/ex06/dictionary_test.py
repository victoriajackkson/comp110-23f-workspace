"""EX07- Testing dictionary functions."""
__author__ = "730400711"

from exercises.ex06.dictionary import invert, count, favorite_color, alphabetizer, update_attendance


# Tests for invert
def test_invert_empty_list() -> None:
    """invert({}) should return {}."""
    assert invert({}) == {}


def test_invert() -> None:
    """invert({}) should return {keys as values, values as keys}."""
    my_dictionary: dict[str, str] = {"hello": "v", "smile" : "big"}
    assert invert(my_dictionary) == {'v': 'hello', 'big': 'smile'}


import pytest
with pytest.raises(KeyError):
    """invert({}) should raise KeyError if keys in {} are the same."""
    test_dict: dict[str, str] = {'alyssa': 'byrnes', 'adam': 'byrnes'}
    invert(test_dict)


#Tests for favorite_color
def test_favorite_color() -> None:
    """favorite_color({}) should return color most reported."""
    my_dict: dict[str, str] = {"Hannah": "Yellow", "Soren": "Yellow", "Kat": "Yellow", "Jacob": "Orange"}
    assert favorite_color(my_dict) == "Yellow"


def test_tie() -> None:
    """favorite_color({}) should return color first in dictionary if tie."""
    my_dict1: dict[str, str] = {"Hannah": "Yellow", "Soren": "Pink", "Tanner": "Pink", "Chloe": "Yellow"}
    assert favorite_color(my_dict1) == "Yellow"


def test_favorite_color_empty_list() -> None:
    """favorite_color({}) should return {}."""
    assert favorite_color({}) == None


#Tests for count
def test_count_empty() -> None:
    """count([]) should return {}."""
    assert count([]) == {}


def test_count() -> None:
    """count([]) should return keys as counter of values in input."""
    my_list: list [str] = ["Soren", "Soren", "Hello", "There"]
    assert count(my_list) == {'Soren': 2, 'Hello': 1, 'There': 1}


def test_count_wrong_input() -> None:
    """count([]) should return at least one item if something in input."""
    my_list1: list [str] = [1]
    assert count(my_list1) == {1: 1}


# Tests for alphabetizer
def test_aplhabetizer_empty_list() -> None:
    """alphabetizer([]) should return {}."""
    assert alphabetizer([]) == {}


def test_alphabetizer() -> None:
    """alphabetizer([]) should return dictionary with words that start with key."""
    my_alphabet_list: list [str] = ["popcorn", "play", "hello", "kitty"]
    assert alphabetizer(my_alphabet_list) == {'p': ['popcorn', 'play'], 'h': ['hello'], 'k': ['kitty']}


def test_alphabetizer_one_item() -> None:
    """test if one item present in input."""
    my_alphabet_list1: list [str] = ["hike"]
    assert alphabetizer(my_alphabet_list1) == {'h': ['hike']}


# Testing update_attendance
def test_update_attendance_empty_student() -> None:
    """update_attendance({}) should return {}."""
    my_input: dict[str, list[str]] = {}
    my_days: str = "Monday"
    my_students: str = ""
    updated_attendance = update_attendance(my_input, my_days, my_students)
    assert updated_attendance == {"Monday": [""]}


def test_update_attendance() -> None:
    """update_attendance() should return students present on each day and update list."""
    my_days: str = "Tuesday"
    my_input: dict[str, list[str]] = {"Friday": ["Caleb", "Mercedes", "Valeria"], "Wednesday": ["Caleb"]}
    my_students: str = "Tyler"
    assert update_attendance(my_input, my_days, my_students) == {'Friday': ['Caleb', 'Mercedes', 'Valeria'], 'Wednesday': ['Caleb'], 'Tuesday': ['Tyler']}


def test_update_attendance_add_students() -> None:
    """update attendance with new students and corresponding days."""
    my_days1: str = "Friday"
    my_input1: dict[str, list[str]] = {"Friday": ["Caleb", "Mercedes", "Valeria"], "Wednesday": ["Caleb"]}
    my_students1: str = "Caleb"
    assert update_attendance(my_input1, my_days1, my_students1) == {'Friday': ['Caleb', 'Mercedes', 'Valeria', 'Caleb'], 'Wednesday': ['Caleb']}