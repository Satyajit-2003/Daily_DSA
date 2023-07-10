class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.edges = {(i, j) for i,j in connections}
        self.res = 0
        self.visit = set()
        self.neigh = {city: [] for city in range(n)}

        for i, j in connections:
            self.neigh[i].append(j)
            self.neigh[j].append(i)

        def dfs(city):
            for n in self.neigh[city]:
                if n in self.visit:
                    continue
                if (n, city) not in self.edges:
                    self.res += 1
                self.visit.add(city)
                dfs(n)
        
        self.visit.add(0)
        dfs(0)

        return self.res
        