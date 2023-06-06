class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        if nums[0] == 1 and nums[-1] == len(nums):
            return 0
        left = nums.index(1)
        right = nums.index(len(nums))
        
        if left <  right:
            return (left + (len(nums)-right-1))
        else:
            return (left + (len(nums)-right-1) - 1)
        