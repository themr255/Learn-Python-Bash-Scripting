"""
Method - pop()

Description: Randomly removes an item from a set and returns the removed item.
"""

# Create a Set of travel destinations in Sri Lanka
travel_destinations = {"Colombo", "Kandy", "Galle", "Sigiriya", "Ella", "Nuwara Eliya", "Mirissa", "Polonnaruwa", "Jaffna"}

# Print the original set of travel destinations
print("Original travel destinations in Sri Lanka: \n{}".format(travel_destinations))

# Randomly removing an travel destination from a set
removed_destination = travel_destinations.pop()

# Printing travel destination which got removed
print("\nTravel Destination removed: {}".format(removed_destination))

# Print the updated set of travel destinations
print("\nUpdated travel destinations in Sri Lanka: \n{}".format(travel_destinations))

"""
                        Output - 
---------------------------------------------------------------
Original travel destinations in Sri Lanka: 
{'Colombo', 'Mirissa', 'Sigiriya', 'Kandy', 'Jaffna', 'Ella', 'Nuwara Eliya', 'Galle', 'Polonnaruwa'}

Travel Destination removed: Colombo

Updated travel destinations in Sri Lanka: 
{'Mirissa', 'Sigiriya', 'Kandy', 'Jaffna', 'Ella', 'Nuwara Eliya', 'Galle', 'Polonnaruwa'}

"""