#125 Valid Palindrom
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        letters = 'abcdefghijklmnñopqrstuvwxyz0123456789'
        ss = ""
        for letter in s:
            if letter in letters:
                ss+=letter
        return ss[(len(ss)//2)+1:] == ss[:(len(ss)//2)][::-1] if len(ss)%2 != 0 else ss[(len(ss)//2):] == ss[:(len(ss)//2)][::-1]
s = "0P"
x = Solution()
x.isPalindrome(s)