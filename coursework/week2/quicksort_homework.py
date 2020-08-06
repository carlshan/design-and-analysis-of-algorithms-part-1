import sys
import numpy as np
sys.setrecursionlimit(10000)

input_data = list(map(int, open('./inputs/QuickSort.txt').readlines()))

def choose_pivot1(array, index):
    return array[index]

def choose_pivot2(array, index):
    return array[index - 1]

def choose_pivot3(array, low, high):
    first = array[low]
    last = array[high - 1]
    mid = (high - low) // 2
    middle = array[mid]

    median = np.median([first, middle, last])

    if median == middle:
        return middle, mid
    elif median == first:
        return first, low
    else:
        return last, high - 1


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array, low, high):
    # pivot = choose_pivot1(array, low)
    # pivot = choose_pivot2(array, high)
    # swap(array, high - 1, low)

    pivot, pivot_ind = choose_pivot3(array, low, high)
    swap(array, low, pivot_ind)

    i = low + 1

    for j in range(low + 1, high):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1

    # Option 1: Swapping with first elemnt
    swap(array, low, i - 1) # change this when changing where the pivot is not the first element

    return i - 1

total = 0
def quicksort(array, low, high):
    global total

    if high == low: return array

    total += (high - low) - 1

    part = partition(array, low, high)

    quicksort(array, low, part)
    quicksort(array, part + 1, high)

    return array

tests = [
    [3, 2, 4, 1],
    [4, 2, 3, 1],
    input_data
]

for test in tests:
    print(test[:10])
    print("====>", quicksort(test, 0, len(test))[:10])
    print("Took {} comparisons".format(total))
    total = 0