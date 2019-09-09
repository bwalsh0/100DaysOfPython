# from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import eyed3
from eyed3 import mp3
from os import listdir
import re

PATH = r'.\Synced Music'
changed, skipped = set(), set()

for fname in [PATH + '\\' + fname for fname in listdir(PATH)]:
    if fname[-3:] == 'mp3':
        mp3 = eyed3.load(fname)
        try:
            artist = mp3.tag.artist
            pattern = re.compile(' & | x | X |, |; ')
            if re.search(pattern, artist):
                # Already skipped this tag, skip again
                if artist in skipped:
                    continue
                newArtist = re.sub(pattern, ' / ', artist)
                
                # Already changed this tag, change duplicate
                if artist in changed:
                    mp3.tag.artist = newArtist
                    mp3.tag.save()
                    continue
                
                confirmation = "(c/x) " + artist + " -> " + newArtist + '\n'
                command = input(confirmation)
                
                if command == 'c':
                    changed.add(artist)
                    mp3.tag.artist = newArtist
                    mp3.tag.save()
                    continue
                
                print("Skipped", artist)
                skipped.add(artist)
                # print(re.sub(pattern, '; ', artist))
        except AttributeError:
            continue
