# This program uses a for loop to make a list of multiplcation expressions
# for the value the user entered. The computer asks the user to enter a
# value along with the number of expressions they want displayed.


def get_number():
    print("Enter a number:")
    number = int(input())
    return number


def get_num_of_times():
    print("Enter the number of multiplication expressions you would" +
          " like to see with this number:")
    num_of_times = int(input())
    return num_of_times


def for_loop(number, num_of_times):
    for n in range(1, num_of_times+1):
        print(f"{number} * {n} = {number * n}")
    print("\nEnd of for loop.")


def main():
    number = get_number()
    num_of_times = get_num_of_times()
    for_loop(number, num_of_times)


main()
