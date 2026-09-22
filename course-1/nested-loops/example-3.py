flights = ["AY664", "BA047", "AF110", "LH554", "AY101"]
airlines = ["AY", "UA", "LH"]

print("flights:", flights)
print("airlines:", airlines)
for airline in airlines:
    print(airline+": ", end="")
    for flight in flights:
        if flight[:2] == airline: print(flight, end=" ")
    print()