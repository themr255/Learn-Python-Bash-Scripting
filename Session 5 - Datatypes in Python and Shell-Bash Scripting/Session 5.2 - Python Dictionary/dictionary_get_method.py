"""
Method - get()

Description: Returns the value for the specified key if the key is in the dictionary.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {"Laptop": 10, "Smartphone": 15, "Tablet": 5, "Headphones": 20}

# Printing Smartphone Item Stock
print("Smartphones in Stock: {}".format(inventory.get('Smartphone')))

"""
                        Output - 
---------------------------------------------------------------
Smartphones in Stock: 15
"""
