import eyed3
from eyed3 import mp3, id3
from eyed3 import plugins
from os import listdir
from os.path import isfile, join
import re

PATH = r'.\Synced Music'
changed, skipped = set(), set()
ctNone, ctRedundant = 0, 0
artists, mismatched = set(), set()
confirmCases = set()


def main():
    for fname in [PATH + '\\' + fname for fname in listdir(PATH)]:
        if fname[-3:] == 'mp3':
            mp3 = eyed3.load(fname)
            try:
                fixCharCase(mp3)
                # handleMultiArtists(mp3)
                # fixAlbumName(mp3)
                # fixGenre(mp3)
            except AttributeError:
                continue
                print("AttributeError at", fname)
    print("Fixed:\n{0} redundant\n{1} blank".format(ctNone, ctRedundant))
    print(sorted(mismatched), len(mismatched))
    if len(mismatched) != 0:
        mismatched.clear()
        confirmCharCase()
        for i in mismatched:
            print(i)
    

def fixCharCase(mp3):
    global mismatched
    artist = mp3.tag.artist
    for i in mismatched:
        keys = i.split('_')
        if artist == keys[0]:
            mp3.tag.artist = keys[1]
            mp3.tag.save()
            return
        elif artist == keys[1]:
            return
    for i in artists:
        caseMatch = i.split('_')
        if caseMatch[0] == artist.lower() and caseMatch[1] != artist.swapcase():
            mismatched.add(caseMatch[1].swapcase() + "_" + artist)
            keepWhich = input("(1 or 2) " + caseMatch[1].swapcase() + "  ||  " + artist + '\n')
            if keepWhich == '1':
                mp3.tag.artist = caseMatch[1].swapcase()
                confirmCases.add(artist + "_" + caseMatch[1].swapcase())
            elif keepWhich == '2':
                mp3.tag.artist = artist
                confirmCases.add(caseMatch[1].swapcase() + "_" + artist)
            mp3.tag.save()
    artists.add(artist.lower() + "_" + artist.swapcase())


def confirmCharCase():
    global mismatched
    for fname in [PATH + '\\' + fname for fname in listdir(PATH)]:
        if fname[-3:] == 'mp3':
            mp3 = eyed3.load(fname)
            try:
                artist = mp3.tag.artist
                for i in confirmCases:
                    keys = i.split('_')
                    if artist == keys[0]:
                        mismatched.add(keys[0] + " -> " + keys[1])
                        mp3.tag.artist = keys[1]
                        mp3.tag.save()
            except AttributeError:
                continue
                print("AttributeError at", fname)


def fixGenre(mp3):
    if mp3.tag.genre.id is None:
        nonStdGenre = mp3.tag.genre.name
        pattern = re.compile(', |; | & | and |')
        if re.search(pattern, nonStdGenre): 
            mp3.tag.genre.name = re.sub(pattern, ';', nonStdGenre)
            mp3.tag.save()
    

def fixAlbumName(mp3):
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


main()
