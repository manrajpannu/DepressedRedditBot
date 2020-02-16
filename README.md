# Depressed

A Python bot that finds when users type "Depressed" on university subreddits.

## Purpose
The main idea behind this bot is to graph data and see which universitys are the most depressed for educational use.

## Disclaimer

I hold no liability for what you do with this script or what happens to you by using this script. Abusing this script *can* get you banned from Reddit, so make sure to read up on proper usage of the Reddit API.

## Dependencies

You will need to install Python's [PRAW](https://praw.readthedocs.org/en/) libraries first:

    pip install tweepy
    pip install praw
    
You will also need to create an app account on Reddit: [[instructions]](https://www.reddit.com/dev/api)

1. Sign in with your Reddit account
2. Create a new app account
4. Generate a new OAuth token with those permissions
5. Manually edit this script and put those tokens in the script inside the config.py file

## Usage

Once you edit the bot script to provide the necessary API keys and the subreddit you want to tweet from, you can run the bot on the command line:

    python depressed_bot.py
 
Look into the script itself for configuration options of the bot.

##Have questions? Need help with the bot?

If you're having issues with or have questions about the bot, please message me.
