def read_floats(n):
    lst = []
    for i in range (1, n+1):
        num = input(f"input value {i} out of {n}: ")
        lst.append(num)
    return(lst)