# The code checks if a 9×9 Sudoku board is valid by ensuring that each number appears only once in every row, column, 
# and 3×3 box using three set dictionaries (rows, cols, boxes). If a duplicate is found, it returns False; 
# otherwise, it returns True.

# Time Complexity: O(1) (Fixed 9×9 board → at most 81 iterations).
# Space Complexity: O(1) (Uses at most 81 elements in rows, cols, boxes, which is constant).
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set) 
        boxes = defaultdict(set)

        N = 9

        for r in range(N):
            for c in range(N):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        return True
