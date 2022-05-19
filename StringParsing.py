# This program asks the user for a single line of text containing a first name
# and last name. It then uses string functions/methods to parse the line and
# print out the name in the form last name, first initial, such as Lastname, F.
# It includes a trailing period after the first initial and
# handles invalid input errors, such as extra spaces or missing name parts.

# References:
#
# https://www.w3schools.com/python/ref_string_split.asp
# https://www.journaldev.com/23625/python-trim-string-rstrip-lstrip-strip
# https://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string


def display_name(last, first):
    print(last + ", " + first[0] + ".")


def first_name(array):
    first = array[0]
    return first


def last_name(array):
    last = array[1]
    return last


def name_array(capitalized_name):
    array = capitalized_name.split()
    length = len(array)
    if(length != 2):
        print("Only enter your first and last name. Try again.")
        main()
    else:
        return array


def get_name():
    print("Enter your first and last name in the format 'Firstname Lastname':")
    name = str(input())
    capitalized_name = name.title()
    return capitalized_name


def main():
    capitalized_name = get_name()
    array = name_array(capitalized_name)
    last = last_name(array)
    first = first_name(array)
    display_name(last, first)


main()
