'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''



class Solution(object):
    def twoSum(self, nums, target):
        temp = len(nums)
        for i in range(temp):
            for j in range(i+1, temp):
                target_result = nums[i] + nums [j]
                result = []
                if target_result == target:
                     result.append(i)
                     result.append(j)
                     return result

nums = [3,3]
target = [6]
run_obj = Solution():
run_obj.twoSum(nums, target)
