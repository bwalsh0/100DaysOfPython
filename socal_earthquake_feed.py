import json, urllib.request
import time
from time import sleep

def parseEvents(features, timeNow, timeLast):
    for event in features:
        timeSince = round((timeNow - event["properties"]["time"]) / 60000)
        if timeLast == event["properties"]["time"]:
            print("No new updates")
            # no new updates, don't parse json
            return timeLast
        magnitude = event["properties"]["mag"]
        location = event["properties"]["place"]
        coords = event["geometry"]["coordinates"]

        print(magnitude, " -- ", location, " -- ", timeSince, "minutes ago")
        # new update in past hour, update counter
        return event["properties"]["time"]
        # for i in range(2):
        #     if event[i]

def main():
    pollFreq = 55 # time in sec. between json requests
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'
    runtimeCount = 0
    timeLast = 0

    latBounds = [32.30, 35.95]
    longBounds = [-123.03, -114.00]

    while True:
        with urllib.request.urlopen(url) as geojson:
            jsonResponse = json.load(geojson)
            metadata = jsonResponse["metadata"]
            currentCount = metadata["count"]
            features = jsonResponse["features"]

            print("Retrieved GeoJSON")

            print("New earthquakes in last hour")
            timeLast = parseEvents(features, metadata["generated"], timeLast)

        sleep(pollFreq)

if __name__ == '__main__':
    main()
