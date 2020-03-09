def marsExploration(s):
    i = 0
    count = 0
    while(i<len(s)-2):
        if(s[i]!='S'):count+=1
        if(s[i+1]!='O'):count+=1
        if(s[i+2]!='S'):count+=1
        i+=3
    return count

s = "SOSSOT"
print(marsExploration(s))