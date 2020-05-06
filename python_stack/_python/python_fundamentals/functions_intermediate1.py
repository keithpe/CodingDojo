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
    if min > max:
        print("min value must be less than max value. Current min={}, Current max={}".format(
            min, max))
        return "*** INVALID ***"
    if min < 0:
        print("min value cannot be less then 0. Current min={}".format(min))
        return "*** INVALID ***"
    num = random.random() * (max-min) + min
    return round(num)


print("**** Testing valid cases ****")
print("** Random number between 0 to 100 =", randInt())
print("** Random number between 0 to 50 = ", randInt(max=50))
print("** Random number between 50 to 100 = ", randInt(min=50))
print("** Random number between 50 to 500 = ", randInt(min=50, max=500))

print("**** Testing Edge Cases ****")
print("** Random number between 1000 to 500 = ", randInt(min=1000, max=500))
print("** Random number between -10 to 500 = ", randInt(min=-10, max=500))
print("*** DONE ***")
