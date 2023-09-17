"""
Method - frozenset()

Description: Immutable version of a Python set object. While elements of a set can be modified at any time,
            elements of the frozen set remain the same after creation.
            Once you create a frozenset, you cannot modify it by adding or removing elements.
"""

# Create a Set of travel destinations in Sri Lanka
travel_destinations = {"Colombo", "Kandy", "Galle", "Sigiriya", "Ella", "Nuwara Eliya", "Mirissa", "Polonnaruwa"}

# Print the original set of travel destinations
print("Original travel destinations in Sri Lanka: \n{}".format(travel_destinations))

# Convert the travel_destinations set to a frozenset
frozen_destinations = frozenset(travel_destinations)

# Attempt to add a new destination to the frozenset (this will raise an error)
try:
    frozen_destinations.add("Galle")
except AttributeError:
    print("\nCannot add to a frozenset.")

# Attempt to remove a destination from the frozenset (this will also raise an error)
try:
    frozen_destinations.remove("Mirissa")
except AttributeError:
    print("\nCannot remove from a frozenset.")

# Print the set of travel destinations
print("\nTravel destinations in Sri Lanka: \n{}".format(travel_destinations))

"""
                        Output - 
---------------------------------------------------------------
Original travel destinations in Sri Lanka: 
{'Mirissa', 'Galle', 'Ella', 'Nuwara Eliya', 'Sigiriya', 'Polonnaruwa', 'Kandy', 'Colombo'}

Cannot add to a frozenset.

Cannot remove from a frozenset.

Travel destinations in Sri Lanka: 
{'Mirissa', 'Galle', 'Ella', 'Nuwara Eliya', 'Sigiriya', 'Polonnaruwa', 'Kandy', 'Colombo'}

"""