########################################
# - Title:   Ticker
# - Author:  Lukas Pichler
# - Date:    2017-11-29
########################################

from bittrex import Bittrex
import json
import sqlite3
import time

my_bittrex = Bittrex(None, None)


# function to get bid/ask info for given market and stores the data in sqlite db
def get_ticker_for_name(market_name):

	result = my_bittrex.get_ticker(market_name)
	parsed_json = json.dumps(result)

	t = json.loads(parsed_json)
	bid = t["result"]["Bid"]
	ask = t["result"]["Ask"]

	db_location = "data/" + market_name
	db = sqlite3.connect(db_location)

	cursor = db.cursor()
	cursor.execute("CREATE TABLE if not exists kurs(id INTEGER PRIMARY KEY, bid DECIMAL, ask DECIMAL)")
	db.commit()

	# insert data
	cursor.execute('''INSERT INTO kurs(id, bid, ask) VALUES(?,?,?)''', (int(time.time()), bid, ask))
	db.commit()

	db.close