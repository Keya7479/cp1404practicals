"""
Test cases for the Taxi class
"""
from prac_09.taxi import Taxi


def main():
    """Tests for Taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    print(f"{my_taxi.name} drove {my_taxi.drive(40)}.")
    print(my_taxi)
    my_taxi.start_fare()
    print(f"{my_taxi.name} drove {my_taxi.drive(100)}.")
    print(my_taxi)


main()
