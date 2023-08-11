"""
Method - index()

Description: The index() method returns the index of the specified element in the list.

Note - List index start with 0.
"""

# Creating a list for Punjabi Menu
PUNJABI = ["Dal Makhni", "Rajma", "Paneer Tikka Masala", "Paneer Makhni", "Butter Roti", "Butter Naan", "Pudhina Paratha", "Plain Roti"]

# Printing Punjabi Menu List
print("Punjabi Menu: {}".format(PUNJABI))

# Getting index of 'Plain Roti' item in PUNJABI list.
index_of_item = PUNJABI.index("Plain Roti")

# Finally, printing index of 'Plain Roti' item in Punjabi Menu
print("Index of 'Plain Roti' item in Punjabi Menu: {}".format(index_of_item))

"""
                        Output - 
---------------------------------------------------------------
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha', 'Plain Roti']
Index of 'Plain Roti' item in Punjabi Menu: 7
"""

