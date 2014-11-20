# DAX / FTSE COMPARISON, updates every 10 seconds.
# finance.google.com scraper
# can also be used to track specific quotes such as:
#("GOOG","NASDAQ") 


import urllib2
import json
import time
import datetime

class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
    
    def get(self,symbol,exchange):
        url = self.prefix+"%s:%s"%(exchange,symbol)
        #print url
        u = urllib2.urlopen(url)
        content = u.read()
        content = unicode(content, errors='ignore')
        
        obj = json.loads(content[3:])
        return obj[0]
        
        
if __name__ == "__main__":
    c = GoogleFinanceAPI()
    
    while 1:     
        print '______________________________'
        print datetime.datetime.now()
        quote = c.get("UKX","INDEXFTSE")
        print "FTSE = " + str(quote['l'])
        quote = c.get("DAX","INDEXDB")
        print "DAX = " + str(quote['l'])
        time.sleep(10)
        
