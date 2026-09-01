lst = []
while (integer := int(input("Please enter non-negative integers: "))) >= 0:
    lst.append(integer)
    lst.sort() # Modification
print("The list of non-negative integers is:", lst)
