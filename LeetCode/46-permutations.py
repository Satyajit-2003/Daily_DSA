from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) == 1):
            return [nums[:]]

        result = []

        for i in range(len(nums)):
            n = nums.pop(0)
            res = self.permute(nums)
            for r in res:
                r.append(n)
            result.extend(res)
            nums.append(n)
        
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))
    print(s.permute([0]))
    print(s.permute([]))