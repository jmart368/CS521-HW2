"""
Homework Problem # 2.5
Description: Calculating tips
"""

# prompt the user to enter the subtotal and gratuity
# use the split to insert a ',' as a delimiter
subtotal, gratuity = input("Enter the subtotal, gratuity: ")

# convert the subtotal and gratuity into floats to allow use of decimals
subtotal = float(subtotal)
gratuity = float(gratuity)

# create a formula calculating the total and gratuity in percent format
total = subtotal + (gratuity/100)

# use the format conversion on the total indicating to expand the decimal
print("The gratuity is", gratuity, "and the total is", format(total, ".2f"))
