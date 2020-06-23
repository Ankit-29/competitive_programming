'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
'''
from typing import List

def destCity(paths: List[List[str]]) -> str:
    Hash = dict()
    for path in paths:
        Hash[path[0]] = False
        Hash[path[1]] = True if (path[1] not in Hash) or Hash[path[1]]==True else False
    
    for key in Hash.keys():
        if(Hash[key]):
            return key

paths = [["B","C"],["D","B"],["C","A"]]
print(destCity(paths))