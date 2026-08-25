is_sun_shining = input("Is the sun shining? (Y/N): ").upper() == "Y"
time = int(input("What time is it? (0-23): "))
if is_sun_shining and (time > 10 and time < 16): print("Please use sunscreen.")