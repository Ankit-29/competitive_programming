# Generate all prime Numbers upto a given Value N.
# Algorithm Used :- Sieve of Eratosthenes

def generatePrimeNos(N):
    primes = [True]*(N+1)
    primes[0]=False
    primes[1]=False

    for x in range(2,int(N**0.5)+1):
        if(primes[x]):
            y = 2
            while(x*y<=N):
                primes[x*y] = False
                y +=1
    
    return primes


def main():
    N = int(input())
    primeList = generatePrimeNos(N)
    for x in range(N):
        if primeList[x]:print(x)

main()










