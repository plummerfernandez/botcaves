# A little script to get my followers twitter IDs 
# and display them next to their screen_name (twitter handle)

from twython import Twython, TwythonError
from threading import Event, Thread, Timer

global twitter
print 'twitter client requested' 
twitter = Twython('XXXXXXX',  #API_KEY
				  'XXXXXXX', #APP_SECRET,
                  'XXXXXXX', #OAUTH_TOKEN, 
                  'XXXXXXX')#OAUTH_TOKEN_SECRET
                  


myFollowers = twitter.get_followers_ids(id = "XXXX", count=50) #last 50 followers

for follower in myFollowers["ids"]:
	print follower
	myfriend = twitter.show_user(id = follower)
	print myfriend["screen_name"]
	print "" 
