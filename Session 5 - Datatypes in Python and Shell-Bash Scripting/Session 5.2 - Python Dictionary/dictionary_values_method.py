"""
Method - values()

Description: Returns a view object that displays a list of all the values in the dictionary.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {"Laptop": 10, "Smartphone": 15, "Tablet": 5, "Headphones": 20}

# Extracts the Values of the Dictionary
dictionaryValues = inventory.values()

# Printing Electronics Shop Inventory Dictionary Keys
print("Inventory Items Stock: {}".format(dictionaryValues))

"""
                        Output - 
---------------------------------------------------------------
Inventory Items Stock: dict_values([10, 15, 5, 20])
"""

