integer = 0; i = 0
lst = []; lst2 = list
while integer >= 0:
    integer = int(input("Please enter non-negative integers: "))
    if integer >= 0:
        lst.append(integer)
print(lst)
lst2 = list(dict.fromkeys(lst))
for e in lst2: print(e, end=" ")