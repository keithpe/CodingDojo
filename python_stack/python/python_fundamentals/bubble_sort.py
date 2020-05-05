# -----------------------------------------------------------------------------------------------
# Bubble Sort
#
# Not really an assigment, but an intro to sorting. Bubble sort is very easy
# to implement, but not too efficient. You need to iterate through the data/array to many times.
#
# -----------------------------------------------------------------------------------------------


def bubble_sort(arr):

    something_changed = False

    for i in range(0, len(arr)-1, 1):
        if arr[i] > arr[i+1]:
            something_changed = True
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return something_changed


# Original, unsorted array
arr = [8, 1, 5, 3, 2, 0]

# We keep track of how many times we need to run bubble_sort() before the list is sorted.
counter = 0

# Use something_changed boolean variable in the while loop, to determine whether
# the bubble sort function has changed something.
# Continue to call bubble sort function on the array until it no longer makes changes.

print("\n************** Bubble Sort **************\n")
print("Original array is: {}\n".format(arr))

while True:
    counter += 1
    something_changed = False
    something_changed = bubble_sort(arr)
    if something_changed == False:
        break

print("Sorted array is: {}\n".format(arr))
print("We called bubble_sort() {} times.\n".format(counter))

print("****************** DONE *****************\n")


'''
SAMPLE OUTPUT BELOW
************** Bubble Sort **************

Original array is: [8, 1, 5, 3, 2, 0]

Sorted array is: [0, 1, 2, 3, 5, 8]

We called bubble_sort() 6 times.

****************** DONE *****************
'''
