"""CQ07."""
from __future__ import annotations

__author__ = "730400711"


class Point:
    """Making class Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructing Point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Update the x and y attributes."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creates a new Point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Strings for x and y."""
        p_string: str = f"x: {self.x}; y: {self.y}"
        return p_string
    
    def __mul__(self, factor: int | float) -> Point:
        """Does same thing as scale."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Adds factor to x and y."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
    
# my_point = Point()
# print(my_point)
# my_other_point: Point = Point(2.0, 1.0)
# print(my_other_point)
# new_point = my_point * 3.0
# new_point = my_point + 3.0
# print(new_point)