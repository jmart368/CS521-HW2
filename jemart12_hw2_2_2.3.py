"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: 1 February 2020
Homework Problem # 2.3
Description: Converting feet into meters
"""

# prompt use to eneter meters
feet = float(input("Enter value for feet : "))

# set a formula for feet into meters
meters = feet * 0.305

# format meters to four decimal places
print(feet, "feet is", format(meters, ".4f"), "meters")
