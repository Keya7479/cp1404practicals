"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi (which is a Car) that includes fanciness."""
    flagfall = 4.50  # extra charge for each new fare

    def __init__(self, name, fuel, fanciness: float):
        """
        Initialise a SilverServiceTaxi instance, based on parent class Taxi.

        Fanciness scales (multiplies) the price_per_km.
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip including flagfall"""
        return self.flagfall + super().get_fare()

