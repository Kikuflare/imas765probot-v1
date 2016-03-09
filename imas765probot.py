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

    makomakorin_bot = Bot(app_keys, key_dict['makomakorin_bot'])
    harurunbot = Bot(app_keys, key_dict['harurunbot'])
    yukipyon_bot = Bot(app_keys, key_dict['yukipyon_bot'])
    yayoicchi_bot = Bot(app_keys, key_dict['yayoicchi_bot'])
    amimami_bot = Bot(app_keys, key_dict['amimami_bot'])
    ohimechin_bot = Bot(app_keys, key_dict['ohimechin_bot'])

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
        hour on minute 0, while new followers should be followed back every 20 minutes
        at minute 10, 30, and 50. If a queue is empty, a new queue will be generated.
        """

        # Get current minute
        minute = datetime.datetime.now().minute
        
        # Tweet a new media file if current time is on the 0 minute
        if minute % 60 == 0:
            if makomakorin_bot.tweet_enabled and (makomakorin_bot.count_rows(makomakorin_bot.queue_table) > 0):
                makomakorin_bot.tweet()
                
            if harurunbot.tweet_enabled and (harurunbot.count_rows(harurunbot.queue_table) > 0):
                harurunbot.tweet()
                
            if yukipyon_bot.tweet_enabled and (yukipyon_bot.count_rows(yukipyon_bot.queue_table) > 0):
                yukipyon_bot.tweet()
                
            if yayoicchi_bot.tweet_enabled and (yayoicchi_bot.count_rows(yayoicchi_bot.queue_table) > 0):
                yayoicchi_bot.tweet()
                
            if amimami_bot.tweet_enabled and (amimami_bot.count_rows(amimami_bot.queue_table) > 0):
                amimami_bot.tweet()
                
            if ohimechin_bot.tweet_enabled and (ohimechin_bot.count_rows(ohimechin_bot.queue_table) > 0):
                ohimechin_bot.tweet()
                
        # Follow back users (every 20 minutes at minute 10, 30, 50)
        if (minute + 10) % 20 == 0:
            if makomakorin_bot.follow_back_enabled:
                makomakorin_bot.follow_back()
                
            if harurunbot.follow_back_enabled:
                harurunbot.follow_back()
                
            if yukipyon_bot.follow_back_enabled:
                yukipyon_bot.follow_back()
                
            if yayoicchi_bot.follow_back_enabled:
                yayoicchi_bot.follow_back()
                
            if amimami_bot.follow_back_enabled:
                amimami_bot.follow_back()
                
            if ohimechin_bot.follow_back_enabled:
                ohimechin_bot.follow_back()
        
        # If a queue is empty, start a new queue
        if makomakorin_bot.count_rows(makomakorin_bot.queue_table) == 0:
            makomakorin_bot.smart_queue()

        if harurunbot.count_rows(harurunbot.queue_table) == 0:
            harurunbot.smart_queue()
            
        if yukipyon_bot.count_rows(yukipyon_bot.queue_table) == 0:
            yukipyon_bot.smart_queue()
        
        if yayoicchi_bot.count_rows(yayoicchi_bot.queue_table) == 0:
            yayoicchi_bot.smart_queue()
        
        if amimami_bot.count_rows(amimami_bot.queue_table) == 0:
            amimami_bot.smart_queue()
        
        if ohimechin_bot.count_rows(ohimechin_bot.queue_table) == 0:
            ohimechin_bot.smart_queue()
            
        # Try to align next loop to be as close to HH:MM:00 as possible
        time.sleep(60 - datetime.datetime.now().second)


if __name__ == "__main__":
    main()