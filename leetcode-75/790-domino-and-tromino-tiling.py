class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[None for i in range(4)] for j in range(n+2)]
        MOD = (10 ** 9) + 7

        def get_state(t1, t2):
            if not t1 and not t2:
                return 0
            if t1 and not t2:
                return 1
            if not t1 and t2:
                return 2
            return 3
        
        def solve(i, t1, t2):
            if i == n:
                return 1
            state = get_state(t1, t2)
            if dp[i][state]:
                return dp[i][state]
            
            t3 = t4 = i+1 < n

            count = 0
            # t1 t3
            # t2 t4

            # __ -> Occupied before
            # [] -> Placing now
            # ** -> Free

            if t1 and t2 and t3:
                # __[][]
                # __[]**
                count += solve(i+1, False, True) 
            if t1 and t2 and t4:
                # __[]**
                # __[][]
                count += solve(i+1, True, False) 
            if t1 and not t2 and t3 and t4:
                # __[][]
                # ____[]
                count += solve(i+1, False, False)
            if not t1 and t2 and t3 and t4:
                # ____[]
                # __[][]
                count += solve(i+1, False, False)
            if t1 and t2:
                # __[]**
                # __[]**
                count += solve(i+1, True, True)
            if t1 and t2 and t3 and t4:
                # __[][]
                # __[][]
                count += solve(i+1, False, False)
            if t1 and not t2 and t3:
                # __[][]
                # ____**
                count += solve(i+1, False, True)
            if not t1 and t2 and t4:
                # ____**
                # __[][]
                count += solve(i+1, True, False)
            if not t1 and not t2:
                # ____**
                # ____**
                count += solve(i+1, True, True)

            dp[i][state] = count % MOD
            return dp[i][state]
        
        return solve(0, True, True)