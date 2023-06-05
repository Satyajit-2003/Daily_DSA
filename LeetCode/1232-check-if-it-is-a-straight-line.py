class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Taking the 1st two cordinates as reference
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x1 == x2:
            slope = float('inf')
        else:
            slope = (y2 - y1) / (x2 - x1)
        # Checking the slope of all the other cordinates
        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i - 1]
            x2, y2 = coordinates[i]
            if x1 == x2:
                if slope != float('inf'):
                    return False
            else:
                if slope != (y2 - y1) / (x2 - x1):
                    return False
        
        return True