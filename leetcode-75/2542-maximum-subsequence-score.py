class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(i, j) for i, j in zip(nums1, nums2)]
        pairs = sorted(pairs, key = lambda p: p[1], reverse=True)

        heap = []
        sum1 = 0
        res = 0

        for i, j in pairs:
            sum1 += i
            heappush(heap, i)

            if len(heap) > k:
                t = heappop(heap)
                sum1 -= t
            if len(heap) == k:
                res = max(res, sum1*j)

        return res
        
                