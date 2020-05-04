"""
Homework Problem # 3.3
Description: Estimating areas
"""

import math

# find the latitude(x) and longitude(y) locations for the following cities
# retrieved from travelmath.com/airport/

# location for Atlanta, GA
atlanta_x, atlanta_y = 33.7488889, -84.3880556

# location from Orlando, FL
orlando_x, orlando_y = 28.5380556, -81.3794444

# location for Savannah, GA
savannah_x, savannah_y = 32.0833333, -81.1

# loaction from Charlotte, NC
charlotte_x, charlotte_y = 35.2269444, -80.8433333

# given average radius for Earth in km
earth_radius = 6371.01

# use distance formula from problem 3.2 to determine distance for all cities
# distance from atlanta to orlando
# note: book uses arccos which is incorrect, switch to acos
atlanta_orlando = earth_radius * math.acos(
    math.sin(math.radians(atlanta_x))
    * math.sin(math.radians(orlando_x))
    + math.cos(math.radians(atlanta_x))
    * math.cos(math.radians(orlando_x))
    * math.cos(math.radians(atlanta_y - orlando_y)))

# distance from orlando savannah
orlando_savannah = earth_radius * math.acos(
    math.sin(math.radians(orlando_x))
    * math.sin(math.radians(savannah_x))
    + math.cos(math.radians(orlando_x))
    * math.cos(math.radians(savannah_x))
    * math.cos(math.radians(orlando_y - savannah_y)))

# distance from savannah to atlanta
# use this side to form the two congruent triangles
savannah_atlanta = earth_radius * math.acos(
    math.sin(math.radians(savannah_x))
    * math.sin(math.radians(atlanta_x))
    + math.cos(math.radians(savannah_x))
    * math.cos(math.radians(atlanta_x))
    * math.cos(math.radians(savannah_y - atlanta_y)))

# distance from atlanta to charlotte
atlanta_charlotte = earth_radius * math.acos(
    math.sin(math.radians(atlanta_x))
    * math.sin(math.radians(charlotte_x))
    + math.cos(math.radians(atlanta_x))
    * math.cos(math.radians(charlotte_x))
    * math.cos(math.radians(atlanta_y - charlotte_y)))

# distance from charlotte to savannah
charlotte_savannah = earth_radius * math.acos(
    math.sin(math.radians(charlotte_x))
    * math.sin(math.radians(savannah_x))
    + math.cos(math.radians(charlotte_x))
    * math.cos(math.radians(savannah_x))
    * math.cos(math.radians(charlotte_y - savannah_y)))

# find the areas of the two triangles using the formula given in 2.14
# area of triangle 1 for atlanta, orlando and savannah
s1 = (atlanta_orlando + orlando_savannah + savannah_atlanta) / 2
area1 = math.sqrt(
    s1 * (s1 - atlanta_orlando)
    * (s1 - orlando_savannah)
    * (s1 - savannah_atlanta))

# area for triangle 2  for atlanta, savnnah, and charlotte
s2 = (savannah_atlanta + atlanta_charlotte + charlotte_savannah) / 2
area2 = math.sqrt(
    s2 * (s2 - savannah_atlanta)
    * (s2 - atlanta_charlotte)
    * (s2 - charlotte_savannah))

# calculate total area by adding area of two triangles
total_area = area1 + area2

print("The estimated enclosed area between Atlanta, Orlando, Savannah \
and Charlotte is", format(total_area, ".2f"), "km")
