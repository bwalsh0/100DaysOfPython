import json
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import matplotlib.mlab as mlab
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

# calculate msg streak
streakEnd = []
for i in range(len(timestamps) - 1):
    if (timestamps[i+1] - timestamps[i]) > 1:
        streakEnd.append(timestamps[i]) # last day of streak

if not streakEnd:
    print("No missed days")
else:
    print(*streakEnd, sep=', ')

(mu, sigma) = norm.fit(timestamps)

plt.hist(timestamps,
         bins=80,
         align='mid')
y = mlab.normpdf(80, mu, sigma)
l = plt.plot(80, y, 'r--', linewidth=2)
plt.grid(True)
plt.axis([0, 730, 0, 2000])
plt.ylabel('Msg count')
plt.xlabel('Day since first message')
plt.text(75, 1600, 'bin=3.5days')
plt.show()

# Graphs messages by frequency per day of year - some values hardcoded.
# bins=80 where each bar on graph represents 3-4 days.
# (x,y) where (day,msgItemCount)
