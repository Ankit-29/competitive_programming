'''
Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.
Letters in some of the SOS messages are altered by cosmic radiation during transmission. 
Given the signal received by Earth as a string,determine how many letters of Sami's SOS 
have been changed by radiation.
For example, Earth receives SOSTOT. Sami's original message was SOSSOS.
Two of the message characters were changed in transit.
Print the number of letters in Sami's message that were altered by cosmic radiation.
Input: SOSSPSSQSSOR
Output: 3
'''
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