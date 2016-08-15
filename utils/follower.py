import sys
import json
import tweepy
import time

"""
Short script for getting a list of friends who are not following you. In other
words, users who you follow but do not follow you back. Results are printed as:

[user id] [screen name]

Simply run this script by passing the key of the account as the first argument.
If there is no keys.json file, you can simply write the keys and secrets
directly into this script.

WARNING: Calls to GET users/lookup are rate limited to 180 requests in a 15
minute interval. This script will sleep for 15 minutes if it hits 180 requests
in order to respect the API limit.
"""

key = sys.argv[1] # Assigned to command line argument

with open('../keys.json') as key_data:
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
        
        if len(friends) > 5000:
            time.sleep(60)
            
    # Grab list of users who follow the account
    followers = []
    for page in tweepy.Cursor(api.followers_ids).pages():
        followers.extend(page)
        
        if len(followers) > 5000:
            time.sleep(60)
    
    print("Following {} users.".format(len(friends)))
    
    not_following = list()
    
    # Check relationship status for each user and add them to a list if they are not following
    for friend in friends:
        if friend not in followers:
            user = api.get_user(friend)
            not_following.append(user)
            if len(not_following) >= 180:
                time.sleep(900)
    
    print("")
    print("Friends who are not following ({0}):".format(screen_name))
    for friend in not_following:
        print("{} {}".format(friend.id, friend.screen_name))
    
    print("")
    print("Done.")


if __name__ == "__main__":
    main()