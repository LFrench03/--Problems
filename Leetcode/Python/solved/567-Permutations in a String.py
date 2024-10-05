#567 Permutations in a String
'''
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm, w, s = Counter(s1), len(s1), set(s1)
        i = 0
        while i < len(s2):
            if s2[i] in s:                
                hm[s2[i]] -= 1
                if hm[s2[i]] == 0:
                    hm.pop(s2[i])
            if i >= w and s2[i-w] in s:    
                hm[s2[i-w]] += 1
                if hm[s2[i-w]] == 0:
                    hm.pop(s2[i-w])
            if len(hm) == 0:
                return True
            i+=1
        return False

s1 = "abcdxabcde"
s2 = "abcdeabcdx"
x = Solution()
x.checkInclusion(s1,s2)