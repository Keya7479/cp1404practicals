"""
Emails
stores users' emails (unique keys) and names (values) in a dictionary
Estimate: 20 minutes
Actual:   20 minutes
"""


def main():
    """convert email addresses to dictionaries of name to email"""
    email = input("Email: ")
    name_to_email = {}

    while email != "":
        name = extract_name(email)
        verification = input(f"Is your name {name}? (Y/n)").upper()
        if verification != "Y" and verification != "":
            name = input("Name: ")
        name_to_email[name] = email
        email = input("Email: ")

    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email"""
    name = " ".join((email.split("@")[0]).split(".")).title()
    return name


main()
