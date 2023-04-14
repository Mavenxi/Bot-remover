# Importing Libraries
from instabot import Bot
from time import sleep
from random import randint
import my_config

# Instantiate the bot object
bot = Bot()

# Login to the Instagram account
bot.login(username=my_config.USERNAME, password=my_config.PASSWORD)

# Get the followers of our Instagram account
followers = bot.get_user_followers(bot.user_id)

# Loop over all the followers
for follower in followers:
    # Check if the follower follows back
    if follower not in bot.get_user_following(bot.user_id):
        try:
            bot.block(follower)
            print(f"Blocked {bot.get_username_from_user_id(follower)}")
            # Wait for a random amount of time between 6 and 12 seconds
            sleep(randint(6, 12))
        except Exception as e:
            print(e)
            # Wait for a random amount of time between 30 and 300 seconds
            sleep(randint(30, 300))
