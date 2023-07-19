class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n <= 2:
            return dp[n]
        
        for i in range(n-2):
            dp.append(dp[-1]+dp[-2]+dp[-3])
        
        return dp[-1]