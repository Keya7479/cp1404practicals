"""Project Class."""


class Project:
    """Project class."""

    def __init__(self, name, date, priority, cost, completion):
        """Initialize a Project object."""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return string representation of data in a Project."""
        return (f"{self.name}, start: {self.date}, priority {self.priority}, estimate ${self.cost:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Determine if self is less than other based on priority"""
        return int(self.priority) < int(other.priority)

    def is_complete(self):
        """Determine if project is complete"""
        return self.completion == 100

