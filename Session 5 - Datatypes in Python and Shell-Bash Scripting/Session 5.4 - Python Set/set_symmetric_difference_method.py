"""
Method - symmetric_difference()

Description: Returns all the items present in given sets, except the items in their intersections.
"""

# Define sets representing different finish options for Asian Paints color products
smooth_finish_colors = {"Satin Blue", "Antique White", "Classic Ivory", "Silk White"}
ultra_sheen_finish_colors = {"Satin Blue", "Glossy Black", "Metallic Silver"}

# Print the set of smooth_finish_colors
print("Smooth Finish Colors:", smooth_finish_colors)

# Print the set of ultra_sheen_finish_colors
print("Ultra Sheen Finish Colors:", ultra_sheen_finish_colors)

# Find elements that are in either of the sets but not in both
symmetric_diff = smooth_finish_colors.symmetric_difference(ultra_sheen_finish_colors)

# Print the all the colors present in both color type
print("\nColors that are present in either of the sets but not in both:\n", symmetric_diff)


"""
                        Output - 
---------------------------------------------------------------
Smooth Finish Colors: {'Satin Blue', 'Antique White', 'Silk White', 'Classic Ivory'}
Ultra Sheen Finish Colors: {'Satin Blue', 'Glossy Black', 'Metallic Silver'}

Colors that are present in either of the sets but not in both:
{'Classic Ivory', 'Antique White', 'Glossy Black', 'Silk White', 'Metallic Silver'}

"""