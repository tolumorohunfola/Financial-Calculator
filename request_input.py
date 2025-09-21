from check_end import * # importing all variables and functions from the check end file


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
        while input_variable.isalpha() == True or float(input_variable) < 0 or float(input_variable) > 100:
            print("Your input is invalid. It must be a positive number less than 100.")
            input_variable = input(description)
            check_end(input_variable)
    elif type_needed == "simple or compound":
        while input_variable != "simple" and input_variable != "compound":
            print("Your input is invalid.")
            input_variable = input(description)
            check_end(input_variable)

    return input_variable