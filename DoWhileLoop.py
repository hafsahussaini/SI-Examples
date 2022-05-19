# This program uses a do loop to make a list of multiplcation expressions for
# the value the user entered.There is an input validation section that checks
# that the user enters a positive number. If they enter a negative number, it
# displays an error message asking them to try again and enter a positive
# number. If the value is entered as a positive value, the program then
# displays the output according to the input.


def do_loop():
    get_number()
    get_num_of_times(number, n, num_of_times)
    while True:
        print(str(number) + "*" + str(n) + "=" + str(number * n))
        n = n + 1
        if not(n <= num_of_times):
            break


def get_number():
    print("Enter a number: ")
    number = int(input())
    while number <= 0:
        print("You must enter a positive number, try again:")
        number = int(input())
    return number


def get_num_of_times(number, n):
    print("Enter the number of expressions you would like displayed:")
    num_of_times = float(input())
    if num_of_times <= 0:
        print("Please enter a positive number:")
        num_of_times = float(input())
    while True:
        print(str(number) + "*" + str(n) + "=" + str(number * n))
        n = n + 1
        if not(n <= num_of_times):
            break
    return num_of_times


def main():
    number = get_number()
    n = 1
    num_of_times = get_num_of_times(number, n)


main()
