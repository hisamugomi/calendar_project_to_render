import pandas as pd
from datetime import datetime, date, time, timezone, timedelta

calendar_events = [
    {"start": datetime(2025, 10, 22, 8, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 9, 0, tzinfo=timezone.utc), "label": "Meeting"},
    {"start": datetime(2025, 10, 22, 9, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 10, 0, tzinfo=timezone.utc), "label": "Part-time"},
    {"start": datetime(2025, 10, 22, 12, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 22, 13, 30, tzinfo=timezone.utc), "label": "✅ Coding"},
    {"start": datetime(2025, 10, 23, 10, 0, tzinfo=timezone.utc), "end": datetime(2025, 10, 23, 15, 0, tzinfo=timezone.utc), "label": "Busy"}
]


def to_datetime(dt_or_d):
    if type(dt_or_d) is date:
        print('date changed to datetime ', dt_or_d)
        return datetime.combine(dt_or_d, time.min).astimezone(tz=timezone(timedelta(hours=9)))
    else: return dt_or_d

# The function to find the free time from the list of busy times
def figureoutfree(listoftimes):
    freetimes = []
    for i in range(len(listoftimes) -1):
        current_event_end = listoftimes[i]['end']
        next_event_start = listoftimes[i+1]['start']
        if current_event_end < next_event_start :
            freetimes.append(f"After {listoftimes[i]['label']} slot between {current_event_end} & {next_event_start}")
    return freetimes
# # Given the df, give us the range of dates to check
# def rangeofdates(df):


# Given the date, figure out the list of times that are occupied
def findlistoftimes(events, targetdate): 
    targetdateevents = [e for e in events if e['start'].date() == targetdate]
    return targetdateevents

#List out what is needed for today
def todaytasks(listoftimes):

    events = []
    for i in range(len(listoftimes) -1):
        current_event_start = listoftimes[i]['start']
        current_event_end = listoftimes[i]['end']

        events.append(f"{listoftimes[i]['label']}")
    return(events)

#Main funciton to return the free times.
def list_free_times(calendar_events):
    return figureoutfree(findlistoftimes(calendar_events, date(2025, 10, 22)))
#This function fills the schedule for an event each hour
def fillsched(targetday, event, full_sched):
    eventtime = event["end"] - event["start"]
    starttime = event["start"].time() 
    totalhours = int(eventtime.total_seconds()/ 3600)
    for i in range(totalhours):
        full_sched.append({
            "start" : datetime.combine(targetday, time(int(starttime.strftime("%H")), 0), tzinfo=timezone.utc),
            "end" : datetime.combine(targetday, time(int(starttime.strftime("%H")) + 1, 0), tzinfo=timezone.utc),
            "label" : event['label']
        })
    return full_sched
def fillfree_til(targetday, event, hour, full_sched):
    untilfirstevent = event["start"] - datetime.combine(targetday, time(hour, 0), tzinfo=timezone.utc)
    hourdifference = int(untilfirstevent.total_seconds()/3600)
    for l in range(0, hourdifference):
        full_sched.append({
            "start" : datetime.combine(targetday, time(l+8, 0), tzinfo=timezone.utc),
            "end" : datetime.combine(targetday, time(l+9, 0), tzinfo=timezone.utc),
            "label" : "free"
        })
    return full_sched

def checkifquarterstart(event):
    if event["start"].minute in [15,30,45]:
        print("It in 15/30/45")
        return True
    elif event["start"].minute in [0]:
        return False
    else: #Round up the minute to 15, 30, 45
        print("need to round the minutes")
        return False

def checkifquarterend(event):
    if event["end"].mintue in [15,30,45]:
        print("ends in 15,30,45")
        return True
    elif event["end"].minute in [0]:
        return False
    else: #Round up the minute to 15, 30, 45
        print("need to round the minutes")
        return False
    
def fillquarter(today, event, hour, quarter): #Fill the event with the quarter
    time(hour, quarter)
    
