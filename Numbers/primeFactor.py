# Prime Factorizaion
# Function to generate PrimeFactors of given No

def isPrime(n,primes):
    for x in range(0,len(primes)):
        if(n%primes[x]==0):
            return False
        if(primes[x]**0.5)<n:
            break

    primes.append(n)
    return True

def primeFactor(N):
    res = list()
    primes = [2]
    p = 2
    while(N!=1):
        if(N%p==0):
            N = N/p
            res.append(str(p))
        else:
            p += 1 if(p==2) else 2
            while(not(isPrime(p,primes))):
                p +=1

    return res

print(" x ".join(primeFactor(5728042130)))
# 2 x 5 x 23 x 61 x 408271

