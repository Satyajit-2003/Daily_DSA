class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_sq(i: int, j: int) -> int:
            return ((i//3)*3) + j//3
        rows = [[], [], [], [], [], [], [], [], []]
        cols = [[], [], [], [], [], [], [], [], []]
        squ = [[], [], [], [], [], [], [], [], []]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j])
                sq = get_sq(i,j)
                if val in rows[i] or val in cols[j] or val in squ[sq]:
                    print(i,j)
                    print(rows, cols, squ)
                    return False
                rows[i].append(val)
                cols[j].append(val)
                squ[sq].append(val)
        
        return True

 
