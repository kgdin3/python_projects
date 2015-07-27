# Author: Keith Dinning
# Assignment Number: Lab 8
# File Name: number_analysis_dinning.py
# Course/Section: COSC 1336 Section 002
# Date: 4-13-14
# Instructor: Dr. B. Hohlt

# This program asks the user to enter a series of 20 numbers and stores
# the numbers in a list. The program then displays the lowest and highest
# numbers in the list and the total and average of the numbers.

# Global constant for amount of numbers to be entered by user
MAX = 5

# main function
def main():

    # Describe the program to the user
    print('This program will ask you to enter 5 numbers and will')
    print('display the lowest number, highest number, the sum of the')
    print('numbers, and the average of the numbers.')
    
    # Get a list with numbers stored in it
    numbers = get_values()

    # Analyze the numbers
    do_analysis(numbers)

    input('press enter to continue')
    
# The get_values function gets a series of values from the user and
# stores them in a list. The function returns a reference to the list.
def get_values():
    numbers = []
    for i in range(MAX):
        value = float(input('Enter a number: '))
        numbers.append(value)
    return numbers

# The do_analysis function analyzes the list of numbers and determines
# and displays the highest and lowest number and the sum and average
# of the numbers.
def do_analysis(numbers):
    print('The lowest number is: ' + str(min(numbers)))
    print('The highest number is: ' + str(max(numbers)))
    print('The total of the numbers is: ' + str(sum(numbers)))
    print('The average of the numbers is: ' + str(sum(numbers)/len(numbers)))
    
    
# Call the main function
main()

# Tested with values:
# 3
# 10
# 22
# 76
# 95
