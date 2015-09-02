import twitter_authorization
from twitter_urls import *
import requests
import json


def twitter_search():
	token = twitter_authorization.get_access_token()
	bearer_token = 'Bearer %s' % token
	payload = {'q': '#nfpguesses', 'count': 100}
	headers = {'Authorization': bearer_token}
	response = requests.get(SEARCH_ENDPOINT, params = payload, headers=headers)
	response_json = json.loads(response.text)
	return response_json

def twitter_statues(response):
	#strips out metadata from twitter search
	response = twitter_search()
	statuses = response['statuses']
	return statuses

def number_of_tweets(statuses):
	tweets = len(statuses)
	return tweets

def nfp_tweets():
	response = twitter_search()
	statuses = twitter_statues(response)
	tweets = number_of_tweets(statuses)
	return statuses, tweets

