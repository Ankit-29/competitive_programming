


def totalJewels(stones:str,jewels:str)-> int:
    Hash = dict()
    count = 0
    for x in jewels:
        Hash[x] = True
    for x in stones:
        if(x in Hash):
            count += 1
            
    return count

jewels = "aA", 
stones = "aAAbbbb"
print(totalJewels(stones,jewels))