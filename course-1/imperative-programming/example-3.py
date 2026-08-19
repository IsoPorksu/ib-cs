n = int(input('Please type a positive integer: '))

if n <= 0: print('Error! Please type a positive integer next time!')
else: # Do factorial manually
    i = n-1
    result = n
    while i > 0:
        result = result*i
        i -= 1
    print(result)