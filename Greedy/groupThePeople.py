'''
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. 
Given the array groupSizes of length n telling the group size each person belongs to, return the groups 
there are and the people's IDs each group includes.
You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there 
exists at least one solution. 

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
'''
from typing import List
def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    groups = dict()
    ret = list()
    for idx, value in enumerate(groupSizes):
        if(value in groups):
            if(len(groups[value])!=value):
                groups[value].append(idx)
            else:
                ret.append(groups[value])
                groups[value] = list()
                groups[value].append(idx)
        else:
            groups[value] = list()
            groups[value].append(idx)
        
    for key in groups.keys():
        ret.append(groups[key])
            
    return ret
    
groupSizes = [3,3,3,3,3,1,3]
print(groupThePeople(groupSizes))