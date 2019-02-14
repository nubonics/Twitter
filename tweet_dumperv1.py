#!/usr/bin/env python
# encoding: utf-8

import datetime as DT
import jsonlines
import tweepy #https://github.com/tweepy/tweepy
import csv

with jsonlines.open('credentials.json','r') as reader:
	for obj in reader:
		consumer_key = obj['consumer_key']
		consumer_secret = obj['consumer_secret']
		access_key = obj['access_key']
		access_secret = obj['access_secret']



def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
	
	tweet_times = [[tweet.created_at] for tweet in alltweets]
	today = DT.date.today()
	week_ago = int((today - DT.timedelta(days=7)).strftime("%Y%m%d"))
	my_dict = dict()
	for tweet in alltweets:
			time_of_tweet = int(tweet.created_at.strftime("%Y%m%d"))
			if time_of_tweet - week_ago < 8 and time_of_tweet - week_ago > -1:
				with jsonlines.open('tweets.json','a') as writer:
					my_dict['user_id'] = tweet.id_str
					#my_dict['creation'] = tweet.created_at
					my_dict['tweet'] = tweet.text
					writer.write(my_dict)
	

if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets()
