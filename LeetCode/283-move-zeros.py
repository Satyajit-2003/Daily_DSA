from typing import List

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
        
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))
    print(s.moveZeroes([0]))
    print(s.moveZeroes([1,0]))
    print(s.moveZeroes([0,0,1]))