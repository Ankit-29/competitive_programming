# Fast Modular exponentiation
# Function to calculate x = (a^N)%y
# Complexity O(logN)

def fastModExpoIterative(val, power, mod):
    res = 1
    val = val % mod
    while(power > 0):
        if(power % 2 != 0):
            res = (res*val)%mod

        power = int(power/2)
        val = (val*val)%mod

    return res

def fastModExpoRecursive(val, power, mod):
    val = val%mod
    if(power==0):
        return 1

    R = fastModExpoRecursive(val,int(power/2),mod)
    if(power%2==0):
        return (R*R)%mod
    else:
        return (val*R*R)%mod

print(fastModExpoIterative(3,1000,10**9))
print(fastModExpoRecursive(3,1000,10**9))


