""" turns twitter searches into guesses"""

from twitter_search import nfp_tweets
from tweet_class import Entries

def single_response_parser(statuses):
	tweet = statuses['text']
	user = statuses['user']['screen_name']
	created_at = statuses['created_at']
	guess = "foo"
	entry = {
	"tweet": tweet,
	"user": user,
	"created_at": created_at,
	"guess": guess
	}
	return entry

def response_generator(statuses, number_of_tweets):
	entry_list = []
	for i in range(0, number_of_tweets):
		entry = single_response_parser(statuses[i])
		entry_list.append(entry)
	return entry_list

def main():
	statuses, number_of_tweets = nfp_tweets()
	entry_list = response_generator(statuses, number_of_tweets)
	for entry in entry_list:
		print entry['tweet'], entry['user'], entry ['guess']

if __name__ == '__main__':
	main()