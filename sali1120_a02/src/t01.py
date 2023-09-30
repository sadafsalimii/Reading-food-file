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

from Food import Food
from Food_utilities import read_foods, by_origin

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

origin = int(input(f"Enter a origin as an int\n{Food.origins()}: "))

origins = by_origin(foods, origin)

for food in origins:
    print(food, end="\n\n")
