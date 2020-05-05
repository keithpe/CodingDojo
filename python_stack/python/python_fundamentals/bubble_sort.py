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


arr = [8, 1, 5, 3, 2, 0]

print(arr)

# Use something_changed boolean variable to determine whether the bubble sort function
# has changed something. Continue to call bubble sort function on the array until
# it no longer makes changes.
while True:
    something_changed = False
    something_changed = bubble_sort(arr)
    if something_changed == False:
        break

print(arr)
