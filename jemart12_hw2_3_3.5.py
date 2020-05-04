"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: 1 February 2020
Homework Problem # 3.5
Description: Area of rectangular polygon
"""

import math

# prompt the user to enter the number of sides as an interger
number_of_sides = int(input("Enter the number of sides: "))

# prompt the user to enter the length of sides as a float
length_of_sides = float(input("Enter the length of sides: "))

# establish the formula for the area of the polygon
area_of_polygon = (number_of_sides * length_of_sides ** 2) / (
    4 * math.tan(math.pi / number_of_sides))

# format your ouput to two decimal places
print("The area of the polygon is", format(area_of_polygon, ".2f"))
