class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        arr = []
        def backtrack(i, k, add):
            if k == 0 and add == n:
                res.append(arr.copy())
                return 
            if add > n or k == 0 or i == 10:
                return
            
            # Include i
            arr.append(i)
            backtrack(i+1, k-1, add+i)
            arr.pop()

            # Exclude i
            backtrack(i+1, k, add)
        
        backtrack(1, k, 0)
        return res