"""
CP1404/CP5632 Practical
program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output.
Each line consists of NUMBER_IN_LINE random numbers between MINIMUM and MAXIMUM.
"""
import random

NUMBERS_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("Enter number of 'quick picks': "))
for quick_pick in range(number_of_quick_picks):
    line = []
    for number in range(NUMBERS_IN_LINE):
        line.append(random.randint(MINIMUM, MAXIMUM))
    line.sort()
    print(" ".join(f"{number:3}" for number in line))



