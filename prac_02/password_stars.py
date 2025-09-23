"""

Program to get password from the user.
"""

password = input("Enter password: ")
MINIMUM_LENGTH = 3

while len(password) < MINIMUM_LENGTH:
    print(f"Error: password length is less than {MINIMUM_LENGTH} characters")
    password = input("Enter password: ")

print("*" * len(password))
