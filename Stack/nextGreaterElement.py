# Next Greater Element Problem
''' 
Given an array, print the Next Greater Element (NGE) for every element. 
The Next greater Element for an element x is the first greater element 
on the right side of x in array. Elements for which no greater element exist, 
consider next greater element as -1 
'''

def nextGreaterElement(arr):
    stack = list()
    for x in arr:
        if(not(len(stack)) or stack[-1]>x):
            stack.append(x)
        else:
            while(len(stack) and stack[-1]<x):
                ele = stack.pop()
                print(str(ele) + " --> " + str(x))
            stack.append(x)
            
    while(len(stack)):
        ele = stack.pop()
        print(str(ele) + " --> -1")
        
arr = [13, 7, 6, 12]
nextGreaterElement(arr)


