'''
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''
haystack = "sadbutsad"
needle = "sad"
k, j =0, 0
if len(haystack) < len(needle):
    print(-1)

for i in range(len(haystack)):
    if haystack[i:i+len(needle)] == needle:
        print(i)

print(-1)
