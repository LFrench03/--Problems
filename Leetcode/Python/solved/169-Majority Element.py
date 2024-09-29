class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num = nums[0]
        for i in nums:
            if i!=num and nums.count(i) > nums.count(num):
                num = i
        return num