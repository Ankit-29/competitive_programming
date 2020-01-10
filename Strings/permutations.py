# Permutations of String
# Time Complexit: O(n*n!)
# Backtracking Approach

def permOfString(s,left,right,result):
    if(left==right):
        result.append("".join(s))
    else:
        for x in range(left,right):
            s[x],s[left] = s[left],s[x]
            permOfString(s,left+1,right,result)
            s[x],s[left] = s[left],s[x]
    return result

s = "code"
allPerms = permOfString(list(s),0,len(s),list())
for perm in allPerms:
    print(perm)