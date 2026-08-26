a = int(input("Please enter integer a: "))
b = int(input("Please enter integer b: "))
c = int(input("Please enter integer c: "))

ab = a - b
ac = a - c
bc = b - c
if ab * bc > 0: result = b
elif ab * ac < 0: result = a
else: result = c
print(result)