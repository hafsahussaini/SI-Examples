# This program displays high, low, and average scores based on input from
# scores.txt.
# It verifies that the file exists and then uses string functions/methods to
# parse the file content and adds each score to an array.
# It displays the array contents and then calculates and displays the high,
# low, and average score.
# This program include error handling in case the file is formatted
# incorrectly
# It works for any given number of scores in the file.
#
# References:
#
#   https://www.w3schools.com/python/ref_string_isdigit.asp
#   https://kite.com/python/answers/how-to-check-if-a-file-is-empty-in-python
#   https://www.hashbangcode.com/article/stopping-code-execution-python
#   https://stackoverflow.com/questions/4639126/python-handle-missing-files-from-a-sequence


import os.path
from os import path
import sys


def display_results(average, lowest_score, highest_score):
    print(f"The average score is: {average:.2f}")
    print("The lowest score is: " + str(lowest_score))
    print("The highest score is: " + str(highest_score))


def calculate_lowest(scores):
    scores.sort()
    lowest_score = scores[0]
    return lowest_score


def calculate_highest(scores):
    scores.sort(reverse=True)
    highest_score = scores[0]
    return highest_score


def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average


def sum(scores):
    total = 0
    for index in range(len(scores)):
        total += scores[index]
    return total


def read_file(filename):
    try:
        with open(filename, "r") as f:
            scores = []
            for line in f:
                line = line.strip()
                score = line.split(",")
                try:
                    score = float(score[1])
                    scores.append(score)
                except:
                    print("There is a missing score next to '" + line + "'.")
                    continue
        print(scores)
        return scores
    except IOError:
        print("File is missing.")


def check_if_empty(filename):
    filesize = os.path.getsize(filename)
    if filesize == 0:
        print("The file is empty.")
        exit(1)
    else:
        scores = read_file(filename)
        return scores


def main():
    filename = "scores.txt"
    if path.exists(filename) == True:
        scores = check_if_empty(filename)
        highest_score = calculate_highest(scores)
        lowest_score = calculate_lowest(scores)
        average = calculate_average(scores)
        display_results(average, lowest_score, highest_score)
    else:
        print("This file does not exist.")


main()
