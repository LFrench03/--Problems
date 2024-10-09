#172 Factorial trailing zeroes
'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
 

Follow up: Could you write a solution that works in logarithmic time complexity?
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
    
    def trailingZeroes2(self, n: int) -> int: #Iterativo
        fact = 1
        for i in range(1, n+1):
            fact *= i
        print(fact)
        fact = str(fact)[::-1]
        for i in range(len(fact)):
            if fact[i]!="0":
                fact=fact[:i]
                break
        return len(fact)    
    
    def trailingZeroes2(self, n: int) -> int:
        def factorial(n: int) -> int: #Recursivo
            if n == 0: #condicion de parada
                return 1 #caso base
            return n*factorial(n-1) #llamada recursiva
        result = factorial(n)
        result = str(result)[::-1]
        for i in range(len(result)):
            if result[i]!="0":
                result=result[:i]
                break
        return len(result)
x = Solution()
print(x.trailingZeroes2(15))