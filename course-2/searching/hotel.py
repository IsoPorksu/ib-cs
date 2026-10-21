class Reservation:
    def __init__(self, name, room):
        self.name = name
        self.room = room
reservations = [Reservation("John", 111), Reservation("Mary", 123), Reservation("Diana", 111)]

key = "Dave"

index = 0
found = False
while not found and index < len(names):
    if names[index] == key:
        found = True
    else:
        index += 1
if found: print(rooms[index])
else: print(f"{key} is not a guest here")