# Fractional Knapsack Greedy
'''
Given weights and values of n items, we need to put these items in a knapsack 
of capacity W to get the maximum total value in the knapsack. we can break items 
for maximizing the total value of knapsack.
'''

def fracKnapsackGreedy(bagSize, items):
    profit = 0
    # Calculate Pi/Wi
    items = list(map(lambda x: (x[0], x[1], x[0]/x[1]), items))
    # Sort Items by Pi/Wi
    items.sort(key=lambda x: x[2], reverse=True)
    for item in items:
        if(bagSize-item[1] >= 0):
            bagSize -= item[1]
            profit += item[0]
        else:
            profit += item[2]*bagSize
            bagSize = 0

        if(bagSize == 0):
            return profit


bagSize = 15
# Structure of List: [(P1,W1),(P2,W2),...(Pn,Wn)]
items = [(10, 2), (5, 3), (15, 5), (7, 7), (6, 1), (18, 4), (3, 1)]
print(fracKnapsackGreedy(bagSize, items))
