from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def calcCost(num: int) -> int:
            curr_cost = 0
            for j in range(len(nums)):
                curr_cost += ( abs( num - nums[j] ) * cost[j] )
            return curr_cost

        left = min(nums)
        right  = max(nums)
        
        while left < right:
            mid = (left + right)//2

            if calcCost(mid) < calcCost(mid + 1):
                right = mid
            else:
                left = mid + 1

        return calcCost(left)

if __name__ == "__main__":
    s = Solution()
    print(s.minCost([1,3,5,2], [2,3,1,14]))  # 8
    print(s.minCost([2,2,2,2,2], [4,2,8,1,3])) # 0