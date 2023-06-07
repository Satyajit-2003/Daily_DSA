from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(grid[0])):
            ans = 0
            for j in range(len(grid)):
                if len(str(grid[j][i])) > ans:
                    ans = len(str(grid[j][i]))
            res.append(ans)

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findColumnWidth([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.findColumnWidth([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))