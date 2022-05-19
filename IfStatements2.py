# This program asks the user to enter a distance (in miles) and whether they
# want the entered distance to be converted into US measurements (yards, feet,
# and inches) or metric measurements (kilometers, meters, and centimeters).
# It then uses the distance and the choice (of US or metric) to calculate
# measurements.


def get_choice():
    print("Enter U for the distance to be converted into US measurements " +
          "yards, feet, and inches) or M for metric conversions  " +
          " (kilometers, meters, and centimeters):")
    choice = input()
    return choice


def get_miles():
    print("Enter a distance in the unit of miles to have it calculated into " +
          " either US or Metric measurements:")
    miles = int(input())
    return miles


def calculate_yards(miles):
    yards = miles * 1760
    return yards


def calculate_feet(miles):
    feet = miles * 5280
    return feet


def calculate_inches(miles):
    inches = miles * 63360
    return inches


def calculate_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers


def calculate_meters(miles):
    meters = miles * 1609.34
    return meters


def calculate_centimeters(miles):
    centimeters = miles * 160934
    return centimeters


def display_results(value, label):
    print(f"{value:.0f} {label}")
    return value


def main():
    miles = get_miles()
    choice = get_choice()
    if choice == "U" or choice == "u":
        yards = calculate_yards(miles)
        display_results(yards, "yards")
        feet = calculate_feet(miles)
        display_results(feet, "feet")
        inches = calculate_inches(miles)
        display_results(inches, "inches")
    elif choice == "M" or choice == "m":
        kilometers = calculate_kilometers(miles)
        display_results(kilometers, "kilometers")
        meters = calculate_meters(miles)
        display_results(meters, "meters")
        centimeters = calculate_centimeters(miles)
        display_results(centimeters, "centimeters")
    else:
        print("To have your distance converted, you must enter U or M.")


main()
