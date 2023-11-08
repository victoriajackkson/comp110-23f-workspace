"""CQ07."""
from __future__ import annotations

__author__ = "730400711"


class Point:
    """Making class Point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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