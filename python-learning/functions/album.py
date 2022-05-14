def make_album(artist_name, album_name, songs_count = None):
    album = {'artist_name': artist_name, 'album_name': album_name}
    if songs_count:
        album['songs_count'] = songs_count
    return album

albums = []
while True:
    print(" enter 'q' at any time to quit")
    
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_name = input("Album name: ")
    if album_name == 'q':
        break

    album = make_album(artist_name, album_name)
    albums.append(album)
    print(albums)
