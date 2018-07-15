import sys

def number_of_swaps(arr):
    pass









# main
if __name__ == "__main__":
    # the elements have value based on start Index 0
    array = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

    min_swaps = number_of_swaps(array)

    print("Minimum number of swaps required to sort the array={}".format(min_swaps))