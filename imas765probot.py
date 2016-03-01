# imas765probot by Kiku

import tweepy
import os
import json
import random
import time
import datetime
import psycopg2
import boto3
import botocore
from urllib.parse import urlparse
from pytz import timezone


# Load key data from keys.json
with open('keys.json') as key_data:
    key_dict = json.load(key_data)
    
    enabled_app = key_dict['app']['enabled']
    
    consumer_key = key_dict['app']['consumer_key']
    consumer_secret = key_dict['app']['consumer_secret']
    bucket = key_dict['app']['bucket_name']
    max_download_attempts = key_dict['app']['max_download_attempts']
    max_tweet_attempts = key_dict['app']['max_tweet_attempts']
    num_followers = key_dict['app']['num_followers']
    
    database_url = key_dict['database']['url']
    
    enabled_makoto = key_dict['makomakorin_bot']['enabled']
    access_token_makoto = key_dict['makomakorin_bot']['access_token']
    access_token_secret_makoto = key_dict['makomakorin_bot']['access_token_secret']
    queue_table_makoto = key_dict['makomakorin_bot']['queue_table']
    recent_queue_table_makoto = key_dict['makomakorin_bot']['recent_queue_table']
    request_sent_table_makoto = key_dict['makomakorin_bot']['request_sent_table']
    recent_limit_makoto = key_dict['makomakorin_bot']['recent_limit']
    bucket_directory_makoto = key_dict['makomakorin_bot']['bucket_directory']
    follow_back_makoto = key_dict['makomakorin_bot']['follow_back']
    
    enabled_haruka = key_dict['harurunbot']['enabled']
    access_token_haruka = key_dict['harurunbot']['access_token']
    access_token_secret_haruka = key_dict['harurunbot']['access_token_secret']
    queue_table_haruka = key_dict['harurunbot']['queue_table']
    recent_queue_table_haruka = key_dict['harurunbot']['recent_queue_table']
    request_sent_table_haruka = key_dict['harurunbot']['request_sent_table']
    recent_limit_haruka = key_dict['harurunbot']['recent_limit']
    bucket_directory_haruka = key_dict['harurunbot']['bucket_directory']
    follow_back_haruka = key_dict['harurunbot']['follow_back']
    
    enabled_yukiho = key_dict['yukipyon_bot']['enabled']
    access_token_yukiho = key_dict['yukipyon_bot']['access_token']
    access_token_secret_yukiho = key_dict['yukipyon_bot']['access_token_secret']
    queue_table_yukiho = key_dict['yukipyon_bot']['queue_table']
    recent_queue_table_yukiho = key_dict['yukipyon_bot']['recent_queue_table']
    request_sent_table_yukiho = key_dict['yukipyon_bot']['request_sent_table']
    recent_limit_yukiho = key_dict['yukipyon_bot']['recent_limit']
    bucket_directory_yukiho = key_dict['yukipyon_bot']['bucket_directory']
    follow_back_yukiho = key_dict['yukipyon_bot']['follow_back']

    enabled_yayoi = key_dict['yayoicchi_bot']['enabled']
    access_token_yayoi = key_dict['yayoicchi_bot']['access_token']
    access_token_secret_yayoi = key_dict['yayoicchi_bot']['access_token_secret']
    queue_table_yayoi = key_dict['yayoicchi_bot']['queue_table']
    recent_queue_table_yayoi = key_dict['yayoicchi_bot']['recent_queue_table']
    request_sent_table_yayoi = key_dict['yayoicchi_bot']['request_sent_table']
    recent_limit_yayoi = key_dict['yayoicchi_bot']['recent_limit']
    bucket_directory_yayoi = key_dict['yayoicchi_bot']['bucket_directory']
    follow_back_yayoi = key_dict['yayoicchi_bot']['follow_back']

    enabled_amimami = key_dict['amimami_bot']['enabled']
    access_token_amimami = key_dict['amimami_bot']['access_token']
    access_token_secret_amimami = key_dict['amimami_bot']['access_token_secret']
    queue_table_amimami = key_dict['amimami_bot']['queue_table']
    recent_queue_table_amimami = key_dict['amimami_bot']['recent_queue_table']
    request_sent_table_amimami = key_dict['amimami_bot']['request_sent_table']
    recent_limit_amimami = key_dict['amimami_bot']['recent_limit']
    bucket_directory_amimami = key_dict['amimami_bot']['bucket_directory']
    follow_back_amimami = key_dict['amimami_bot']['follow_back']
    
    enabled_takane = key_dict['ohimechin_bot']['enabled']
    access_token_takane = key_dict['ohimechin_bot']['access_token']
    access_token_secret_takane = key_dict['ohimechin_bot']['access_token_secret']
    queue_table_takane = key_dict['ohimechin_bot']['queue_table']
    recent_queue_table_takane = key_dict['ohimechin_bot']['recent_queue_table']
    request_sent_table_takane = key_dict['ohimechin_bot']['request_sent_table']
    recent_limit_takane = key_dict['ohimechin_bot']['recent_limit']
    bucket_directory_takane = key_dict['ohimechin_bot']['bucket_directory']
    follow_back_takane = key_dict['ohimechin_bot']['follow_back']

    
