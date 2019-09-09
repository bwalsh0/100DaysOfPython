import eyed3
from eyed3 import mp3
from os import listdir
from os.path import isfile, join
import re

PATH = r'.\Synced Music'
changed, skipped = set(), set()
ctNone, ctRedundant = 0, 0

def main():
    for fname in [PATH + '\\' + fname for fname in listdir(PATH)]:
        if fname[-3:] == 'mp3':
            mp3 = eyed3.load(fname)
            try:
                handleMultiArtists(mp3)
                handleMissingAlbum(mp3)
            except AttributeError:
                continue
    print("Fixed:\n{0} redundant\n{1} blank".format(ctNone, ctRedundant))
        
def handleMissingAlbum(mp3):
    global ctRedundant; global ctNone
    album = mp3.tag.album
    if album is None:
        print(mp3.tag.title, " || ", mp3.tag.artist)
        mp3.tag.album = "Synced Music"
        mp3.tag.save()
        ctNone += 1
    elif 'Single' in album:
        print(mp3.tag.title, " || ", album, " || ", mp3.tag.artist)
        mp3.tag.album = "Synced Music"
        mp3.tag.save()
        ctRedundant += 1
        
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