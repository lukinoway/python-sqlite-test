########################################
# - Title:   Ticker-Data-Viewer
# - Author:  Lukas Pichler
# - Date:    2017-12-04
########################################
import datetime
import sqlite3


def strategy(dataset, percentage, window, startamount):
	#print('strategy: percentage = {0}'.format(percentage))
	high = 0
	low = 0
	
	buy = 0
	sell = 0
	
	total_profit = 0
	orders = []
	amount = startamount
	for i in range(0, len(dataset), 12):
		if i < window:
			continue
		else:
			if low > data[i][1] or low == 0:
				low = data[i][1]
			if high < data[i][1]:
				high = data[i][1]
				
			# order handling
			if data[i][1] > low*(1 + percentage/100) and buy == 0:
				buy = data[i][1]
				#print(data[i])
				
			if data[i][1] < high*(1 - percentage/2/100) and buy > 0:
				sell = data[i][1]
				#print(data[i])
				
			if buy > 0 and sell > 0:
				#print('found order')
				
				profit = (sell-buy)/ buy * 100
				#print('buy: {0}; sell: {1}; profit: {2}'.format(buy, sell, profit))
				orders.append((buy, sell, profit))
				total_profit = total_profit + profit
				amount = amount * (1 + profit / 100)
				#print('amount: {0}'.format(amount))
				
				# reset values
				low = 0
				high = 0
				buy = 0
				sell = 0
	
	#print('total profit %: {0}'.format(total_profit))
	#print('start amount: {0}, final amount: {1}'.format(startamount, amount))
	print('{0};{1};{2};'.format(window, percentage, total_profit))
# select data from kurs tabl
ticker = "kraken_XETHZEUR"
print(ticker)
db_location = "data/" + ticker

db = sqlite3.connect(db_location)

cursor = db.cursor()
cursor.execute("SELECT id, bid, ask FROM kurs")
all_rows = cursor.fetchall()

data = []
for row in all_rows:
	format_date = datetime.datetime.fromtimestamp(
        int(row[0])
    ).strftime('%Y-%m-%d %H:%M:%S')
	data.append((format_date, row[1]))

db.close

# test strategy
print("window;percentage;total_profit;")
for window in range(12, 49, 12):
	#print("---------------------------------------------------")
	#print('window: {0}'.format(window))
	for i in range(2,11):
		#print("------")
		strategy(data, i, window, 100)