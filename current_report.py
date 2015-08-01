""" Identifies the current BLS report Month and Year based on the 
current date and time"""

import datetime



def current_report():
	current_date = datetime.datetime.now().date()
	current_time = datetime.datetime.now().date()

	mos = 7
	year = 1986
	return (mos, year)


