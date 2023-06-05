class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ''
        incrementer = 2 * (numRows - 1)
        for r in range(numRows):
            for i in range(r, len(s), incrementer):
                res += s[i]
                if (r not in [0,numRows-1] and i+ incrementer - (2 * r) < len(s)):
                    res += s[i + incrementer - (2 * r)]
        
        return res