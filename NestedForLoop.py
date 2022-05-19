# This program creates a multiplication table with nested loops and limits the
# factors based on user input values.
#
# References:
# https://www.youtube.com/watch?v=0rWHH5JfKdo
# https://www.youtube.com/watch?v=Dpkfh-hX4-M
# https://stackoverflow.com/questions/27312273/python-meaning-of-end-in-the-
# statement-print-t-end/27312325


def nested_loop(start, end):
    print('', end='\t')
    for i in range(start, end + 1):
        print(i, end='\t')
    print('')

    for i in range(start, end + 1):
        print(i, end='\t')
        for j in range(start, end + 1):
            print(i * j, end='\t')
        print('')


def get_value(label):
    print("Enter " + label + " value:")
    value = int(input())
    return value


def main():
    start = get_value("starting")
    end = get_value("ending")
    nested_loop(start, end)


main()
