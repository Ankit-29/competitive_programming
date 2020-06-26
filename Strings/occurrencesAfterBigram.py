'''
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
'''

from typing import List
def findOcurrences(text: str, first: str, second: str) -> List[str]:
    arr = text.split(" ")
    ret = list()
    if len(arr) < 3:
        return ret

    for i in range(2, len(arr)):
        if arr[i - 2] == first and arr[i - 1] == second:
            ret.append(arr[i])
    return ret

text = "alice is a good girl she is a good student"; first = "a"; second = "good"
print(findOcurrences(text,first,second))
