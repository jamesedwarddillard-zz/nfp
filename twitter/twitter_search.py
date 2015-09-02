import twitter_authorization
from twitter_urls import *
import requests
import json

token = twitter_authorization.get_access_token()
bearer_token = 'Bearer %s' % token
payload = {'q': '#nfpguesses', 'count': 1}
headers = {'Authorization': bearer_token}

def main():
	""" Main function """
	response = requests.get(SEARCH_ENDPOINT, params = payload, headers=headers)
	response_json = json.loads(response.text)
	tweet = response_json['statuses'][0]['text']
	user = response_json['statuses'][0]['user']['screen_name']
	print "{} - {}".format(tweet, user)


if __name__ == "__main__":
	main()

