# ---------------------------------------------------------------------------------------
# Assigment: Underscore
#
# Objectives:
#
# Understand callbacks
# Practice anonymous functions
# Create a custom Python module
#
# To create a custom Python module, you will simply define several functions,
# or methods, into a single class!
#
# We'll talk about classes soon--for now you can use the code below and follow the
# pattern for calling the methods as shown below.
#
# ---------------------------------------------------------------------------------------


class Underscore:
    def map(self, iterable, callback):

        # should return [2,4,6]
        # _.map([1, 2, 3], lambda x: x*2)

        newArray = []

        for i in range(0, len(iterable), 1):
            newArray.append(callback(iterable[i]))

        return newArray

    def find(self, iterable, callback):

        # should return the first value that is greater than 4
        # _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)

        for i in range(0, len(iterable), 1):
            if callback(iterable[i]):
                found = iterable[i]
                break

        return found

    def filter(self, iterable, callback):
        # should return [2,4,6]
        # _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

        newArray = []

        for i in range(0, len(iterable), 1):
            if callback(iterable[i]):
                newArray.append(iterable[i])

        return newArray

    def reject(self, iterable, callback):
        #  should return [1,3,5]
        # _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

        newArray = []

        for i in range(0, len(iterable), 1):
            if not callback(iterable[i]):
                newArray.append(iterable[i])

        return newArray


# -----------------------------------------------
# Create an instance of our underscore class
# -----------------------------------------------

_ = Underscore()  # yes we are setting our instance to a variable that is an underscore


print('\n*********************** The Underscore Class ***************************\n')
print(' Create an underscore class and define four methods for it.')
print(' This app implements those four methods: filter, map, find and reject\n')
print(' .filter: Filters the array. In this case it returns all the even')
print('          elements from the origin array.\n')
print('    .map: Maps each element in the array to a element in the new')
print('          array. In this case it maps each value to its double.\n')
print('   .find: Finds elements in the original array and returns them')
print('          in a new array. In this case it returns first value > 4\n')
print(' .reject: Selects elements from the original array that do NOT meet a')
print('          certain requirement. In this case it rejects all odd numbers')
print('          and returns them in a new array.')
print('\n*************************** .filter *************************************\n')

# should return [2,4,6]
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(' evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)')
print(' evens = {}'.format(evens))

print('\n**************************** .map ***************************************\n')

# should return [2,4,6]
doubles = _.map([1, 2, 3], lambda x: x*2)
print(' doubles = _.map([1, 2, 3], lambda x: x*2)')
print(' doubles = {}'.format(doubles))

print('\n*************************** .find ***************************************\n')

# should return the first value that is greater than 4
found = _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)
print(' found = _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)')
print(' found = {}'.format(found))

print('\n************************** .reject **************************************\n')
#  should return [1,3,5]
rejects = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(' rejects = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)')
print(' rejects = {}'.format(rejects))

print('\n**************************** DONE ***************************************\n')

# -----------------------------------------------------------------------------------------
# Tests for the four underscore functions
# -----------------------------------------------------------------------------------------

# should return [2,4,6]
# _.map([1, 2, 3], lambda x: x*2)

# should return the first value that is greater than 4
# _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)

# should return [2,4,6]
# _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

#  should return [1,3,5]
# _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
