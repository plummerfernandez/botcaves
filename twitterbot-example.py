#### python retweet or fav twitterbot ####
###### by Matthew Plummer-Fernandez ######
# Based on:
#http://www.silkstream.net/blog/2014/06/retweeting-with-your-twython-twitter-bot.html

###make sure you have installed twython
#sudo apt-get install python dev
#sudo apt-get install python-pip
#sudo pip install twython
from twython import Twython, TwythonError
from threading import Event, Thread, Timer

### put in your own API Keys and auth codes here. Get them from:
## dev.twitter.com
## manage apps
## create new app
global twitter
print 'twitter client requested' 
twitter = Twython('XXXXXXX',  #API_KEY
				  'XXXXXXX', #APP_SECRET,
                  'XXXXXXX', #OAUTH_TOKEN, 
                  'XXXXXXX')#OAUTH_TOKEN_SECRET
                  


## FAVOURITE FUNCTION
def favbot():
	print "Doing fav function now"
	searchresults = twitter.search(q='money', count = 1)
	for item in searchresults["statuses"]:
		print "" 
		print item["text"]
		print item["id"]
		try:
			twitter.create_favorite(id = item["id_str"])
			print " I favorited it"
		except TwythonError as e:
			print e
		
		

## RETWEET FUNCTION
def retweetbot():
	print "Doing retweet function now"
	searchresults = twitter.search(q='#iiclouds', count = 1) #OR #lol -#fun
	for item in searchresults["statuses"]:
		print "" 
		print item["text"]
		print item["id"]
		try:
			twitter.retweet(id = item["id_str"])
		except TwythonError as e:
			print e

## METHOD TO RUN AT INTERVALS (NODE STYLE)
def call_repeatedly(interval, func, *args): ## you can pass arguments too which is useful
	global stopped
    stopped = Event()
    def loop():
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set

stopped = None
## just checking....
print " HELLO I AM WORKING"
## Run the porcess once immediately when we launch
favbot()

## SET TIMER
check_followers_timer = call_repeatedly(60, favbot) #seconds

while True:
	try:
		#whatever
	except KeyboardInterrupt:
		stopped.set()
		raise
