biggest_difference = 0
prev_value = 0
for i in range (0, 101):
    value = i * (i - 20) * (i - 100) + 120000
    if i > 0:
        difference = value - prev_value
        if difference > biggest_difference:
            biggest_difference = difference
    prev_value = value
print(biggest_difference)