"""
Method - intersection_update()

Description: Finds the intersection of different sets and updates it to the set that calls the method.
"""

# Define playlists as sets of songs
rock_playlist = {"Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"}
pop_playlist = {"Shape of You", "Uptown Funk", "Bohemian Rhapsody"}

# Print the set of Ed Sheeran Songs Playlist
print("Ed Sheeran Playlist:", rock_playlist)

# Print the set of Mix English Songs Playlist
print("Mix English Playlist:", pop_playlist)

# Use intersection_update to update rock_playlist with songs in common with pop_playlist
rock_playlist.intersection_update(pop_playlist)

# Print the updated Rock Songs Playlist
print("\nRock and Pop Song:", rock_playlist)


"""
                        Output - 
---------------------------------------------------------------
Ed Sheeran Playlist: {'Hotel California', 'Stairway to Heaven', 'Bohemian Rhapsody'}
Mix English Playlist: {'Uptown Funk', 'Shape of You', 'Bohemian Rhapsody'}

Rock and Pop Song: {'Bohemian Rhapsody'}

"""