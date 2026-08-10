# if its a regular 9*9 sudoku board
# TC: O(9×9) = O(1) because Sudoku board size is fixed
# SC: O(9×9) = O(1) because we store at most 81 cells
#if the board is generalized to n × n
# TC: O(n²) — scan every cell once.
# SC: O(n²) — sets can collectively store information proportional to all cells.
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


        