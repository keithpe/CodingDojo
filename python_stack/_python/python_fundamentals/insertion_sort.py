# --------------------------------------------------------------------------------------
# Insertion Sort
#
# The outer loop moves from left to right
# The inner loop starts from the position of the outer loop, and continues to the left.
#
# From inside the inner loop, compare the value of the element at inner loop pointer
# to the value of the element to it's left. If the rightmost value is less than the
# leftmost value, swap them. We keep moving lower numbers to the left.
#
# --------------------------------------------------------------------------------------


def insertion_sort(arr):

    # Keep track of how many times we move through loop
    # The outer loop starts from the 2nd position (array position 1) to the end of
    # the array. The inner loop moves from outer loops position, back down to the
    # beginning of array, at position 0

    outer_loop_counter = 0
    inner_loop_counter = 0

    # Outer loop moves from 2nd array position to the last array position.
    for i in range(1, len(arr), 1):

        outer_loop_counter += 1

        # Inner loop moves left, starting from the position of inner loop pointer
        for j in range(i, 0, -1):

            inner_loop_counter += 1

            # If the value at the inner loop position is less than the value in the
            # array position to its left, then swap them, otherwise keep moving left
            # until we get to the beginning of the array.

            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

        # Print the array to see it change as the outer loop progresses
        print('arr', arr)

    print("Outer Loop {} times".format(outer_loop_counter))
    print("Inner Loop {} times".format(inner_loop_counter))


array = [5, 3, 1, 7, 8, 2]
print("Original Array contents: {}".format(array))
insertion_sort(array)
print("Modified Array contents: {}".format(array))
