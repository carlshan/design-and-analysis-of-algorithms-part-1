import random

def swap(array, i, j):
    """Helper function to swap elements at the ith and jth position in array"""
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def choose_pivot(array):
    """Choose an element uniformly at random from array between low and high."""
    index = random.choice(range(len(array)))
    return array[index], index


def partition(array):
    """Partitions the array such that all elements less than
    the chosen pivot are to the left and those higher are to the right"""

    pivot, pivot_ind = choose_pivot(array)
    swap(array, 0, pivot_ind)

    i = 1

    for j in range(1, len(array)):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1

    swap(array, 0, i - 1)

    return pivot, i - 1

def randomized_selection(array, length, i):
    """
    Parameters:
        array (list)
        n (int) - the length of the array
        i (int) - the ith order statistic to find

    High level description:
    0. if n == 1: return array[0]
    1. choose pivot uniformly from the array at random
    2. partition A around p
        let j = new index of p
        if i == j by dumb luck, we can return the partition as the ith order statistic
        else we compare i and j. If j > i, then we need to recurse on
        the left partition with randomized_selection(left, j-i, i)
        if j < i, then we recurse on the right partition with randomized_selection(right, n-j, i-j)
    """
    # print(array, length, i)
    if length == 1: return array[0]

    part, part_index = partition(array)

    if part_index == i: # We found the ith order statistic, and it's the partition. How lucky! Let's return it.
        return part

    # Else we need to recurse on one of the two sub-arrays.
    if part_index > i: # Partition was higher than the ith order statistic. Recurse on left half of array.
        left = array[:part_index]
        return randomized_selection(left, len(left), i)
    else: # Partition was smaller. Recurse on right half of array.
        right = array[part_index + 1:]
        return randomized_selection(right, len(right), i - part_index - 1)


# Testing
def test():
    test1 = [4, 3, 1, 2, 5, 6, 7, 8, 9]
    random.shuffle(test1)
    length = len(test1)
    print('result', randomized_selection(test1, length, 0)) # should return 1
    random.shuffle(test1)
    print('result', randomized_selection(test1, length, 1)) # should return 2
    random.shuffle(test1)
    print('result', randomized_selection(test1, length, 2)) # should return 3
    random.shuffle(test1)
    print('result', randomized_selection(test1, length, 3)) # should return 4


if __name__ == '__main__':
    test()