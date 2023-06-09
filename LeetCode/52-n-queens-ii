class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        board = [['.']*n for i in range(n)]
        self.res = 0

        def backtrack(r):
            if r == n:
                self.res += 1
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
        return self.res

if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(4))
    print(s.totalNQueens(1))
    print(s.totalNQueens(2))
    print(s.totalNQueens(8))