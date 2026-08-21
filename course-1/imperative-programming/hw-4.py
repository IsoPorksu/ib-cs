total = int(input("Enter the total: "))
action = ''
if total > 18:
    action = 'stay'
    if total > 21: action = 'bust'
else: action = 'hit'
print(action)