"""
Method - pop()

Description: Removes and returns an element from a dictionary having the given key.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20, 'Air Conditioner' : 8}

# Printing Electronics Shop Inventory
print('Electronics Shop Inventory:', inventory)

# Removing 'Air Conditioner' item from inventory
remove_element = inventory.pop('Air Conditioner')

# Printing Electronics Shop Inventory after removing the item 'Air Conditioner'
print('Electronics Shop Inventory after removing the item:', inventory)


"""
                        Output - 
---------------------------------------------------------------
Electronics Shop Inventory: {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20, 'Air Conditioner': 8}
Electronics Shop Inventory after removing the element: {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20}
"""

