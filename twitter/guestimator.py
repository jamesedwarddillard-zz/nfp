""" turns twitter searches into guesses"""

from twitter_search import nfp_tweets

response, tweets = nfp_tweets()

def single_response_parser(response):
	tweet = response['statuses'][0]['text']
	user = response['statuses'][0]['user']['screen_name']
	created_at = response['statuses'][0]['created_at']
	return tweet, user, created_at

def main():
	print tweets

if __name__ == '__main__':
	main()