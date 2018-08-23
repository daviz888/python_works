import screen
screen.clear()

def make_album(album_title, artist_name, track_number = ''):
    album = {
        'title': album_title,
        'artist': artist_name
    }

    if track_number:
        album['tracks'] = track_number

    return album

process = True

while process:
    artist_name = input("Enter artist name : ")
    album_title = input("Enter album title: ")

    music_album = make_album(artist_name, album_title)
    print("New album Created:")
    for key, value in music_album.items():
        print(f'\t{key.title()} : {value.title()}')

    process = input("\nDo you want to create another musice album? [y/n] ")
    if process.upper() == 'N':
        process = False
    screen.clear()

# slow_rock_album = make_album('slow rock', 'scorpion')
# rnb_album = make_album('RNB', 'j-lou')
# melow_album = make_album('mellow touch', 'gary v')
# print(slow_rock_album)
# print(rnb_album)
# print(melow_album)
# print("\nAlbums with Tracks")
# retro_album = make_album('september', 'earth wind & fire', track_number = 6)

# print(retro_album)