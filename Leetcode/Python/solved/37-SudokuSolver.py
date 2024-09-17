#37. Sudoku Solver  
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

-Each of the digits 1-9 must occur exactly once in each row.
-Each of the digits 1-9 must occur exactly once in each column.
-Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
Example: 
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_empty_location(arr, l):
            for row in range(9):
                for col in range(9):
                    if(arr[row][col] == "."):
                        l[0]= row
                        l[1]= col
                        return True
            return False

        def used_in_row(arr, row, num):
            for i in range(9):
                if(arr[row][i] == num):
                    return True
            return False
        
        def used_in_col(arr, col, num):
            for i in range(9):
                if(arr[i][col] == num):
                    return True
            return False
        
        def used_in_box(arr, row, col, num):
            for i in range(3):
                for j in range(3):
                    if(arr[i + row][j + col] == num):
                        return True
            return False
        
        def check_location_is_safe(arr, row, col, num):
            return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)
        
        def solve_sudoku(arr):
            # 'l' es una variable de tipo lista que mantiene el registro de filas y columnas en find_empty_location  
            l =[0, 0]
        
            if(not find_empty_location(arr, l)):
                return True
            row = l[0]
            col = l[1]
            
            for num in range(1, 10):
                if(check_location_is_safe(arr, row, col, str(num))):
                    arr[row][col]= str(num)

                    if(solve_sudoku(arr)):
                        return True
                    
                    arr[row][col] = "."     
            return False
        solve_sudoku(board)