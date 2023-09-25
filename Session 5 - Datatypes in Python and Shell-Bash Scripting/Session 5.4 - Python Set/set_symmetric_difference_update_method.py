"""
Method - symmetric_difference_update()

Description: finds the symmetric difference of two sets (non-similar items of both sets)
             and updates it to the set that calls the method.
"""

# Define sets representing different finish options for Asian Paints color products
smooth_finish_colors = {"Satin Blue", "Antique White", "Classic Ivory", "Silk White"}
ultra_sheen_finish_colors = {"Satin Blue", "Glossy Black", "Metallic Silver"}

# Print the set of smooth_finish_colors
print("Smooth Finish Colors:", smooth_finish_colors)

# Print the set of ultra_sheen_finish_colors
print("Ultra Sheen Finish Colors:", ultra_sheen_finish_colors)

# Find elements that are in either of the sets but not in both smooth_finish_colors and ultra_sheen_finish_colors
# Basically find non-similar items in both sets
smooth_finish_colors.symmetric_difference_update(ultra_sheen_finish_colors)

# Print the all the colors present in smooth_finish_colors set after calling symmetric_difference_update method
print("\nUpdated Smooth Finish Colors Set:\n", smooth_finish_colors)


"""
                        Output - 
---------------------------------------------------------------
Smooth Finish Colors: {'Antique White', 'Classic Ivory', 'Silk White', 'Satin Blue'}
Ultra Sheen Finish Colors: {'Metallic Silver', 'Glossy Black', 'Satin Blue'}

Updated Smooth Finish Colors Set:
 {'Metallic Silver', 'Silk White', 'Classic Ivory', 'Glossy Black', 'Antique White'}

"""