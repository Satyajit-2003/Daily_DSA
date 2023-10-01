class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        arrow = 1
        end = points[0][1]
        for j in range(1, len(points)):
            if points[j][0] <= end:
                continue
            else:
                arrow += 1
                end = points[j][1]
        
        return arrow