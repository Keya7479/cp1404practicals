"""
CP1404/CP5632 - Practical
Program to analyse scores with a simple consol menu UI
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars 
(Q)uit"""


def main():
    """Menu UI for various functions."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Your result is {determine_result(score)}")
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid input :(")
        print(MENU)
        choice = input(">>> ").upper()
    print("Bye bye :)")


def get_valid_score():
    """Get score and check it is valid: within range 0-100."""
    score = int(input("Enter your score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Enter your score (0-100): "))
    return score


def determine_result(score):
    """Determine result based on grading boundaries for score."""
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


def print_asterisks(score):
    """Print number of asterisks equal to score."""
    print("*" * score)


main()
