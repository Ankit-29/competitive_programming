'''
Given a string of digits S, insert a minimum number of opening and closing parentheses into it such that the 
resulting string is balanced and each digit d is inside exactly d pairs of matching parentheses.
Let the nesting of two parentheses within a string be the substring that occurs strictly between them. An 
opening parenthesis and a closing parenthesis that is further to its right are said to match if their nesting 
is empty, or if every parenthesis in their nesting matches with another parenthesis in their nesting. The 
nesting depth of a position p is the number of pairs of matching parentheses m such that p is included in the 
nesting of m. For example, in the following strings, all digits match their nesting depth: 0((2)1), (((3))1(2)), 
((((4)))), ((2))((2))(1). The first three strings have minimum length among those that have the same digits in 
the same order, but the last one does not since ((22)1) also has the digits 221 and is shorter.
Given a string of digits S, find another string S', comprised of parentheses and digits, such that:
all parentheses in S' match some other parenthesis,
removing any and all parentheses from S' results in S,
each digit in S' is equal to its nesting depth, and
S' is of minimum length.
Input: S = "221"
Output: ((22)1)
Input: S = "321"
Output: (((3)2)1)
'''
def nestingDepthSet2(s: str) -> str:
    last = 0
    ret = ""
    openBrack = 0
    for x in range(len(s)):
        new = s[x]
        if(int(new) == last):
            ret += new
        elif(int(new)>last):
            ret += "("*(int(new)-openBrack)+new
            openBrack += int(new) - openBrack 
            last = int(new)
        else:
            ret += ")"*(openBrack-int(new))+new
            openBrack -= openBrack-int(new)
            last = int(new)

    ret += ")"*(openBrack)
    return ret

s = "321"
print(nestingDepthSet2(s))