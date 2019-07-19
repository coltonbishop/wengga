from gap import *
import sys


def load_new_data():

	clear()
	# Large corpus of english Text for Which Transled Data Does Not Yet Exist
	english_sources = ["data/book1.txt", "data/book2.txt", "data/book3.txt"]
	# English Text for Which Transled Data Exists
	translated_sources = ["data/book4.txt", "data/book5.txt"]
	read_in(english_sources, translated_sources)

# load_new_data()

# x = get_phrases()

load_new_data()

# print x[0][1000]
for k in range(0,3):
	print critical_phrase()
