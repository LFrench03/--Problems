#962 Maximum Width Ramp
'''
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

Constraints:

2 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5 * 10^4

'''
class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        lhs = [0]
        for i, e in enumerate(nums):
            if nums[i] < nums[lhs[-1]]:
                lhs.append(i)
        
        max_width = 0
        j = len(nums)-1
        while lhs:
            i = lhs.pop()
            while j-i > max_width:
                if nums[i] <= nums[j]:
                    max_width = j-i
                    break
                j -= 1
        return max_width
        