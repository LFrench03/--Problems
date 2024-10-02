#233 Number of digit One
'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example 1:

Input: n = 13
Output: 6

Example 2:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 109
'''

# Only works until 10**7
# class Solution:
#     def countDigitOne(self, n: int) -> int:
#         return str([x for x in range(n+1)]).count("1") 
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        multiplier = 1
        while multiplier <= n:
            divider = multiplier * 10
            count += (n // divider) * multiplier
            count += min(max(n % divider - multiplier + 1, 0), multiplier)
            multiplier *= 10
        return count
n = 82488329
x = Solution()
x.countDigitOne(n)