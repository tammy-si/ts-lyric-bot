import requests
import os
from lyricsgenius import Genius
import random
import re
import tweepy

def get_lyric():
    # getting lyrics from genius
    GENIUS_ACCESS_TOKEN = os.environ.get("GENIUS_ACCESS_TOKEN")

    genius = Genius(GENIUS_ACCESS_TOKEN)
    album = genius.search_album('Folklore Deluxe', "Taylor Swift")
    random_track = random.choice(album.tracks[:-1])
    track = random_track.to_dict()
    lyrics = track['song']['lyrics']
    # first we clean the lyrics and turn into a list so we can get a random lyric
    lines = lyrics.split('\n')
    cleaned = [line for line in lines if '[' not in line and line != '']   
    # some problems wiht ads at the last lines so we have to split to get lyrics
    cleaned[-1] = cleaned[-1].split("See Taylor Swift")[0]
    cleaned[-1] = re.split('(\d+)', cleaned[-1])[0]
    # now after cleaning we get a random lyric
    return random.choice(cleaned)
    


def lambda_handler(event, context):

    # getting the tweet
    random_lyric = get_lyric()

    ## authentication for twitter
    client = tweepy.Client(
        consumer_key=os.environ.get("CONSUMER_KEY"),
        consumer_secret=os.environ.get("CONSUMER_SECRET"),
        access_token=os.environ.get("TWEET_ACCESS_TOKEN"),
        access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET")
    )
    # posting the tweet
    client.create_tweet(text=random_lyric)

    return {"statusCode": 200, "tweet": random_lyric}


