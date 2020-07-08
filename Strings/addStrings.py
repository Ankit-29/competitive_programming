'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

def addStrings(num1: str, num2: str) -> str:
    return iToS(sToI(num1) + sToI(num2))

def sToI(num:int) -> int:
    cToI = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    n = 0
    place = 1
    for x in list(num)[::-1]:
        n += cToI[x]*place
        place *= 10
    
    return n
    
def iToS(num:int) -> str:
    iToC = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
    s = ""
    if(num==0):return "0"
    while(num):
        s = iToC[num%10] + s
        num //= 10
        
    return s 

num1 = "98"; num2 = "9"
print(addStrings(num1,num2))