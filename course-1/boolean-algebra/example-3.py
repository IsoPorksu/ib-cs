day = int(input("Please enter the day of the week as an integer between 1 and 7: "))
vacation = True if input("Is James on vacation? (Y/N)") == "Y" or "y" else False
if vacation: sleep_late = True
elif day == 6 or day == 7: sleep_late = True
else: sleep_late = False
print(sleep_late)