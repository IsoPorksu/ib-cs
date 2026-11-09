while True:
    number = input("Enter a decimal number: ")
    try: print(float(number))
    except ValueError: print("Please enter a decimal number.")