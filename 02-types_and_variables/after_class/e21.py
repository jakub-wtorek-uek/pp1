# 21.	Write a program that displays the results of three dice rolls and the sum of the dice rolled.
# Apply a random number generator:
# https://docs.python.org/3/library/random.html

from random import randint

n1 = randint(1, 6)
n2 = randint(1, 6)
n3 = randint(1, 6)

rolls_sum = n1 + n2 + n3

print(f"Rolls: {n1} {n2} {n3}\nSum of them: {rolls_sum}")
