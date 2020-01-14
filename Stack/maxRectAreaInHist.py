# Maximum Rectangular Area in Histogram
'''
Find the largest rectangular area possible in a given histogram 
where the largest rectangle can be made of a no of contiguous bars. 
For simplicity,all bars have same width and the width is 1 unit.
'''
# Time Complexity O(N)

def maxRectAreaInHistogram(arr):
    stack = list()
    currArea = maxArea = x = 0
    while(x<len(arr)):
        if(not(len(stack)) or arr[x]>=arr[stack[-1]]):
            stack.append(x)
            x += 1
        else:
            eleIdx = stack.pop()
            if(not(len(stack))):
                currArea = arr[eleIdx]*x
            else:
                currArea = arr[eleIdx]*(x-stack[-1]-1)
            maxArea = max(currArea,maxArea)

    while(not(len(stack))):
        eleIdx = stack.pop()
        if(not(len(stack))):
            currArea = arr[eleIdx]*x
        else:
            currArea = arr[eleIdx]*(x-stack[-1]-1)
        maxArea = max(currArea,maxArea)
    return maxArea

arr = [6, 2, 5, 4, 5, 1, 6]
print(maxRectAreaInHistogram(arr))

