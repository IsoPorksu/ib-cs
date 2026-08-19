total = int(input("Enter the total: "))
action = ''
if total > 17:
    action = 'hit'
    if total > 22: action = 'stay'
else: action = 'bust'
print(action)