'''
Input: a = 2, b = 4
Output: 4

Input: a = -1, b = -4
Output: -1

'''

class solution():
    def find_max(self, a, b):
        if a > b:
            return a
        elif a < b:
            return b
            
a = -4
b  = -1
find_max_result = solution()
value  = find_max_result.find_max(a,b)
print(value)
