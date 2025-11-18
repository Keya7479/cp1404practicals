"""
Taxi simulator program.
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

WELCOME_MESSAGE = "Let's drive!"
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator menu that lets users pick a taxi and drive it while summing a bill."""
    bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    # Would this be a good chance to use a global variable for taxis?
    # As I have to pass it through to my other functions anyway.
    print(WELCOME_MESSAGE)
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available")
            display_taxis(taxis)
            current_taxi = get_chosen_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                cost_of_drive = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost_of_drive}")
                bill += cost_of_drive
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_chosen_taxi(taxis):
    """Get a chosen taxi from user."""
    try:
        return taxis[int(input("Choose taxi: "))]
    except (IndexError, ValueError):
        print("Invalid taxi choice")


main()
