# Assignment: For Loop Basic II

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Biggie Size
#
# Given a list, write a function that changes all positive numbers in the list to "big".
#
# Example: biggie_size([-1,3,5,-5])  returns that same list, but whose values are now [-1, "big", "big", 05]
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def biggie_size(myList):
    for i in range(0, len(myList), 1):
        if myList[i] > 0:
            myList[i] = "big"
    return myList


print("**** biggie_size() ****")
myList = [-1, 3, 5, -5]
myList = biggie_size(myList)
print("myList=", myList)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# count_positives
#
# Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that
# zero is not considered to be a positive number).
#
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it.
# Example: count_positives([1,6,-4,-2,-7,-2]) changes thte list to [1,6,-4,-2,-7,2]
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def count_positives(myList):
    positives = 0
    for i in range(0, len(myList), 1):
        if myList[i] > 0:
            positives += 1

    myList[len(myList)-1] = positives
    return myList


print("**** count_positives ****")

myList = [1, 6, -4, -2, -7, -2]
print('Before:', myList)
myList = count_positives(myList)
print('After', myList)

myList = [-1, 1, 1, 1]
print('Before:', myList)
myList = count_positives(myList)
print('After', myList)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# sum_total
#
# Create a function that takes a list and returns the sum of all the values in the array.
#
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def sum_total(myList):
    sum = 0
    for i in range(0, len(myList), 1):
        sum += myList[i]

    return sum


print("**** sum_total ****")
myList = [1, 2, 3, 4]
print("myList=", myList, " sum=", sum_total(myList))

myList = [6, 3, -2]
print("myList=", myList, " sum=", sum_total(myList))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Average
#
# Create a function that takes a list and returns the average of all the values.
#
# Example: average([1,2,3,4]) should return 2.5
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def average(myList):
    sum = 0
    for i in range(0, len(myList), 1):
        sum += myList[i]
    return (sum / len(myList))


print("**** average ****")

myList = [1, 2, 3, 4]
print("myList=", myList)
print("sum=", average(myList))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Length
#
# Create a function that takes a list and returns the length of the list.
#
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def length(myList):
    return len(myList)


print("**** length() ****")
myList = [37, 2, 1, -9]
print("The length of {} is {}".format(myList, len(myList)))

myList = []
print("The length of {} is {}".format(myList, len(myList)))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Minimum
#
# Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty
# have the function return False
#
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def minimum(myList):
    if len(myList) == 0:
        return False

    minimum = myList[0]
    for i in range(0, len(myList), 1):
        if minimum > myList[i]:
            minimum = myList[i]

    return minimum


print("**** minimum ****")
myList = [37, 2, 1, -9]
print("The minimum value in the list {} is {}".format(myList, minimum(myList)))

myList = []
print("The minimum value in the list {} is {}".format(myList, minimum(myList)))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# maximum
#
# Create a function that takes a list and returns the maximum value in the array. If the list is empty have the
# function return False.
#
# Example: maximum([37,2,-9]) should return 37
# Example: maximum([]) should return False
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def maximum(myList):
    if len(myList) == 0:
        return False

    maximum = myList[0]
    for i in range(0, len(myList), 1):
        if maximum < myList[i]:
            maximum = myList[i]

    return maximum


print("**** maximum ****")
myList = [37, 2, 1, -9]
print("The maximum value in the list {} is {}".format(myList, maximum(myList)))

myList = []
print("The maximum value in the list {} is {}".format(myList, maximum(myList)))
