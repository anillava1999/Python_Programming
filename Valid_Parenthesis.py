'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        k = {
    '(': ')',
    ')': '(',
    '{': '}',
    '}': '{',
    '[': ']',
    ']': '['
    }
        input_key = s
        listString=list(input_key)

        temp = 0
        g = 1
        for i in range(len(listString)):
            if len(listString) % 2 == 0 and i % 2 == 0:
                #k[i + temp] == k[i+g]
                kk = listString[i + temp]
                #print(kk)
                if k.get(kk) == listString[i+g]:
                    result = True
                else:
                    result = False
                    break
        return result
                
