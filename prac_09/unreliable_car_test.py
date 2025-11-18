"""
Test cases for UnreliableCar
"""
from prac_09.unreliable_car import UnreliableCar

MAX_NUMBER_OF_RUNS = 10


def main():
    """Test UnreliableCars."""
    unreliable_car1 = UnreliableCar(name="Bad car :(", fuel=100, reliability=30)
    number_of_successful_drives = 0
    for i in range(1, MAX_NUMBER_OF_RUNS):
        if unreliable_car1.drive(10):
            # when car fails to drive it returns 0, which can be treated as a boolean.
            number_of_successful_drives += 1

    print(
        f"In {MAX_NUMBER_OF_RUNS} runs, {unreliable_car1.name} successfully drove {number_of_successful_drives} times with a reliability of "
        f"{unreliable_car1.reliability}")


main()
