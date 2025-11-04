"""Guitar Class."""
CURRENT_YEAR = 2022
VINTAGE_MINIMUM_YEAR = 50


class Guitar:
    """Guitar class."""

    def __init__(self, name="", year=0, cost=0.00):
        """Initialize a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of data in a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """????????????"""
        return self.year < other.year

    def get_age(self):
        """Gets age of Guitar."""
        guitar_age = CURRENT_YEAR - self.year
        return guitar_age

    def is_vintage(self):
        """Checks if Guitar is vintage."""
        return self.get_age() >= VINTAGE_MINIMUM_YEAR
