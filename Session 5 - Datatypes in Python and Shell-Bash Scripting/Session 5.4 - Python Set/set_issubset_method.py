"""
Method - issubset()

Description: Returns True if set A is the subset of B, i.e. if all the elements of set A are present in set B .
             Else, it returns False
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

# Check if smooth_finish_colors is subset of ultra_sheen_finish_colors set
print("\nIs Smooth Finish a Subset of Ultra Sheen Finish:", smooth_finish_colors.issubset(ultra_sheen_finish_colors))

# Check if smooth_finish_colors is subset of mix_colors set
print("\nIs Smooth Finish a Subset of Mix Colors:", smooth_finish_colors.issubset(mix_colors))


"""
                        Output - 
---------------------------------------------------------------
Smooth Finish Colors: {'Satin Blue', 'Antique White', 'Classic Ivory', 'Silk White'}
Ultra Sheen Finish Colors: {'Satin Blue', 'Glossy Black', 'Metallic Silver'}
Mix Colors: {'Satin Blue', 'Classic Ivory', 'Metallic Silver', 'Silk White', 'Glossy Black', 'Antique White'}

Is Smooth Finish a Subset of Ultra Sheen Finish: False

Is Smooth Finish a Subset of Mix Colors: True

"""