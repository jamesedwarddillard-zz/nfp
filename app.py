import os
from flask import Flask
from bls_reader.bls_reader import bls_reader
from written_months import written_months
from current_report import current_report
from twitter.guestimator import response_generator, single_response_parser
port = int(os.environ.get('Port', 5000))

app = Flask(__name__)

@app.route("/")
def placeholder():
	return "Transmission of material in #nfpguesses is embargoed."

@app.route("/current")
def nfp():
	mos, year = current_report()
	month = written_months(mos)
	jobs = bls_reader(mos, year)
	sign = ''
	if jobs < 0:
		sign = '-'
	else:
		sign = '+'
	return "The jobs number for the most recent report ({}, {}) is {}{:,}. - #nfpguesses".format(month, year, sign, jobs)

@app.route("/guesses")
def guesses():
	statuses, number_of_tweets = response_generator()
	guesses = []
	for i in range(0, number_of_tweets):
		status = statuses[i]
		entry = single_response_parser(status)
		return entry[0], entry[1] 


if __name__ == "__main__":
	app.run()