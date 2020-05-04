"""
Homework Problem # 3.1
Description: Area of a pentagon
"""

import math

# prompt the use to enter the radius
radius = input("Enter the length from the center to a vertex: ")

# format the radius into float
radius = float(radius)

# create a formula for the side using the math function
side = 2 * radius * math.sin(math.pi/5)

# create a formula for the area using the math function
area = (3 * math.sqrt(3)/2) * side**2

print("The area of the pentagon is", format(area, ".2f"))
