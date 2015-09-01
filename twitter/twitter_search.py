import twitter_authorization

token = twitter_authorization.get_access_token()

def main():
	""" Main function """
	token = twitter_authorization.get_access_token()
	return token


if __name__ == "__main__":
	main()

