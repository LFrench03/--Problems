#73 Set Matrix Zeroes
'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

'''
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix[0]), len(matrix)
        for i in range(m):
            for j in range(n):
                if 0 in matrix[i]: 
                    if matrix[i][j] != 0: matrix[i][j] = '0'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0: continue
                for i in range(m): matrix[i][j] = 0 
        for i in range(m):
            for j in range(n): 
                if matrix[i][j] == '0': matrix[i][j] = 0
        print(matrix)
matrix = [[1,0,0]]
x = Solution()                
x.setZeroes(matrix)
