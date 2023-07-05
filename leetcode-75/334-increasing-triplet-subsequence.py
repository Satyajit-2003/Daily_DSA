class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = k = float('inf')
        for _ in nums:
            i = min(i, _)
            if i < _ < j:
                j = _
            elif i < j < _:
                return True

        return False
