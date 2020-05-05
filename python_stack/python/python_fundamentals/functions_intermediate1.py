# Assignment:
# Functions Intermediate I
#
# Objectives:
# Practice using default parameter values,
# Practice passing in named arguments,
# Become familiar with pyhon's random module

# Create a single function randint() that takes up to 2 arguments.
import random


def randInt(min=0, max=100):
    num = random.random() * (max-min) + min
    return round(num)


print("** Random number between 0 to 100 =", randInt())
print("** Random number between 0 to 50 = ", randInt(max=50))
print("** Random number between 50 to 100 = ", randInt(min=50))
print("** Random number between 50 to 500 = ", randInt(min=50, max=500))
print("*** DONE ***")
