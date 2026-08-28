lst1 = []
lst2 = []
lst3 = []
for i in range (8): lst1.append(i**2)
for i in range (4): lst2.append(f"2**{i} is {2**i}")
for i in range (6): lst3.append((i, i+5))
print(lst1, lst2, lst3)