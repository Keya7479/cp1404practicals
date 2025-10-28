"""ProgrammingLanguage Class."""


class ProgrammingLanguage:
    """ProgrammingLanguage class."""

    def __init__(self, name="", typing="Static", reflection="Yes", year=0):
        """Initialize a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of data in a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """determine if programming language is dynamically typed."""
        return self.typing == "Dynamic"
