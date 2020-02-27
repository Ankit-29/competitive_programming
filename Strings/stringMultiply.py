'''
Given two non-negative integers num1 and num2 represented as strings, return the product of 
num1 and num2, also represented as a string.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
Note:
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

def multiply(num1: str, num2: str) -> str:
    return toInt(num1)*toInt(num2)       

def toInt(num: str) -> int:
    Hash = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
    if(num in Hash):return Hash[num]
    place = 10**(len(num)-1)
    ret = 0
    for x in num:
        ret += Hash[x]*place
        place //=10
    return ret

num1 = "123"; num2 = "456"
print(multiply(num1,num2))
