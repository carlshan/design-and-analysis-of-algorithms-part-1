def merge(left, right):
    output = []

    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    while i < len(left):
        output.append(left[i])
        i += 1

    while j < len(right):
        output.append(right[j])
        j += 1

    return output


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        midpoint = len(array) // 2
        left = merge_sort(array[:midpoint])
        right = merge_sort(array[midpoint:])

        merged = merge(left, right)
        return merged

# Counting inversions below

def merge_count(left, right):
    output = []
    i, j = 0, 0

    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            inversions += len(left) - i
            j += 1

    while i < len(left):
        output.append(left[i])
        i += 1

    while j < len(right):
        output.append(right[j])
        j += 1

    return output, inversions


def merge_sort_count(array):
    if len(array) == 1:
        return array, 0
    else:
        midpoint = len(array) // 2
        left, left_count = merge_sort_count(array[:midpoint])
        right, right_count = merge_sort_count(array[midpoint:])

        merged, m_count = merge_count(left, right)

        total = left_count + right_count + m_count
        return merged, total

input_file = [int(line.replace('\n', '')) for line in open("IntegerArray.txt").readlines()]

def test():
    test_arr = [2, 10, -1, 100] # 2 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")

    test_arr = [2, 10, -1, 100] # 2 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")

    test_arr = [2, 10, 100] # 0 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")

    test_arr = [10, 1, 100] # 1 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")

    test_arr = [1000, 10, 1, 100] # 4 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")

    test_arr = [1000, 0, 10, -2, 1, 100] # 8 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")

    test_arr = [1, 10, 100, 0, 5, 1000] # 5 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")

    test_arr = [1, 5, 0, 2] # 3 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")

    test_arr = [2, 0, 1] # 2 inversions
    sorted_arr, counter = merge_sort_count(test_arr)
    print(test_arr, "has", counter, "inversions.")