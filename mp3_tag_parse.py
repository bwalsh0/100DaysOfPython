from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

f = "..\\Synced Music" # path truncated, get every file in folder

song = MP3File(f)
song.set_version(VERSION_1)
for i in song.get_tags():
    print(i)
