class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        memory = {}
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        def max_moves(row, column):
            if (row,column) in memory:
                return memory[(row,column)]
            if not (column < cols-1):
                return 0
            res = 0
            if (row > 0) and grid[row-1][column+1] > grid[row][column]:
                res = max(res, max_moves(row-1, column+1)+1)
            if grid[row][column+1] > grid[row][column]:
                res = max(res, max_moves(row, column+1)+1)
            if (row+1 < rows) and grid[row+1][column+1] > grid[row][column]:
                res = max(res, max_moves(row+1, column+1)+1)

            memory[(row,column)] = res
            return res            
            

        for i in range(rows):
            res = max(res, max_moves(i,0))

        return res

