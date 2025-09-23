"""
CP1404/CP5632 - Practical
Program to get password from the user
"""
MINIMUM_LENGTH = 3


def main():
    """Get password and print a number of asterisks respective to length of password."""
    password = get_valid_password()
    print_asterisks(password)


def get_valid_password():
    """Get a valid password that is equal to or greater MINIMUM_LENGTH."""
    password = input(f"Enter password (must be > {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Error: password length is less than {MINIMUM_LENGTH} characters")
        password = input(f"Enter password (must be > {MINIMUM_LENGTH} characters): ")
    return password


def print_asterisks(password):
    """Print number of asterisks equal to the number of characters in the provided password."""
    print("*" * len(password))


main()
