"""
Method - append()

Description: The append() method adds an item to the end of the list.
"""

# Creating a list for Punjabi Menu
PUNJABI = ["Dal Makhni", "Rajma", "Paneer Tikka Masala", "Paneer Makhni", "Butter Roti", "Butter Naan", "Pudhina Paratha"]

# Printing Punjabi Menu List
print("Punjabi Menu: {}".format(PUNJABI))

# Adding one more menu item in PUNJABI list
PUNJABI.append("Plain Roti")

# Finally, printing Punjabi Menu List again
print("Punjabi Menu: {}".format(PUNJABI))

"""
                        Output - 
---------------------------------------------------------------
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha']
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha', 'Plain Roti']
"""

