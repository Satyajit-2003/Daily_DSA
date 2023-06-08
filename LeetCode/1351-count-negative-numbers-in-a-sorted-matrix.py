from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:            
            l,r = 0, len(row)
            while l < r:
                mid = l + (r - l) // 2
                if row[mid] < 0:
                    r = mid
                else:
                    l = mid + 1            
            count += (len(row) - l)        

        return count

if __name__ == '__main__':
    s = Solution()
    print(s.countNegatives([[4,3,2,-1],
                            [3,2,1,-1],
                            [1,1,-1,-2],
                            [-1,-1,-2,-3]]))
    print(s.countNegatives([[3,2],
                            [1,0]]))