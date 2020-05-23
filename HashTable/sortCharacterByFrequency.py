'''
Given a string, sort it in decreasing order based on the frequency of characters.

Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Input:
"cccaaa"
Output:
"cccaaa"
'''

def frequencySort(s: str) -> str:
    Hash = dict()

    for letter in s:
        if(letter in Hash):
            Hash[letter] += 1
        else:
            Hash[letter] = 1
    
    itemList = list(Hash.items())
    itemList.sort(key=lambda x:(x[1],x[0]), reverse=True)
    
    string = ""
    for item in itemList:
        string += item[0]*item[1]
        
    return string

s = "tree"
print(frequencySort(s))