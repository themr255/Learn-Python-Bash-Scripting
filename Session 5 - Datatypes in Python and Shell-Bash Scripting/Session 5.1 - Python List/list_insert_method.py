"""
Method - insert()

Description: The insert() method inserts an element to the list at the specified index.

Note - List index start with 0.
"""

# Creating a list for Punjabi Menu
PUNJABI = ["Dal Makhni", "Rajma", "Paneer Tikka Masala", "Paneer Makhni", "Butter Roti", "Butter Naan", "Pudhina Paratha"]

# Printing Punjabi Menu List
print("Punjabi Menu: {}".format(PUNJABI))

# Adding one more menu item 'Plain Roti' in PUNJABI list at index 4 but in Python index starts with 0, so it will be 3.
PUNJABI.insert(3, "Plain Roti")

# Finally, printing Punjabi Menu List again
print("Punjabi Menu: {}".format(PUNJABI))

"""
                        Output - 
---------------------------------------------------------------
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha']
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Plain Roti', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha']
"""

