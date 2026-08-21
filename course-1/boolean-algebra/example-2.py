year = int(input("Enter a year: "))
is_leap_year = False
if year % 4 == 0:
    is_leap_year = True
    if year % 100 == 0:
        is_leap_year = False
        if year % 400 == 0:
            is_leap_year = True
print(is_leap_year)