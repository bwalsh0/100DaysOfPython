import eyed3
from eyed3 import mp3
from os import listdir
from os.path import isfile, join
import re

PATH = r'C:\Users\Bryan Walsh\Music\Synced Music'

changed = set()
skipped = set()

def main():
    for fname in [PATH + '\\' + fname for fname in listdir(PATH)]:
        if fname[-3:] == 'mp3':
            mp3 = eyed3.load(fname)
            try:
                handleMultiArtists(mp3)
                handleMissingAlbum(mp3)
            except AttributeError:
                continue
        
def handleMissingAlbum(mp3):
    album = mp3.tag.album
    if album == '':
        print(mp3.tag.title, " -- by ", mp3.tag.artist)


def handleMultiArtists(mp3):
    artist = mp3.tag.artist
    pattern = re.compile(' & |, |; ')
    if re.search(pattern, artist):
        # Already skipped this tag, skip again
        if artist in skipped:
            return
        newArtist = re.sub(pattern, ' / ', artist)
        
        # Already changed this tag, change duplicate
        if artist in changed:
            mp3.tag.artist = newArtist
            mp3.tag.save()
            return
        
        confirmation = "(c/x) " + artist + " -> " + newArtist + '\n'
        command = input(confirmation)
        
        if command == 'c':
            changed.add(artist)
            mp3.tag.artist = newArtist
            mp3.tag.save()
            return
        
        print("Skipped", artist)
        skipped.add(artist)
        # print(re.sub(pattern, '; ', artist))

main()
