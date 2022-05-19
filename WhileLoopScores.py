# This program asks the user to enter grade scores. It begins by asking the
# user how many scores they would like to enter. Then it uses a loop to
# request each score and add it to a total. Finally, it calculates and displays
# the average for the entered scores.


def get_num_of_scores():
    print("Enter the number of scores you will put in:")
    num_of_scores = int(input())
    return num_of_scores


def get_scores(num_of_time):
    print("Enter score " + str(num_of_time) + " :")
    scores = float(input())
    return scores


def process_average(num_of_scores):
    total = 0
    n = 1
    while n <= num_of_scores:
        score = get_scores(n)
        total = total + score
        n = n + 1
    average = total / num_of_scores
    return average


def display_results(num_of_scores, average):
    print("The average of " + str(num_of_scores) + " scores from what you " +
          "entered is: " + str(average))


def main():
    num_of_scores = get_num_of_scores()
    average = process_average(num_of_scores)
    display_results(num_of_scores, average)


main()