# Connect to AWS S3 using boto3
s3 = boto3.resource('s3')
client = boto3.client('s3')

# Parsed database url
PARSED_URL = urlparse(database_url)

# Time intervals for various functions
LOOP_DELAY = 60     # 1 minute

# Create auth for each bot
auth_makoto = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_makoto.set_access_token(access_token_makoto, access_token_secret_makoto)
auth_makoto.secure = True
api_makoto = tweepy.API(auth_makoto)

auth_haruka = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_haruka.set_access_token(access_token_haruka, access_token_secret_haruka)
auth_haruka.secure = True
api_haruka = tweepy.API(auth_haruka)

auth_yukiho = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_yukiho.set_access_token(access_token_yukiho, access_token_secret_yukiho)
auth_yukiho.secure = True
api_yukiho = tweepy.API(auth_yukiho)

auth_yayoi = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_yayoi.set_access_token(access_token_yayoi, access_token_secret_yayoi)
auth_yayoi.secure = True
api_yayoi = tweepy.API(auth_yayoi)

auth_amimami = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_amimami.set_access_token(access_token_amimami, access_token_secret_amimami)
auth_amimami.secure = True
api_amimami = tweepy.API(auth_amimami)

auth_takane = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_takane.set_access_token(access_token_takane, access_token_secret_takane)
auth_takane.secure = True
api_takane = tweepy.API(auth_takane)

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
    
    while enabled_app:
        """
        Tweet a media file and follow back new followers. Files should be tweeted every
        hour on minute 0, while new followers should be followed back every 20 minutes
        at minute 10, 30, and 50. If a queue is empty, a new queue will be generated.
        """

        # Get current minute
        minute = datetime.datetime.now().minute
        
        # Tweet a new media file if current time is on the 0 minute
        if minute % 60 == 0:
            if enabled_makoto and (count_rows(queue_table_makoto) > 0):
                tweet(api_makoto, queue_table_makoto, recent_queue_table_makoto, recent_limit_makoto)
                
            if enabled_haruka and (count_rows(queue_table_haruka) > 0):
                tweet(api_haruka, queue_table_haruka, recent_queue_table_haruka, recent_limit_haruka)
                
            if enabled_yukiho and (count_rows(queue_table_yukiho) > 0):
                tweet(api_yukiho, queue_table_yukiho, recent_queue_table_yukiho, recent_limit_yukiho)
                
            if enabled_yayoi and (count_rows(queue_table_yayoi) > 0):
                tweet(api_yayoi, queue_table_yayoi, recent_queue_table_yayoi, recent_limit_yayoi)
                
            if enabled_amimami and (count_rows(queue_table_amimami) > 0):
                tweet(api_amimami, queue_table_amimami, recent_queue_table_amimami, recent_limit_amimami)
                
            if enabled_takane and (count_rows(queue_table_takane) > 0):
                tweet(api_takane, queue_table_takane, recent_queue_table_takane, recent_limit_takane)
        
        # Follow back users (every 20 minutes at minute 10, 30, 50)
        if (minute + 10) % 20 == 0:
            if follow_back_makoto:
                follow_back(api_makoto, request_sent_table_makoto)
                
            if follow_back_haruka:
                follow_back(api_haruka, request_sent_table_haruka)
                
            if follow_back_yukiho:
                follow_back(api_yukiho, request_sent_table_yukiho)
                
            if follow_back_yayoi:
                follow_back(api_yayoi, request_sent_table_yayoi)
                
            if follow_back_amimami:
                follow_back(api_amimami, request_sent_table_amimami)
                
            if follow_back_takane:
                follow_back(api_takane, request_sent_table_takane)
        
        # If a queue is empty, start a new queue
        if count_rows(queue_table_makoto) == 0:
            smart_queue(queue_table_makoto, recent_queue_table_makoto, recent_limit_makoto, bucket_directory_makoto)

        if count_rows(queue_table_haruka) == 0:
            smart_queue(queue_table_haruka, recent_queue_table_haruka, recent_limit_haruka, bucket_directory_haruka)
            
        if count_rows(queue_table_yukiho) == 0:
            smart_queue(queue_table_yukiho, recent_queue_table_yukiho, recent_limit_yukiho, bucket_directory_yukiho)
        
        if count_rows(queue_table_yayoi) == 0:
            smart_queue(queue_table_yayoi, recent_queue_table_yayoi, recent_limit_yayoi, bucket_directory_yayoi)
        
        if count_rows(queue_table_amimami) == 0:
            smart_queue(queue_table_amimami, recent_queue_table_amimami, recent_limit_amimami, bucket_directory_amimami)
        
        if count_rows(queue_table_takane) == 0:
            smart_queue(queue_table_takane, recent_queue_table_takane, recent_limit_takane, bucket_directory_takane)
            
        # Try to align next loop to be as close to HH:MM:00 as possible
        time.sleep(LOOP_DELAY - datetime.datetime.now().second)


