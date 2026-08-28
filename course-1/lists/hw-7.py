integer = 0
lst = []
while integer >= 0:
    integer = int(input("Please enter non-negative integers: "))
    if integer >= 0:
        if integer not in lst: lst.append(integer)
        else:
            lst.remove(integer)
            lst.insert(0, integer)
print("The list of non-negative integers is:", lst)
