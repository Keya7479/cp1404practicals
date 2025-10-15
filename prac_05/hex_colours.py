"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

COLOUR_TO_CODE = {"brightlilac": "#d891ef", "coralpink": "#f88379", "bisque2": "#eed5b7", "aquamarine1": "#7fffd4",
                  "carnelian": "#b31b1b", "daffodil": "#ffff31", "deepskyblue4": "#00688b", "deeppink4": "#8b0a50"}

max_name_length = max(len(code) for code in list(COLOUR_TO_CODE.keys()))
for colour, code in COLOUR_TO_CODE.items():
    print(f"{colour:{max_name_length}} is {code}")

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid name")
    colour_name = input("Enter colour name: ").lower()
