#7 Reverse Interger
'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''
class Solution:
    def reverse(self, x: int) -> int: 
        result = int(str(x)[::-1]) if x>=0 else int(str(x)[::-1][:-1] )  
        result = result if x>=0 else result*-1
        if result > (2**31 -1) or result < (-2**31 ) :
            return 0
        return result 
        