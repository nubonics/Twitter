import argparse
from screen_names import sname
from tweet_dumperv1 import get_all_tweets
from iter_friends_list import iter_friends_list


parser = argparse.ArgumentParser()
parser.add_argument('--screen_name', type=str, help='The screen name of the person you wish to scrape information on.')
args = parser.parse_args()
screen_name = args.screen_name


def main(screen_name):
	sname(screen_name)
	iter_friends_list
	
	
if __name__ == "__main__":
	main(screen_name)
