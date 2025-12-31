from django.shortcuts import render
from datetime import datetime, timedelta, timezone, date
import os
import cal
from dotenv import load_dotenv

Calkey = os.getenv("GOOGLE_ICAL_URL")
Caljs = os.getenv("Calendar_JScode")

busy_events =  [
    {"start": datetime(2025, 10, 22, 10, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 16, 30, tzinfo=timezone.utc), "label": "Busy"},
    {"start": datetime(2025, 10, 22, 16, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 17, 0, tzinfo=timezone.utc), "label": "Meeting"},
    {"start": datetime(2025, 10, 22, 21, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 13, 30, tzinfo=timezone.utc), "label": "✅ Coding"},
]


# Create your views here.

def makesched(events):
    day_schedule = []
    for i in range(len(events)):
        # Add the busy event itself
        day_schedule.append(events[i])
        
        # 2. Check for a gap between this event and the next one
        if i < len(events) - 1:
            current_end = events[i]['end']
            next_start = events[i+1]['start']
            
            if next_start > current_end:
                # We found a gap! Create a "Free" event
                day_schedule.append({
                    "start": current_end,
                    "end": next_start,
                    "label": "free",
                    "type": "free"  # We'll use this for the CSS class
                })
        elif events[i]['end']: day_schedule.append({
            "start": events[i]['end'],
            "end": datetime(2025, 10, 23, 20, 0, tzinfo=timezone.utc),
            "label": "free",
            "type": "free"  # We'll use this for the CSS class
        })
    return day_schedule

def fill_schedule_free(calkey):
    busy_events = cal.todaysevents(calkey)

    day_schedule = makesched(busy_events)
    return day_schedule
#I want to create it so that it shows a full days worth of schedules with hours. Ideally takes the day schedule from function fill_schedule_free
def full_schedule(days_sche):
    #Get the date
    targetday = date(days_sche[0]["start"])
    full_schedule = []
    # #Loops through every hour.
    # for i in range(1,24):
    #     #1. Need to check if i o'clock is occupied, if occupied, give us a json 
    #     #of what is in that timeslot, and put it into the full_schedule array / list
    #     #How do I change the i into an hour. and I need to pass the hour to check 
    #     # if it is occupied             
        
    return
    
def get_full_schedule(events):
    return events

def welcome_message():
    message = f"Welcome Hisamu, \n {datetime.today().date()}"
    return message
def free_times():
    free_times = busy_events

    return free_times 
def home(request):
    context = {
        'message': welcome_message(),
        'free_times' : free_times(),
        'schedules' : makesched(busy_events),
        'full_schedule' : fill_schedule_free(Calkey),
        'status': 'Success',
        'caljs' : Caljs
    }
    return render(request, 'hello.html', context)