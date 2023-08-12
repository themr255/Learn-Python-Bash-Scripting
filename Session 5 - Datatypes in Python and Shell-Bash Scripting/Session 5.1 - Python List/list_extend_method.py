"""
Method - extend()

Description: The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
"""

# Creating a list for Punjabi Menu
PUNJABI = ["Dal Makhni", "Rajma", "Paneer Tikka Masala", "Paneer Makhni", "Butter Roti", "Butter Naan"]

# Printing Punjabi Menu List
print("Punjabi Menu: {}".format(PUNJABI))

# Speciality in our Punjabi Menu List
SPECIALITY = ["Pudhina Paratha", "Plain Roti"]

# Adding Speciality items in PUNJABI menu list
PUNJABI.extend(SPECIALITY)

# Finally, printing Punjabi Menu List again
print("Punjabi Menu: {}".format(PUNJABI))

"""
                        Output - 
---------------------------------------------------------------
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan']
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha', 'Plain Roti']
"""

