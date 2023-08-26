"""
Method - copy()

Description: Returns a copy (shallow copy) of the dictionary.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {"Laptop": 10, "Smartphone": 15, "Tablet": 5, "Headphones": 20}

# Copying the original inventory
copied_inventory = inventory.copy()

# Printing Original Electronics Inventory
print('Original Inventory:', inventory)

# Printing Copied Electronics Inventory
print('Copied Inventory:', copied_inventory)


"""
                        Output - 
---------------------------------------------------------------
Original Inventory: {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20}
Copied Inventory: {'Laptop': 10, 'Smartphone': 15, 'Tablet': 5, 'Headphones': 20}
"""

