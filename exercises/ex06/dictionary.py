"""EX06- Dictionary related utility functions."""
__author__ = "730400711"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Returns dictionary that inverts keys and values of input dictionary."""
    invert_dict: dict[str, str] = {}
    for elem in input_dict:
        if input_dict[elem] in invert_dict:
            raise KeyError
        new: str = elem
        key_added = input_dict[elem]
        invert_dict[key_added] = new
    return invert_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Takes dictionary of names and faviorite colors and returns color that appears most frequently."""
    color_counter: dict[str, int] = {}
    favorite: str = ""
    max: int = 0
    for color in input_dict.values():
        if color in color_counter:
            color_counter[color] += 1
        else: 
            color_counter[color] = 1
        if color_counter[color] > max or (color_counter[color] == max and color != favorite):
            max = color_counter[color]
            favorite == color
    return color


def count(input_list: list[str]) -> dict[str, int]:
    """Dictionary produced from list with keys as counter of values of item in input list."""
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
            

def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Given list, dictionary produced with words that start with key."""
    word_dict: dict[str, list[str]]= {}
    for word in list1:
        word = word.lower()
        first_letter = word[0].lower()

        if first_letter in word_dict:
            word_dict[first_letter].append(word)
        else:
            word_dict[first_letter] = [word]
    return word_dict


def update_attendance(input: dict[str, list[str]], weekday: str, student: str) -> dict[str, list[str]]:
    """Update attendance each day with student's names."""
    if weekday in input:
        input[weekday].append(student)
    else:
        input[weekday] = [student]
    return input