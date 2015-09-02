import twitter_authorization
from twitter_urls import *
import requests
import json

token = twitter_authorization.get_access_token()
bearer_token = 'Bearer %s' % token
payload = {'q': '#nfpguesses', 'count': 10}
headers = {'Authorization': bearer_token}

def main():
	""" Main function """
	response = requests.get(SEARCH_ENDPOINT, params = payload, headers=headers)
	response_json = json.loads(response.text)
	print response.status_code
	print response_json


if __name__ == "__main__":
	main()

