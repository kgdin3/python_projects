# Author: Keith Dinning
# Assignment Number: Lab 2
# File Name: celsius_to_fahrenheit_dinning.py
# Course/Section: COSC 1336 Section 002
# Date: 1-26-14
# Instructor: Dr. B. Hohlt

# This program converts Celsius temperatures to Fahrenheit temperatures
# and displays the result

# Ask user to enter temperature in Celsius (C)
C = float(input('What is the temperature in Celsius?'))

# Convert Celsius temperature to Fahrenheit temperature (F)
F = (9/5)*C + 32

# Display temperature in Fahrenheit
print('The temperature in Fahrenheit is', \
      format(F, '.1f'), "degrees")

# Tested with values:     
# Input used temperature in Celsius = 100
# Output = 212.0 

input('press enter to continue')


