import sqlite3

# select data from kurs table
print("DB Test")
db = sqlite3.connect("data/BTC-LTC")

cursor = db.cursor()
cursor.execute("SELECT id, bid, ask FROM kurs")
all_rows = cursor.fetchall()
for row in all_rows:
	print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

db.close
