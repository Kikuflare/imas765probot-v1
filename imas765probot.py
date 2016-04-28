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
    harurun_bot_ = Bot(app_keys, key_dict['harurun_bot_'])
    chihaya_bot_ = Bot(app_keys, key_dict['chihaya_bot_'])
    yayoicchi_bot = Bot(app_keys, key_dict['yayoicchi_bot'])
    iorin_bot_ = Bot(app_keys, key_dict['iorin_bot_'])
    amimami_bot = Bot(app_keys, key_dict['amimami_bot'])
    yukipyon_bot = Bot(app_keys, key_dict['yukipyon_bot'])
    ohimechin_bot = Bot(app_keys, key_dict['ohimechin_bot'])
    mikimiki_bot_ = Bot(app_keys, key_dict['mikimiki_bot_'])
    hibikin_bot_ = Bot(app_keys, key_dict['hibikin_bot_'])
    azusa_bot__ = Bot(app_keys, key_dict['azusa_bot__'])
    ricchan_bot_ = Bot(app_keys, key_dict['ricchan_bot_'])

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
                
            if harurun_bot_.tweet_enabled and (harurun_bot_.count_rows(harurun_bot_.queue_table) > 0):
                harurun_bot_.tweet()
                
            if chihaya_bot_.tweet_enabled and (chihaya_bot_.count_rows(chihaya_bot_.queue_table) > 0):
                chihaya_bot_.tweet()
                
            if yayoicchi_bot.tweet_enabled and (yayoicchi_bot.count_rows(yayoicchi_bot.queue_table) > 0):
                yayoicchi_bot.tweet()
                
            if iorin_bot_.tweet_enabled and (iorin_bot_.count_rows(iorin_bot_.queue_table) > 0):
                iorin_bot_.tweet()
                
            if amimami_bot.tweet_enabled and (amimami_bot.count_rows(amimami_bot.queue_table) > 0):
                amimami_bot.tweet()
                
            if yukipyon_bot.tweet_enabled and (yukipyon_bot.count_rows(yukipyon_bot.queue_table) > 0):
                yukipyon_bot.tweet()
                
            if ohimechin_bot.tweet_enabled and (ohimechin_bot.count_rows(ohimechin_bot.queue_table) > 0):
                ohimechin_bot.tweet()
                
            if mikimiki_bot_.tweet_enabled and (mikimiki_bot_.count_rows(mikimiki_bot_.queue_table) > 0):
                mikimiki_bot_.tweet()
                
            if hibikin_bot_.tweet_enabled and (hibikin_bot_.count_rows(hibikin_bot_.queue_table) > 0):
                hibikin_bot_.tweet()
                
            if azusa_bot__.tweet_enabled and (azusa_bot__.count_rows(azusa_bot__.queue_table) > 0):
                azusa_bot__.tweet()
                
            if ricchan_bot_.tweet_enabled and (ricchan_bot_.count_rows(ricchan_bot_.queue_table) > 0):
                ricchan_bot_.tweet()
                
        # Follow back users (every 30 minutes at minute 15 and 45)
        if (minute + 15) % 30 == 0:
            if makomakorin_bot.follow_back_enabled:
                makomakorin_bot.follow_back()
                
            if harurun_bot_.follow_back_enabled:
                harurun_bot_.follow_back()
                
            if chihaya_bot_.follow_back_enabled:
                chihaya_bot_.follow_back()
                
            if yayoicchi_bot.follow_back_enabled:
                yayoicchi_bot.follow_back()
                
            if iorin_bot_.follow_back_enabled:
                iorin_bot_.follow_back()
                
            if amimami_bot.follow_back_enabled:
                amimami_bot.follow_back()
                
            if yukipyon_bot.follow_back_enabled:
                yukipyon_bot.follow_back()
                
            if ohimechin_bot.follow_back_enabled:
                ohimechin_bot.follow_back()
                
            if mikimiki_bot_.follow_back_enabled:
                mikimiki_bot_.follow_back()
                
            if hibikin_bot_.follow_back_enabled:
                hibikin_bot_.follow_back()
                
            if azusa_bot__.follow_back_enabled:
                azusa_bot__.follow_back()
                
            if ricchan_bot_.follow_back_enabled:
                ricchan_bot_.follow_back()
                
        # Unfollow users who are no longer following (every hour at minute 30)
        if (minute + 30) % 60 == 0:
            if makomakorin_bot.unfollow_enabled:
                makomakorin_bot.unfollow()
                
            if harurun_bot_.unfollow_enabled:
                harurun_bot_.unfollow()
                
            if chihaya_bot_.unfollow_enabled:
                chihaya_bot_.unfollow()
                
            if yayoicchi_bot.unfollow_enabled:
                yayoicchi_bot.unfollow()
                
            if iorin_bot_.unfollow_enabled:
                iorin_bot_.unfollow()
                
            if amimami_bot.unfollow_enabled:
                amimami_bot.unfollow()
                
            if yukipyon_bot.unfollow_enabled:
                yukipyon_bot.unfollow()
                
            if ohimechin_bot.unfollow_enabled:
                ohimechin_bot.unfollow()
                
            if mikimiki_bot_.unfollow_enabled:
                mikimiki_bot_.unfollow()
                
            if hibikin_bot_.unfollow_enabled:
                hibikin_bot_.unfollow()
                
            if azusa_bot__.unfollow_enabled:
                azusa_bot__.unfollow()
                
            if ricchan_bot_.unfollow_enabled:
                ricchan_bot_.unfollow()
        
        # If a queue is empty, start a new queue
        if makomakorin_bot.count_rows(makomakorin_bot.queue_table) == 0:
            makomakorin_bot.smart_queue()

        if harurun_bot_.count_rows(harurun_bot_.queue_table) == 0:
            harurun_bot_.smart_queue()
            
        if chihaya_bot_.count_rows(chihaya_bot_.queue_table) == 0:
            chihaya_bot_.smart_queue()
            
        if yayoicchi_bot.count_rows(yayoicchi_bot.queue_table) == 0:
            yayoicchi_bot.smart_queue()
            
        if iorin_bot_.count_rows(iorin_bot_.queue_table) == 0:
            iorin_bot_.smart_queue()
            
        if amimami_bot.count_rows(amimami_bot.queue_table) == 0:
            amimami_bot.smart_queue()
            
        if yukipyon_bot.count_rows(yukipyon_bot.queue_table) == 0:
            yukipyon_bot.smart_queue()
        
        if ohimechin_bot.count_rows(ohimechin_bot.queue_table) == 0:
            ohimechin_bot.smart_queue()
            
        if mikimiki_bot_.count_rows(mikimiki_bot_.queue_table) == 0:
            mikimiki_bot_.smart_queue()
            
        if hibikin_bot_.count_rows(hibikin_bot_.queue_table) == 0:
            hibikin_bot_.smart_queue()
            
        if azusa_bot__.count_rows(azusa_bot__.queue_table) == 0:
            azusa_bot__.smart_queue()
            
        if ricchan_bot_.count_rows(ricchan_bot_.queue_table) == 0:
            ricchan_bot_.smart_queue()
            
        # Try to align next loop to be as close to HH:MM:00 as possible
        time.sleep(60 - datetime.datetime.now().second)


if __name__ == "__main__":
    main()