class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False for _ in range(len(isConnected))]
        def visit(city):
            if visited[city]:
                return
            visited[city] = True
            for i, conn in enumerate(isConnected[city]):
                if conn and not visited[i]:                    
                    visit(i)

        provinces = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                visit(i)

        return provinces