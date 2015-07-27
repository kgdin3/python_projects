# Author: Keith Dinning
# Assignment Number: Lab 3
# File Name: bmi_dinning.py
# Course/Section: COSC 1336 Section 002
# Date: 2-2-14
# Instructor: Dr. B. Hohlt

# This program calculates and displays body mass index (BMI)

# main function
def main():
    # Get input
    weight = float(input('What is your weight in pounds?'))
    height = float(input('What is your height in inches? '))

    # Calculate and display body mass index (BMI)
    show_bmi(weight,height)

    input('press enter to continue')
    
# define the show_bmi function.
def show_bmi(weight,height):
    bmi = weight*(703/(height*height))
    print('Your bmi is', \
      format(bmi, '.2f'))
   
# Call the main function
main()

# Tested with values:
# Input used weight = 170
# Input used height = 72
# Output = 23.05
