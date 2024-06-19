'''
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first 
two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k 
(hence they are underscores).
'''

nums = [1,1,2]
nums_exa = []
nums_last_ele = []
for i in range(len(nums)):
    if nums[i] in nums_exa:
        nums_last_ele.append('_')
    else:
        nums_exa.append(nums[i])
        
nums = nums_exa + nums_last_ele
print(nums)
