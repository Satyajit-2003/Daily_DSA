class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        visit = set()
        queue.append(tuple(entrance  + [0]))
        visit.add(tuple(entrance))
        steps = 0

        while queue:
            x, y, d = queue.popleft()
            if (x in [0, len(maze)-1] or y in [0, len(maze[0])-1]) and [x, y] != entrance:
                return d
            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dx = x + i
                dy = y + j
                if 0 <= dx < len(maze) and 0 <= dy < len(maze[0]) and maze[dx][dy] != '+':
                    if (dx, dy) in visit:
                        continue
                    visit.add((dx, dy))
                    queue.append((dx, dy, d+1))
        return -1