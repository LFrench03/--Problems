#1671 Minimum Number of Renovals to Make Mountain Array
'''
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.

Hints:

-Think the opposite direction instead of minimum elements to remove the maximum mountain subsequence

-Think of LIS it's kind of close
'''
class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        dp1, dp2, answer = [0] * n, [0] * n, 0
        # for increasing subsequence
        for i in range(n):
            max_incr = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp1[j] > max_incr:
                        max_incr = dp1[j] 
            dp1[i] = max_incr + 1
        # for decreasing subsequence
        for i in range(n-1, -1, -1):
            max_decr = 0
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    if dp2[j] > max_decr:
                        max_decr = dp2[j] 
            dp2[i] = max_decr + 1
        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:
                temp = dp1[i] + dp2[i] - 1
                if temp > answer:
                    answer = temp
        return n - answer
        
