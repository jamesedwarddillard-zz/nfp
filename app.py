import os
from flask import Flask
from bls_reader.bls_reader import bls_reader
from written_months import written_months
from current_report import current_report
port = int(os.environ.get('Port', 5000))

app = Flask(__name__)

@app.route("/")
def placeholder():
	return "Transmission of material in #nfpguess.es is embargoed."

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
	return "The jobs number for the most recent report ({}, {}) is {}{:,}. - #nfpguess.es".format(month, year, sign, jobs)

if __name__ == "__main__":
	app.run()