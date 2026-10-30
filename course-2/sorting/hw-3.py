def insertion_sort(array):
    n = len(array)
    i = 1
    while i < n: # repeat n-1 times
        val = array[i]
        j = i - 1 # total 2 statements
        while j >= 0 and array[j] > val: # repeat i times
            array[j+1] = array[j]
            j = j - 1 # total 2 statements
        else:
            array[j+1] = val
            i = i + 1 # total 2 statements

arr = [9, 7, 2, 11]
insertion_sort(arr)
print(arr)