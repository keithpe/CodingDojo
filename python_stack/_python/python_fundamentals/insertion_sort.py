# --------------------------------------------------------------------------------------
# Insertion Sort
#
# The outer loop moves from left to right
# The inner loop starts from the position of the outer loop, and continues to the left
# From inside the inner loop, compare the value of inner loop pointer to the index
# value to it's left. If the rightmost value is less than the leftmost value, swap them
#
# --------------------------------------------------------------------------------------


def insertion_sort(arr):

    # Outer loop moves from 2nd array position to the last array position.
    for i in range(1, len(arr), 1):

        # Inner loop moves left, starting from the position of inner loop pointer
        for j in range(i, 0, -1):

            # If the value at the inner loop position is less than the value in the
            # array position to its left, then swap them, otherwise keep moving left
            # until we get to the beginning of the array.

            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

        # Print the array to see it change as the outer loop progresses
        print('arr', arr)


array = [5, 3, 1, 7, 8, 2]
print("Original Array contents: {}".format(array))
insertion_sort(array)
print("Modified Array contents: {}".format(array))
