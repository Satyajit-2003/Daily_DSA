from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        distribution = [0] * k
        
        def backtrack(i):
            nonlocal min_unfairness, distribution
            
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(distribution))
                return
            if min_unfairness <= max(distribution):
                return
            
            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]
        
        backtrack(0)
        return min_unfairness
        
if __name__ == "__main__":
    s = Solution()
    print(s.distributeCookies([8,15,10,20,8], 2))
    print(s.distributeCookies([6,1,3,2,2,4,1,2], 3))
    print(s.distributeCookies([75027,58436,95472,89426,10786,32325,99823,33237], 5))
    print(s.distributeCookies([64,32,16,8,4,2,1,1000], 8))