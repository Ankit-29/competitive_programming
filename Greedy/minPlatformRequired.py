# Minimum Number of Platforms Required for a Railway/Bus Station
'''
    Given arrival and departure times of all trains that reach a 
    railway station, the task is to find the minimum number of 
    platforms required for the station so that no train waits.
'''

def minPlatformsRequired(arrivals: list, departues: list) -> int:
    reqPlatforms = 1
    currReq = 0
    # Sort Arrival and Departure time
    arrivals.sort()
    departues.sort()
    i = j = 0
    while(i < len(arrivals) and j < len(departues)):
        if(arrivals[i] <= departues[j]):
            currReq += 1
            reqPlatforms = max(currReq, reqPlatforms)
            i += 1
        else:
            currReq -= 1
            j += 1

    return reqPlatforms


arrivals = [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
departues = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
print(minPlatformsRequired(arrivals, departues))
