"""
Method - popitem()

Description: Removes and returns the last element (key, value) pair inserted into the dictionary.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20}

# Printing Electronics Shop Inventory
print('Electronics Shop Inventory:', inventory)

# Removing last item from inventory
remove_element = inventory.popitem()

# Printing what item got removed from inventory
print('Removed Element:', remove_element)

# Printing Electronics Shop Inventory after removing the last itm of inventory
print('Electronics Shop Inventory after removing the last item:', inventory)


"""
                        Output - 
---------------------------------------------------------------
Electronics Shop Inventory: {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20}
Removed Element: ('Headphones', 20)
Electronics Shop Inventory after removing the last element: {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5}
"""

