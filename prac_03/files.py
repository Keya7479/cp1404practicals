"""
CP1404/CP5632 - Practical
Various file manipulation mini programs
"""


"""1. opens a file called name.txt and writes user inputted name to it."""
name = input("Enter name: ")
in_file = open("name", "w")
print(name, file=in_file)
in_file.close()

"""2. opens "name.txt" and reads the name then prints: Hi Bob!"""
name = input("Enter name: ")
in_file = open("name", "w")
print(f"Hi {name}!", file=in_file)
in_file.close()

"""3. opens numbers.txt, reads only the first two numbers, adds them together then prints the result"""
with open("numbers", "r") as in_file:
    print(int(in_file.readline()) + int(in_file.readline()))

"""4. prints the total for all lines in numbers.txt"""
total = 0
with open("numbers", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)
