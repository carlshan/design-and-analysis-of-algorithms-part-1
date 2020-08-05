
def choose_pivot(array, length):
    return array[0], 0


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array, low, high):
    pivot = array[low]
    i, j = low + 1, high - 1 # initializes i to be first position after pivot and j to be last index

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while (i <= j and array[j] >= pivot):
            j -= 1

        # Opposite process of the one above
        while (i <= j and array[i] <= pivot):
            i += 1

        # We either found a value for both j and i that is out of order
        # in which case we swap and continue
        # or i is higher than j, in which case we exit the loop
        # after swapping the pivot into its rightful position
        if i <= j:
            swap(array, i, j)
            # The loop continues
        else: # everything has been partitioned
            swap(array, low, j)
            return j


def quicksort(array, low, high):
    if high - low <= 1: return array

    part = partition(array, low, high)

    quicksort(array, low, part)
    quicksort(array, part + 1, high)

    return array

test = [3, 8, 2, 5, 1, 4, 7, 6]
print(quicksort(test, 0, len(test)))