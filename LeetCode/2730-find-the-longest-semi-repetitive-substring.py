class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        repeated = False        
        longest = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s):
                if j > i and s[j] == s[j - 1]:
                    if not repeated:
                        repeated = True
                    else:
                        break                
                j += 1
            print(longest, i, j)
            longest = max(longest, j - i)            
            i += 1
            repeated = False

        return longest

if __name__ == '__main__':
    s = Solution()
    print(s.longestSemiRepetitiveSubstring('0001'))