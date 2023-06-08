class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if (nums[mid] == target):
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([-1,0,3,5,9,12], 9))
    print(s.searchInsert([-1,0,3,5,9,12], 2))
    print(s.searchInsert([5], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))