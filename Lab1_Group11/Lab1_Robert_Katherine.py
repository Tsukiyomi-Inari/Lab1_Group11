#
#   @Authors:  Katherine Bellman & Robert Savoie
#   @Date: September 28th 2021
#
#   @Project Name: Credit Card Number Validator
#   @Project Description:   A program that validates credit card numbers with Luhn Algorithm
#
from os import system
import math

card_number = []
check_digit = ""
DIVIDE_BY = 10
GREATER_THAN = 9

system("cls")
system("Lab 1: Credit Card Validator - Group 11")


# accept card number as string with/out spaces  from user
input = input("Please enter a credit card number:")
  

for count in input:
    card_number.append(count)

# remove rightmost digit(checking digit) from input number, excluding it from calculations
check_digit = card_number[-1]
del card_number[-1]

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
