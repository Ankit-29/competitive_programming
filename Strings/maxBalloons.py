'''
Given a string text, you want to use the characters of text to form as many instances of the 
word "balloon" as possible.You can use each character in text at most once. Return the maximum 
number of instances that can be formed.
Input: text = "nlaebolko"
Output: 1
Input: text = "loonbalxballpoon"
Output: 2
'''

def maxNumberOfBalloons(text: str) -> int:
    freq = [0]*26
    balloon = {'a':1,'b':1,'l':2,'o':2,'n':1}
    for x in text:
        freq[ord(x)-ord('a')] += 1

    m = float("inf")      
    for x in balloon.keys():
        m = min(m,freq[ord(x)-ord('a')]//balloon[x]) 
    
    return m

text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))