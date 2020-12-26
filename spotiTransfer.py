import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import csv
import time

def wipeFile(filename):
    open(filename, 'w').close()

def openCSV(filename):
    songs = []
    with open(filename, newline='') as csvfile:
        db = csv.reader(csvfile)
        for row in db:
            songs.append(row)
        return songs
        
def writeCSV(songs, filename):
    wipeFile(filename)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(songs)

def authUser():
    print("Before pressing enter please make sure that your default browser \n \
     is signed into the correct spotify account you would like to authenticate.")
    scope = 'user-library-read user-library-modify'

    username = input("Enter your username for the account you want to authenticate: ")
    choice = input("Are you signed into that username in your browser? Type YES or NO: ")
    if(choice != "YES"):
        print("EXITING")

    try:
        token = util.prompt_for_user_token(username, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)

    # Create Spotify object
    spotifyObject = spotipy.Spotify(auth=token)


    # User information
    user = spotifyObject.current_user()
    displayName = user['display_name']

    print()
    print(">>> The User Account is now authorized for " + displayName + " :)")
    print("Please delete the .cache-" + username + " or .cache-" + displayName + " file to delete \n your saved credentials and require authentication again (Or remove a mistaken account)")


def getSongs():
    scope = 'user-library-read user-library-modify'

    username = input("Enter your username: ")
    filename = input("Enter filename for destination CSV: ")
    if(filename[-4:] != '.csv'):
        print("NOT A CSV FILE. RELAUNCH PROGRAM")
        exit()

    try:
        token = util.prompt_for_user_token(username, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)

    # Create Spotify object
    spotifyObject = spotipy.Spotify(auth=token)


    # User information
    user = spotifyObject.current_user()
    displayName = user['display_name']

    print()
    print(">>> It is time to Save Your Songs " + displayName + " :)")

    LIMIT = 50
    OFFSET = 0
    BATCHNUM = 1
    listOfSongs = []

    while(True):
        BATCHNUM += 1
        songs = spotifyObject.current_user_saved_tracks(LIMIT, OFFSET)
        songs = songs['items']
        numSongs = len(songs)
        if(numSongs > 0):
            for song in songs:
                ADDED = song['added_at']
                track = song['track']
                TRACKNAME = track['name']
                ARTIST = track['artists'][0]['name']
                ID = track['id']

                entry = []
                entry.append(ADDED)
                entry.append(TRACKNAME)
                entry.append(ARTIST)
                entry.append(ID)

                listOfSongs.append(entry)

            
            if(numSongs == 50):
                OFFSET += LIMIT
            else:
                break
        else:
            break
    #print(listOfSongs)
    writeCSV(listOfSongs, filename)

def addSongs():
    scope = 'user-library-read user-library-modify'

    username = input("Enter your username: ")
    filename = input("Enter the filename of the song backup CSV file: ")
    if(filename[-4:] != '.csv'):
        print("NOT A CSV FILE. RELAUNCH PROGRAM")
        exit()

    try:
        token = util.prompt_for_user_token(username, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)

    # Create Spotify object
    spotifyObject = spotipy.Spotify(auth=token)


    # User information
    user = spotifyObject.current_user()
    displayName = user['display_name']

    print()
    print(">>> It is time to Transfer Your Tunes " + displayName + " :)")
    print()

    listOfSongs = openCSV(filename)
    for i in range(len(listOfSongs) - 1, -1, -1):
        song = listOfSongs[i][3]
        arr = []
        arr.append(song)
        spotifyObject.current_user_saved_tracks_add(arr)
        print(listOfSongs[i][1] + " -- ADDED")
        time.sleep(1)


choice = int(input("Select 0 to Authenticate a User, 1 to Save Songs or 2 to Transfer Saved Songs\n"))
if(choice == 0):
    authUser()
elif(choice == 1):
    getSongs()
else:
    addSongs()