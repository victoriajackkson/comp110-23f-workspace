"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730400711"


class Simpy:
    """This is my class to represent Simpy."""
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, ones: list[float]):
        """Constructor to initialize the values attributed to Simpy object."""
        self.values = ones
    
    def __str__(self) -> str:
        """Method to produce strings of text for Simpy."""
        my_string: str = f"Simpy{self.values}"
        return my_string
    
    def fill(self, filling_list: float, times_to_fill: int) -> None:
        """Method to fill in simpy's values with specific number of repeating values."""
        my_list = []
        for number in range(times_to_fill):
            my_list.append(filling_list)
        self.values = my_list
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Method to fill in values attribute with range of values."""
        assert step != 0.0
        self.values = []
        if step > 0:
            number = start
            while number < stop:
                self.values.append(number)
                number += step
        else:
            number = start
            while number > stop:
                self.values.append(number)
                number += step

    def sum(self) -> float:
        """Sums all of the items in the values attribute."""
        sum: float = 0.0
        for number in self.values:
            sum += number
        return sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Magic method to add simpy objects and floats."""
        if isinstance (rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_numbers = []
    # adds two Simpy objects
            for x in range(len(self.values)):
                new_numbers.append(self.values[x] + rhs.values[x])
        else:
    # adds Simpy and float
            for x in self.values:
                new_numbers = [x + rhs]
        return Simpy(new_numbers) 
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Magic method to raise Simpy objects and floats."""
        new_numbers = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
    # raises two Simpys
            for x in range(len(self.values)):
                new_numbers.append(self.values[x] ** rhs.values[x])
        else:
    # raises Simpy by float
            for x in self.values:
                new_numbers.append(x ** rhs)
        return Simpy(new_numbers) 
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Magic method to see if objects are equal."""
        new_values =[]
        equal: bool = False
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
    # for two Simpys
            for x in range(len(self.values)):
                if self.values[x] == rhs.values[x]:
                    new_values.append(self.values[x] and rhs.values[x])
                    equal = True
        else:
    # raises Simpy by float
            if rhs in self.values:
                new_values != equal
        return new_values
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for >."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            return Simpy([x > y for x, y in zip(self.values, rhs.values)])
        else:
            return Simpy([i > rhs for i in self.values])

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Operator overload to add subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list) and all(isinstance(x, bool) for x in rhs):
            return Simpy([self.values[value]] for value in range(len(self.values)) if rhs[value])
