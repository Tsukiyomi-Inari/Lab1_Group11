#
#   @Authors:  Katherine Bellman & Robert Savoie
#   @Date: September 28th 2021
#
#   @Project Name: Credit Card Number Validator
#   @Project Description:   A program that validates credit card numbers with Luhn Algorithm
#

from os import system
from colorama import Fore

system("title Lab 1 - Robert & Katherine")

# Functions
def card_validator(card_number):
    # Creates a list of numbers from input
    def card_digits(input):
        return [int(digits) for digits in str(input)]
    numbers = card_digits(card_number)
    # Puts odd and even numbers in their own variables
    odd_numbers = numbers[-1::-2]
    even_numbers = numbers[-2::-2]
    # Creates a total using the sum of odd numbers and the sum of even numbers * 2
    # and returns the remainder of that total divided by 10
    total = 0
    total += sum(odd_numbers)
    for digits in even_numbers:
        total += sum(card_digits(digits*2))
    return total % 10

def create_banner():
    banner = "==========================\n" + "= Card Number Validation =\n" + "==========================\n"
    return banner

def validate_input(input):
    MAX_LEN = 16
    # Checks if input is blank
    if input != "":
        # Checks if input is numeric
        if input.isnumeric():
            # Checks if input is above MAX_LEN
            if len(input) <= MAX_LEN:
                # Checks is card_validator returns a non-zero value
                if card_validator(input) == 0:
                    valid = "a valid"
                    return valid
                else:
                    valid = "not a valid"
                    return valid
            else:
                error = "Error - Card number can't be more than 16 digits.\n"
                return error
        else:
            error = "Error - Card number must be numeric.\n"
            return error    
    else:
        error = "Error - Please enter a card number.\n"
        return error
# End of Functions


# Main code block

# Repeatable program loop
repeat = True
while repeat:
    system("cls")
    print(create_banner())

    # If input is non-numeric, blank, or over 16 digits requests input again.
    output_message = ""
    while output_message != "a valid" and output_message != "not a valid":
        card_number = input("Please input a card number: ").strip()
        output_message = validate_input(card_number)
        if output_message != "a valid" and output_message != "not a valid":
            print(output_message)
            system("pause")
            system("cls")
            print(create_banner())

    # Clears system and outputs message based on entered card number
    system("cls")
    print(create_banner())
    print(f"Entered Card Number: {card_number}\n")
    print(f"{card_number} is {output_message} card number.")

    repeat = input("\nPress [y] to repeat: ") == "y"
# End of main code block