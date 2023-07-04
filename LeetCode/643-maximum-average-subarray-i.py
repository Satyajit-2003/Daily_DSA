from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k-1
        loc_sum = sum(nums[:k])
        max_avg = float('-inf')
        while r < len(nums):
            if l != 0:
                loc_sum -= nums[l-1]
                loc_sum += nums[r]
            max_avg = max(max_avg, loc_sum/k)
            l += 1
            r += 1

        return max_avg

if __name__ == "__main__":
    s= Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
    print(s.findMaxAverage([5], 1))
    print(s.findMaxAverage([0,1,1,3,3], 4))