from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(temp_nums, index):
            if (index == len(nums)):
                result.append(temp_nums.copy())
                return
            
            # Excluding the element at index 
            backtrack(temp_nums, index + 1)

            # Including the element at index
            backtrack(temp_nums + [nums[index]], index + 1)

        backtrack([], 0)
        return result



if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets([0]))
    print(s.subsets([]))