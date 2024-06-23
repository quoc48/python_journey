def make_album(artist, album_title, album_song=None):
    album = {'artist': artist, 'album_title': album_title, 'song': album_song}
    if album_song:
        album_info = (f"\nAlbum information:"
                      f"\tArtist: {album['artist'].title()}"
                      f"\tTitle: {album['album_title']}"
                      f"\tSongs: {album['song']}")
    else:
        album_info = (f"\nAlbum information:"
                      f"\tArtist: {album['artist'].title()}"
                      f"\tTitle: {album['album_title']}")
    return album_info

while True:
    print("\nProvide album information:")
    print("(enter 'q' at any time to quit!)")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_name = input("Album name: ")
    if album_name == 'q':
        break

    songs = input("Album songs: ")
    if songs == 'q':
        break
    elif songs:
        songs = int(songs)
    else:
        songs = None

    print(make_album(artist_name,album_name,songs))



