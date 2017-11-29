########################################
# - Title:   Ticker-Manager
# - Author:  Lukas Pichler
# - Date:    2017-11-29
########################################

import ticker

ticker_file = open("cfg/ticker_monitor.cfg")
kraken_file = open("cfg/kraken_ticker.cfg")

# process bittrex file
for line in ticker_file:
	market = line.replace("\n", "") # remove new line 
	ticker.get_ticker_for_name(market)
	
# process kraken file
for line in kraken_file:
	market = line.replace("\n", "") # remove new line 
	ticker.get_kraken_ticker_for_name(market)

ticker_file.close()
kraken_file.close()