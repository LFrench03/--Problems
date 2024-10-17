#118 Pascal's Triangle
'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

1 <= numRows <= 30
'''
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = [[1]]
        for _ in range(1,numRows):
            temp, row = [0] + pascal[-1] + [0], []
            for i in range(len(temp) - 1): row.append(temp[i] + temp[i+1])
            pascal.append(row)
        return pascal