def tweet(api, queue_name, recent_queue_name, recent_limit):
    """
    This function will attempt to download a file from S3 (up to max_download_attempts)
    to the local filesystem. Next, it will attempt to tweet the file. If successful, it
    will update the corresponding recent queue table with the latest file.    
    """
    for attempt in range(max_download_attempts):
        # Pop the newest filepath from the queue, determine destination temp filepath
        filepath = get_newest_row(queue_name)
        delete_row(queue_name, filepath)
        temp_file = os.path.abspath(filepath)
        dirname = os.path.dirname(temp_file)

        # Create folder of the destination temp file, otherwise download_file will fail
        # with a FileNotFoundError
        if not os.path.isdir(dirname):
            os.makedirs(dirname)

        # Download the file to the local filesystem. If the attempt failed, retry with
        # the next file in the queue.
        try:
            s3.meta.client.download_file(bucket, filepath, temp_file)
        except FileNotFoundError as error:
            print("{0}: Could not download file, the destination folder does not exist.".format(api.me().screen_name))
            continue
        except botocore.exceptions.ClientError as error:
            print("{0}: Could not download file, the file does not exist in the bucket.".format(api.me().screen_name))
            continue
        except IsADirectoryError as error:
            print("{0}: There was an error when saving the file (attempted to download a folder instead of a file).".format(api.me().screen_name))
            break
            
        tweet_media(api, filepath)
        
        # Push the tweeted file into the table of recent tweets, and remove the oldest entries
        # from the table until the limit is reached
        insert_recent(recent_queue_name, filepath)
        row_count = count_rows(recent_queue_name)
        if row_count > recent_limit:
            for i in range(row_count - recent_limit):
                delete_oldest_row(recent_queue_name, 'timestamp')
                
        break


def tweet_media(api, filepath):
    # Takes an absolute file path to a media file and posts a tweet with the file.
    for attempt in range(max_tweet_attempts):
        try:
            # This uploads the file and receives a media_id value
            ids = []
            uploaded = api.media_upload(filepath)
            ids.append(uploaded['media_id'])

            # Use the media_id value to tweet the file
            api.update_status(media_ids=ids)
            print("{0}: Tweeted file {1}".format(api.me().screen_name, os.path.basename(filepath)))

        except tweepy.error.TweepError as error:
            if error.response is not None:
                if error.response.status_code == 429:
                    print("{0}: Could not tweet file. Request limit reached.".format(api.me().screen_name))
                elif error.response.status_code == 500:
                    print("{0}: Could not tweet file. Twitter server error.".format(api.me().screen_name))
                    continue # Server error is likely temporary, try tweeting again
                elif error.response.status_code == 503:
                    print("{0}: Could not tweet file. Service unavailable.".format(api.me().screen_name))
                    continue # Server error is likely temporary, try tweeting again
                else:
                    print("{0}: Could not tweet file. Reason: {1} ({2})".format(api.me().screen_name, error.reason, error.response.status_code))
                    continue # Error *may* be temporary, try tweeting again
            else:
                print("{0}: Something went very wrong. Reason: {1}".format(api.me().screen_name, error.reason))

        except TypeError as error:
            print("{0}: Could not tweet file. Uploading failed.".format(api.me().screen_name))
        
        break


