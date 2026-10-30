def selection_sort(array):
    n = len(array)
    for i in range(n-1): # Selecting ith smallest element
        print(array)
        smallest = array[i]
        for j in range(i+1, n):
            if array[j] < smallest:
                smallest = array[j]
                smallest_ind = j
        # Swap if necessary
        if smallest_ind != i:
            array[i], array[smallest_ind] = array[smallest_ind], array[i]

def bubble_sort(array):
    n = len(array)
    ordered = False
    while not ordered:
        print(array)
        ordered = True
        for i in range(n-1):
            if array[i] > array[i+1]:
                (array[i], array[i+1]) = (array[i+1], array[i])
                ordered = False

arr = [-4, 11, 7, -12, 6, 1]
selection_sort(arr)
arr = [-4, 11, 7, -12, 6, 1]
print()
bubble_sort(arr)