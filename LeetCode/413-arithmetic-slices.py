class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums)<3:
            return 0
        res = 0
        count = 0
        for i in range(2, len(nums)):
            if (nums[i-1] - nums[i-2]) == (nums[i] - nums[i-1]):
                count += 1
            else:
                res += (count*(count+1))/2
                count = 0
        
        return int(res + (count*(count+1))/2)

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().numberOfArithmeticSlices(nums))