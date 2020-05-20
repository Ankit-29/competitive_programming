'''
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies 
that the ith kid has.For each kid check if there is a way to distribute extraCandies among the kids 
such that he or she can have the greatest number of candies among them. Notice that multiple kids can 
have the greatest number of candies.

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
'''
from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maxCandies = max(candies)
    possibilities = [False]*len(candies)
    for idx in range(len(candies)):
        if(maxCandies <= (extraCandies+candies[idx])):
            possibilities[idx] = True

    return possibilities




candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
