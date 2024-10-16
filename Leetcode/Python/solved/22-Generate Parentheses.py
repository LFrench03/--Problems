#22 Generate Parentheses
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
'''
class Solution:
    def backtrack(self, ln, rn, result, tmp):
        if ln > rn:
            return
            
        if ln==0 and rn>0:
            tmp += ")" * rn
            result.append(tmp)
            return

        self.backtrack(ln-1, rn, result, tmp+"(")
        self.backtrack(ln, rn-1, result, tmp+")")
        return