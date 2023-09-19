"""
Method - difference()

Description: Returns a set that contains the difference between two sets.
"""

# Define playlists as sets of songs
ed_sheeran_playlist = {"Thinking Out Loud", "Perfect", "Photograph", "Shape of You"}
mix_english_songs_playlist = {"Photograph", "Shape of You", "Too Good At Goodbyes", "Girls Like You", "Faded", "Happier"}

# Print the set of Ed Sheeran Songs Playlist
print("Ed Sheeran Playlist:", ed_sheeran_playlist)

# Print the set of Mix English Songs Playlist
print("Mix English Playlist:", mix_english_songs_playlist)

# Find the difference between ed_sheeran_playlist and mix_english_songs_playlist
ed_sheeran_song_not_in_mix_english_songs = ed_sheeran_playlist.difference(mix_english_songs_playlist)

# Print the which Ed Sheeran Playlist not present in Mix English Playlist
print("\nEd Sheeran Songs not in Mix English Playlist:", ed_sheeran_song_not_in_mix_english_songs)


"""
                        Output - 
---------------------------------------------------------------
Ed Sheeran Playlist: {'Shape of You', 'Thinking Out Loud', 'Photograph', 'Perfect'}
Mix English Playlist: {'Too Good At Goodbyes', 'Shape of You', 'Photograph', 'Girls Like You', 'Happier', 'Faded'}

Ed Sheeran Songs not in Mix English Playlist: {'Thinking Out Loud', 'Perfect'}

"""