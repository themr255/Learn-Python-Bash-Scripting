"""
Method - copy()

Description: The copy() method returns a shallow copy of the list.
"""

# Creating a list for Punjabi Menu
TEMP_MENU = ['Butter Naan', 'Butter Roti', 'Dal Makhni', 'Paneer Makhni', 'Paneer Tikka Masala', 'Plain Roti', 'Pudhina Paratha', 'Rajma']

# Printing Punjabi Menu List
print("TEMP Menu: {}".format(TEMP_MENU))

# Copying TEMP_MENU list to PUNJABI.
PUNJABI = TEMP_MENU.copy()

# Finally, printing Punjabi Menu List
print("Punjabi Menu: {}".format(PUNJABI))

"""
                        Output - 
---------------------------------------------------------------
TEMP Menu: ['Butter Naan', 'Butter Roti', 'Dal Makhni', 'Paneer Makhni', 'Paneer Tikka Masala', 'Plain Roti', 'Pudhina Paratha', 'Rajma']
Punjabi Menu: ['Butter Naan', 'Butter Roti', 'Dal Makhni', 'Paneer Makhni', 'Paneer Tikka Masala', 'Plain Roti', 'Pudhina Paratha', 'Rajma']
"""

