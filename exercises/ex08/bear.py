"""File to define Bear class."""
__author__ = "730400711"


class Bear:
    """Creating a class to represent Bear."""
    age: int
    hunger_score: int

    def __init__(self):
        """Creating self method."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Each day bears age and eat."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Creating method for what bear's eat in river."""
        self.hunger_score += num_fish
        return None