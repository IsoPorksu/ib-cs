class Product:
    current_id = 0 # Example 2
    def __init__(self, description, price):
        self.description = description
        self.id_num = Product.current_id
        Product.current_id += 1
        self.price = price
    def __str__(self):
        return f"product {self.description}, id {self.id_num}, @ {self.price}"

ps = [Product("thinkpad",  1299.95), Product("mac", 3299.95)] # Calls __init__() behind the scenes in INITialise a new piece of data.
for p in ps:
    print(p) # Calls __str()__ behind the scenes to get the string form of the data to print
