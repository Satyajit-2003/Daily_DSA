from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total = 0
        i = 0
        j = len(costs) - 1
        left = []
        right = []
        while k > 0:
            while len(left)< candidates and  i <= j:
                heapq.heappush(left, costs[i])
                i += 1
            while len(right)< candidates and  i <= j:
                heapq.heappush(right, costs[j])
                j -= 1
            
            if len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    total += heapq.heappop(left)
                else:
                    total += heapq.heappop(right)
            elif len(left) > 0:
                total += heapq.heappop(left)
            elif len(right) > 0:
                total += heapq.heappop(right)

            k -= 1

        return total

if __name__ == "__main__":
    s = Solution()
    print(s.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))
    print(s.totalCost([1,2,4,1], 3, 3))