def full_schedule(days_sche):
    #Get the date
    targetday= days_sche[0]["start"].date()
    full_schedule = []
    counter = 8
    i_days_sche = len(days_sche)
    print(datetime.combine(targetday, days_sche[0]["start"].time(), tzinfo=timezone.utc)
    )
    # datetime.combine(targetday, time(8, 0), tzinfo=timezone.utc)  This can set the time for the target date  
        #1. Need to check if i o'clock is occupied, if occupied, give us a json of what is in that timeslot, and put it into the full_schedule array / list How do I change the i into an hour. and I need to pass the hour to check if it is occupied  

        #if 8am < busy_event : for i in 8 - busy_event[start] fullsched.append()
    eventnum = 0
    if datetime.combine(targetday, time(8, 0), tzinfo=timezone.utc) < days_sche[0]["start"]:
        print(fillfree_til(targetday, days_sche[0], counter, full_schedule))

        # morningtime = days_sche[0]["start"] - datetime.combine(targetday, time(8, 0), tzinfo=timezone.utc)
        # #Figures out the hours from 8am to the first event
        # totalhours = int(morningtime.total_seconds()/ 3600)
        # print("Getting to if statement for 8am")
        # print(totalhours)
        # for i in range(0, totalhours):
        #     full_schedule.append({
        #         "start" : datetime.combine(targetday, time(i+8, 0), tzinfo=timezone.utc),
        #         "end" : datetime.combine(targetday, time(i+9, 0), tzinfo=timezone.utc),
        #         "label" : "free"
        #     })

        #If there is an event eariler or at 8am we need ot list this with each hour. So lets make a func to add each hour and its label to each hour just by passing the event and full_sched
    elif datetime.combine(targetday, time(8, 0), tzinfo=timezone.utc) >= days_sche[0]["start"]:
        fillsched(targetday, days_sche[0], full_schedule)
        counter += 1
        eventnum += 1
    while counter != 20 & eventnum != len(days_sche):
        for i in range(1, len(days_sche)):
            eventnum = i
            if datetime.combine(targetday, time(counter, 0), tzinfo=timezone.utc) < days_sche[i]["start"]:
                fillfree_til(targetday, days_sche[i], counter, full_schedule)
            elif datetime.combine(targetday, time(counter, 0), tzinfo=timezone.utc) == days_sche[i]["start"]:#If the event starts with the counter / hour 
                if checkifquarterend(days_sche[eventnum]) == True:
                    break
            elif datetime.combine(targetday, time(counter, 0), tzinfo=timezone.utc) > days_sche[i]["start"]:
                if checkifquarterstart(days_sche[eventnum]) == True: #If it starts in a quarter We need to check whether it ends in a quarter, if so, fill until that quarter, and check if there is a event until the hour is done, then counter / time + 1, if no event fill free for the quarter(need to create fill quarter func), if no end in quarter, fill quarter then fill sched.   
                    if checkifquarterend(days_sche[eventnum]) == True:
                        #If the event ends in a quarter Fill the event details

                        if eventnum == len(days_sche):
                            break
                        elif eventnum < len(days_sche):
                            checkifquarterstart(days_sche[eventnum+1])#Check if the next event starts in 15 / 30 / 45

                    # while the hour ends:
                        # checkthenextevent
                elif checkifquarterend(days_sche[eventnum]) == True:#If the event ends in a quarter 
                    break


            fillsched(targetday, days_sche[eventnum], full_schedule)


 
        
        
        counter +=1


    print(full_schedule)

    #What to do tomorrow
    #time = 8
    #while time != 20
    #  For i in len(days_sched):
    #    if time(time) #8am# < days_sched[i]
    #           fillsched.append("start": time, "end" : time+1, "label":"free")
    #    elif time(time) >= days_sched[i]:
    #      #if it is 30 or 15 mins add free until starting time, then maybe add a label that indicates that so that the css can pick up that the box is gonna be smaller than usual
    #      add busy from that 15min mark to the hour so + 45 to that starting time so that it comes to an hour
    #      then time + 1
    #      while time != days_sched[i]["end"]:
    #           fillsched.append("start":dayssched[l]["start"]","end" : time+1, "label":"free")
    #           if it ends in 15, 30 or 45 we need to add the label and busy with 60 - x with free. But we need to check if there is another event starting from x - 60
    #           if days_sched[i+1]["start"] == days_sched[i+1]["end"]
    #             add the next schedule and the next event then and there
    #             
    #           time += 1




    #After we do the minute we can check the minute scheduler make chunk it into hours
    #Can we also chunck it into 15 minutes?
    #for i in range 8, 20
    #  if i == 
    #I think the best bet is to chunk it into quarters,
    #if quarter / half / 3quarters 
    #   add free or not for the first quarter, and busy for other
    #   For this we need the following mini funcitons.
    #   - check if quarter
    #   - add the schedule for the quarter
    #   - check if there is an event right after or in that hour
    #   


    return full_schedule
full_schedule(findlistoftimes(calendar_events, date(2025, 10, 22)))