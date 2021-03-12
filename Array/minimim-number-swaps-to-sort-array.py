import sys


def number_of_swaps(arr):
    count = 0
    arr_sorted = sorted(arr)

    for i in range(0, len(arr), +1):
        if (arr_sorted[i] != arr[i]):
            count += 1
            swap(arr, i, arr_sorted.index(arr[i]))

    return count


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# main
if __name__ == "__main__":
    # the elements have value based on start Index 0
    array = (list(map(int, sys.stdin.readline().strip().split(' '))))

    min_swaps = number_of_swaps(array)

    print('Minimum number of swaps required to sort the array={}'.format(min_swaps))
