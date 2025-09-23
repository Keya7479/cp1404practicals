"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """
    Get both user input and random score and display respective results.
    """
    # for user input score
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"Your score of {score:.2f} is {result}")
    # for random score
    score = random.randint(0, 100)
    result = determine_result(score)
    print(f"Your random score of {score:.2f} is {result}")


def determine_result(score):
    """Determine result based on grading boundaries for score."""
    if score < 0 or score > 100:
        return "invalid"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


main()
