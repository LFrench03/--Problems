#189 Rotate Array
'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''
# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if len(nums) > 1:
#             i = 0
#             while i < k:
#                 nums[:] = [nums[-1]] + nums[:-1]
#                 i+=1
#         print(nums)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
       k = k % len(nums)      
       r = len(nums) - k
       new = nums[0:r]
       nums[0:r] = []
       nums.extend(new)
lista = [-1,-100,3,99]
k = 2
x = Solution()
x.rotate(lista, k)