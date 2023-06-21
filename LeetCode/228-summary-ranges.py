from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        res = []
        start = 0
        end = 0
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i-1]:
                if start == end:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + '->' + str(nums[end]))
                start = end = i
            else:
                end += 1

        if start == end:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + '->' + str(nums[end]))       
        
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([0,1,2,4,5,7]))
    print(s.summaryRanges([0,2,3,4,6,8,9]))
    print(s.summaryRanges([]))