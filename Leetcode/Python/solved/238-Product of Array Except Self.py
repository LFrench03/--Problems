#238 Product of Array Except Self
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         def prod(values: list[int], exc:int) -> int:
#             result = 1
#             index = 0
#             while index < len(values):
#                 result *= values[index] if index != exc else 1
#                 index+=1
#             return result
#         index = 0
#         temp = nums[:]
#         while index < len(nums):
#             nums[index] = prod(temp, index)
#             index+=1
#         return nums
    
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n  

        left = 1
        for i in range(n):
            output[i] *= left  
            left *= nums[i]    

        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right 
            right *= nums[i]   

        return output
nums = [0,0]
x = Solution()
x.productExceptSelf(nums)