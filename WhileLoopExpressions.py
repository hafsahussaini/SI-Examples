# This program uses a loop to make a list of multiplcation expressions for
# the value the user entered. The computer asks the user to enter a value
# along with the number of expressions they want displayed.


def get_number():
    print("Enter a number:")
    number = int(input())
    return number


def get_num_of_times():
    print("Enter the number of multiplication expressions you would" +
          " like to see with this number:")
    num_of_times = float(input())
    return num_of_times


def process_expressions():
    number = get_number()
    num_of_times = get_num_of_times()


def display_results(number, num_of_times):
    n = 1
    while n <= num_of_times:
        print(str(number) + "*" + str(n) + "=" + str(number * n))
        n = n + 1


def main():
    number = get_number()
    num_of_times = get_num_of_times()
    display_results(number, num_of_times)


main()
