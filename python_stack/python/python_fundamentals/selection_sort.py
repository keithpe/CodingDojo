# ---------------------------------------------------------------------------------------
# Selection Sort
#
# ---------------------------------------------------------------------------------------


def selection_sort(arr):

    # Track how many times we loop through the array.
    counter = 0

    # Track the minimum value and its index location
    # throgh each loop we'll swap minimum with index of outer loop index.
    # minimum_value = arr[0]
    # minimum_index = 0

    for i in range(0, len(arr)-1, 1):
        minimum_value = arr[i]
        minimum_index = i
        counter += 1
        for j in range(i, len(arr), 1):
            if arr[j] < minimum_value:
                minimum_value = arr[j]
                minimum_index = j

        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]

    return counter


print('\n***************************** Selection Sort *******************************\n')
array = [3, 5, 1, 2, 3, 4, 7, 3]
print('   Original array: {}\n'.format(array))
counter = selection_sort(array)
print('   Modified array: {}\n'.format(array))
print('   The selection_sort() function traversed the array {} times'.format(counter))
print('\n****************************************************************************\n')


'''
SAMPLE OUTPUT 
***************************** Selection Sort *******************************

   Original array: [3, 5, 1, 2, 3, 4, 7, 3]

   Modified array: [1, 2, 3, 3, 3, 4, 5, 7]

   The selection_sort() function traversed the array 7 times

****************************************************************************
'''
