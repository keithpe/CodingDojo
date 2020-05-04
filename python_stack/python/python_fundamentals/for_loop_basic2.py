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
