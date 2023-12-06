"""Dictionary related utility functions."""

__author__ = "730400711"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    data_rows: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        data_rows.append(row)
    file_handle.close()
    return data_rows

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the table.
    for elem in table:
        # for each dictionary, get the value at key "header" and add that to result list
        result.append(elem[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it is a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loops through keys as one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key(header), make a dictionary entry with all the columns
        result[key] = column_values(table, key)
    return result

def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces new column with only certain amount of rows of data for each column."""
    result: dict[str, list[str]] = {}
    # loops through each of the columns in first row of table
    for column_name in table:
        N_values = []
        # gets values for column
        column_values = table[column_name]
        # loops through N items in table column
        for index in range(min(N, len(column_values))):
            # for each dictionary, get value at key "row_number" and add to n_values
            N_values.append(column_values[index])
        result[column_name] = N_values
    return result

def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produces new table with specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for name in column_names:
        result[name] = table[name]
    return result

def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces new table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    # loops through each column in first parameter
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result

def count(input: list[str]) -> dict[str, int]:
    """Produces list where each key is unique value in given list and is associated with the count of times it appeared in input."""
    result: dict[str, int] = {}
    for item in input:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result