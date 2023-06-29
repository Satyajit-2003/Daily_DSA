from typing import List

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

if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([1,2,3,4,5]))
    print(s.increasingTriplet([5,4,3,2,1]))
    print(s.increasingTriplet([2,1,5,0,4,6]))