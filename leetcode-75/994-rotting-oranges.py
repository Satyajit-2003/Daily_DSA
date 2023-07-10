class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i , j))
        
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for i, j in [(0, 1), (1, 0), (-1, 0), (0,-1)]:
                    dx = x + i
                    dy = y + j
                    if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == 1:
                        fresh -= 1
                        queue.append((dx, dy))
                        grid[dx][dy] = 2
            time += 1

        if fresh > 0:
            return -1
        return time
