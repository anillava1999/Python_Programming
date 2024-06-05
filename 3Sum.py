
'''

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        nums  = sorted(nums)
        result = 0
        data  = []
        len_list = len(nums)

        for i in range(len_list):
            for j in range(len_list):
                for k in range(len_list):
                    if i != j and i != k and j != k:
                        result = nums[i] + nums[j] + nums[k]
                        if result == 0:
                        #data.append([])
                        value = nums[i] , nums[j] , nums[k]
                        data.extend([value])
                        
        #print(data)

        unique_rows = set()
        result = []

        for row in data:
            sorted_row = tuple(sorted(row))
            if sorted_row not in unique_rows:
                unique_rows.add(sorted_row)
                result.append(row)


        return result
                
