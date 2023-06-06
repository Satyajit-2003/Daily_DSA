class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      rows = len(matrix)
      cols = len(matrix[0])
      for i in range(len(matrix)):
        if matrix[i][0] <= target <= matrix[i][cols-1]:
            if target in matrix[i]:
                return True
            else:
                return False