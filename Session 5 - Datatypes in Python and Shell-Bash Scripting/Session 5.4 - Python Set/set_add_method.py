"""
Method - add()

Description: Adds a given element to a set. If the element is already present, it doesn't add any element.
"""

# Create a Set of travel destinations in Sri Lanka
travel_destinations = {"Colombo", "Kandy", "Galle", "Sigiriya", "Ella", "Nuwara Eliya", "Mirissa", "Polonnaruwa"}

# Print the original set of travel destinations
print("Original travel destinations in Sri Lanka: \n{}".format(travel_destinations))

# Add a new travel destination using the 'add' method
travel_destinations.add("Jaffna")

# Print the updated set of travel destinations
print("\nUpdated travel destinations in Sri Lanka: \n{}".format(travel_destinations))

"""
                        Output - 
---------------------------------------------------------------
Original travel destinations in Sri Lanka: 
{'Galle', 'Ella', 'Polonnaruwa', 'Nuwara Eliya', 'Mirissa', 'Sigiriya', 'Colombo', 'Kandy'}

Updated travel destinations in Sri Lanka: 
{'Galle', 'Ella', 'Polonnaruwa', 'Nuwara Eliya', 'Mirissa', 'Sigiriya', 'Colombo', 'Kandy', 'Jaffna'}

"""