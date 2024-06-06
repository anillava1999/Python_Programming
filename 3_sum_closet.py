'''

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        stored_result = 0
        arr = nums
        pp = 0

        # Run three nested loops each loop 
        # for each element of triplet
        for i in range (len(arr)) :
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len( arr)):
                    result = (arr[i] + arr[j] + arr[k])
                    final_result = (abs(result))
                    #print(final_result)         
                    if final_result >= target:
                        if final_result > stored_result and target >= stored_result :
                            stored_result = final_result
                    elif target >= final_result:
                        final_result = final_result


        if target > 0:
            print("")
        else:
            stored_result = final_result
            return stored_result

                                        
        return stored_result
    
nums = [0,0,0]
target = 1
p1 = Solution()
p1.threeSumClosest(nums,target)
