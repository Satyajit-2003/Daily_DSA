from typing import List

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != '*':
                stack.append(ch)
            else:
                stack.pop()
        return ''.join(stack)
    
if __name__ == "__main__":
    s = Solution()
    print(s.removeStars("ab**c"))
    print(s.removeStars("abc**d"))
    print(s.removeStars("abc**d*"))
    print(s.removeStars("abc**d*"))