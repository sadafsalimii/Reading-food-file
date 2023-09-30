"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Asma Salimi
ID:      200831120
Email:   sali1120@mylaurier.ca
__updated__ = "2022-09-26"
-------------------------------------------------------
"""
# Imports

# Constants

from Food_utilities import read_foods, average_calories

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

avg = average_calories(foods)

print(f"Average Calories: {avg}")
