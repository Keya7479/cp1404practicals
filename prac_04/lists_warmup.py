"""
CP1404/CP5632 - Practical
Practise using lists
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

print(f"1: {numbers[0]}")  # 3
print(f"2: {numbers[-1]}")  # 2
print(f"3: {numbers[3]}")  # 1
print(f"4: {numbers[:-1]}")  # 3, 1, 4, 1, 5, 9
print(f"5: {numbers[3:4]}")  # 1
print(f"6: {5 in numbers}")  # true
print(f"7: {7 in numbers}")  # false
print(f"8: {"3" in numbers}")  # false
print(f"9: {numbers + [6, 5, 3]}")  # 3, 1, 4, 1, 5, 9, 2, 6, 5, 3

# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers)

# 2. Change the last element of numbers to 1
numbers[0] = "1"
print(numbers)

# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Print whether 9 is an element of numbers
print(9 in numbers)
