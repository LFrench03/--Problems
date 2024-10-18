#3 Longest Substring Without repeating characters
'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        maxlen = 0
        while i <= j and j < len(s):
            while s[j] in s[i:j]:
                i += 1
            j += 1
            maxlen = max(maxlen, j-i)
        return maxlen
        
                
s = "dvdf"
x = Solution()              
x.lengthOfLongestSubstring(s)

