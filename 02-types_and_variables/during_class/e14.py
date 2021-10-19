# 14.	The radius of the circle has the value 5.
# Write a program that calculates the area and circumference of the circle. Use the algorithm below.

#####
# Calculation of the area and circumference of a circle
##

# determine radius and PI
from math import pi as PI
radius = 5

# calculate area
area = PI * radius ** 2

# calculate circumference
circumference = 2 * PI * radius

# display results
print(f"Area: {round(area, 2)}\nCircumference: {round(circumference, 2)}")
