#54 Spiral Matrix 
'''
Given an m n n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

Hint 1: Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.

Hint 2: We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then we move inwards by 1 
and repeat. That's all. That is all the simulation that we need.

Hint 3: Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column. Similarly, by 
changing values for j, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always 
best to simulate edge cases like a single column or a single row to see if anything breaks or not.
'''
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n, m = len(matrix[0]), len(matrix)
        total, result = n*m, []
        def recurse(n:int, m:int, start=0, step=1) -> list[int] :
            if len(result) == total: return result
            for i in range(start, n, step):
                result.append(matrix[start][i])
                if len(result) == total: return result
            for i in range(start+1, m, step):
                result.append(matrix[i][n-1])
                if len(result) == total: return result
            step *=-1
            n-=1
            m-=1
            for i in range(n-1,start-1,step):
                result.append(matrix[m][i])
                if len(result) == total: return result
            for i in range(m-1, start, step):
                result.append(matrix[i][start])
                if len(result) == total: return result
            step *=-1
            return recurse(n,m,start+1,step)
        return recurse(n,m)
matrix = [[1,2],[4,5],[7,8]]
n = Solution()
n.spiralOrder(matrix)