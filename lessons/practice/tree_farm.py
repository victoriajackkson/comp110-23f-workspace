""""Christmas treee farm practice."""

class ChristmasTreeFarm:
    """Class to represent CTF."""
    plots: list[int]

    def __init__(self, plots:int, initial_planting: int):
        """constructor."""
        self.plots = []
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
        i += 1
        while i < plots:
            self.plots.append(0)
    
    def plant(self, plot_idx: int):
        """ghdglkg."""
        plot_idx: int = 0
        while plot_idx < self.plots:
            self.plots += 1
        plot_idx += 1
        if self.plots > 1:
            self.plots.append(1)
    
    def growth(self):
        """fghdfogl."""
        self.plots = []
        for p in self.plots:
            if len(self.plots) <= 0:
                self.plots += 1

    def harvest(self, replant: bool) -> int:
        """hjrogerg."""
        count: int = 0
        for trees in self. plots:
            if trees <= 5:
                replant == False
            else:
                replant == True
                count += 1
        return count