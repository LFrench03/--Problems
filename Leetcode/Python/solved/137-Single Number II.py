#137 Single Number II
'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return nums[[nums.count(x) for x in nums].index(min([nums.count(x) for x in nums]))]
# nums = [0,1,0,1,0,1,99]
# x = Solution()
# x.singleNumber(nums)

class Solution2:
    def singleNumber(self, nums: list[int]) -> int:
        return ((3*sum((set(nums))))-sum(nums))//2