# A linear time selection algorithm to find the ith order statistic
# in an array.
# Unlike randomized selection, this following algorithm is deterministic.
import random
from randomized_selection import swap
import numpy as np

def _break_into_chunks(array, length, chunk_size):
    prev = 0
    arrays = []
    for i in range(length):
        if i % 5 == 0 and i != 0:
            new_array = array[prev : i]
            arrays.append(new_array)
            prev = i

    arrays.append(array[prev : ]) # finishes the last elements of the array
    return arrays

def _get_median(array):
    mid = len(array) // 2
    return array[mid]

def _get_medians(array):
    """
    Given an array of sorted arrays of size chunk_size, returns the medians of each array in a list
    """
    medians = [_get_median(arr) for arr in array]
    return medians


def choose_pivot(array, length, chunk_size=5):
    """
    Unlike the choose_pivot() function in randomized selection, this
    will instead return the median of the medians of all the subsections
    of the array.
    """

    # Step 1. Break the array into contiguous chunks of 5 elements each
    chunks = _break_into_chunks(array, length, chunk_size)

    # Step 2. Sort each group
    sorted_chunks = [sorted(chunk) for chunk in chunks]

    # Step 3. Find the medians of each chunk
    medians = _get_medians(sorted_chunks)

    # Step 4. Find the median of medians
    # med_of_medians = _get_median(medians) # A more straightforward way of getting the median
    med_of_medians = deterministic_selection(medians, len(medians), len(medians) // 2) # I'm actually surprised this worked

    return med_of_medians, array.index(med_of_medians)

def partition(array, length):
    """Partitions the array such that all elements less than
    the chosen pivot are to the left and those higher are to the right"""

    pivot, pivot_ind = choose_pivot(array, length)
    swap(array, 0, pivot_ind)

    i = 1

    for j in range(1, len(array)):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1

    swap(array, 0, i - 1)

    return pivot, i - 1

def deterministic_selection(array, length, i):
    if length == 1: return array[0]

    part, part_index = partition(array, length)

    if part_index == i: # We found the ith order statistic, and it's the partition. How lucky! Let's return it.
        return part

    # Else we need to recurse on one of the two sub-arrays.
    if part_index > i: # Recurse on lower half
        left = array[:part_index]
        return deterministic_selection(left, len(left), i)
    else:
        right = array[part_index + 1:]
        return deterministic_selection(right, len(right), i - part_index - 1)


def test_medians():
    test = list(range(1, 100))
    random.shuffle(test)
    print(choose_pivot(test, len(test), 5))

# Testing
def test():
    test1 = [5, 6, 2, 1, 9, 8, 3, 4, 7]
    length = len(test1)
    print(deterministic_selection(test1, length, 0)) # should return 1
    print(deterministic_selection(test1, length, 1)) # should return 2
    print(deterministic_selection(test1, length, 2)) # should return 3
    print(deterministic_selection(test1, length, 3)) # should return 4
    print(deterministic_selection(test1, length, 8)) # should return 4

if __name__ == "__main__":
    #test_medians()
    test()