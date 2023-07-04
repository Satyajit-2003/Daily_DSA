class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                print(t[i], s[j])
                j += 1
            i += 1

        if j == len(s):
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("acb", "ahbgdc"))
    print(s.isSubsequence("", "ahbgdc"))
