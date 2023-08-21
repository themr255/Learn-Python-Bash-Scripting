"""
Method - items()

Description: Returns a view object that displays a list of dictionary's (key, value) tuple pairs.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {"Laptop": 10, "Smartphone": 15, "Tablet": 5, "Headphones": 20}

# Printing Electronics Shop Inventory Dictionary
print("Inventory: {}".format(inventory.items()))

"""
                        Output - 
---------------------------------------------------------------
Inventory: dict_items([('Laptop', 10), ('Smartphone', 15), ('Tablet', 5), ('Headphones', 20)])
"""

