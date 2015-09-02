import twitter_authorization
from twitter_urls import *
import requests
import json


def twitter_search():
	token = twitter_authorization.get_access_token()
	bearer_token = 'Bearer %s' % token
	payload = {'q': '#nfpguesses'}
	headers = {'Authorization': bearer_token}
	response = requests.get(SEARCH_ENDPOINT, params = payload, headers=headers)
	response_json = json.loads(response.text)
	return response_json

def number_of_tweets(response):
	statuses = response['statuses']
	tweets = len(statuses)
	return tweets

def nfp_tweets():
	response = twitter_search()
	tweets = number_of_tweets(response)
	return response, tweets

