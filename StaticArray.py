# This program uses a static array or fixed-size array that continues to accept
# scores until the user enters a negative value. Once a negative number is
# entered, an array of previously entered scores will be displayed.


def display_array(scores):
    print(str(scores))


def display_scores_array(num_of_scores):
    scores = [None] * num_of_scores
    for index in range(0, num_of_scores):
        print("Enter score " + str(index + 1) + " :")
        score = int(input())
        if score >= 0:
            scores[index] = score
        if score < 0:
            break
    return scores


def get_num_of_scores():
    print("How many scores would you like to enter?")
    num_of_scores = int(input())
    return num_of_scores


def main():
    num_of_scores = get_num_of_scores()
    scores = display_scores_array(num_of_scores)
    display_array(scores)


main()
