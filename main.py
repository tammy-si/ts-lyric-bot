import requests
import os
from lyricsgenius import Genius
import json
import random
import re

def get_lyric(lyrics):
    # first we clean the lyrics and turn into a list so we can get a random lyric
    lines = lyrics.split('\n')
    cleaned = [line for line in lines if '[' not in line and line != '']   
    # some problems wiht ads at the last lines so we have to split to get lyrics
    cleaned[-1] = cleaned[-1].split("See Taylor Swift")[0]
    cleaned[-1] = re.split('(\d+)', cleaned[-1])[0]
    # now after cleaning we get a random lyric
    return random.choice(cleaned)
    

    

# getting lyrics from genius
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

genius = Genius(ACCESS_TOKEN)
album = genius.search_album('Folklore Deluxe', "Taylor Swift")
random_track = random.choice(album.tracks[:-1])
track = random_track.to_dict()
lyrics = track['song']['lyrics']
title = track['song']['title']
random_lyric = get_lyric(lyrics)
print(title)
print(random_lyric)

