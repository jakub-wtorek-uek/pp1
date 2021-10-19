# 19.	The length of the sides of the triangle is a, b and c.
# Write a program that calculates the area of the triangle using the Heron formula.
# Read the values of the sides of the triangle from the keyboard.
# Using the program, calculate the area of the triangle for the sides 3, 4 and 5.

from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))

print(area)
