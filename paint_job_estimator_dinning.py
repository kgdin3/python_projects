# Author: Keith Dinning
# Assignment Number: Lab 3
# File Name: paint_job_estimator_dinning.py
# Course/Section: COSC 1336 Section 002
# Date: 2-2-14
# Instructor: Dr. B. Hohlt

# This program determines and displays the cost and amount
# of paint neeeded and the hours of labor required and
# calculates the total cost of the paint job

# main function
def main():
    # get input
    wall_space = float(input('How many square feet of wall space need painted?'))
    paint_price = float(input('What is the price of paint per gallon?'))

    # calculate gallons of paint needed
    gallons = (wall_space/115)
    print('The number of gallons of paint needed is', \
          format(gallons, '.2f'))
    
    # calculate labor hours needed
    labor = ((wall_space/115)*8)
    print('The hours of labor required is', \
          format(labor, '.2f'))
    
    # calculate total cost of paint
    total_paint_cost = (gallons*paint_price)
    print('The total cost of the paint required is', \
          format(total_paint_cost, '.2f'), 'dollars')

    # calculate labor cost
    labor_cost = (labor*20)
    print('The total cost of labor is', \
          format(labor_cost, '.2f'), 'dollars')

    # calculate the total cost estimate
    show_cost_estimate(total_paint_cost,labor_cost)

    input('press enter to continue')

# define the show_cost_estimate function
def show_cost_estimate(total_paint_cost,labor_cost):
    total = (total_paint_cost + labor_cost)
    print('The total cost of the paint job is', \
          format(total, '.2f'), 'dollars')

# call the main function
main()

# Tested with values:
# 1000
# 20
# Outputs:
# 8.70
# 69.57
# 173.91
# 1391.30
# 1565.22
      
