"""
CP1404/CP5632 - Practical
Answer questions about random.rand
"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1? 15
# What was the smallest number you could have seen, what was the largest? 5, 20
#
# What did you see on line 2? 3
# What was the smallest number you could have seen, what was the largest? 3, 9
# Could line 2 have produced a 4? no
#
# What did you see on line 3? 2.8934915192769806
# What was the smallest number you could have seen, what was the largest? 2.5, 5.5

# produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))
