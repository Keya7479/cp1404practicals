"""
Test program for Guitar class.
"""

from guitar import Guitar

gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 100)

print(f"{gibson_guitar.name} get_age() - Expected 100. Got {gibson_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
print(f"{gibson_guitar.name} is_vintage() - Expected True. Got {gibson_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
