# This program  asks the user for a line of text.
# It then uses string functions/methods to delete leading, trailing, and
# duplicate spaces.
# Lastly, it prints the line of text backwards.
#
# Reference:
# http://www.datasciencemadesimple.com/remove-spaces-in-python/
#


def display_backwards(cleaned_text):
    print(cleaned_text[::-1])


def remove_duplicate_spaces(stripped_text):
    import re

    cleaned_text = re.sub(' +', ' ', stripped_text)
    return cleaned_text


def strip_text(text_line):
    stripped_text = text_line.strip()
    return stripped_text


def get_text_line():
    print("Enter a line of text:")
    text_line = str(input())
    return text_line


def main():
    text_line = get_text_line()
    stripped_text = strip_text(text_line)
    cleaned_text = remove_duplicate_spaces(stripped_text)
    display_backwards(cleaned_text)


main()

