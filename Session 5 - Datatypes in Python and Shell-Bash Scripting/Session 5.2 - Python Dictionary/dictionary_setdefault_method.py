"""
Method - setdefault()

Description: Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the
dictionary.
"""

# Creating a dictionary for Electronics Shop Inventory
inventory = {'Nothing': 'Smartphone', 'Samsung': 'Smartphone', 'iPhone': 'Smartphone'}

# Printing Electronics Inventory
print('Electronics Shop Inventory:', inventory)

# Nokia was not present in above dictionary still will give its default value set in below
item_category = inventory.setdefault('Nokia', 'Smartphone')

print('Item Category =', item_category)

# Now here you can also see that Nokia key with value has been added
print('Electronics Shop Inventory after using setdefault method:', inventory)


"""
                        Output - 
---------------------------------------------------------------
Electronics Shop Inventory: {'Nothing': 'Smartphone', 'Samsung': 'Smartphone', 'iPhone': 'Smartphone'}
Item Category = Smartphone
Electronics Shop Inventory after using setdefault method: {'Nothing': 'Smartphone', 'Samsung': 'Smartphone', 'iPhone': 'Smartphone', 'Nokia': 'Smartphone'}
"""

