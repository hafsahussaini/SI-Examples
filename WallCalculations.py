# This program asks the user for the dimensions (height, width, and length) of
# the room they are going to paint. It also asks for the cost per gallon of
# paint and how many square feet one gallon of paint covers. It then uses the
# input to calculate the total area of the four walls, the number of gallons
# needed to paint them, and the total cost of paint.
# The original program has been split into independent functions.


def calculate_total_cost(num_of_gallons_needed, cost_per_gallon):

    total_cost = (num_of_gallons_needed * cost_per_gallon)
    print(f"The total cost for the paint needed will be ${total_cost:.2f}.")
    return total_cost


def get_cost_per_gallon():

    print("What is the cost per gallon of the paint you will be using?")
    cost_per_gallon = int(input())
    return cost_per_gallon


def calculate_num_of_gallons_needed(total_area, one_gallons_coverage):

    num_of_gallons_needed = int((total_area / one_gallons_coverage) + 0.9999)
    print("You will need " + str(num_of_gallons_needed) +
          " gallons to paint the four walls.")
    return num_of_gallons_needed


def get_one_gallons_coverage():

    print("Enter number of square feet that one gallon will cover:")
    one_gallons_coverage = float(input())
    return one_gallons_coverage


def calculate_total_area(length, width, height):

    total_area = 2 * length * height + 2 * width * height
    print("The total area you will need to cover with paint is " + str(
        total_area) + " square feet.")
    return total_area


def get_height():

    print("Enter the room's height (in feet):")
    height = float(input())
    return height


def get_width():

    print("Enter the width of the room (in feet):")
    width = float(input())
    return width


def get_length():

    print("Enter the length of the room you want to paint (in feet):")
    length = float(input())
    return length


def main():

    length = get_length()
    width = get_width()
    height = get_height()
    total_area = calculate_total_area(length, width, height)
    one_gallons_coverage = get_one_gallons_coverage()
    num_of_gallons_needed = calculate_num_of_gallons_needed(
        total_area, one_gallons_coverage)
    cost_per_gallon = get_cost_per_gallon()
    total_cost = calculate_total_cost(num_of_gallons_needed, cost_per_gallon)

main()
