"""
Method - discard()

Description: Used to remove a specific element from a set if it exists in the set. If the element is not present in the set, the discard method does nothing and doesn't raise any errors.
"""

# Create a Set of travel destinations in Sri Lanka
travel_destinations = {"Colombo", "Kandy", "Galle", "Sigiriya", "Ella", "Nuwara Eliya", "Mirissa", "Polonnaruwa"}

# Use the 'copy' method to create a copy of the set
copied_destinations = travel_destinations.copy()

# Print the original set of travel destinations
print("\nOriginal travel destinations in Sri Lanka: \n{}".format(travel_destinations))

# Destination to discard
destination_to_discard = "Sigiriya"

# Use the 'discard' method to remove a travel destination (if it exists)
travel_destinations.discard(destination_to_discard)

# Print the updated set of travel destinations
print("\nUpdated travel destinations in Sri Lanka: \n{}".format(travel_destinations))

"""
                        Output - 
---------------------------------------------------------------
Original travel destinations in Sri Lanka: 
{'Sigiriya', 'Colombo', 'Polonnaruwa', 'Kandy', 'Galle', 'Ella', 'Mirissa', 'Nuwara Eliya'}

Updated travel destinations in Sri Lanka: 
{'Colombo', 'Polonnaruwa', 'Kandy', 'Galle', 'Ella', 'Mirissa', 'Nuwara Eliya'}

"""