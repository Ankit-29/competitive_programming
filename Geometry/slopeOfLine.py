'''
Given two co-ordinates, find the slope of a straight line.

Examples:
Input  : x1 = 4, y1 = 2, 
         x2 = 2, y2 = 5 
Output : -1.5
'''


def slope(x1: float, y1: float, x2: float, y2: float) -> float:
    return (y2-y1)/(x2-x1)


x1 = 4; y1 = 2 
x2 = 2; y2 = 5 
print(slope(x1, y1, x2, y2))
