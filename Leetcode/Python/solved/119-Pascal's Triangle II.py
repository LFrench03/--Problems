#119 Pascal's Triangle II
'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]

Constraints:

0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pascal = [[1]]
        for _ in range(1,rowIndex+1):
            temp, row = [0] + pascal[-1] + [0], []
            for i in range(len(temp) - 1): row.append(temp[i] + temp[i+1])
            pascal.append(row)
        return pascal[-1]      