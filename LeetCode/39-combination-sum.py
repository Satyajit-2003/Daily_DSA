from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, temp_res, total):
            if (total == target):
                res.append(temp_res.copy())
                return
            if (i >= len(candidates)) or (total > target):
                return
                
            temp_res.append(candidates[i])
            backtrack(i, temp_res, total + candidates[i])
            temp_res.pop()

            backtrack(i+1, temp_res, total)

        backtrack(0, [], 0)

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
    print(s.combinationSum([2,3,5], 8))
    print(s.combinationSum([2], 1))