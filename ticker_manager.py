########################################
# - Title:   Ticker-Manager
# - Author:  Lukas Pichler
# - Date:    2017-11-29
########################################

import ticker

ticker_file = open("cfg/ticker_monitor.cfg")

for line in ticker_file:
	market = line.replace("\n", "") # remove new line 
	ticker.get_ticker_for_name(market)

ticker_file.close()