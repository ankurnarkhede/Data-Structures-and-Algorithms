def swap(a, x, y):
    'swapping of a[x] and a[y]'
    a[x], a[y] = a[y], a[x]


def InsertionSort(a):
    "perform inseRTION sort on array a"
    for i in range(1, len(a), +1):
        key = a[i]
        j = i - 1
        while (j >= 0 and a[j] > key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


# main
n = int(input('Enter no of elements:'))
a = []
for i in range(0, n, +1):
    a.append(int(input("Enter an element:")))
print('Initial array:', a)

InsertionSort(a)

print('Insertion sorted array:', a)
