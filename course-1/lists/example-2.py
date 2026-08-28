integer = 0
lst = []
while integer >= 0:
    integer = int(input("Please enter non-negative integers: "))
    if integer >= 0:
        lst.append(integer)
        lst.sort() # Modification
print("The list of non-negative integers is:", lst)
