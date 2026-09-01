lst = []; lst2 = list
while (integer := int(input("Please enter non-negative integers: "))) >= 0:
    lst.append(integer)
print(lst)
lst2 = list(dict.fromkeys(lst))
for e in lst2: print(e, end=" ")