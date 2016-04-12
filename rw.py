import httplib
import httplib2
import urllib
import urllib2
import base64
import sys
import json
import random
import time

uid = "17018"
key = "Fb25c7QCcd"
sid = "5"
per_page=20
num_page=12
ratings = ["3.0", "3.5", "4.0"]

rw = httplib.HTTPConnection("rainwave.cc",80)
counter = 0

for page in range(num_page):
	#Requests unrated songs, 20 at a time
	rw.request("POST", "/api4/unrated_songs?user_id={}&key={}&sid={}&per_page={}".format(uid, key, sid, per_page))
	resp = rw.getresponse()
	#print resp.status, resp.reason

	for song in json.loads(resp.read())["unrated_songs"]:
		counter+=1
		rating = random.choice(ratings)
		#print "#{} Rating song {} from album {} with a {}".format(counter, song["title"], song["album_name"], rating)
		print "#{} Rating song #{} with a {}".format(counter, song["id"], rating)
		
		rw.request("POST", "/api4/rate?user_id={}&key={}&sid={}&rating={}&song_id={}".format(uid, key, sid, rating, song["id"]))
		resp = rw.getresponse()
		#print resp.status, resp.reason
		rw.close()
		time.sleep(0.1)
	
rw.close()