def follow_back(api, request_sent_table):
    """
    Retrieves a follower list of length num_followers and checks with the database to see if a
    follow request has been sent to the user in the past. If not, send the user a follow request.
    
    A follow request will ONLY be sent if a request has not been sent already. Users with
    protected accounts have one chance to accept, and users who unfollow and follow again will
    not be sent a second follow request.
    """
    try:
        # items() returns an iterator object. Copy the items from the iterator
        # into a regular list of followers.
        followers_iterator = tweepy.Cursor(api.followers).items(num_followers)
        followers = [follower for follower in followers_iterator]

        # Check if a follow request has already been sent, if not, then send a follow request
        for follower in followers:
            if not request_sent(request_sent_table, follower.id_str):
                try:
                    # Send the follow request
                    follower.follow()
                    update_request_sent(request_sent_table, follower.id_str, follower.screen_name)
                    print("{0}: Follow request sent to {1}".format(api.me().screen_name, follower.screen_name))

                except tweepy.error.TweepError as error:
                    if error.response is not None:
                        if error.response.status_code == 403:
                            # This error can occur if a previous follow request is sent to a protected account,
                            # and the request is still pending approval by the user. It can also occur if the
                            # user is blocking the account.
                            print("{0}: Could not follow user {1}. {2}".format(api.me().screen_name, follower.screen_name, error.reason))
                        elif error.response.status_code == 429:
                            print("{0}: Could not follow user. Request limit reached.".format(api.me().screen_name))
                        else:
                            print("{0}: Could not follow user. Error status code {1}".format(api.me().screen_name, error.response.status_code))

    except tweepy.error.TweepError as error:
        if error.response is not None:
            if error.response.status_code == 429:
                print("{0}: Could not follow user. Request limit reached.".format(api.me().screen_name))
            elif error.response.status_code == 500:
                print("{0}: Could not follow user. Twitter server error.".format(api.me().screen_name))
            elif error.response.status_code == 503:
                print("{0}: Could not follow user. Service unavailable.".format(api.me().screen_name))
            else:
                print("{0}: Could not follow user. Error status code {1}".format(api.me().screen_name, error.response.status_code))
        else:
            print("{0}: Something went very wrong. Reason: {1}".format(api.me().screen_name, error.reason))


def smart_queue(queue_table_name, recent_queue_table_name, recent_limit, prefix):
    """
    Randomly adds files to a queue table. However, this algorithm will
    attempt to ensure that the most recently posted files will not appear at the front
    of the queue. IMPORTANT: "front of the queue" in this instance means the newest files
    added to the table.

    The most recently posted files are kept in a table called [prefix]_recent_queue,
    where [prefix] is the screen_name of a twitter bot. The table length, at maximum,
    should be equal to a user limit defined in keys.json with the key "recent_limit".

    Valid files are drawn from the pool by excluding the recent files. This list is
    then shuffled, and a certain number (up to recent_limit) of those files are
    selected to be placed at the start of a list called new queue. The remaining
    files are mixed with the recent files to form the rest of the list.
    
    When building the new queue, the list is traversed in reverse order to make
    the aforementioned group of files go at the front of the queue.

    Arguments:
    ->queue - Name of the queue table
    ->recent_queue - Name of the recent queue table
    ->recent_limit -  Maximum number of files for the recent_queue table
    ->prefix - The AWS S3 folder in which to look for files

    Example argument list:
    'makomakorin_bot_queue', 'makomakorin_bot_recent_queue', 96, 'makoto'

    NOTE:
    Why do we create a temp2 list with the recent files instead of using recent_queue?
    This is because it is possible for recent_queue to contain files that are no
    longer in the regular file pool. This method ensures that no dead files are put
    into the queue.
    """
    new_queue = []

    # Fetch a list of the most recent files posted
    recent_queue = [row[0] for row in get_table_contents(recent_queue_table_name)]

    # Generate a list of files for the next queue
    response = client.list_objects(Bucket=bucket,Prefix=prefix)
    file_pool = [file['Key'] for file in response['Contents'] if not file['Key'].endswith('/')]

    # Split the files into two groups, shuffle the first group
    temp = [row for row in file_pool if row not in recent_queue]
    temp2 = [row for row in file_pool if row in recent_queue] # SEE NOTE IN THE COMMENT ABOVE
    random.shuffle(temp)

    # Determine how many files to place at the front
    end = len(temp) if len(temp) < recent_limit else recent_limit
    for i in range(end):
        new_queue.append(temp.pop())

    # Form the rest of the queue, and shuffle again
    temp = temp + temp2
    random.shuffle(temp)

    # Finish creating the queue
    new_queue = new_queue + temp

    # Push the queue to the table
    conn = create_connection()
    cur = conn.cursor()

    for filepath in new_queue[::-1]:
        timestamp = str(datetime.datetime.now())
        cur.execute("INSERT INTO {0} (filepath, timestamp) VALUES ('{1}', '{2}')".format(queue_table_name, filepath, timestamp))

    conn.commit()
    cur.close()
    conn.close()
    print("File queue {0} shuffled.".format(queue_table_name))


