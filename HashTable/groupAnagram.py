# Group Anagrams
'''
Given an array of strings, group anagrams together.
'''
def groupAnagrams(strs: list) -> list:
    Hash = dict()  
    for s in strs:
        freq = [0]*26 # Frequency List
        for x in s:
            # Calculate Frequency
            freq[ord(x)-ord('a')] += 1
        # Make Key for Hash using freq list
        key = tuple(freq)
        if(key not in Hash):
            Hash[key] = list()
        Hash[key].append(s) 
    return list(Hash.values())

strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
