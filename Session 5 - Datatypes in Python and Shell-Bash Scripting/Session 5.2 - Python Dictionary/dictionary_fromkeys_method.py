"""
Method - fromkeys()

Description: Creates a dictionary from the given sequence of keys and values.
"""

# keys for the dictionary
item_brand = {'Samsung', 'iPhone', 'Nothing'}

# value for the dictionary
item_category = 'Smartphone'

# Now create an inventory dictionary from the given sequence of keys - item_brand and values - item_category
inventory = dict.fromkeys(item_brand, item_category)

# Printing Electronics Inventory
print('Electronics Shop Inventory:', inventory)


"""
                        Output - 
---------------------------------------------------------------
Electronics Shop Inventory: {'iPhone': 'Smartphone', 'Nothing': 'Smartphone', 'Samsung': 'Smartphone'}
"""

