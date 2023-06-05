class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        strx = strx[::-1]

        if strx[-1] == '-':
            strx = '-' + strx[:-1]
        
        x = int(strx)
        if x > 2**31 -1 or x < -2**31:
            return 0
        else:
            return x
