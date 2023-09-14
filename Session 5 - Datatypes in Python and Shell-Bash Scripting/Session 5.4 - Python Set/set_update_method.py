"""
Method - update()

Description: Used to modify a set by adding elements from another iterable (such as a list, tuple, or another set) to the original set.
"""

# Create a Set of travel destinations in Sri Lanka
travel_destinations = {"Colombo", "Kandy", "Galle", "Sigiriya", "Ella", "Nuwara Eliya", "Mirissa", "Polonnaruwa"}

# Print the original set of travel destinations
print("Original travel destinations in Sri Lanka: \n{}".format(travel_destinations))

# Creating a new_locations set having new travel destination of Sri Lanka
new_locations = {"Jaffna", "Trincomalee", "Hikkaduwa"}

# Update the set of travel destinations with the new locations
travel_destinations.update(new_locations)

# Print the updated set of travel destinations
print("\nUpdated travel destinations in Sri Lanka: \n{}".format(travel_destinations))

"""
                        Output - 
---------------------------------------------------------------
Original travel destinations in Sri Lanka: 
{'Galle', 'Colombo', 'Mirissa', 'Nuwara Eliya', 'Ella', 'Sigiriya', 'Kandy', 'Polonnaruwa'}

Updated travel destinations in Sri Lanka: 
{'Galle', 'Colombo', 'Mirissa', 'Nuwara Eliya', 'Ella', 'Sigiriya', 'Hikkaduwa', 'Trincomalee', 'Kandy', 'Jaffna', 'Polonnaruwa'}

"""