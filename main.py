"""
This is the main loop file for our AutoTube Bot!

This script has been modified.
"""

from datetime import date
import time
from utils.CreateMovie import CreateMovie, GetDaySuffix
from utils.RedditBot import RedditBot

#Subreddit the bot pulls images from (try subs with lots of images, not videos or text)
sub = "chatgpt"

#Create Reddit Data Bot
redditbot = RedditBot()

def create_video():

    # Gets our new posts pass if image related subs. Default is memes
    posts = redditbot.get_posts(sub)

    # Create folder if it doesn't exist
    redditbot.create_data_folder()

    # Go through posts and find 5 that will work for us.
    for post in posts:
        redditbot.save_image(post)

    # Wanted a date in my titles so added this helper
    DAY = date.today().strftime("%d")
    DAY = str(int(DAY)) + GetDaySuffix(int(DAY))
    dt_string = date.today().strftime("%A %B") + f" {DAY}"

    # Create the movie itself!
    CreateMovie.CreateMP4(redditbot.post_data)

create_video()
