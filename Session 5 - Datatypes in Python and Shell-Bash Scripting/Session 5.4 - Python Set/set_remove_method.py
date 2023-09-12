"""
Method - remove()

Description: Removes the specified element from the set.

Note: If the element passed to remove() doesn't exist, KeyError exception is thrown.
"""

# Create a Set of travel destinations in Sri Lanka
travel_destinations = {"Colombo", "Kandy", "Galle", "Sigiriya", "Ella", "Nuwara Eliya", "Mirissa", "Polonnaruwa"}

# Print the original set of travel destinations
print("Original travel destinations in Sri Lanka: \n{}".format(travel_destinations))

# Remove a travel destination from set
destination_to_remove = "Polonnaruwa"

try:
    travel_destinations.remove(destination_to_remove)
    print("\nRemoved from the travel destinations: {}".format(destination_to_remove))
except KeyError:
    print("\nTravel destinations is not present in set: {}".format(destination_to_remove))

# Print the updated set of travel destinations
print("\nUpdated travel destinations in Sri Lanka: \n{}".format(travel_destinations))

"""
                        Output - 
---------------------------------------------------------------
Original travel destinations in Sri Lanka: 
{'Polonnaruwa', 'Kandy', 'Nuwara Eliya', 'Galle', 'Ella', 'Colombo', 'Sigiriya', 'Mirissa'}

Removed from the travel destinations: Polonnaruwa

Updated travel destinations in Sri Lanka: 
{'Kandy', 'Nuwara Eliya', 'Galle', 'Ella', 'Colombo', 'Sigiriya', 'Mirissa'}

"""