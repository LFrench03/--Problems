#1401 Longest Happy String
'''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct memorywer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct memorywer in this case.

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''
class Solution:
    def __init__(self):
        self.longest = ''

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        memory = {'a':a, 'b':b, 'c':c}
        def backtrack(memory, actual):
            if len(actual) > len(self.longest):
                self.longest = actual
            a, b, c = sorted(memory.items(), key=lambda x: x[1], reverse=True)

            if a[1] > 0 and not (len(actual) >= 2 and actual[-2::] == a[0]*2):
                memory[a[0]] -= 1
                backtrack(memory, actual+a[0])
                memory[a[0]] += 1
            elif b[1] > 0 and not (len(actual) >= 2 and actual[-2::] == b[0]*2):
                memory[b[0]] -= 1
                backtrack(memory, actual+b[0])
                memory[b[0]] += 1
            elif c[1] >0 and not (len(actual)>= 2 and actual[-2::] == c[0]*2):
                memory[c[0]] -= 1
                backtrack(memory,actual+c[0])
                memory[c[1]] += 1
        backtrack(memory, self.longest)
        return self.longest 
        
a, b, c = 1, 1, 7
x = Solution()
x.longestDiverseString(a,b,c)