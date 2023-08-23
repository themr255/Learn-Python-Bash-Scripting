"""
Method - keys()

Description: Extracts the keys of the dictionary and returns the list of keys as a view object.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {"Laptop": 10, "Smartphone": 15, "Tablet": 5, "Headphones": 20}

# Extracts the Keys of the Dictionary
dictionaryKeys = inventory.keys()

# Printing Electronics Shop Inventory Dictionary Keys
print("Inventory Items: {}".format(dictionaryKeys))

"""
                        Output - 
---------------------------------------------------------------
Inventory Items: dict_keys(['Laptop', 'Smartphone', 'Tablet', 'Headphones'])
"""

