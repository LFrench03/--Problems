#289 Game of Life
'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

Follow up:

-Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
-In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you addirection_rowess these problems?
'''
class Solution:
    def neighbor(self, row: int, col: int, m: int, n: int, board: list[list[int]]) -> int:
        neighbor = 0
        # Check adjacent cells (up, down, left, right)
        if col < n - 1: 
            neighbor += 1 if board[row][col + 1] else 0
        if col > 0: 
            neighbor += 1 if board[row][col - 1] else 0
        if row > 0: 
            neighbor += 1 if board[row - 1][col] else 0
        if row < m - 1: 
            neighbor += 1 if board[row + 1][col] else 0

        # Check diagonal neighbor
        if row > 0 and col > 0:  # Above left
            neighbor += 1 if board[row - 1][col - 1] else 0
        if row > 0 and col < n - 1:  # Above right
            neighbor += 1 if board[row - 1][col + 1] else 0
        if row < m - 1 and col > 0:  # Below left
            neighbor += 1 if board[row + 1][col - 1] else 0
        if row < m - 1 and col < n - 1:  # Below right
            neighbor += 1 if board[row + 1][col + 1] else 0            
        return neighbor

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        res = [[0] * n for _ in range(m)] #Initialize result board
        for i in range(m):
            for j in range(n):
                element = board[i][j]
                neighbor = self.neighbor(i, j, m, n, board)
                # Apply the rules of Game of Life
                if element:  # Live cell
                    res[i][j] = 1 if 2 <= neighbor <= 3 else 0 # Live if condition else Die
                else:  # Dead cell
                    if neighbor == 3: res[i][j] = 1 # Reproduction (becorn alive)
        board[:] = res[:]

# # Test example
# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# x = Solution()
# x.gameOfLife(board)
# print(board) 

'''
This code implements the "Game of Life" using an approach that relies on counting how many living neighbors each cell has and applying the rules of the game to 
determine its future state. It does this by using an additional array to store the results. Although this approach is clear and easy to understand, it consumes additional 
space.
'''

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
x = Solution()
x.gameOfLife(board)

class Solution2:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        # Define directions for neighbors (including diagonals)
        directions = [
            (-1, -1), (-1, 0), (-1, 1), 
            (0, -1), (0, 1), (1, -1), 
            (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                # Count live neighbors
                for direction_row, direction_column in directions:
                    row, column = i + direction_row, j + direction_column
                    if 0 <= row < m and 0 <= column < n:  # Make sure it is within boundaries
                        live_neighbors += (board[row][column] == 1) or (board[row][column] == -1)

                # Apply the rules of Game of Life
                if board[i][j] == 1:  # Live cell
                    board[i][j] = 1 if 2 <= live_neighbors <= 3 else -1 # Live if condition else Die
                else:  # Dead cell
                    if live_neighbors == 3: board[i][j] = 2  # Reproduction (becorn alive)

        # Update board
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0  # Dead
                elif board[i][j] == 2:
                    board[i][j] = 1  # Live
'''
1. Compact Code: Reducing the use of additional functions and address management using a list and a loop to count neighbors.
2. Use of Intermediate States: Instead of a second array, the values 2 and -1 are used to mark state changes, thus optimizing memory.
3. Single Iteration Step: The counting and updating logic is performed in a single pass, making the execution time more efficient.
1. Time: The complexity is still O(m x n), since we go through each cell of the board.
2. Space: The space complexity is reduced to O(1), using only constant additional space for temporary variables.
'''
# Test example
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
x = Solution2()
x.gameOfLife(board)
print(board)  