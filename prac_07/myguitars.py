"""
Program to read all each guitar in guitars.csv and store them in a list of Guitar objects.
Display these using a loop.
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read FILENAME csv, save as list of objects, display sorted list."""
    guitars = extract_guitars()
    displayer_sorted_guitars(guitars)


def extract_guitars():
    """Extract guitars from FILENAME as list of objects (Guitars)."""
    guitars = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()  # Ignore header line
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], float(parts[2]))
            guitars.append(guitar)
    return guitars


def displayer_sorted_guitars(guitars):
    """Display Sorted guitars."""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
