import requests
from icalendar import Calendar
from datetime import datetime, date, time, timezone, timedelta
import pandas as pd
import os
from dotenv import load_dotenv

ICAL_URL = os.gotenv('GOOGLE_ICAL_URL')


response = requests.get(ICAL_URL)

summaryone = []


# change the date to datetime
def to_datetime(dt_or_d):
    if type(dt_or_d) is date:
        print('date changed to datetime ', dt_or_d)
        return datetime.combine(dt_or_d, time.min).astimezone(tz=timezone(timedelta(hours=9)))
    else: return dt_or_d

index = 0
# 2. Parse it
cal = Calendar.from_ical(response.content)

print(cal)

# 3. Loop through events
for event in cal.walk('VEVENT'):
    # 4. Get event data
    summary = event.get('summary')
    start = event.get('dtstart').dt
    end = event.get('dtend').dt
    summaryone.append({ 'starttime' : to_datetime(start), 'endtime': end,"eventname": summary})

filtered = sorted(summaryone, key = lambda x: x['starttime'])
df = pd.DataFrame(filtered)

print(df)

# def freetime(date):
#     if x == date:
#         listoftimes.append(x)

# def figureoutfree(listoftimes):
    
# def rangeofdates(df):

