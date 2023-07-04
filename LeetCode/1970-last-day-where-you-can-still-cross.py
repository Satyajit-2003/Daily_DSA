from typing import List

class Solution:
    def is_possible(self, mid: int, row: int, col: int, cells: List[List[int]]) -> bool:
        grid = [[0]*col for _ in range(row)]

        for i in range(mid):
            x, y = cells[i]
            grid[x-1][y-1] = 1
        
        visited = set()
        stack = [(0,cols) for cols in range(col) if grid[0][cols] == 0]

        while stack:
            x, y = stack.pop()
            if x == row-1:
                return True
            if (x, y) in visited:
                continue
            visited.add((x,y))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                n_row = x + dx
                n_col = y + dy
                if 0 <= n_row < row and 0 <= n_col < col and grid[n_row][n_col] == 0:
                    stack.append((n_row,n_col))

        return False         

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        left, right = 0, len(cells)-1
        res = - 1
        while left <= right:
            mid = (left + right)//2
            if self.is_possible(mid, row, col, cells):
                res = mid
                left = mid + 1
            else:
                right = mid -1
        
        return res

if __name__ == "__main__":
    print(Solution().latestDayToCross(2,2,[[1,1],[2,1],[1,2],[2,2]]))
    print(Solution().latestDayToCross(2,2,[[1,1],[1,2],[2,1],[2,2]]))
    print(Solution().latestDayToCross(3,3,[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))
    print(Solution().latestDayToCross(3,3,[[1,3],[2,1],[3,2],[2,2],[1,1],[1,2],[2,3],[3,3],[3,1]]))