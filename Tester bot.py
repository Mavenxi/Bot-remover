import os
from instabot import Bot
from time import sleep
from random import randint
import my_config

# Delete the session file
session_file = "my_session.pkl" # Replace with your session file name
session_file_path = os.path.join("sessions", session_file)

if os.path.exists(session_file_path):
    os.remove(session_file_path)

# Login to the Instagram account using a custom session file name
bot = Bot()
bot.session_file = session_file
bot.login(username=my_config.USERNAME, password=my_config.PASSWORD)

# get the followers and followings of our Instagram account
followers = bot.get_user_followers(my_config.USERNAME)
following = bot.get_user_following(my_config.USERNAME)
non_followers = set(following) - set(followers)

# Loop over all the users and unfollow non-followers
for non_follower in non_followers:
    try:
        bot.unfollow(non_follower)
        sleep(randint(6, 12))
    except Exception as e:
        print(e)
        sleep(randint(30, 300))
