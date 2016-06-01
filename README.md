#imas765probot
## About

imas765probot is a script that runs several image bots on Twitter.

https://twitter.com/makomakorin_bot  
https://twitter.com/harurun_bot_  
https://twitter.com/chihaya_bot_  
https://twitter.com/yayoicchi_bot  
https://twitter.com/iorin_bot_  
https://twitter.com/amimami_bot  
https://twitter.com/yukipyon_bot  
https://twitter.com/ohimechin_bot  
https://twitter.com/mikimiki_bot_  
https://twitter.com/hibikin_bot_  
https://twitter.com/azusa_bot__  
https://twitter.com/ricchan_bot_  

imas765probot runs on Python 3 and uses a modified version of the tweepy library to interact with Twitter. The script is hosted on Heroku and tweets every hour on the dot. In addition, the script checks for new followers every 30 minutes and will attempt to follow back new followers.

File assets are stored on Amazon S3 and are downloaded to the local filesystem at the time of tweeting. The Boto 3 API is used to access and interact with Amazon Web Services.

I used herokupostgres to store file queues instead of keeping the queues in memory. This is done because Heroku worker dynos are cycled every 24 hours. Using a persistent database allows the queues to be preserved in between cycles.

Contact me at https://twitter.com/Saiyushu for feedback, suggestions, submissions, or anything else.
