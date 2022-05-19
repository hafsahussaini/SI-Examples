# This program calculates and displays an entered distance (in miles) into
# yards, feet, and inches.
# Every calculation and input is in separate functions.


def get_miles():
    print("Enter a distance in the unit of miles to have it calculated into " +
          "yards, feet, and inches.")
    miles = float(input())
    return miles


def calculate_yards(miles):
    yards = miles * 1760
    return yards


def calculate_feet(yards):
    feet = yards * 3
    return feet


def calculate_inches(feet):
    inches = feet * 12
    return inches


def display_results(miles, yards, feet, inches):
    print(f"{yards:.0f} yards")
    print(f"{feet:.0f} feet")
    print(f"{inches:.0f} inches")


def main():
    miles = get_miles()
    yards = calculate_yards(miles)
    feet = calculate_feet(yards)
    inches = calculate_inches(feet)
    display_results(miles, yards, feet, inches)


main()
