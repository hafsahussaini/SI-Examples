# This program calculates and displays an entered age (in years) in units of
# months, days, hours, and seconds.
# It processes new information within separate functions.


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


def calculate_hours(days):
    hours = days * 24
    return hours


def calculate_seconds(days):
    seconds = days * 24 * 60 * 60
    return seconds


def display_results(months, days, hours, seconds):
    print(f"You are {months:.0f} months old.")
    print(f"That is equivalent to {days:.0f} days.")
    print(f"That is also equivalent to {hours:.0f} hours.")
    print(f"Your age in years is equivalent to {seconds:.0f} seconds.")


def main():
    age = get_age()
    months = calculate_months(age)
    days = calculate_days(age)
    hours = calculate_hours(days)
    seconds = calculate_seconds(days)
    display_results(months, days, hours, seconds)


main()
