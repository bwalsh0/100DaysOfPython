import csv
import time
import datetime
"""
Pulls date and subject columns from a .csv and creates a reminders
Date format: (mm/dd/yyyy, 07/12/2019)

Intended for large spreadsheets with deadlines, such as a course
syllabus/schedule or job application spreadsheet

Refresh interval is hourly by default, variable 'refreshRate'
Work in progress, purpose is to practice .csv parsing

Still needs to handle:
- Multiple events for one day
- Input sanitization
- Proper notification alert
"""

refreshRate = 60 * 60 # 1 hour, 3600 seconds

while True:
    reminderList = []
    eventList = []

    with open(".\\internship_apps_2019_megadoc.csv") as csvfile:
        sheet = csv.DictReader(csvfile)
        for row in sheet:
            # get date from each row
            reminderList.append(row['Date'])
            eventList.append(row['Company Name'])
        csvfile.close()

    currDatetime = datetime.datetime.now().strftime("%m/%d/%Y")
    print(currDatetime)

    for index, reminder in enumerate(reminderList):
        if currDatetime == reminder:
            # send alert (only print for now, sys notification later)
            print(reminder, "--", eventList[index])

    time.sleep(refreshRate)
