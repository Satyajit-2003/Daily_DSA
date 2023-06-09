from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] + nums[r] == target:
                return [l+1 , r+1]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        
        return [l+1, r+1]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([2,3,4], 6))
    print(s.twoSum([-1,0], -1))