# Counts the number of rows in the table, returns count as an integer
def count_rows(table_name):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM {}".format(table_name))

    count = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return count


# Returns the newest row in the table (based on date of insertion)
def get_newest_row(table_name):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("SELECT filepath FROM {} ORDER BY timestamp DESC LIMIT 1".format(table_name))

    row = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return row


def delete_oldest_row(table_name, fieldname):
    """
    Delete oldest row in the table

    Takes table_name and fieldname strings. fieldname is the name of the column
    in the table called table_name which the function uses to order by date.
    Therefore, the column should be of an appropriate date type that can be ordered.

    Do not call this function on a table without a date field.
    """
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("""DELETE FROM {0}
                   WHERE {1}
                   IN (SELECT {1}
                       FROM {0}
                       ORDER BY {1}
                       ASC
                       LIMIT 1)""".format(table_name, fieldname))

    conn.commit()
    cur.close()
    conn.close()


# Delete a single row in the table
def delete_row(table_name, id):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM {} WHERE filepath = ('{}')".format(table_name, id))

    conn.commit()
    cur.close()
    conn.close()


# Delete all rows in the table, resulting in a valid, but empty table
def clear_table(table_name):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM {}".format(table_name))

    conn.commit()
    cur.close()
    conn.close()


def insert_recent(table_name, entry):
    """
    Insert entry into a recent_queue table. Each row should have a path to an file
    and a timestamp of when the insertion occurred.

    The timestamp is provided by Python's datetime module.
    """
    conn = create_connection()
    cur = conn.cursor()

    timestamp = str(datetime.datetime.now())

    cur.execute("INSERT INTO {0} (filepath, timestamp) VALUES ('{1}','{2}')".format(table_name, entry, timestamp))

    conn.commit()
    cur.close()
    conn.close()


# Helper function for creating a connection to the database
def create_connection():
    return psycopg2.connect(database=PARSED_URL.path[1:],
                            user=PARSED_URL.username,
                            password=PARSED_URL.password,
                            host=PARSED_URL.hostname,
                            port=PARSED_URL.port)


# Check if the given id is in a request_sent table (returns either True or False)
def request_sent(table_name, id):
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT id FROM {0} WHERE id = ('{1}')".format(table_name, id))

    status = cur.fetchone() is not None

    conn.commit()
    cur.close()
    conn.close()

    return status


# Push the id and screen name of the follower to the list of sent requests
def update_request_sent(table_name, id, screen_name):
    conn = create_connection()
    cur = conn.cursor()
    
    timestamp = str(datetime.datetime.now())

    cur.execute("INSERT INTO {0} (id, screen_name, timestamp) VALUES ('{1}','{2}','{3}')".format(table_name, id, screen_name, timestamp))

    conn.commit()
    cur.close()
    conn.close()


# Get all rows and columns of a table
def get_table_contents(table_name):
    conn = create_connection()
    cur = conn.cursor()

    entries = []

    cur.execute("SELECT * FROM {}".format(table_name))

    for row in cur.fetchall():
        entries.append(row)

    conn.commit()
    cur.close()
    conn.close()

    return entries


if __name__ == "__main__":
    main()