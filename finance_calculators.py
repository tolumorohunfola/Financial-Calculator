# A program to calculate monthly payments for a house or returns for an investment where the details are provided by the user

import math # importing the math module

# intro and flagging how to exit
print("This is a program to calculate monthly payments for a house or returns for an investment. To terminate the program, please type 'end' when input is requested.")

# checking termination of program with if statement (repeated several times so created as function)
def check_end(input_variable):
    if input_variable == 'end':
        print("The program has been terminated as requested.")
        quit()

#function to request input since it occurs a lot in this program
def request_input(description, type_needed):
    #first request for input with description as what is sent to user
    input_variable = input(description).lower().strip()
    check_end(input_variable)
    # if statement to check which type needed
    if type_needed == "investment or bond":
        # while statement to repeatedly request input until it is valid
        while input_variable != "bond" and input_variable != "investment":
            print("Your input is invalid.")
            input_variable = input(description)
            check_end(input_variable)
    elif type_needed == "positive whole number":
        # while statement to repeatedly request input until it is valid
        while input_variable.isdigit() == False or int(input_variable) < 0:
            print("Your input is invalid. It must be a positive, whole number.")
            input_variable = input(description)
            check_end(input_variable)
    elif type_needed == "interest rate":
        # while statement to repeatedly request input until it is valid
        while input_variable.isdigit() == False or int(input_variable) < 0 or int(input_variable) > 100:
            print("Your input is invalid. It must be a positive, whole number less than 100.")
            input_variable = input(description)
            check_end(input_variable)
    elif type_needed == "simple or compound":
        while input_variable != "simple" and input_variable != "compound":
            print("Your input is invalid.")
            input_variable = input(description)
            check_end(input_variable)

    return input_variable


# Presenting the two types of calculations available to user and requesting their confirmation for which type they would like to do

# * Could try to do this by printing the two options as a table when I refactor to allow for better formatting in any font. **************************************************
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# user_menu_choice being saved as the lowered and stripped version
user_menu_choice = request_input("Enter either 'investment' or 'bond' from the menu above to proceed: ", "investment or bond")
# confirms the user's choice
print(f"Thank you for choosing to see the calculation for your {user_menu_choice}.")

#nested if statement to run the calculations based on inputs
if user_menu_choice == "investment":
    # runs if the user input is investment
    # ask the user to input deposit amount, interest rate (%), number of years of investing planned, preference of simple or compound interest
    deposit_amount = int(request_input("Please type in the amount of money you will be depositing: ", "positive whole number"))
    interest_rate_invest = float(request_input("Please type in the interest rate in percent: ", "interest rate"))
    number_of_years_of_investing = int(request_input("Please type in the number of years you plan to invest for: ", "positive whole number"))
    interest_choice = request_input("Please type your interest preference between simple or compound interest: ", "simple or compound")
    # changing the interest rate input into the interest rate needed for the formula. - dividing it by 100
    interest_rate_invest_decimal = interest_rate_invest / 100

    if interest_choice == "simple":
        # simple interest formula
        total_amount = deposit_amount * (1 + interest_rate_invest_decimal * number_of_years_of_investing)
        print(f"As you have chosen simple interest, the total amount you can expect when you deposit £{deposit_amount} at a {interest_rate_invest}% interest rate for {number_of_years_of_investing} years is approximately £{total_amount:.2f}")
        # used :.2f to ensure the output is in 2 decimal places
    elif interest_choice == "compound":
        # compound interest formula
        total_amount = deposit_amount * math.pow((1 + interest_rate_invest_decimal), number_of_years_of_investing)
        print(f"As you have chosen compound interest, the total amount you can expect when you deposit £{deposit_amount} at a {interest_rate_invest}% interest rate for {number_of_years_of_investing} years is approximately £{total_amount:.2f}")



if user_menu_choice == "bond":
    # if the user input is bond

    # ask the user to input the present value of the house (int), the interest rate in percent, the number of months they plan to take to repay the bond
    house_present_value = int(request_input("Please type in the current value of the house in pounds without commas or spaces: ", "positive whole number"))
    interest_rate_bond_yearly = float(request_input("Please type in the annual interest rate in percent: ", "interest rate"))
    number_of_months_to_repay = int(request_input("Please type in the number of months you plan to take to repay the bond: ", "positive whole number"))

    # adjusting the interest rate to be monthly and dividing by 100
    interest_rate_bond_monthly = interest_rate_bond_yearly / 12 / 100

    # bond repayment formula
    repayment = (interest_rate_bond_monthly * house_present_value) / (1 - (1 + interest_rate_bond_monthly) ** (-number_of_months_to_repay))
    print(f"If the present value of the house is £{house_present_value}, the yearly interest rate is {interest_rate_bond_yearly}% and you plan to take {number_of_months_to_repay} months to repay, you will need to pay £{repayment:.2f} per month on the bond.")



