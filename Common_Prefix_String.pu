'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        k = list(sorted(strs,key = len))

        #print(k)
        q = 1
        new_list = []
        len_k = len(k)
        if len_k >= 2:
            for i in k:
                fresh = ''
                for j in range(len(i)):
                    next_value = k[q][j]
                    if i[j] == next_value:
                        fresh = fresh +  i[j]
                    elif i[j] != next_value:
                        break
                new_list.append(fresh)
                #print(new_list)
                len_of_k = len(k)
                q += 1
                print(" ")
                if len(k) == q:
                    break

            k = list(sorted(new_list,key = len))
            if len(k[0]) >= 2:
                return k[0]
            elif len(k[0]) == 1:
                return k[0]
            else:
                return ""
        if len_k < 2:
            return k[0]


