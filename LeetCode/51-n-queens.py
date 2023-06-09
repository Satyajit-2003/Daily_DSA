from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        board = [['.']*n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                board_now = [''.join(row) for row in board]
                res.append(board_now)
                return
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r-c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        backtrack(0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
    print(s.solveNQueens(1))
    print(s.solveNQueens(2))