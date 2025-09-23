"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert temperatures using menu UI."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = concert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def concert_fahrenheit_to_celsius(fahrenheit):
    # concert Fahrenheit to Celsius
    # question: is this function docstring really necessary?
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    # concert Celsius to Fahrenheit
    return celsius * 9.0 / 5 + 32


main()
