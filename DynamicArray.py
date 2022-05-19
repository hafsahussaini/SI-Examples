# This program asks the user to enter grade scores by first asking the
# number of scores they will enter (list length). Then it uses a loop to
# request each score and adds them to a dynamic array. Finally,
# it calculates and displays the high, low, and average for the entered scores.
#
# References:
# https://www.youtube.com/watch?v=9c9qhIcB3NA
# https://www.programiz.com/python-programming/methods/list/append
# https://www.programiz.com/python-programming/methods/list/sort


def display_results(average, lowest_score, highest_score):
    print("The average score is: " + str(average))
    print("The lowest score is: " + str(lowest_score))
    print("The highest score is: " + str(highest_score))


def calculate_highest(scores):
    scores.sort(reverse=True)
    highest_score = scores[0]
    return highest_score


def calculate_lowest(scores):
    scores.sort()
    lowest_score = scores[0]
    return lowest_score


def calculate_average(total, num_of_scores):
    average = total / num_of_scores
    return average


def sum(scores):
    total = 0
    for index in range(len(scores)):
        total += scores[index]
    # print("The total is: " + str(total))
    return total


def fixed_array(num_of_scores):
    scores = []
    for i in range(0, num_of_scores):
        print("Enter score " + str(i + 1) + " :")
        score = int(input())
        scores.append(score)

    # print(scores)
    return scores


def get_num_of_scores():
    print("Enter the number of scores that need to be calculated: ")
    num_of_scores = int(input())
    return num_of_scores


def main():
    num_of_scores = get_num_of_scores()
    scores = fixed_array(num_of_scores)
    total = sum(scores)
    average = calculate_average(total, num_of_scores)
    lowest_score = calculate_lowest(scores)
    highest_score = calculate_highest(scores)
    display_results(average, lowest_score, highest_score)


main()
