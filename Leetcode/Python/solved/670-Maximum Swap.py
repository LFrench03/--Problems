#670 Maximum Swap
'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        numstring = str(num)
        n = len(numstring)
        indexs = [-1]*10
        for i in range(n):
            indexs[int(numstring[i])] = i

        for i in range(n):
            digit = int(numstring[i])

            for j in range(9, digit, -1):
                if indexs[j] > i:
                    numlist = list(numstring)
                    numlist[i], numlist[indexs[j]] = numlist[indexs[j]], numlist[i]
                    return int(''.join(numlist))
        return num
        