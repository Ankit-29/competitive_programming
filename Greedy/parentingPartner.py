'''
Cameron and Jamie's kid is almost 3 years old! However, even though the child is more independent now, 
scheduling kid activities and domestic necessities is still a challenge for the couple.
Cameron and Jamie have a list of N activities to take care of during the day. Each activity happens during 
a specified interval during the day. They need to assign each activity to one of them, so that neither of 
them is responsible for two activities that overlap. An activity that ends at time t is not considered to 
overlap with another activity that starts at time t.
For example, suppose that Jamie and Cameron need to cover 3 activities: one running from 18:00 to 20:00, 
another from 19:00 to 21:00 and another from 22:00 to 23:00. One possibility would be for Jamie to cover 
the activity running from 19:00 to 21:00, with Cameron covering the other two. Another valid schedule would be for
Cameron to cover the activity from 18:00 to 20:00 and Jamie to cover the other two. Notice that the first two 
activities overlap in the time between 19:00 and 20:00, so it is impossible to assign both of those activities to 
the same partner. Given the starting and ending times of each activity, find any schedule that does not require the 
same person to cover overlapping activities, or say that it is impossible.

Output is IMPOSSIBLE if there is no valid schedule according to the above rules, or a string of exactly N characters 
otherwise. The i-th character in y must be C if the i-th activity is assigned to Cameron in your proposed
schedule, and J if it is assigned to Jamie

Input: [(360,480),(420,540),(600,660)] 
Output: CJC
Input: [(0,1440),(1,3),(2, 4)]
Output: IMPOSSIBLE
Input: [(99,150),(1,100),(100,301),(2,5),(150,250)]
Output: JCCJJ 
'''
def parentingPartner(tasks):
    Hash = {}
    sortedTasks = sorted(tasks,key=lambda x:(x[0],x[1]))
    CameronCurr = 0; JamieCurr = 0 ;ret = ""
    for x in sortedTasks:
        if(x[0]>=CameronCurr):
            CameronCurr = x[1]
            if(x not in Hash):Hash[x] = []
            Hash[x].append('C')
        elif(x[0]>=JamieCurr):
            JamieCurr = x[1]
            if(x not in Hash):Hash[x] = []
            Hash[x].append('J')
        else:
            return "IMPOSSIBLE"
    for x in tasks:
        ret += Hash[x][0]
        del Hash[x][0]
    
    return ret
    
tasks = [(99,150),(1,100),(100,301),(2,5),(150,250)]
print(parentingPartner(tasks))