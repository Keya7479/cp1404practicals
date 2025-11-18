"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} {", ".join(f"{musician.name} ({musician.instruments})" for musician in self.musicians)}"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument (or no) instrument."""
        return "\n".join((musician.play() for musician in self.musicians))
