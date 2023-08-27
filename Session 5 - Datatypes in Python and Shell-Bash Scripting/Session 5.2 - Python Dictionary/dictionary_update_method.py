"""
Method - update()

Description: Updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {"Laptop": 10, "Smartphone": 15, "Tablet": 5, "Headphones": 20}

# Printing Electronics Shop Inventory
print('Electronics Shop Inventory:', inventory)

# Creating new_items dictionary with new electronics item
new_items = {'Air Conditioner': 8}

# Updating the Electronics Shop Inventory with new_items dictionary
inventory.update(new_items)

# Printing Copied Electronics Inventory
print('Electronics Shop Inventory:', inventory)


"""
                        Output - 
---------------------------------------------------------------
Electronics Shop Inventory: {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20}
Electronics Shop Inventory: {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20, 'Air Conditioner': 8}
"""

