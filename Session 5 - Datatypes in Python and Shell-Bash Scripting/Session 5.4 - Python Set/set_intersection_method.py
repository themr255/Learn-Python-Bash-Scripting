"""
Method - intersection()

Description: Returns a new set with elements that are common to all sets.
"""

# Define playlists as sets of songs
ed_sheeran_playlist = {"Thinking Out Loud", "Perfect", "Photograph", "Shape of You"}
mix_english_songs_playlist = {"Photograph", "Shape of You", "Too Good At Goodbyes", "Girls Like You", "Faded", "Happier"}

# Print the set of Ed Sheeran Songs Playlist
print("Ed Sheeran Playlist:", ed_sheeran_playlist)

# Print the set of Mix English Songs Playlist
print("Mix English Playlist:", mix_english_songs_playlist)

# Find the common songs between ed_sheeran_playlist and mix_english_songs_playlist
common_songs = ed_sheeran_playlist.intersection(mix_english_songs_playlist)

# Print the common songs from both Ed Sheeran and Mix English Playlist
print("\nCommon Songs present in Ed Sheeran and Mix English Playlist:", common_songs)


"""
                        Output - 
---------------------------------------------------------------
Ed Sheeran Playlist: {'Photograph', 'Perfect', 'Thinking Out Loud', 'Shape of You'}
Mix English Playlist: {'Girls Like You', 'Faded', 'Photograph', 'Too Good At Goodbyes', 'Happier', 'Shape of You'}

Common Songs present in Ed Sheeran and Mix English Playlist: {'Shape of You', 'Photograph'}

"""