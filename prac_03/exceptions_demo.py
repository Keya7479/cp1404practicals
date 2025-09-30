"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


def main():
    """divide numbers given by user"""
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = get_nonzero_denominator()
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")


def get_nonzero_denominator():
    """get an integer denominator that is not 0"""
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator must be > 0")
        denominator = int(input("Enter the denominator: "))
    return denominator


main()

# When will a ValueError occur? If input is not an integer.
# When will a ZeroDivisionError occur? denominator = 0.
# Could you change the code to avoid the possibility of a ZeroDivisionError? yes.
