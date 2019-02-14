import oauth2 as oauth
import json
import jsonlines

with jsonlines.open('credentials.json','r') as reader:
	for obj in reader:
		consumer_key = obj['consumer_key']
		consumer_secret = obj['consumer_secret']
		access_key = obj['access_key']
		access_secret = obj['access_secret']

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
ACCESS_TOKEN = oauth.Token(key=access_key, secret=access_secret)
client = oauth.Client(consumer, ACCESS_TOKEN)

screen_name = str()
def sname(screen_name):
	timeline_endpoint = "https://api.twitter.com/1.1/friends/list.json?screen_name={}".format(screen_name)
	response, data = client.request(timeline_endpoint)
	tweets = json.loads(data)
	with jsonlines.open('twitter.json','a') as writer:
		writer.write(tweets)
		

if __name__ == "__main__":
	sname()