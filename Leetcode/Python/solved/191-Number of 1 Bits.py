#191 Number of 1 Bits
'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits
 it has (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
 

Follow up: If this function is called many times, how would you optimize it?
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        def convert_to_binar(n):
            if n<0:
                return None
            if n == 0:
                return 0
            number = []
            binary_number = ""
            def division(n,b):
                if n==0:
                    return b[::-1]
                if n == 1:
                    b.append(n)
                    return b[::-1]
                if n>=2:
                    x = n % 2
                    n = n // 2
                    b.append(x)
                    return division(n,b)
            x = (division(n,number))
            for i in x:
                binary_number+=str(i)
            return binary_number
        return convert_to_binar(n).count("1")    
n = 2147483645
x = Solution()    
x.hammingWeight(n)