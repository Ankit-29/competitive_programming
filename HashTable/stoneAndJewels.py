'''
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type 
of stone you have. You want to know how many of the stones you have are also jewels.
'''
def totalJewels(stones: str, jewels: str) -> int:
    Hash = dict()
    count = 0
    for x in jewels:
        Hash[x] = True

    for x in stones:
        if(x in Hash):
            count += 1

    return count

jewels = "aA"
stones = "aAAbbbb"
print(totalJewels(stones, jewels))
