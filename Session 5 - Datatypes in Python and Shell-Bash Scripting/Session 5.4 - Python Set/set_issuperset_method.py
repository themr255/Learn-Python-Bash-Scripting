"""
Method - issuperset()

Description: Returns True, if all elements of set A are present in set B. Else, it returns False.
"""

# Define sets representing different finish options for Asian Paints color products
smooth_finish_colors = {"Satin Blue", "Antique White", "Classic Ivory", "Silk White"}
ultra_sheen_finish_colors = {"Satin Blue", "Glossy Black", "Metallic Silver"}

mix_colors = {"Satin Blue", "Antique White", "Classic Ivory", "Silk White", "Glossy Black", "Metallic Silver"}

# Print the set of smooth_finish_colors
print("Smooth Finish Colors:", smooth_finish_colors)

# Print the set of ultra_sheen_finish_colors
print("Ultra Sheen Finish Colors:", ultra_sheen_finish_colors)

# Print the set of mix_colors
print("Mix Colors:", mix_colors)

# Check if smooth_finish_colors is superset of ultra_sheen_finish_colors set
print("\nIs Smooth Finish a Superset of Ultra Sheen Finish:", smooth_finish_colors.issuperset(ultra_sheen_finish_colors))

# Check if mix_colors is superset of ultra_sheen_finish_colors set
print("\nIs Mix Colors a Superset of Ultra Sheen Finish:", mix_colors.issuperset(ultra_sheen_finish_colors))


"""
                        Output - 
---------------------------------------------------------------
Smooth Finish Colors: {'Classic Ivory', 'Silk White', 'Satin Blue', 'Antique White'}
Ultra Sheen Finish Colors: {'Metallic Silver', 'Satin Blue', 'Glossy Black'}
Mix Colors: {'Silk White', 'Classic Ivory', 'Satin Blue', 'Metallic Silver', 'Glossy Black', 'Antique White'}

Is Smooth Finish a Superset of Ultra Sheen Finish: False

Is Mix Colors a Superset of Ultra Sheen Finish: True

"""