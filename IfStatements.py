# This program asks user to enter either M, D, H, or S, for the age to be
# converted to either months, days, hours, or seconds, relatively.
# It then asks the user to enter an age in years and converts it based on the
# user's choice, using if and else if statements.


def get_choice():
    print("Enter M to have your age converted into months, D to have it " +
          " converted into days, H to have it converted into hours, or S " +
          " to have it converted into seconds: ")
    choice = input()
    
    return choice


def get_age():
    print("Enter age in years:")
    age = int(input())

    return age


def calculate_months(age):
    months = age * 12

    return months


def calculate_days(age):
    days = age * 365

    return days


def calculate_hours(age):
    hours = age * 365 * 24

    return hours


def calculate_seconds(age):
    seconds = (age * 365) * 24 * 60 * 60

    return seconds


def display_results(value, label):
    print(f"You are {value:.0f} {label} old.")
    
    return value


def main():
    age = get_age()
    choice = get_choice()
    if choice == "M" or choice == "m":
        months = calculate_months(age)
        display_results(months, "months")
    elif choice == "D" or choice == "d":
        days = calculate_days(age)
        display_results(days, "days")
    elif choice == "H" or choice == "h":
        hours = calculate_hours(age)
        display_results(hours, "hours")
    elif choice == "S" or choice == "s":
        seconds = calculate_seconds(age)
        display_results(seconds, "seconds")
    else:
        print("You must enter M, D, H, or S.")


main()

