#1545 Find Kth Bit in Binary String
'''
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.


Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".

Constraints:

1 <= n <= 20
1 <= k <= 2n - 1

Hint:

Since n is small, we can simply simulate the process of constructing S1 to Sn.
'''
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n<=1: return '0'
        def s_i(n):
            s, i = '0', 1
            while i < n:
                s += '1' + "".join(['1' if x == '0' else '0' for x in list(s)])[::-1]
                i += 1 
            return s
        return s_i(n)[k-1]
n, k = 4, 3
x = Solution()
x.findKthBit(n,k)