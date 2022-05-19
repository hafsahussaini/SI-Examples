# This program asks the user for the number of hours they work every
# day and how many dollars they earn every hour. It uses the user's
# input to calcuate his or her pay per week, per month, and per year.
# This program is separated into independent functions.


def Calculate_Annual_Gross_Pay(Monthly_Pay):
    
    Annual_Gross_Pay = Monthly_Pay * 12
    print(f"You are paid ${Annual_Gross_Pay:.2f} annually")
    return Annual_Gross_Pay


def Calculate_Monthly_Pay(Weekly_Pay):
    
    Monthly_Pay = Weekly_Pay * 4
    print(f"Your monthly pay is ${Monthly_Pay:.2f}")
    return Monthly_Pay


def Calculate_Weekly_Pay(dollars, hours):
    
    Weekly_Pay = dollars * (5 * hours)
    print(f"Your weekly pay is ${Weekly_Pay:.2f}")
    return Weekly_Pay


def Get_Dollars():
    
    print("How many dollars do you get paid per hour?")
    dollars = float(input())
    return dollars


def Get_Hours():
    
    print("How many hours do you work on a daily basis?")
    hours = float(input())
    return hours


def main():
    
    hours = Get_Hours()
    Dollars = Get_Dollars()
    Weekly_Pay = Calculate_Weekly_Pay(hours, Dollars)
    Monthly_Pay = Calculate_Monthly_Pay(Weekly_Pay)
    Annual_Gross_Pay = Calculate_Annual_Gross_Pay(Monthly_Pay)

main()
