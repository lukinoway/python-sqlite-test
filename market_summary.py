########################################
# - Title:   Bittrex-Market-Summary
# - Author:  Lukas Pichler
# - Date:    2017-11-29
########################################

from bittrex import Bittrex
import json

my_bittrex = Bittrex(None, None)

result = my_bittrex.get_market_summaries()
parsed_json = json.dumps(result)
json_data = json.loads(parsed_json)

data = []

for entry in json_data["result"]:
	
	market = entry["MarketName"]
	prev_day = entry["PrevDay"]
	bid = entry["Bid"]
	change_rate = bid - prev_day
	
	if bid > 0.0:
		change_percent = change_rate/bid*100
		
		print("-------------------------------------------")
		print(market)
		print("PREV_DAY:", prev_day)
		print("CURRENT:", bid)
		print("CHANGE:", change_rate)
		print("CHANGE_RATE:", change_percent)
		
		data.append((market, bid, prev_day, change_percent))
		

# sort data by change_rate
heros = sorted(data, key=lambda x: x[3], reverse=True)
zeros = sorted(data, key=lambda x: x[3])

print("----------- HEROS -------------")
for i in range(0,9):
	print(heros[i])

print()	
print("----------- ZEROS -------------")
for i in range(0,9):
	print(zeros[i])
