class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        res_arr = []
        for i in range(len(l)):
            subarr = nums[l[i]:r[i]+1]
            subarr.sort()
            diff = subarr[1] - subarr[0]
            for i in range(1, len(subarr)):
                if subarr[i] - subarr[i-1] != diff:
                    res_arr.append(False)
                    break            
            else:
                res_arr.append(True)
        
        return res_arr

if __name__ == "__main__":
    nums = [4,6,5,9,3,7]
    l = [0,0,2]
    r = [2,3,5]
    print(Solution().checkArithmeticSubarrays(nums, l, r))

