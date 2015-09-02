import twitter_authorization
from twitter_urls import *
import requests
import json

token = twitter_authorization.get_access_token()
bearer_token = 'Bearer %s' % token
payload = {'q': '#nfpguesses', 'count': 1}
headers = {'Authorization': bearer_token}

def twitter_search():
	token = twitter_authorization.get_access_token()
	bearer_token = 'Bearer %s' % token
	payload = {'q': '#nfpguesses', 'count': 1}
	headers = {'Authorization': bearer_token}
	response = requests.get(SEARCH_ENDPOINT, params = payload, headers=headers)
	response_json = json.loads(response.text)
	return response_json

def single_response_parser(response):
	tweet = response['statuses'][0]['text']
	user = response['statuses'][0]['user']['screen_name']
	created_at = response['statuses'][0]['created_at']
	return tweet, user, created_at


def main():
	""" Main function """
	response = twitter_search()
	tweet, user, created_at = single_response_parser(response)
	print tweet
	print user
	print created_at


if __name__ == "__main__":
	main()

