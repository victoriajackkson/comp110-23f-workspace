"""Working with csv files."""
from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    # do stuff here
    file_handle.close()
    return result

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary, get the value at key "header" and add that to result list
        result.append(elem[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it is a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loops through eys as one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key(header), make a dictionary entry with all the columns
        result[key] = column_vals(table, key)
    return result