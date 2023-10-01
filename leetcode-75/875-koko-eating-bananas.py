class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            mid = (l + r) // 2
            total = 0
            for p in piles:
                total += ceil(p/mid)
            
            if total <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans