"""
Method - count()

Description: The count() method returns the number of times the specified element appears in the list.
"""

# Creating a list for Punjabi Menu
PUNJABI = ["Dal Makhni", "Rajma", "Paneer Tikka Masala", "Plain Roti", "Paneer Makhni", "Butter Roti", "Butter Naan", "Pudhina Paratha", "Plain Roti"]

# Printing Punjabi Menu List
print("Punjabi Menu: {}".format(PUNJABI))

# Counting number of times ‘Plain Roti’ item appeared in Punjabi Menu
count_of_item = PUNJABI.count("Plain Roti")

# Finally, printing number of times ‘Plain Roti’ item appeared in Punjabi Menu
print("Number of times ‘Plain Roti’ item appeared in Punjabi Menu: {}".format(count_of_item))

"""
                        Output - 
---------------------------------------------------------------
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Plain Roti', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha', 'Plain Roti']
Number of times ‘Plain Roti’ item appeared in Punjabi Menu: 2
"""

