'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = list()
        self.min.append(float("inf"))
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if(self.min[-1]>=x):
            self.min.append(x)

    def pop(self) -> None:
        if(self.stack.pop() == self.min[-1]):
            self.min.pop()
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1] if self.min[-1] != float("inf") else 0 
    

funcs = ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
param = [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]

obj = MinStack()
for x in range(1,len(funcs)):
    if(funcs[x] == "push"):
        obj.push(param[x][0])
    elif(funcs[x] == "pop"):
        obj.pop()
    elif(funcs[x] == "getMin"):
        print(obj.getMin())
    else:
        print(obj.top())

