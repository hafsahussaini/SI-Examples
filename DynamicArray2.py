# This program asks the user to enter grade scores and puts the inputted scores
# into an array. Then it displays the array in order from the highest score to
# the lowest score with a built-in sort function which sorts the grade scores.
#
# Reference:
# https://www.programiz.com/python-programming/methods/list/sort


def display_order(scores):
    scores.sort(reverse=True)
    print("The scores in order of highest to lowest score: " + str(scores))
    return scores


def display_scores_array(num_of_scores):
    scores = []
    for index in range(0, num_of_scores):
        print("Enter score " + str(index + 1) + " :")
        score = int(input())
        scores.append(score)
    return scores


def get_num_of_scores():
    print("How many scores would you like to enter?")
    num_of_scores = int(input())
    return num_of_scores


def main():
    num_of_scores = get_num_of_scores()
    scores = display_scores_array(num_of_scores)
    scores = display_order(scores)


main()
