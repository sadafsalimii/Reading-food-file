"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Asma Salimi
ID:      200831120
Email:   sali1120@mylaurier.ca
__updated__ = "2022-09-26"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name=input("Enter name of food:")
    origin=int(input(f"Enter origin of food{Food.origins()}:"))
    is_vegetarian=input("Is it vegetarian (Y/N):")
    calories=input("Enter number of calories: ")
    if is_vegetarian=="Y":
        food=name,origin,True,calories
    else:
        food=name,origin,False,calories
    #why does that not use Food()
    # OR you could 
    #z=True/false
    #food=Food(name,origin,z,calories)
    
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    #take line and split 
    line=line.split("|")
    if line[2]=="True":
        food=Food(line[0],int(line[1]),True,int(line[3]))
    else:
        food=Food(line[0],int(line[1]),False,int(line[3]))
    #or again can do z=true and then this line after
    return food

#5
def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    
    line = file_variable.readline()
    while line != "":
        f=read_food(line)
        foods.append(f)
        line = file_variable.readline()
    
    return foods

#6
def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for food in foods:
        write_line = f"{food.name}|{food.origin}|{food.is_vegetarian}|{food.calories}\n"
        file_variable.write(write_line)
    return

#7
def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    
    veggies = []
    for food in foods:
        if food.is_vegetarian:
            veggies.append(food)
    return veggies

def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = []
    for food in foods:
        if food.origin == origin:
            origins.append(food)
    return origins

def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total=0
    
    total = 0
    avg = 0
    for food in foods:
        total += food.calories
        avg += 1
    avg = int(total / avg)
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    
    origins = by_origin(foods, origin)
    avg = average_calories(origins)

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    TITLE = ["Food",  "Origin",  "Vegetarian",  "Calories"]
    print(f"{TITLE[0]:<35} {TITLE[1]:<12} {TITLE[2]:<10} {TITLE[3]:<8}")
    print("----------------------------------- ------------ ---------- --------")
    for food in sorted(foods):
        print(
            f"{food.name:<35} {Food.ORIGIN[food.origin]:<12} {food.is_vegetarian!s:>10} {food.calories:>8}"
        )

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result = []
    for food in foods:
        if (food.origin == origin or origin == -1):
            if (food.calories <= max_cals or max_cals == 0):
                if (is_veg == False or food.is_vegetarian == True):
                    result.append(food)

    return result
