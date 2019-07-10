import json, urllib.request
import time
from time import sleep
import tkinter

# Sample output:
# New earthquakes in last interval: 07/07/19 19:24
# >> 2.54  --  17km ESE of Little Lake, CA  --  3 minutes ago

window = tkinter.Tk()
window.title("SoCal Earthquake Feed")

def beginMonitor():
    main()

def parseEvents(features, timeNow, lastId) -> int:
    latBounds = [32.30, 35.95]
    longBounds = [-123.03, -114.00]
    # Bounds define a rough 2d square on the globe enclosing all of CA from 
    # San Luis Obispo, CA to Baja Mexico, MX; and the Pacific Ocean to Las Vegas, NV.

    for i, event in enumerate(features):
        timeSince = round((timeNow - event["properties"]["time"]) / 60000)
        currId = event["properties"]["code"]

        if lastId == currId:
            # No new updates, don't output list
            if i == 0:
                print(">> No new earthquakes")
            return features[0]["properties"]["code"]

        if i == 0:
            timeFmt = time.strftime('%D %H:%M')
            print("New earthquakes in last interval:", timeFmt)
            tkinter.Label(window, text = "Monitor is running...\n\n").pack()

        # Filter only locally-relevant results
        coords = event["geometry"]["coordinates"]
        if ((coords[0] > longBounds[0]) and (coords[0] < longBounds[1])) and \
            ((coords[1] > latBounds[0]) and (coords[1] < latBounds[1])):
            magnitude = event["properties"]["mag"]
            location = event["properties"]["place"]

            # New update in past hour, print and continue until lastId == currId
            output = ">> " + str(magnitude) + "  --  " + location + "  --  " + str(timeSince) + " minutes ago\n"
            print(output)
            tkinter.Label(window, text = output).pack()
    
    return features[0]["properties"]["code"]

def main():
    pollFreq = 55 * 1000 # time in ms between json requests
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'
    lastId = 0

    with urllib.request.urlopen(url) as geojson:
        jsonResponse = json.load(geojson)
        metadata = jsonResponse["metadata"]
        features = jsonResponse["features"]

        print("-- Retrieved GeoJSON --")

        lastId = parseEvents(features, metadata["generated"], lastId)

    window.after(pollFreq, main)

b_begin = tkinter.Button(window, text = "Begin monitoring", command = beginMonitor).pack()
window.mainloop()

# if __name__ == '__main__':
#     main()
