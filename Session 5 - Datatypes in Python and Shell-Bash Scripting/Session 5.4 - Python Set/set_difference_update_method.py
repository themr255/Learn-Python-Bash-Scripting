"""
Method - difference_update()

Description: Computes the difference between two sets (A - B) and updates set A with the resulting set.
"""

# Define playlists as sets of songs
mix_english_songs_playlist = {"Photograph", "Shape of You", "Too Good At Goodbyes", "Girls Like You", "Faded", "Happier"}
ed_sheeran_playlist = {"Thinking Out Loud", "Perfect", "Photograph", "Shape of You"}

# Print the set of Mix English Songs Playlist
print("Mix English Playlist:", mix_english_songs_playlist)

# Print the set of Ed Sheeran Songs Playlist
print("Ed Sheeran Playlist:", ed_sheeran_playlist)

# Here we can see few ed_sheeran_playlist songs present in mix_english_songs_playlist
# So remove all Ed Sheeran songs from mix_english_songs_playlist
mix_english_songs_playlist.difference_update(ed_sheeran_playlist)

# Print the which Ed Sheeran Playlist not present in Mix English Playlist
print("\nMix English Playlist after removing Ed Sheeran Songs:", mix_english_songs_playlist)


"""
                        Output - 
---------------------------------------------------------------
Mix English Playlist: {'Photograph', 'Shape of You', 'Girls Like You', 'Happier', 'Too Good At Goodbyes', 'Faded'}
Ed Sheeran Playlist: {'Perfect', 'Thinking Out Loud', 'Photograph', 'Shape of You'}

Mix English Playlist after removing Ed Sheeran Songs: {'Girls Like You', 'Happier', 'Too Good At Goodbyes', 'Faded'}

"""