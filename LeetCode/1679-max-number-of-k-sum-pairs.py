from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, l, r = 0, 0 ,len(nums) - 1

        while l < r:
            S = nums[l] + nums[r]
            if S > k:
                r -= 1
            elif S < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations([1,2,3,4], 5))
    print(s.maxOperations([3,1,3,4,3], 6))
    print(s.maxOperations([1,1,1,1], 2))