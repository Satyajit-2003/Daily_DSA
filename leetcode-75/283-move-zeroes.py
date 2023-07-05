class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        key = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[key] = nums[i]
                key += 1
            i += 1

        for j in range(key, len(nums)):
            nums[key] = 0
            key += 1