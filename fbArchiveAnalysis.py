import json
import matplotlib.pyplot as plt
import pandas as pd
import pandas.plotting._converter as pandacnv
pandacnv.register()

timestamps = []

with open('message_1.json') as file:
    jsonObj = json.load(file)
    msgs = jsonObj["messages"]
    for i in msgs:
        timestamp = pd.to_datetime(i["timestamp_ms"], unit='ms')
        doy = timestamp.dayofyear - 320

        doy = ((timestamp.year - 2017) * 365) + doy

        timestamps.append(doy)

        # if 'content' in msgs:
        #     print(i["content"])
        # wordcloud


plt.hist(timestamps, bins=80)
plt.show()

# Graphs messages by frequency per day of year - some values hardcoded.
# bins=80 where each bar on graph represents 3-4 days.
# (x,y) where (day,msgItemCount)
