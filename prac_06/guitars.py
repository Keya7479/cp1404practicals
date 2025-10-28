"""
My guitars program.
Gets instance attributes from user and creates Guitar objects to put into guitars (list).
Then prints guitars.

Estimate: 20 minutes
Actual:   20 minutes
"""
from guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")

while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    name = input("Name: ")

print(f"\n...snip...\n")
print("Theses are my guitars:")
for i, guitar in enumerate(guitars, 1):
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")
