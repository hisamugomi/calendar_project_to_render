import pandas as pd
from datetime import datetime, date, time, timezone
calendar_events = [
    {"start": datetime(2025, 10, 22, 1, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 6, 30, tzinfo=timezone.utc), "label": "Busy"},
    {"start": datetime(2025, 10, 22, 8, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 9, 0, tzinfo=timezone.utc), "label": "Meeting"},
    {"start": datetime(2025, 10, 22, 9, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 10, 0, tzinfo=timezone.utc), "label": "Part-time"},
    {"start": datetime(2025, 10, 22, 12, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 13, 30, tzinfo=timezone.utc), "label": "✅ Coding"},
    {"start": datetime(2025, 10, 23, 1, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 23, 2, 0, tzinfo=timezone.utc), "label": "Busy"}
]

#The main function to find the free time 
def freetime(date):
    if x == date:
        listoftimes.append(x)
# The function to find the free time from the list of busy times
def figureoutfree(listoftimes):
    for i in range(len(listoftimes) -1):
        current_event_end = listoftimes[i]['end']
        next_event_start = listoftimes[i+1]['start']

        print(f"After {listoftimes[i]['label']} slot between {current_event_end} & {next_event_start}")

# # Given the df, give us the range of dates to check
# def rangeofdates(df):


# Given the date, figure out the list of times that are occupied
def findlistoftimes(events, targetdate): 
    targetdateevents = [e for e in events if e['start'].date() == targetdate]
    return targetdateevents

figureoutfree(
findlistoftimes(calendar_events, date(2025, 10, 22))
)
#List out what is needed for today
def todaytasks(listoftimes):

    for i in range(len(listoftimes) -1):
        events = []
        current_event_start = listoftimes[i]['start']
        current_event_end = listoftimes[i]['end']

        events.append(f"{listoftimes[i]['label']}")

    return(
    )