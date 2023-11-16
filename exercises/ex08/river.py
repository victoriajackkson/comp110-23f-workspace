"""File to define River class."""
__author__ = "730400711"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Creating River class."""
    day: int
    bears: list[int]
    fish: list[int]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking ages of all animals to see if need to be removed."""
        living_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                living_fish.append(fish)
        self.fish = living_fish
        living_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                living_bears.append(bear)
        self.bears = living_bears
        return None
    
    def remove_fish(self, amount: int):
        """Creating method that removes fish from river."""
        while amount > 0:
            amount -= 1
            self.fish.pop(0)

    def bears_eating(self):
        """Removes amount of fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks hunger score of bears in river."""
        not_hungry: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                not_hungry.append(bear)
        self.bears = not_hungry
        return None

    def repopulate_fish(self):
        """Fish reproduction."""
        r = len(self.fish)
        fish_baby: int = (r // 2) * 4
        for x in range(0, fish_baby):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Bear reproduction."""
        r = len(self.bears)
        bear_baby: int = r // 2
        for x in range(0, bear_baby):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Gives ability to look at fish and bear population each day."""
        print(f"~~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}\n")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulating river for each day of the week."""
        week_day: int = 0
        while week_day < 7:
            self.one_river_day()
            week_day += 1
        return None