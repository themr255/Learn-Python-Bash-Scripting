"""
Method - remove()

Description: The remove() method removes the first matching element.
"""

# Creating a list for Punjabi Menu
PUNJABI = ["Dal Makhni", "Rajma", "Paneer Tikka Masala", "Paneer Makhni", "Butter Roti", "Butter Naan", "Pudhina Paratha", "Plain Roti"]

# Printing Punjabi Menu List
print("Punjabi Menu: {}".format(PUNJABI))

# Removing 'Plain Roti' menu item from PUNJABI list
PUNJABI.remove("Plain Roti")

# Finally, printing Punjabi Menu List again
print("Punjabi Menu: {}".format(PUNJABI))

"""
                        Output - 
---------------------------------------------------------------
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha', 'Plain Roti']
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha']
"""