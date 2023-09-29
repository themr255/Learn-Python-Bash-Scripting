"""
Method - union()

Description: Returns a new set with distinct elements from all the sets.
"""

# Define playlists as sets of songs
ed_sheeran_playlist = {"Thinking Out Loud", "Perfect", "Photograph", "Shape of You"}
mix_english_songs_playlist = {"Photograph", "Shape of You", "Too Good At Goodbyes", "Girls Like You", "Faded", "Happier"}

# Print the set of Ed Sheeran Songs Playlist
print("Ed Sheeran Playlist:", ed_sheeran_playlist)

# Print the set of Mix English Songs Playlist
print("Mix English Playlist:", mix_english_songs_playlist)

# Combine playlists using the union method
english_playlist = ed_sheeran_playlist.union(mix_english_songs_playlist)

# Print the updated set of English Songs Playlist
print("\nCombined Playlist:", english_playlist)


"""
                        Output - 
---------------------------------------------------------------
Ed Sheeran Playlist: {'Thinking Out Loud', 'Shape of You', 'Photograph', 'Perfect'}
Mix English Playlist: {'Happier', 'Faded', 'Girls Like You', 'Too Good At Goodbyes'}

Combined Playlist: {'Happier', 'Photograph', 'Faded', 'Perfect', 'Thinking Out Loud', 'Too Good At Goodbyes', 'Shape of You', 'Girls Like You'}

"""