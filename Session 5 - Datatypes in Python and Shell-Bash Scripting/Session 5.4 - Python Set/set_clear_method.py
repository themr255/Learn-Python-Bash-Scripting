"""
Method - clear()

Description: Removes all items from the set.
"""

# Create a Set of travel destinations in Sri Lanka
travel_destinations = {"Colombo", "Kandy", "Galle", "Sigiriya", "Ella", "Nuwara Eliya", "Mirissa", "Polonnaruwa"}

# Print the original set of travel destinations
print("Original travel destinations in Sri Lanka: \n{}".format(travel_destinations))

# Clear the set using the 'clear' method
travel_destinations.clear()

# Print the updated set of travel destinations
print("\nUpdated travel destinations in Sri Lanka: \n{}".format(travel_destinations))

"""
                        Output - 
---------------------------------------------------------------
Original travel destinations in Sri Lanka: 
{'Galle', 'Ella', 'Colombo', 'Polonnaruwa', 'Sigiriya', 'Kandy', 'Nuwara Eliya', 'Mirissa'}

Updated travel destinations in Sri Lanka: 
set()

"""