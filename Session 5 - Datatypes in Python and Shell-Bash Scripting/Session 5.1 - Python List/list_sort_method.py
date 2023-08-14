"""
Method - sort()

Description: The sort() method sorts the items of a list in ascending or descending order.

Note: Default sort is Ascending sort.
"""

# Creating a list for Punjabi Menu
PUNJABI = ["Dal Makhni", "Rajma", "Paneer Tikka Masala", "Paneer Makhni", "Butter Roti", "Butter Naan", "Pudhina Paratha", "Plain Roti"]

# Printing Punjabi Menu List
print("Punjabi Menu: {}".format(PUNJABI))

# You can use any of below syntax to sort in ascending order.
# For Ascending order use -> PUNJABI.sort()  or PUNJABI.sort(reverse=False)
PUNJABI.sort(reverse=False)

# Finally, printing Punjabi Menu List again
print("Punjabi Menu in Ascending Order: {}".format(PUNJABI))

# For Descending order use -> PUNJABI.sort(reverse=True)
PUNJABI.sort(reverse=True)

# Finally, printing Punjabi Menu List again
print("Punjabi Menu in Descending Order: {}".format(PUNJABI))

"""
                        Output - 
---------------------------------------------------------------
Punjabi Menu: ['Dal Makhni', 'Rajma', 'Paneer Tikka Masala', 'Paneer Makhni', 'Butter Roti', 'Butter Naan', 'Pudhina Paratha', 'Plain Roti']
Punjabi Menu in Ascending Order: ['Butter Naan', 'Butter Roti', 'Dal Makhni', 'Paneer Makhni', 'Paneer Tikka Masala', 'Plain Roti', 'Pudhina Paratha', 'Rajma']
Punjabi Menu in Descending Order: ['Rajma', 'Pudhina Paratha', 'Plain Roti', 'Paneer Tikka Masala', 'Paneer Makhni', 'Dal Makhni', 'Butter Roti', 'Butter Naan']
"""

