#32 Longest Valid Parenthesis
'''
    Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
    substring.

    
    Example 1:

    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".
    Example 2:

    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".
    Example 3:

    Input: s = ""
    Output: 0
    

    Constraints:

    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = 0
        index=[-1] 
        for i in range(len(s)):
            if s[i] == '(':
                index.append(i)
            else:
                index.pop()
                if not index: 
                    index.append(i)
                else:
                    length=max(length, i-index[-1]) 
        return length