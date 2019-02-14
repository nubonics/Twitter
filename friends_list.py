from friends_list import friends_list
from tweet_dumperv1 import get_all_tweets


def iter_friends_list():
	for friend in friends_list():
		get_all_tweets(friend)


if __name__ == "__main__":
	iter_friends_list()
