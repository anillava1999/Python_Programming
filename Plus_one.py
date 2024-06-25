'''
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

'''

digits = [9,9]
Output =  []

check_result = digits[-1] + 1
if check_result >= 10:
    baby = str(check_result)
    #print(baby.split())
    for i in baby:
        temp = int(i)
        Output.append(temp)
else:
    Output.append(check_result)
  
    #print(baby)
print(digits[:-1] + Output)
#print(digits)
