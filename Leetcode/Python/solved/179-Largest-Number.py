#179 Largest Number
'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        num_strings = list(map(str, nums))
        def compare(x, y):
            if x + y > y + x:
                return -1  
            elif x + y < y + x:
                return 1   
            else:
                return 0
        num_strings.sort(key=cmp_to_key(compare))
        largest_num = ''.join(num_strings)
        return '0' if largest_num[0] == '0' else largest_num

####### Test ########
nums = [3,30,34,5,9]
x = Solution()
x.largestNumber(nums)
####################