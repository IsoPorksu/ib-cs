def alternate(lst):
    output = []
    for i in range(1, len(lst)+1):
        if i == 1: output.append(lst[0])
        elif i%2 == 0: output.append(lst[int(-i/2)])
        else: output.append(lst[int((i-1)/2)])
    return output

lst = ["first", "2nd", "3rd", "4th", "4th last", "3rd last", "2nd last", "last"]
print(alternate(lst))