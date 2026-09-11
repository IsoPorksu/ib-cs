from math import *
def print_trigs(k):
    a = k*(pi/5)
    print(f"{a}, {sin(a)}, {cos(a)}")

for i in range(11):
    print_trigs(i)