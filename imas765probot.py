# imas765probot by Kiku

import json
import time
import datetime
from bot import Bot


# Load key data from keys.json, create Bot objects for each bot
with open('keys.json') as key_data:
    key_dict = json.load(key_data)
    
    app_keys = key_dict['app']
    
    app_enabled = app_keys['enabled']
    
    bots = [Bot(app_keys, key_dict['makomakorin_bot']),
            Bot(app_keys, key_dict['harurun_bot_']),
            Bot(app_keys, key_dict['chihaya_bot_']),
            Bot(app_keys, key_dict['yayoicchi_bot']),
            Bot(app_keys, key_dict['iorin_bot_']),
            Bot(app_keys, key_dict['amimami_bot']),
            Bot(app_keys, key_dict['yukipyon_bot']),
            Bot(app_keys, key_dict['ohimechin_bot']),
            Bot(app_keys, key_dict['mikimiki_bot_']),
            Bot(app_keys, key_dict['hibikin_bot_']),
            Bot(app_keys, key_dict['azusa_bot__']),
            Bot(app_keys, key_dict['ricchan_bot_'])]

            
"""
TWITTER API RATE LIMITS
https://dev.twitter.com/rest/public/rate-limits

                                        User auth                       App auth
Title               Resource family     Requests / 15-min window        Requests / 15-min window
GET followers/list      followers               15                              30
GET friends/list        friends                 15                              30
GET friendships/show    friendships             180                             15
"""

def main():
    print("imas765probot started.")
    
    while app_enabled:
        """
        Tweet a media file and follow back new followers. Files should be tweeted every
        hour on minute 0, while new followers should be followed back every 30 minutes
        at minute 15 and 45. Unfollow users who have stopped following every 60 minutes
        at minute 30. If a queue is empty, a new queue will be generated.
        """

        # Get current minute
        minute = datetime.datetime.now().minute
        
        # Tweet a new media file if current time is on the 0 minute
        # Certain conditions must be satisfied before tweeting, refer to the comments
        # for can_tweet() in bot.py
        if minute % 60 == 0:
            for bot in bots:
                if bot.can_tweet():
                    bot.tweet()
                
        # Follow back users (every 30 minutes at minute 15 and 45)
        if (minute + 15) % 30 == 0:
            for bot in bots:
                if bot.follow_back_enabled:
                    bot.follow_back()
                
        # Unfollow users who are no longer following (every hour at minute 30)
        if (minute + 30) % 60 == 0:
            for bot in bots:
                if bot.unfollow_enabled:
                    bot.unfollow()
        
        # If a queue is empty, start a new queue
        for bot in bots:
            if bot.count_rows(bot.queue_table) == 0:
                bot.smart_queue()
            
        # Try to align next loop to be as close to HH:MM:00 as possible
        time.sleep(60 - datetime.datetime.now().second)


if __name__ == "__main__":
    main()