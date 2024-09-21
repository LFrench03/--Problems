#386 Lexicographical Numbers
'''
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
'''
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []  
        current = 1  
        for _ in range(n):
            result.append(current)
            current = self.get_next_number(current, n)     
        return result

    def get_next_number(self, current: int, n: int) -> int:
        if current * 10 <= n:  
            return current * 10
        if current >= n: 
            current //= 1
        current += 1  
        while current % 10 == 0:
            current //= 10
        return current
######## Test ########
x = Solution()
n = 13
x.lexicalOrder(n)
######################