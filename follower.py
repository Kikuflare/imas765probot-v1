import json
import tweepy
import time

"""
Short script for getting a list of friends who are not following you. In other
words, users who you follow but do not follow you back. Results are printed as:

[user id] [screen name] [followed by]

Simply replace the value of the key variable with the key of the account in
the keys.json file. If there is no keys.json file, you can simply write the
keys and secrets directly into this script.

WARNING: Calls to GET friendships/show are rate limited to 180 requests in a 15
minute interval. This script will sleep for 5 seconds between each call in order
to respect the API limit. Therefore, the minimum expected time to complete
execution is (number of people following * 5 seconds).
"""

key = 'example' # replace this with a key from keys.json

with open('keys.json') as key_data:
    key_dict = json.load(key_data)
    
    consumer_key = key_dict['app']['consumer_key']
    consumer_secret = key_dict['app']['consumer_secret']
    
    screen_name = key_dict[key]['screen_name']
    access_token = key_dict[key]['access_token']
    access_token_secret = key_dict[key]['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True

api = tweepy.API(auth)


def main():
    print(screen_name)
    myself = api.get_user(screen_name)
    
    # Grab list of users that the account is following
    friends = []
    for page in tweepy.Cursor(api.friends_ids).pages():
        friends.extend(page)
        
        if len(friends) < myself.friends_count:
            time.sleep(60)
    
    print("Following {} users.".format(len(friends)))
    
    not_following = list()
    
    # Check relationship status for each user and add them to a list if they are not following
    for friend in friends:
        friendship = api.show_friendship(target_id=friend)[1]
        print("{} {} followed_by={}".format(friendship.id, friendship.screen_name,friendship.following))
        
        if not friendship.following:
            not_following.append(friendship)
        
        # We must wait 5 seconds between each call to show_friendship or we will exceed the rate limit
        time.sleep(5)
        
    
    print("")
    print("Friends that are not following ({0}):".format(screen_name))
    for friend in not_following:
        print("{} {}".format(friend.id, friend.screen_name))
    
    print("")
    print("Done.")


if __name__ == "__main__":
    main()