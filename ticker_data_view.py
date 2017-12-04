########################################
# - Title:   Ticker-Data-Viewer
# - Author:  Lukas Pichler
# - Date:    2017-11-29
########################################

import datetime
import sqlite3


import plotly
import plotly.graph_objs as go
import plotly
from plotly.graph_objs import Scatter, Layout


# calc sma
def sma(y_data, window):
	sma_y = []
	for i in range(len(y_data)):
		if i < window:
			continue
		else:
			try:
				sma_value = sum(y_data[i-window:i])/ window
				sma_y.append(sma_value)
			except:
				print("ERROR")
				print(y_data[i-window:i])
			
	return sma_y

# select data from kurs tabl
ticker = "kraken_XZECZEUR"
db_location = "data/" + ticker

db = sqlite3.connect(db_location)

cursor = db.cursor()
cursor.execute("SELECT id, bid, ask FROM kurs")
all_rows = cursor.fetchall()

data = []
x_data = []
y_data = []
for row in all_rows:
	print('{0};{1};{2}'.format(row[0], row[1], row[2]))
	data.append((row[0], row[1]))
	format_date = datetime.datetime.fromtimestamp(
        int(row[0])
    ).strftime('%Y-%m-%d %H:%M:%S')
	x_data.append(format_date)
	y_data.append(row[1])

db.close

#  fast sma
window_fast = 72
sma_fast_trace = go.Scatter(
	x = x_data[window_fast:],
	y = sma(y_data, window_fast),
	mode = 'lines',
	name = 'sma_fast'
)


# slow sma
window_slow = 480
sma_slow_trace = go.Scatter(
	x = x_data[window_slow:],
	y = sma(y_data, window_slow),
	mode = 'lines',
	name = 'sma_slow'
)

# normal data
data_trace = go.Scatter(
	x = x_data,
	y = y_data,
	mode = 'line',
	name = ticker
)

plot_data = [sma_fast_trace, sma_slow_trace, data_trace]

plotly.offline.plot({
	"data": plot_data,
	"layout": Layout(title=ticker)
})


