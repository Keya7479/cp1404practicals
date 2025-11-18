"""
Test cases for UnreliableCar
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars."""
    unreliable_car1 = UnreliableCar(name="Bad car :(", fuel=100, reliability=30)
    successful_drive = 0
    for i in range(1, 10):
        if unreliable_car1.drive(10):
            # when car fails to drive it returns 0, which can be treated as a boolean.
            # But is it ok to use it as a boolean when it's meant to act as an int?
            successful_drive += 1

    print(f"In 10 runs, {unreliable_car1.name} successfully drove {successful_drive} times with a reliability of "
          f"{unreliable_car1.reliability}")


main()
