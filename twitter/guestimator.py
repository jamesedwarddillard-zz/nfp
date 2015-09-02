""" turns twitter searches into guesses"""

from twitter_search import nfp_tweets
from tweet_class import Entries

def single_response_parser(statuses):
	tweet = statuses['text']
	user = statuses['user']['screen_name']
	created_at = statuses['created_at']
	return [tweet, user, created_at]

def main():
	statuses, number_of_tweets = nfp_tweets()
	print number_of_tweets
	guesses = []
	for i in range(0, number_of_tweets):
		status = statuses[i]
		entry = single_response_parser(status)
		print entry


if __name__ == '__main__':
	main()