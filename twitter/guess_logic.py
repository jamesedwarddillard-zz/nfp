""" logic for reading tweets and making them guesses """
import re

test_tweet = "170k #nfpguesses"

def guess_generator(tweet_text):
	searchObj = re.search('[0-9][K|k]', tweet_text, flags = 0)
	if searchObj:
		guess = "guess identified"
	else:
		guess = "Sorry, we didn't get that"
	return guess

def main():
	print guess_generator(test_tweet)

if __name__ == '__main__':
	main()