""" A data class for NFP guess tweets """

class Entries(object):
	def __init__(self, tweet, user, utc_time):
		self.tweet = tweet
		self.user = user
		self.utc_time = utc_time
		self.guess = 'foo'