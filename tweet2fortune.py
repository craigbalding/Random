#!/usr/bin/python
import sys, textwrap 

try:
    import twitter
except ImportError:
    print """Could not import twitter module.  Run "sudo easy_install twitter" to install"""
    sys.exit(1)

try:
    twit = sys.argv[1]
    if twit == '-h' or twit == '--help':
        raise IndexError
except IndexError:
    print """usage: tweetfortune.py twitter_handle > output_filename
To create a valid fortune file run: strfile output_filename
To get a fortune from the generated fortune file: fortune output_filename"""
    sys.exit(1)

# Grab ze timeline
c = twitter.Twitter()
try:
    timeline = c.statuses.user_timeline(id=twit,count=100)
except:
    print "Something went wrong talking to twitter (valid twitter username?).  Bye!"
    sys.exit(1)

# Format ze timeline in la fortuna style
for entry in timeline:
    tweet = entry['text']
    # Skip replies and old style retweets
    if tweet.startswith(('RT','@','.@','. ',' ')):
        continue
    # Skip tweets with URLs - we're seeking wisdom, not resources...
    if tweet.find('://') > -1:
        continue
    tweet = textwrap.fill(tweet)
    print "%s\n                            -- @%s\n%%" % (tweet.encode("ascii", "replace"),twit)

