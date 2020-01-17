# Activity Selection Problem
'''
There are n different activities are given with their starting time and ending time.
Select the maximum number of activities to be done by a single person if only one activity
can be performed at a time.
'''

def activitySelection(activities):
    res = list()
    # Sort Activities acc to Final Time
    activities.sort(key=lambda x:x[1])
    x = 0 
    # Always Select the first sorted activity    
    res.append(1)
    for y in range(1,len(activities)):
        # If activity has start time greater than end time 
        # of previous then select the activity
        if(activities[y][0]>=activities[x][1]):
            res.append(y+1)
            x = y
    return res

# Structure of List: [(S1,E1),(S2,E2),...(Sn,En)]
activities = [(3,4),(8,9),(0,6),(1,2),(5,9),(5,7)]
print(activitySelection(activities))
