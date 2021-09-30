#
#   @Authors:  Katherine Bellman & Robert Savoie
#   @Date: September 28th 2021
#
#   @Project Name: Credit Card Number Validator
#   @Project Description:   A program that validates credit card numbers with Luhn Algorithm
#
from os import system

import colorama

card_number = []
check_digit = ""
DIVIDE_BY = 10
GREATER_THAN = 9
MAX_DIGITS = 16

def stringToList(input):
    """
    Takes a string, trims any white space then
    for each digit, is then appended into the empty list
    "check digit"
    :rtype: string
    :return:
        a list of numeric items
    """

    # loop through each digit assigning them to individual index's
    for count in input:
        card_number.append(count)

def validInputCheck():
    """
    takes input and will only allow
    program to continue with valid input
     it checks for:
     1. Null entry
     2. Non numeric characters
     3. Length exceeding 16

     if invalid, error message will be printed to
     the console and user will be promped again
    :return:
    True when valid
    False when in-valid
    """
    if input == " " :
        print(colorama.Fore.RED + "\nError: input can not be empty\n" + colorama.Fore.RESET)
        system("cls")
        return False

    elif input.isalpha() == True or input.isnumeric() == False:
        print(colorama.Fore.RED + f"\nError: input must consist of only numbers\n" + colorama.Fore.RESET)
        system("cls")
        return False

    elif (len(input) > MAX_DIGITS):
        print(colorama.Fore.RED + f"\nError: input can not be more then {MAX_DIGITS}\n" + colorama.Fore.RESET)
        system("cls")
        return False

    else:
        return True


system("cls")
system("Lab 1: Credit Card Validator - Group 11")
# accept card number as string with/out spaces  from user
input = input("Please enter a credit card number:").strip()

validInputCheck(input)

stringToList(input)

# remove rightmost digit(checking digit) from input number, excluding it from calculations
check_digit = card_number[-1]
del card_number[-1]
print(card_number)
# Reverse the order of remaining input
card_number.reverse()

# double every value at even intervals, if any result is greater than 9, subtract 9 from it(the doubled value)
even_element = []
for index, number in card_number:
    even_element = index[number] 

# Add together all the results (values) and re-add checking digit


# If divisible by 10, it is valid. Where it can not be divided by 10, the card number is invalid

# Test card numbers:
# mastercard             5105105105105100
# Union pay              6200000000000005
# FAKE                   4242424242424241
# mastercard(2 series)   2223003122003222
