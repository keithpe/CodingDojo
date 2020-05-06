# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Countdown
#
# Create a function that accepts a number as an input. Reurn a new list that counts down by one from the number
# as the 0th element, down to 0, as the last element).
#
# Example: countdown(5), should return [5,4,3,2,1,0]
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def countdown(num):
    list = []
    for i in range(num, 0-1, -1):
        list.append(i)
    return list


print("**** countdown() ****")

mylist = countdown(5)
print(mylist)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Print and Return
#
# Create a function that will receive a list with two numbers. Print the first value and return the second.
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def printAndReturn(num1, num2):
    print('num1 inside the function', num1)
    return(num2)


print("**** printAndReturn() ****")

myNum = printAndReturn(5, 3)
print('myNum', myNum)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# First Plus Length
#
# Create a function that accepts a list and returns the sum of the first value in th elist plus the lists length
#
# Example: first_plus_length
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def first_plus_length(list):
    return list[0] + len(list)


print("**** first_plus_length ****")

myList = [0, 1, 2, 3, 4, 5]
sum = first_plus_length(myList)
print('myList is:', myList, 'sum is:', sum)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Values Greater than Second
#
# Write a function that accepts a list and creates a new list containing only the values from the original list
# that are greater than it's 2nd value. Print how many values this is and then return the new list. If the list
# has less than 2 elements, have the function return false.
#
# Example: values_greater_than_second([5,2,3,2,1,4]), should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return false.
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def values_greater_than_second(myList):

    if len(myList) < 2:
        return False

    secondValue = myList[1]
    newList = []

    for i in range(0, len(myList), 1):
        if myList[i] > secondValue:
            newList.append(myList[i])
    return newList


print("**** values_greater_than_second() ****")

myList = [5, 2, 3, 2, 1, 4]
newList = values_greater_than_second(myList)
print('newList is:', newList)

myList = [3]
newList = values_greater_than_second(myList)
print('newList is:', newList)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# This length, That value
#
# Write a function that accepts two integers as parameters: size and value. The function should create and return
# a list whose length is equal to the given size, and whose values are all the given value.
#
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def length_and_value(size, value):
    newList = []
    for i in range(0, size, 1):
        newList.append(value)

    return newList


size = 4
value = 7
print("**** length_and_value() ****")
myList = length_and_value(size, value)
print('size=', size, 'value=', value)
print('myList=', myList)

size = 6
value = 2
myList = length_and_value(size, value)
print('size=', size, 'value=', value)
print('myList=', myList)
