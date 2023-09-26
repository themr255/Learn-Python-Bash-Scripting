"""
Method - isdisjoint()

Description: Returns True if two sets don't have any common items between them, i.e. they are disjoint. Else the
             returns False. """

# Define sets representing different finish options for Asian Paints color products
smooth_finish_colors = {"Satin Blue", "Antique White", "Classic Ivory", "Silk White"}
ultra_sheen_finish_colors = {"Satin Blue", "Glossy Black", "Metallic Silver"}

# Print the set of smooth_finish_colors
print("Smooth Finish Colors:", smooth_finish_colors)

# Print the set of ultra_sheen_finish_colors
print("Ultra Sheen Finish Colors:", ultra_sheen_finish_colors)

# Check if two sets - smooth_finish_colors and ultra_sheen_finish_colors have no common elements
are_disjoint = smooth_finish_colors.isdisjoint(ultra_sheen_finish_colors)

# Here smooth_finish_colors and ultra_sheen_finish_colors sets have one common color - Satin Blue
# So these sets are not Disjoint

# Print the all the colors present in both color type
print("\nAre Sets Disjoint:", are_disjoint)


"""
                        Output - 
---------------------------------------------------------------
Smooth Finish Colors: {'Antique White', 'Classic Ivory', 'Satin Blue', 'Silk White'}
Ultra Sheen Finish Colors: {'Satin Blue', 'Metallic Silver', 'Glossy Black'}

Are Sets Disjoint: False

"""
