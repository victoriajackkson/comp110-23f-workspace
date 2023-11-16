"""File to define Fish class."""
__author__ = "730400711"


class Fish:
    """Creating a class for Fish."""
    age: int
    
    def __init__(self):
        """Creating self method for Fish class."""
        self.age = 0
        return None
    
    def one_day(self):
        """Fish age each day."""
        self.age += 1
        return None
    