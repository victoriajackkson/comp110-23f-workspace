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
    """Takes dictionary of names and favorite colors and returns color that appears most frequently."""
    color_counter: dict[str, int] = {}
    favorite: int = 0
    # Returning empty string if no input.
    if not input_dict:
        return ""
    for color in input_dict:
        if input_dict[color] in color_counter:
            color_counter[input_dict[color]] += 1
        else: 
            color_counter[input_dict[color]] = 1
    for color in color_counter:
        if color_counter[color] > favorite:
            favorite = color_counter[color]
    for color in color_counter:
        if color_counter[color] == favorite:
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
    word_dict: dict[str, list[str]] = {}
    for word in list1:
        # word = word.lower()
        first_letter = word[0].lower()

        if first_letter in word_dict:
            word_dict[first_letter].append(word)
        else:
            word_dict[first_letter] = [word]
    return word_dict


def update_attendance(input: dict[str, list[str]], weekday: str, student: str) -> dict[str, list[str]]:
    """Update attendance each day with student's names."""
    if weekday in input:
        if student not in input[weekday]:
            input[weekday].append(student)
    else:
        input[weekday] = [student]
    return input