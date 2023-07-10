class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heappush(heap, -1 * i)

        for i in range(k):
            ele = heappop(heap)

        return ele * -1