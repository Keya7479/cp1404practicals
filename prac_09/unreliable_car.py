"""
UnreliableCar class
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, reliability: int, **kwargs):
        """
        Initialise a Taxi instance, based on parent class Car.

        Reliability is a number between 1 and 100.
        """
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only if randomly generated number is less than self.reliability"""
        random_number = random.randint(1, 100)
        if random_number >= self.reliability:
            distance = 0  # car will not drive any distance
        return super().drive(distance)
