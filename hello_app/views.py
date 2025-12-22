from django.shortcuts import render
from datetime import datetime, timedelta, timezone, date

busy_events =  [
    {"start": datetime(2025, 10, 22, 10, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 16, 30, tzinfo=timezone.utc), "label": "Busy"},
    {"start": datetime(2025, 10, 22, 16, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 17, 0, tzinfo=timezone.utc), "label": "Meeting"},
    {"start": datetime(2025, 10, 22, 21, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 13, 30, tzinfo=timezone.utc), "label": "✅ Coding"},
]

# Create your views here.
def get_full_schedule(busy_events):
    full_schedule = []
    
    for i in range(len(busy_events)):
        # Add the busy event itself
        full_schedule.append(busy_events[i])
        
        # 2. Check for a gap between this event and the next one
        if i < len(busy_events) - 1:
            current_end = busy_events[i]['end']
            next_start = busy_events[i+1]['start']
            
            if next_start > current_end:
                # We found a gap! Create a "Free" event
                full_schedule.append({
                    "start": current_end,
                    "end": next_start,
                    "label": "free",
                    "type": "free"  # We'll use this for the CSS class
                })
        elif busy_events[i]['end']: full_schedule.append({
            "start": busy_events[i]['end'],
            "end": datetime(2025, 10, 23, 20, 0, tzinfo=timezone.utc),
            "label": "free",
            "type": "free"  # We'll use this for the CSS class
        })
    return full_schedule

def welcome_message():
    message = f"Welcome Hisamu, \n {datetime.today().date()}"
    return message

def home(request):
    context = {
        'message': welcome_message(),
        'full_schedule' : get_full_schedule(busy_events),
        'status': 'Success'
    }
    return render(request, 'hello.html', context)