# Power Set
# Function to generate Power Set of a given Set

def powerSet(S):
    P = list()
    l = len(S)
    totSubs = 2**l
    for x in range(totSubs):
        i = 0
        subSet = list()
        while(x):
            if(x%2!=0):
                subSet.append(S[i])
            
            x = int(x/2)
            i += 1
        P.append(subSet) 

    P.sort(key = lambda x:len(x))
    return P

S = input().split()
P = powerSet(S)
for x in P:
    print("{ ",end="")
    print(",".join(x),end=" }\n")
