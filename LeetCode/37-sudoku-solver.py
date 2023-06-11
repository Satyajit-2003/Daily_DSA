from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.flag = False
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squ = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    squ_id = ((i//3)*3) + j//3
                    squ[squ_id].add(num)
                    

        def backtrack(i, j):
            if i == 9:
                self.flag = True
                return

            new_i = i + (j+1)//9
            new_j = (j+1) % 9

            if board[i][j] != '.':
                backtrack(new_i, new_j)
            
            else:
                squ_id = ((i//3)*3) + j//3
                for val in range(1, 10):
                    if val not in rows[i] and val not in cols[j] and val not in squ[squ_id]:
                        rows[i].add(val)
                        cols[j].add(val)
                        squ[squ_id].add(val)
                        board[i][j] = str(val)

                        backtrack(new_i, new_j)

                        if not self.flag:
                            rows[i].remove(val)
                            cols[j].remove(val)
                            squ[squ_id].remove(val)
                            board[i][j] = str('.')

        backtrack(0, 0)

if __name__ == '__main__':
    s = Solution()
    board =    [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(board)
    print(board)