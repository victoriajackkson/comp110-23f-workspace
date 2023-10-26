"""Continuing conditionals."""
my_number_string: str = input("guess a number: ")
my_number: int = int(my_number_string)

if my_number == 10:
    print(str(my_number) + " Right")
else:
    print(str(my_number) + " Wrong")
