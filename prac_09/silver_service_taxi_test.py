"""
Test cases for the SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Tests for Taxi class."""
    silver_service_taxi1 = SilverServiceTaxi(name="Fancy Taxi", fuel=100, fanciness=2)
    distance_driven = silver_service_taxi1.drive(18)
    print(silver_service_taxi1)
    print(f"{silver_service_taxi1.name} drove {distance_driven} at a cost of ${silver_service_taxi1.get_fare():.2f}")


main()
