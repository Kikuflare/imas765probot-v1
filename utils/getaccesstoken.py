import webbrowser
import tweepy

"""
Short script for generating access tokens for Twitter apps.

Instructions:
1. Log into the Twitter account that will host the app
2. Go to https://apps.twitter.com/ and create a new app
3. Go to the app page and find the Keys and Access Tokens page
4. Copy and paste the Consumer Key (API Key) and Consumer Secret (API Secret)
   into the corresponding variables in the code below
5. Log into the Twitter account that you want to grant an access token to
6. Run this script
7. A page asking for permission to authorize the app for the account should
   open up in your browser, click the Authorize app button
8. You will be given a PIN that you should copy and enter into the command
   prompt for this script
9. The access token and access token secret will be displayed in the command
   prompt if authorization is successful, copy it somewhere more permanent or
   you will have to repeat the process from step 6 if you lose the keys
"""

consumer_key = ""
consumer_secret = ""

if __name__ == "__main__":

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Open authorization URL in browser
    webbrowser.open(auth.get_authorization_url())

    # Ask user for verifier pin
    pin = input('Verification pin number from twitter.com: ').strip()

    # Get access token
    token = auth.get_access_token(verifier=pin)

    # Give user the access token
    # print(token) # IF THE SCRIPT IS CRASHING ON THE LINES BELOW, UNCOMMENT THIS LINE
    print("Key: {}".format(token[0]))
    print("Secret: {}".format(token[1]))