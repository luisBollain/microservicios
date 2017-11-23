import os
from flask import Flask, abort, render_template, request
import urllib, json
from twython import Twython

app = Flask(__name__)

@app.route("/api/v1/twitter")
def get_tweets():  
  consumer_key = "i4696DEhzA9K2ZIhke25TC8Jp"
  consumer_secret = "r1ciwC4QgPva74K6v1pDNFK9m7kcVdPiWSEPnC27XGUP9ZeW4o"
  access_token = "2579335548-yWOg5bk5lltKfKZ98XPv0ZjvJnSk3Pti7rFCgtK"
  access_token_secret = "iKzAlhMBZZPFwv1l3ulp9uK1ndLxFdExFmMNyTVWtgfxM"

  twitter = Twython(consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)
  
	query = request.args.get('q')
	result = self.twitter.search(q=query)
  	
  	tweets = result['statuses']
	return tweets

if __name__ == '__main__':
   	
    port = int(os.environ.get('PORT', 8084))
    
    app.debug = True
    
    app.run(host='0.0.0.0', port=port)
