########################################
# - Title:   Ticker-Data-Viewer
# - Author:  Lukas Pichler
# - Date:    2017-11-29
########################################

import datetime
import sqlite3
import plotly
from plotly.graph_objs import Scatter, Layout

# select data from kurs table

ticker = "BTC-XLM"
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

plotly.offline.plot({
    "data": [Scatter(x=x_data, y=y_data)],
    "layout": Layout(title=ticker)
})




