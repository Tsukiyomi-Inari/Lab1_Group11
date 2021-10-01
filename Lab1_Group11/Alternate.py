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
    def card_digits(input):
        return [int(digits) for digits in str(input)]
    numbers = card_digits(card_number)
    odd_numbers = numbers[-1::-2]
    even_numbers = numbers[-2::-2]
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
    if input != "":
        if input.isnumeric():
            if len(input) <= MAX_LEN:
                if card_validator(input) == 0:
                    valid = "Entered card number is valid."
                    return valid
                else:
                    valid = "Entered card number is not valid."
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
repeat = True
while repeat:
    system("cls")
    print(create_banner())

    output_message = ""
    while output_message != "Entered card number is valid." and output_message != "Entered card number is not valid.":
        card_number = input("Please input a card number: ").strip()
        output_message = validate_input(card_number)
        if output_message != "Entered card number is valid." and output_message != "Entered card number is not valid.":
            print(output_message)

    print(output_message)

    repeat = input("\nPress [y] to repeat: ") == "y"
# End of main code block