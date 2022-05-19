# This program uses a built-in sort function to sort the grade scores from the
# previous scores activity and displays the scores array in order from highest
# to lowest score.
#
# Reference:
# https://www.programiz.com/python-programming/methods/built-in/sorted


def display_results(scores):
    print("The scores in order from highest to lowest: " +
          str(sorted(scores, reverse=True)))


def static_array(num_of_scores):
    scores = [None] * num_of_scores
    for index in range(0, num_of_scores):
        print("Enter score " + str(index + 1) + " :")
        score = int(input())
        scores[index] = score

    return scores


def get_num_of_scores():
    print("Enter the number of scores that need to be calculated: ")
    num_of_scores = int(input())
    return num_of_scores


def main():
    num_of_scores = get_num_of_scores()
    scores = static_array(num_of_scores)
    display_results(scores)


main()
