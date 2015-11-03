""" logic for reading tweets and making them guesses """
import re

test_tweet = "170,000"

def guess_finder(tweet_text):
	if numb_k_find(tweet_text):
		guess = numb_k_transform(tweet_text)
		return guess
	elif full_number_find(tweet_text):
		guess = full_number_transform(tweet_text)
		return guess
	else:
		return "Sorry, we didn't get that"

def numb_k_find(tweet_text):
	searchObj = re.search('[0-9]*[K|k]', tweet_text, flags = 0)
	return searchObj

def numb_k_transform(tweet_text):
	searchObj = numb_k_find(tweet_text)
	match = searchObj.group()
	number = re.search('[0-9]*', match, flags = 0)
	guess = number.group()
	guess = int(guess)*1000
	return guess

def full_number_find(tweet_text):
	searchObj = re.search('170,000', tweet_text, flags = 0)
	return searchObj

def full_number_transform(tweet_text):
	searchObj = full_number_find(tweet_text)
	match = searchObj.group()
	number = re.sub(r'\D', "", match)
	guess = int(number)
	return guess

def main():
	print guess_finder(test_tweet)

if __name__ == '__main__':
	main()