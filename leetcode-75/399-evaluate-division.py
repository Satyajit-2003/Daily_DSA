# USING DFS NOT SO EFFICIENT 58ms 16.3MB
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            graph[eq[0]].append([eq[1], values[i]])
            graph[eq[1]].append([eq[0], 1 / values[i]])

        def dfs(src, tar):
            if src not in graph or tar not in graph:
                return float(-1)
            stack = [(src, 1)]
            visit = set()
            visit.add(src)

            while stack:
                n, w = stack.pop()
                if n == tar:
                    return w
                for node, weight in graph[n]:
                    if node not in visit:
                        stack.append([node, w*weight])
                        visit.add(node)
            
            return -1
        
        return [dfs(eq[0], eq[1]) for eq in queries]


# USING BFS MUCH MORE EFFICIENT 40 ms 16.3 MB
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            graph[eq[0]].append([eq[1], values[i]])
            graph[eq[1]].append([eq[0], 1 / values[i]])

        def dfs(src, tar):
            if src not in graph or tar not in graph:
                return float(-1)
            queue = deque()
            queue.append((src, 1))
            visit = set()
            visit.add(src)

            while queue:
                n, w = queue.popleft()
                if n == tar:
                    return w
                for node, weight in graph[n]:
                    if node not in visit:
                        queue.append([node, w*weight])
                        visit.add(node)
            
            return -1
        
        return [dfs(eq[0], eq[1]) for eq in queries]
