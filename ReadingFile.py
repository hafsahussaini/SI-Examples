# This program displays high, low, and average scores based on input
# from scores.txt.
# It verifies that the file exists and then uses string functions/methods to
# parse the file content and adds each score to an array.
# It displays the array contents and then calculates and displays the high,
# low, and average score.
# It formats the average to two decimal places.
# It works for any given number of scores in the file.
# References:
#
#   https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in
#       -python/
#   https://www.guru99.com/python-check-if-file-exists.html
#   https://www.youtube.com/watch?v=Uh2ebFW8OYM
#   https://www.youtube.com/watch?v=4mX0uPQFLDU


import os.path
from os import path


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
    with open(filename, 'r') as f:
        scores = []
        for line in f:
            line = line.strip()
            score = line.split(",")
            print(score)
            try:
                score = float(score[1])
                scores.append(score)
            except:
                continue
    return scores


def main():
    filename = "scores.txt"
    if path.exists(filename) == True:
        scores = read_file(filename)
        highest_score = calculate_highest(scores)
        lowest_score = calculate_lowest(scores)
        average = calculate_average(scores)
        display_results(average, lowest_score, highest_score)
    else:
        print("This file does not exist.")


main()
