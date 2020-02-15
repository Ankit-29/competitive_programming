'''
At a lemonade stand, each lemonade costs $5.Customers are standing in a queue to buy from you, 
and order one at a time (in the order specified by bills).Each customer will only buy one 
lemonade and pay with either a $5, $10, or $20 bill.You must provide the correct change 
to each customer, so that the net transaction is that the customer pays $5.
Note that you don't have any change in hand at first.
Return true if and only if you can provide every customer with correct change.
Input: [5,5,5,10,20]
Output: True
Input: [10,10]
Output: false
'''
from typing import List
def lemonadeChange(bills: List[int]) -> bool:
    Hash = {5:0,10:0,20:0}
    for x in range(len(bills)):
        change = bills[x] - 5
        if(change==5 and Hash[change]>0):
            Hash[change] -=1
            change = 0
        if(change==15):
            if(Hash[10]>0):
                Hash[10] -=1
                change -= 10
            if(change==15 and Hash[5]>=3):
                Hash[5] -=3
                change = 0
            if(change==5 and Hash[5]>0):
                Hash[5] -=1
                change = 0
        if(change):return False
        Hash[bills[x]] += 1
        
    return True

bills = [5,5,5,10,20]
print(lemonadeChange(bills))
