from bittrex import Bittrex
import json
import sqlite3
import time

my_bittrex = Bittrex(None, None)  # or defaulting to v1.1 as Bittrex(None, None)
#print(my_bittrex.get_markets())
result = my_bittrex.get_ticker("BTC-LTC")
print(result)
parsed_json = json.dumps(result)
print(parsed_json)

t = json.loads(parsed_json)
bid = t["result"]["Bid"]
ask = t["result"]["Ask"]

print(bid)
print(ask)

print(int(time.time()))

print("DB Test")
db = sqlite3.connect("data/BTC-LTC")

cursor = db.cursor()
cursor.execute("CREATE TABLE if not exists kurs(id INTEGER PRIMARY KEY, bid DECIMAL, ask DECIMAL)")
db.commit()

# insert data
cursor.execute('''INSERT INTO kurs(id, bid, ask) VALUES(?,?,?)''', (int(time.time()), bid, ask))
print("inserted data")
db.commit()

db.close
