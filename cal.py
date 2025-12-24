import requests
from icalendar import Calendar
from datetime import datetime, date, time, timezone, timedelta
import pandas as pd
import os
from dotenv import load_dotenv
import calll

load_dotenv()
ICAL_URL = os.getenv('GOOGLE_ICAL_URL')

calendar_events = [
    {"start": datetime(2025, 10, 22, 1, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 6, 30, tzinfo=timezone.utc), "label": "Busy"},
    {"start": datetime(2025, 10, 22, 8, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 9, 0, tzinfo=timezone.utc), "label": "Meeting"},
    {"start": datetime(2025, 10, 22, 9, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 10, 0, tzinfo=timezone.utc), "label": "Part-time"},
    {"start": datetime(2025, 10, 22, 12, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 13, 30, tzinfo=timezone.utc), "label": "✅ Coding"},
    {"start": datetime(2025, 10, 23, 1, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 23, 2, 0, tzinfo=timezone.utc), "label": "Busy"}
]

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

# print(cal)

# 3. Loop through events
for event in cal.walk('VEVENT'):
    # 4. Get event data
    summary = event.get('summary')
    start = event.get('dtstart').dt
    end = event.get('dtend').dt
    summaryone.append({ 'starttime' : to_datetime(start), 'endtime': end,"eventname": summary})

filtered = sorted(summaryone, key = lambda x: x['starttime'])
df = pd.DataFrame(filtered)

# print(df)
free_times = calll.list_free_times(calendar_events)
print(free_times)
