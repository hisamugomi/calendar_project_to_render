from django.shortcuts import render
from datetime import datetime, timedelta, timezone, date
import cal

busy_events =  [
    {"start": datetime(2025, 10, 22, 10, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 16, 30, tzinfo=timezone.utc), "label": "Busy"},
    {"start": datetime(2025, 10, 22, 16, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 17, 0, tzinfo=timezone.utc), "label": "Meeting"},
    {"start": datetime(2025, 10, 22, 21, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 13, 30, tzinfo=timezone.utc), "label": "✅ Coding"},
]


# Create your views here.
def fill_schedule_free(busy_events):
    day_schedule = []
    
    for i in range(len(busy_events)):
        # Add the busy event itself
        day_schedule.append(busy_events[i])
        
        # 2. Check for a gap between this event and the next one
        if i < len(busy_events) - 1:
            current_end = busy_events[i]['end']
            next_start = busy_events[i+1]['start']
            
            if next_start > current_end:
                # We found a gap! Create a "Free" event
                day_schedule.append({
                    "start": current_end,
                    "end": next_start,
                    "label": "free",
                    "type": "free"  # We'll use this for the CSS class
                })
        elif busy_events[i]['end']: day_schedule.append({
            "start": busy_events[i]['end'],
            "end": datetime(2025, 10, 23, 20, 0, tzinfo=timezone.utc),
            "label": "free",
            "type": "free"  # We'll use this for the CSS class
        })
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
    free_times = cal.free_times
    return free_times 
def home(request):
    context = {
        'message': welcome_message(),
        'free_times' : free_times,
        'day_schedule' : get_full_schedule(busy_events),
        'status': 'Success'
    }
    return render(request, 'hello.html', context)